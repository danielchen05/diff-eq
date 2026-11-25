#!/usr/bin/env python3
"""Audit links, original question/solution scopes, MathML and the offline distribution."""
from collections import Counter
from hashlib import sha256
import json
from pathlib import Path
import re
import subprocess
import sys
from tempfile import TemporaryDirectory
from lxml import etree, html
from export import export

ROOT=Path(__file__).resolve().parents[1]
DIST=ROOT/'dist'
CONTENT=ROOT/'content/reference'
document=html.fromstring((DIST/'index.html').read_text())
main=document.get_element_by_id('content')
catalog=json.loads((CONTENT/'catalog.json').read_text())
problems=json.loads((CONTENT/'problems.json').read_text())
ids=document.xpath('//@id')
assert len(ids)==len(set(ids)), 'Duplicate fragment identifiers'
assert document.xpath('//nav[@aria-label="Primary"]/a/@href')==['#formula-sheet','#notes']
for href in main.xpath('.//a/@href'):
    assert href.startswith('#') and href[1:] in ids,href
for src in document.xpath('//img/@src|//script/@src|//link/@href'):
    assert (DIST/src).is_file(),src
search=json.loads(document.get_element_by_id('search-index').text)
entries={i['id']:i for i in search}
assert len(entries)==len(search) and entries.keys()<=set(ids)
directory=main.get_element_by_id('topic-directory')
sheet=main.get_element_by_id('formula-sheet')
aliases=json.loads(document.get_element_by_id('legacy-links').text)
assert set(aliases.values())<=set(ids)
assert aliases['cheatsheet']=='formula-sheet' and aliases['problems']=='notes'
topics=[t['id'] for t in catalog]
assert sheet.xpath('./section/@data-topic')==topics
assert directory.xpath('.//nav[@class="sheet-nav"]//a/@href')==['#sheet-'+t for t in topics]
assert directory.xpath('.//nav[@class="notes-nav"]//a[@class="topic-link"]/@href')==['#'+t for t in topics]
assert main.xpath('.//article[contains(@class," active")]/@id')==['formula-sheet']
assert main.get_element_by_id('notes').xpath('.//ol/li/a/@href')==['#'+t for t in topics]
assert len(main.xpath('.//li[@class="problem"]'))==len(problems)
assert not main.xpath('.//details[@open]')
retired={'problem-pond','problem-phase-alien','initial-models','modeling'}
assert not retired.intersection(ids) and retired<=aliases.keys()
for unit,questions in {'higher-order':['hom-triple'],'higher-order-forcing':['nonhom-triple','higher-guess','pilot-third']}.items():
    chapter=main.get_element_by_id('higher-order-odes')
    current=chapter.xpath('.//section[@id=$id]//li[@class="problem"]/@id',id=unit)
    assert set(current)=={'problem-'+key for key in questions}
assert main.get_element_by_id('problem-nonhom-triple').xpath('.//details[@class="solution"]')
for slug in topics:
    chapter=main.get_element_by_id(slug)
    sections=chapter.xpath('.//section[@class="lesson"]')
    units=[section.get('id') for section in sections]
    formulas=sheet.xpath('./section[@data-topic=$slug]//div[@class="formula-entry"]/h3/a/@href',slug=slug)
    rail=directory.xpath('.//li[@data-chapter=$id]/ul/li/a/@href',id=slug)
    assert rail==formulas==['#'+unit for unit in units]
    assert all(unit in entries and 'formula-'+unit in entries for unit in units)
    number=0
    for group in chapter.xpath('.//details[@class="practice"]'):
        assert group.getparent().find('h2') is not None
        questions=group.xpath('./ol/li')
        assert questions and group.find('summary').text.endswith(f'({len(questions)})')
        assert int(group.find('ol').get('start'))==number+1
        for element in questions:
            number+=1
            entry=entries[element.get('id')]
            assert entry['title']==f'Problem {number}' and entry['type']=='Problem'
            assert element.find('div[@class="problem-prompt"]') is not None
            assert not element.xpath('.//h2|.//h3|.//h4')
for q in problems:
    key='problem-'+q['id']
    assert q['source'] and key in entries and q['solution_kind'] in {'none','full','partial'}
    element=main.get_element_by_id(key)
    assert element.tag=='li' and 'title' not in q
    unit='direction-fields' if q['id'] in ('field','source-exponential-field') else q['unit']
    unit='real-roots' if unit=='complex-roots' else unit
    assert element.xpath('ancestor::section[@class="lesson"]/@id')==[unit]
    assert element.xpath('ancestor::details[@class="practice"]/@id')==[f'bank-{q["topic"]}-{unit}']
    assert (element.find('details[@class="solution hint"]') is not None)==bool(q.get('hint'))
    detail=element.find('details[@class="solution"]')
    assert (detail is None)==(not q['solution'])==(q['solution_kind']=='none')
    if detail is not None:
        assert detail.find('summary').text==('Setup' if q['solution_kind']=='partial' else 'Solution')
for figure in (DIST/'assets/figures').glob('*.svg'):
    tree=etree.parse(str(figure))
    assert tree.xpath('//*[@data-tex]') and not tree.xpath('//*[local-name()="text"]'),figure
math=document.findall('.//math')
assert len(math)>750 and not document.findall('.//merror')
assert all(len(m.xpath('./semantics/annotation[@encoding="application/x-tex"][normalize-space()]'))==1 for m in math)
assert document.xpath('//a[@class="brand"]//mfrac') and main.xpath('.//figcaption//math')
assert all(el.get('alt') for el in main.findall('.//img'))
for unit in ('existence','phase-lines','phase-portraits','preservation'):
    sheet_table=sheet.get_element_by_id('formula-'+unit).find('.//table')
    notes_table=main.get_element_by_id(unit).find('./div[@class="lesson-notes"]//table')
    assert etree.tostring(sheet_table,method='c14n')==etree.tostring(notes_table,method='c14n'),unit
portraits=main.get_element_by_id('phase-portraits').find('.//table')
assert portraits.xpath('./thead/tr/th/text()')==['Eigenvalues','Linear type','Stability']
assert portraits.xpath('./tbody/tr[td[2]="Improper node"]/td[3]/text()') == ['Asymptotically stable', 'Unstable']
assert portraits.xpath('./tbody/tr[td[2]="Spiral node (spiral source)"]/td[3]/text()')==['Unstable']
preservation=main.get_element_by_id('preservation').find('.//table')
assert preservation.xpath('./thead/tr/th/text()')==['Eigenvalues','Linear type','Linear stability','Nonlinear type','Nonlinear stability']
assert preservation.xpath('./tbody/tr[td[2]="Center"]/td[position()>2]/text()')==['Stable','Inconclusive','Inconclusive']
improper_rows = preservation.xpath('./tbody/tr[td[2]="Improper node"]')
assert [row[2].text_content() for row in improper_rows] == ['Asymptotically stable', 'Unstable']
for row in improper_rows:
    assert 'one independent eigenvector' in row[0].text_content()
    assert row[3].text_content() == 'Inconclusive' and row[4].text_content() == row[2].text_content()
for prefix in ('formula-', ''):
    classification = main.get_element_by_id(prefix + 'classification')
    if not prefix:
        classification = classification.find('./div[@class="lesson-notes"]')
    assert not classification.xpath('.//math[@display="block"]')
    assert 'fundamental set' in main.get_element_by_id(prefix + 'variation').text_content().lower()
    wronskian = main.get_element_by_id(prefix + 'wronskian')
    tests = wronskian.xpath('.//ul/li')
    assert len(tests) == 2
    assert 'one point' in tests[0].text_content() and 'linearly independent' in tests[0].text_content()
    assert 'every point' in tests[1].text_content() and 'linearly dependent' in tests[1].text_content()
    assert 'continuous normalized coefficients' in wronskian.text_content()
for key in ('abel','formula-abel'):
    block=main.get_element_by_id(key)
    assert not block.findall('.//details')
    assert block.xpath('.//math[@display="block"]//annotation/text()')==[r'W(t)=W(t_0)e^{-\int_{t_0}^{t}p(s)\,ds}.']
for key in ('wronskian','formula-wronskian'):
    assert not any(r'\int_' in formula for formula in main.get_element_by_id(key).xpath('./div//annotation/text()'))
for key in ('fundamental-matrix','formula-fundamental-matrix'):
    block=main.get_element_by_id(key)
    assert 'side by side as columns' in ' '.join(block.itertext())
    assert any(r'\det\Phi' in expr for expr in block.xpath('.//annotation/text()'))
prose=' '.join(main.xpath('.//text()[not(ancestor::math)]'))
assert not re.search(r'\$|\\begin\{|\\frac\b|\{\{figure:|[=±∫√≠≤≥]',prose)
visible_text=' '.join(main.itertext()).lower()
assert not any(term in visible_text for term in ['alien craft','gallons','chemicals in a pond','linear drag','outflow concentration'])
for forbidden in ['teach a section','worksheet builder','practice exam','theorem booklet','midterm','quiz review','heun','poincaré','power series','localStorage','degenerate node','proportional exponentials','Peano','Lipschitz','Picard','star node','fundamental pair','combine trials for products','when an eigenvalue is zero']:
    assert forbidden.lower() not in ((DIST/'index.html').read_text()+(DIST/'assets/app.js').read_text()).lower(),forbidden
subprocess.run(['node','--check',str(DIST/'assets/app.js')],check=True)
subprocess.run(['node','--check',str(DIST/'assets/redirect.js')],check=True)
for t in catalog:
    redirect=html.fromstring((DIST/(t['id']+'.html')).read_text())
    assert redirect.xpath('//meta[@http-equiv="refresh"]/@content')==['0;url=index.html#'+t['id']]
with TemporaryDirectory() as tmp:
    path=Path(tmp)/'reference.html'
    export(path)
    portable=html.fromstring(path.read_text())
    assert not portable.xpath('//script[@src]|//link[@rel="stylesheet"]')
    for src in portable.xpath('//img/@src|//link[@rel="icon"]/@href'):
        assert src.startswith('data:image/svg+xml;base64,'),src[:50]
    assert 'data:font/ttf;base64,' in portable.find('.//style').text
    assert portable.get_element_by_id('search-index').text==document.get_element_by_id('search-index').text
    assert portable.xpath('//@id')[:-1]==ids
    assert len(portable.findall('.//math'))==len(document.findall('.//math'))
    if len(sys.argv)>1:
        assert sha256(path.read_bytes()).digest()==sha256(Path(sys.argv[1]).read_bytes()).digest(), 'Export is stale'
print(f'{len(ids)} unique anchors, {len(search)} search entries, {len(catalog)} chapters, {len(problems)} source problems. '
      f'{dict(Counter(p["solution_kind"] for p in problems))}. Standalone assets and {len(math)} LaTeX expressions verified.')
