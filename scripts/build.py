#!/usr/bin/env python3
"""Compile an offline-first mathematical reference from the edited course materials."""
from collections import defaultdict
from functools import lru_cache
from hashlib import sha256
from html import escape
import json
from pathlib import Path
import re
import shutil
import subprocess

from lxml import etree, html as lh

from figures import bifurcation, field, phase_line, radial

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / 'content/reference'
DIST = ROOT / 'dist'
ASSETS = DIST / 'assets'
CACHE = ROOT / '.render-cache'
catalog = json.loads((CONTENT / 'catalog.json').read_text())
problems = json.loads((CONTENT / 'problems.json').read_text())
topic_by_id = {t['id']: t for t in catalog}
index = []
figures = {
    'growth': ("Direction field and exponential integral curves for y prime equals y.", "Every solution is tangent to the segments it crosses."),
    'ellipse': ("Direction field with slope negative twice x divided by y. The field is undefined along the horizontal axis.", "The gap on the horizontal axis marks points where the equation is undefined."),
    'phase-z': ("Sign arrows point right, left, right, left across the roots zero, one and two.", "Filled points mark the stable equilibria. The open point at $1$ is unstable."),
    'bifurcation': ('Equilibrium branches meet at the parameter values negative one and zero.', 'Solid branches are stable and dashed branches are unstable. Read the bifurcation values $c=-1$ and $c=0$ on the horizontal axis.'),
    'radial': ("Two clockwise circles. Radial arrows point away from the inner circle and toward the outer circle.", "The dashed inner cycle is unstable. The solid outer cycle is stable.")
}
aliases = {
    'classification':'order ordinary nonlinear linearity differential equations ode',
    'direction-fields':'slope field direction fields integral curve tangent slopefields',
    'calculus':'integration by parts partial derivatives antiderivatives double angle',
    'separation':'separable separation of variables separate variables implicit solutions',
    'integrating-factor':'linear integrating factor integrating factors IF first order product rule',
    'existence':'existence uniqueness nonlinear IVP initial value problem continuous partial derivative rectangle',
    'phase-lines':'autonomous phase line stable unstable semi-stable semistable equilibrium equilibria logistic',
    'bifurcations':'bifurcation diagram parameter fixed points',
    'real-roots':'characteristic equation roots real complex imaginary repeated conjugates constant coefficient higher order IVP',
    'wronskian':'W linear independence superposition fundamental set row reduction',
    'abel':"Abel Abel's formula Abels theorem Wronskian normalized coefficient",
    'repeated-roots':'reduction of order second independent solution',
    'undetermined':'undetermined coefficients trial guess forcing resonance nonhomogeneous UC',
    'variation':'variation of parameters VOP Wronskian normalization',
    'matrices':'linear algebra eigenvalue eigenvector trace determinant characteristic polynomial',
    'conversion':'convert nth order system matrix conversion',
    'fundamental-matrix':'fundamental matrix matrices Wronskian columns recover system',
    'repeated-systems':'Jordan chain generalized eigenvector generalized eigenvectors defective repeated eigenvalue',
    'phase-portraits':'phase plane portrait improper node saddle spiral node spiral sink spiral source center centre stability',
    'linearization':'Jacobian critical fixed stationary points nonlinear linearisation',
    'preservation':'hyperbolic local stability type classification center centre',
    'cycles':'limit cycle polar periodic orbit clockwise asymptotic stability',
    'laplace-ivp':'initial value problem inverse Laplace partial fractions derivatives IVP',
    'steps':'Heaviside step function unit step discontinuous forcing',
    'euler':'Euler numerical method forward explicit tangent approximation',
}
unit_map = {'complex-roots':'real-roots'}
for q in problems:
    if q['id'] in ('field', 'source-exponential-field'):
        q['unit'] = 'direction-fields'
    q['unit'] = unit_map.get(q['unit'], q['unit'])


def sections(slug):
    md = (CONTENT / f'{slug}.md').read_text()
    parts = re.split(r'^## (.+?) \{#([\w-]+)\}\s*$', md, flags=re.M)
    if parts[0].strip() or len(parts) < 4:
        raise ValueError(f'Invalid headings in {slug}')
    return [(parts[i+1],parts[i],parts[i+2].strip()) for i in range(1,len(parts),3)]


@lru_cache(maxsize=None)
def render(md):
    if not md:
        return ''
    md = re.sub(r"(?<=[A-Za-z0-9})])(?:\\prime\b)+", lambda m: "'"*m.group().count(r'\prime'), md)
    figure_metadata = [figures[name] for name in re.findall(r'\{\{figure:([\w-]+)\}\}',md)]
    key = CACHE / sha256(('reader-v5\0'+md+'\0'+json.dumps(figure_metadata)).encode()).hexdigest()
    if key.exists():
        return key.read_text()
    compiled = subprocess.run(['pandoc','--from=markdown+tex_math_dollars','--to=html5','--mathml','--wrap=none'],
                              input=md, text=True, capture_output=True, check=True)
    if compiled.stderr.strip() or '<merror' in compiled.stdout:
        raise ValueError(compiled.stderr or md)
    tree = lh.fragment_fromstring(compiled.stdout,create_parent='div')
    # The comparison uses one semantic table even when its rows reflow on a phone.
    for table in tree.xpath('.//div[@class="stability-comparison"]/table'):
        table.set('role','table')
        headers = table.findall('./thead/tr/th')
        for header in headers:
            header.set('scope','col')
        for row in table.findall('./tbody/tr'):
            for cell,header in zip(row.findall('td'),headers):
                cell.set('data-label',header.text_content())
    for selector, tag, class_name in [('.//table','div','table-scroll'), ('.//math[@display="block"]','span','display-equation')]:
        for node in tree.findall(selector):
            parent = node.getparent()
            wrapper = etree.Element(tag,attrib={'class':class_name})
            parent.replace(node,wrapper)
            wrapper.tail, node.tail = node.tail, None
            wrapper.append(node)
    for node in tree.xpath('.//math[not(@display="block")]'):
        tex = node.find('.//annotation')
        if tex is not None and len(tex.text or '') >= 22:
            parent = node.getparent()
            wrapper = etree.Element('span',attrib={'class':'long-inline'})
            parent.replace(node,wrapper)
            wrapper.tail, node.tail = node.tail, None
            wrapper.append(node)
    for heading in tree.xpath('.//h3|.//h4'):
        heading.attrib.pop('id',None)
    for par in tree.findall('.//p'):
        if len(par) == 0 and (m := re.fullmatch(r'\{\{figure:([\w-]+)\}\}',par.text or '')):
            name=m.group(1)
            alt,caption=figures[name]
            fig=etree.Element('figure',attrib={'class':'math-figure '+name})
            etree.SubElement(fig,'img',src=f'assets/figures/{name}.svg',alt=alt)
            caption_element=lh.fragment_fromstring(render(caption))
            caption_element.tag='figcaption'
            fig.append(caption_element)
            fig.tail=par.tail
            par.getparent().replace(par,fig)
    result=''.join(lh.tostring(el,encoding='unicode',method='html') for el in tree).strip()
    key.write_text(result)
    return result


def searchable(markup):
    tree=lh.fragment_fromstring(markup or '<span></span>',create_parent='div')
    annotations=tree.findall('.//annotation')
    tex=' '.join(a.text or '' for a in annotations)
    for a in annotations:
        a.drop_tree()
    return ' '.join(' '.join(tree.itertext()).split()), tex


def add_index(target, title, group, subject, markup='', extra=''):
    plain, tex = searchable(markup)
    index.append(dict(id=target,title=title,type=group,topic=subject,
                      terms=f'{aliases.get(target,"")} {extra}',body=plain,tex=tex))


def anchor(href, label, cls=''):
    klass = f' class="{cls}"' if cls else ''
    return f'<a href="#{href}"{klass}>{escape(label)}</a>'


search_icon = '<svg aria-hidden="true" viewBox="0 0 20 20"><circle cx="8.6" cy="8.6" r="5.5"/><path d="m12.8 12.8 4.1 4.1"/></svg>'
print_icon = '<svg aria-hidden="true" viewBox="0 0 20 20"><path d="M5 7V3h10v4M5.5 14H3V7h14v7h-2.5M6 12h8v5H6z"/><path d="M14 9h1"/></svg>'


def page_top(title, crumb, description='', action=''):
    return (f'<div class="page-top"><div class="breadcrumbs">{crumb}</div><h1 tabindex="-1">{escape(title)}</h1>'
            + (f'<p class="deck">{escape(description)}</p>' if description else '')
            + (f'<div class="page-tools">{action}</div>' if action else '')+'</div>')


topic_sections = {t['id']: sections(t['id']) for t in catalog}
unit_titles = {key:title for items in topic_sections.values() for key,title,_ in items}
questions_by_unit = defaultdict(list)
for q in problems:
    if q['topic'] not in topic_by_id or q['unit'] not in unit_titles:
        raise ValueError(q['id'])
    questions_by_unit[q['unit']].append(q)

# Keep the original group bookmarks even where the packet filed a group under an adjacent chapter.
practice_ids = {key:f'bank-{items[0]["topic"]}-{key}' for key,items in questions_by_unit.items()}
legacy_links = {
    'cheatsheet':'formula-sheet', 'problems':'notes', 'sheet-first':'sheet-first-order',
    'sheet-existence':'sheet-qualitative', 'sheet-forcing':'sheet-nonhomogeneous',
    'sheet-plane':'formula-phase-portraits', 'sheet-cycles':'formula-cycles',
    'all-topics-title':'notes', 'initial-models':'classification', 'modeling':'integrating-factor',
    'bank-first-order-modeling':'integrating-factor', 'problem-pond':'integrating-factor',
    'problem-phase-alien':'phase-lines', 'bank-nonhomogeneous-higher-order':'higher-order-odes',
}
for topic in catalog:
    slug = topic['id']
    order = [key for key,_,_ in topic_sections[slug]]
    order.extend(key for key in questions_by_unit if key not in order)
    first = next((key for key in order if any(q['topic']==slug for q in questions_by_unit.get(key,[]))),None)
    if first:
        legacy_links['problems-'+slug] = practice_ids[first]


def print_control(label='Print'):
    return f'<button type="button" class="print-link js-only" data-open-print>{print_icon}{escape(label)}</button>'


def topic_page(topic):
    slug, title = topic['id'], topic['title']
    add_index(slug,title,'Notes','Topics & Practice',render(topic['summary']))
    at = catalog.index(topic)
    crumb = anchor('notes','All topics')+f'<span aria-hidden="true">/</span>Topic {at+1} of {len(catalog)}'
    tools = print_control('Print topic')+anchor('sheet-'+slug,'Topic formulas','return-sheet')
    pieces = [f'<article class="page notes-page" id="{slug}" data-nav="notes">',
              page_top(title,crumb,topic['summary'],tools),'<div class="read-column">']
    number = 0
    for unit,heading,md in topic_sections[slug]:
        markup = render(md)
        add_index(unit,heading,'Notes',title,markup)
        pieces.append(f'<section class="lesson" id="{unit}"><h2 tabindex="-1">{escape(heading)}</h2><div class="lesson-notes">{markup}</div>')
        items = questions_by_unit.get(unit,[])
        if items:
            pieces.append(practice_group(unit,items,title,number))
            number += len(items)
        pieces.append('</section>')
    navigation=[]
    if at:
        prev=catalog[at-1]
        navigation.append(f'<a rel="prev" href="#{prev["id"]}"><small>Previous topic</small>{escape(prev["title"])}</a>')
    if at+1 < len(catalog):
        nxt=catalog[at+1]
        navigation.append(f'<a rel="next" href="#{nxt["id"]}"><small>Next topic</small>{escape(nxt["title"])}</a>')
    pieces.extend(['<nav class="end-links" aria-label="Continue reading">',*navigation,'</nav></div></article>'])
    return ''.join(pieces)


def practice_group(unit,items,chapter,start):
    count=len(items)
    label=f'Practice {"problem" if count==1 else "problems"} ({count})'
    out=[f'<details class="practice" id="{practice_ids[unit]}"><summary>{label}</summary>',
         f'<ol class="problem-list" start="{start+1}">']
    for number,q in enumerate(items,start+1):
        key='problem-'+q['id']
        prompt=render(q['prompt'])
        add_index(key,f'Problem {number}','Problem',chapter,prompt,unit_titles[unit])
        out.append(f'<li class="problem" id="{key}" tabindex="-1"><div class="problem-prompt">{prompt}</div>')
        if q['credit']:
            out.append(f'<p class="credit">{escape(q["credit"])}</p>')
        if q.get('hint'):
            out.append(f'<details class="solution hint"><summary>Hint</summary><div class="answer">{render(q["hint"])}</div></details>')
        if q['solution']:
            label='Solution' if q['solution_kind']=='full' else 'Setup'
            out.append(f'<details class="solution"><summary>{label}</summary><div class="answer">{render(q["solution"])}</div></details>')
        out.append('</li>')
    return ''.join(out)+'</ol></details>'


def notes_overview():
    rows = []
    for topic in catalog:
        rows.append(f'<li><a href="#{topic["id"]}"><h3>{escape(topic["title"])}</h3><p>{escape(topic["summary"])}</p></a></li>')
    add_index('notes','Topics & Practice','Notes','Course overview',extra='original problems notes chapters exercises index')
    return (
        '<article class="page overview" id="notes" data-nav="notes"><div class="page-top">'
        '<div class="breadcrumbs">AS.110.302 <span aria-hidden="true">/</span> Daniel Chen</div>'
        '<h1 tabindex="-1">Topics &amp; Practice</h1><p class="deck">Course notes, worked examples, and original problems by topic.</p>'
        '<div class="page-tools">'+print_control('Print topics')+'</div></div>'
        '<ol class="overview-topics">'+''.join(rows)+'</ol></article>')


def formula_page():
    chapters = sections('cheatsheet')
    if [slug for slug,_,_ in chapters] != list(topic_sections):
        raise ValueError('Formula sheet chapters do not match the course order')
    out = ['<article class="page sheet-page active" id="formula-sheet" data-nav="formula-sheet">',
           '<header class="sheet-header"><div class="sheet-heading"><div class="breadcrumbs">AS.110.302 <span aria-hidden="true">/</span> Daniel Chen</div>'
           '<h1 tabindex="-1">Formula Sheet</h1><p class="deck">Select a method to open its notes and practice.</p>'
           '<div class="page-tools">'+print_control('Print formulas')+'</div></div>',
           '<a class="sheet-figure" href="#direction-fields" aria-label="Open the direction field example for y prime equals y">'
           '<img src="assets/figures/growth.svg" alt="Direction field with exponential integral curves.">'
           '<span>Direction field for '+render("$y'=y$").removeprefix('<p>').removesuffix('</p>')+'</span></a></header>']
    add_index('formula-sheet','Formula Sheet','Formula Sheet','Differential Equations',extra='cheatsheet cheat sheet formulas methods exam review')
    for slug,title,md in chapters:
        key='sheet-'+slug
        methods=re.split(r'^### (.+?) \{#([\w-]+)\}\s*$',md,flags=re.M)
        if methods[0].strip() or methods[2::3] != [unit for unit,_,_ in topic_sections[slug]]:
            raise ValueError(f'Formula methods do not match {slug}')
        add_index(key,title,'Formula Sheet','Course topics',extra=' '.join(methods[1::3]))
        out.append(f'<section class="sheet-block" id="{key}" data-topic="{slug}"><h2 tabindex="-1">{escape(title)}</h2>')
        for i in range(1,len(methods),3):
            heading,unit,body=methods[i:i+3]
            markup=render(body.strip())
            target='formula-'+unit
            add_index(target,heading,'Formula Sheet',title,markup,aliases.get(unit,''))
            out.append(f'<div class="formula-entry" id="{target}"><h3 tabindex="-1">{anchor(unit,heading)}</h3><div class="formula-body">{markup}</div></div>')
        out.append('</section>')
    out.append('</article>')
    return ''.join(out)


def reader():
    sheet_links=[]
    note_links=[]
    for n,t in enumerate(catalog,1):
        slug,title=t['id'],escape(t['title'])
        # The ordinal marks the chapters in the author's course sequence.
        number=f'<span class="topic-number" aria-hidden="true">{n:02d}</span>'
        sheet_links.append(f'<li><a class="topic-link" href="#sheet-{slug}">{number}<span>{title}</span></a></li>')
        units=''.join(f'<li>{anchor(unit,label)}</li>' for unit,label,_ in topic_sections[slug])
        note_links.append(f'<li class="outline-chapter" data-chapter="{slug}"><a class="topic-link" href="#{slug}">{number}<span>{title}</span></a><ul class="outline-sections">{units}</ul></li>')
    return (
        '<div class="notes-layout"><aside class="course-outline" aria-label="Course contents">'
        '<button class="outline-toggle" id="outline-toggle" type="button" aria-controls="topic-directory" aria-expanded="false">'
        '<svg aria-hidden="true" viewBox="0 0 20 20"><path d="M3 5h2m3 0h9M3 10h2m3 0h9M3 15h2m3 0h9"/></svg>Contents'
        '<svg class="chevron" aria-hidden="true" viewBox="0 0 16 16"><path d="m4 6 4 4 4-4"/></svg></button>'
        '<div id="topic-directory" class="topic-directory"><nav class="sheet-nav" aria-label="Formula sheet contents">'
        '<h2>On the formula sheet</h2><ol class="outline-chapters">'+''.join(sheet_links)+'</ol></nav>'
        '<nav class="notes-nav" aria-label="Course topics"><h2>Course topics</h2><a class="overview-link" href="#notes">All topics</a>'
        '<ol class="outline-chapters">'+''.join(note_links)+'</ol></nav></div></aside><div class="notes-reading">'+
        formula_page()+notes_overview()+''.join(topic_page(t) for t in catalog)+'</div></div>')


def build():
    ASSETS.mkdir(exist_ok=True,parents=True)
    CACHE.mkdir(exist_ok=True)
    field('growth');field('ellipse');phase_line();radial();bifurcation()
    pages = reader()
    template=(ROOT/'ui/page.html').read_text()
    brand_math=render(r'$\displaystyle\frac{dy}{dt}$').removeprefix('<p>').removesuffix('</p>')
    options=''.join(f'<option value="{t["id"]}">{escape(t["title"])}</option>' for t in catalog)
    output=(template.replace('@@PAGES@@',pages).replace('@@SEARCH@@',search_icon).replace('@@BRAND_MATH@@',brand_math)
            .replace('@@PRINT_TOPICS@@',options)
            .replace('@@LEGACY@@',json.dumps(legacy_links,separators=(',',':'))).replace('@@INDEX@@',json.dumps(index,ensure_ascii=False,separators=(',',':')).replace('<','\\u003c')))
    (DIST/'index.html').write_text(output)
    shutil.copyfile(ROOT/'ui/404.html', DIST/'404.html')
    for f in ('style.css','app.js','favicon.svg','math.ttf','math-font-license.txt'):
        shutil.copyfile(ROOT/'ui'/f,ASSETS/f)
    # Keep existing links to the retained resources working. These contain no legacy UI.
    for old,dest in [(t['id'],t['id']) for t in catalog]+[('cheatsheet','formula-sheet'),('practice','notes')]:
        url='index.html#'+dest
        redirect=(f'<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Differential Equations</title>'
                  f'<meta http-equiv="refresh" content="0;url={url}"><script src="assets/redirect.js" data-dest="{dest}"></script>'
                  f'</head><body><a href="{url}">Open the course reference</a></body></html>')
        (DIST/(old+'.html')).write_text(redirect)
    shutil.copyfile(ROOT/'ui/redirect.js',ASSETS/'redirect.js')
    stats={'topics':len(catalog),'notes_sections':len(unit_titles),'problems':len(problems),'worked_solutions':sum(p['solution_kind']=='full' for p in problems),
           'partial_setups':sum(p['solution_kind']=='partial' for p in problems),'formula_topics':len(sections('cheatsheet')), 'formula_methods':len(unit_titles), 'practice_groups':len(practice_ids),
           'native_mathml':output.count('<math ')}
    (ROOT/'review').mkdir(exist_ok=True)
    (ROOT/'review/build-summary.json').write_text(json.dumps(stats,indent=2)+'\n')
    print(json.dumps(stats))


if __name__ == '__main__':
    build()
