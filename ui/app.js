'use strict';

(() => {
  const pages = Array.from(document.querySelectorAll('article.page'));
  const byId = id => document.getElementById(id);
  const primary = Array.from(document.querySelectorAll('[data-dest]'));
  const dialog = byId('search');
  const input = byId('query');
  const results = byId('results');
  const status = byId('search-status');
  const launcher = byId('open-search');
  const sheet = byId('formula-sheet');
  const overview = byId('notes');
  const outlines = document.querySelector('.course-outline');
  const toggle = byId('outline-toggle');
  const noteChapters = Array.from(outlines.querySelectorAll('.outline-chapter'));
  const sheetLinks = Array.from(outlines.querySelectorAll('.sheet-nav .topic-link'));
  const noteSections = Array.from(outlines.querySelectorAll('.outline-sections a'));
  const overviewLink = outlines.querySelector('.overview-link');
  const legacy = JSON.parse(byId('legacy-links').textContent);
  const printDialog = byId('print-options');
  let active = sheet;
  let highlighted = null;

  function setOutline(open) {
    outlines.classList.toggle('is-open',open);
    toggle.setAttribute('aria-expanded',String(open));
  }
  toggle.addEventListener('click',()=>setOutline(!outlines.classList.contains('is-open')));
  window.matchMedia('(max-width:780px)').addEventListener('change',()=>setOutline(false));
  document.addEventListener('keydown',event=>{
    if (event.key==='Escape' && !dialog.open && !printDialog.open && outlines.classList.contains('is-open')) {
      setOutline(false);
      toggle.focus();
    }
  });

  function currentLink(link, isCurrent, value) {
    if (isCurrent) link.setAttribute('aria-current',value);
    else link.removeAttribute('aria-current');
  }
  function highlightSection(section) {
    if (highlighted===section) return;
    highlighted=section;
    const hash=section ? '#'+section.id : '';
    for (const link of [...sheetLinks,...noteSections]) currentLink(link,link.hash===hash,'location');
  }
  let frame=0;
  function markReadingPosition() {
    frame=0;
    if (active===overview || printState) return;
    const sections=active.querySelectorAll(active===sheet ? '.sheet-block' : '.lesson');
    const edge=parseFloat(getComputedStyle(document.documentElement).scrollPaddingTop)+3;
    let current=active===sheet ? sections[0] : null;
    for (const section of sections) {
      if (section.getBoundingClientRect().top>edge) break;
      current=section;
    }
    if (window.scrollY>0 && window.scrollY+window.innerHeight>=document.documentElement.scrollHeight-2) {
      current=sections[sections.length-1];
    }
    highlightSection(current);
  }
  window.addEventListener('scroll',()=>{
    if (!frame) frame=requestAnimationFrame(markReadingPosition);
  },{passive:true});

  function navigate(moveFocus) {
    if (printState) endPrint();
    let id;
    try { id=decodeURIComponent(location.hash.slice(1)); } catch { id=''; }
    if (id==='content') {
      active.querySelector('h1').focus();
      return;
    }
    const anchor=byId(Object.hasOwn(legacy,id) ? legacy[id] : id);
    const page=anchor?.closest('article.page') || sheet;
    const target=page.contains(anchor) ? anchor : page;
    const changed=active!==page;
    active=page;
    for (const item of pages) item.classList.toggle('active',item===page);
    document.body.dataset.view=page.dataset.nav;
    setOutline(false);
    currentLink(overviewLink,page===overview,'page');
    for (const chapter of noteChapters) {
      const selected=chapter.dataset.chapter===page.id;
      chapter.classList.toggle('selected',selected);
      currentLink(chapter.querySelector('.topic-link'),selected,'page');
    }
    for (const link of primary) currentLink(link,link.dataset.dest===page.dataset.nav,'page');

    // A bookmark or search match can point into a collapsed bank. Reveal only its questions.
    const practice=target.closest('details.practice');
    if (practice) practice.open=true;
    const group=target.closest('.sheet-block,.lesson');
    highlightSection(group || (page===sheet ? sheet.querySelector('.sheet-block') : null));
    const focusTarget=target.matches('li.problem') ? target :
      target.matches('details.practice') ? target.querySelector('summary') : target.querySelector('h1,h2,h3');
    if (moveFocus && focusTarget) focusTarget.focus({preventScroll:true});
    if (target===page) {
      if (changed || moveFocus) window.scrollTo(0,0);
    } else target.scrollIntoView({block:'start'});
    document.title=page.querySelector('h1').textContent+' · Differential Equations';
  }

  // Links remain ordinary fragment links. Back, Forward, and file URLs use the same route.
  window.addEventListener('hashchange', () => navigate(true));
  document.addEventListener('click', event => {
    const link = event.target.closest('a[href^="#"]');
    if (!link || event.defaultPrevented || event.metaKey || event.ctrlKey || event.shiftKey || event.altKey) return;
    if (link.hash === '#content') {
      event.preventDefault();
      active.querySelector('h1').focus();
      return;
    }
    if (link.closest('dialog')) dialog.close();
    if (link.hash === location.hash) {
      event.preventDefault();
      navigate(true);
    }
  });

  function normalize(value) {
    const substitutions = {'′':"'",'″':"''",'‴':"'''",'’':"'",'−':'-','²':'^2','³':'^3',
                           'θ':'theta','λ':'lambda','μ':'mu','φ':'phi','∫':'int','√':'sqrt'};
    return value.toLowerCase().normalize('NFD').replace(/[\u0300-\u036f]/g,'').replace(/[′″‴’−²³θλμφ∫√]/g,c=>substitutions[c])
      .replaceAll('–',' ').replaceAll('—',' ').replaceAll('-',' ').replace(/\s+/g,' ').trim();
  }
  const compact = value => value.replace(/[\s\\{}(),]/g,'');
  function formulaText(value) {
    const printable=value.replace(/[−–]/g,'-').replace(/[′’]/g,"'").replace(/″/g,"''").replace(/‴/g,"'''")
      .replace(/²/g,'^2').replace(/³/g,'^3').replace(/μ/g,'mu').replace(/λ/g,'lambda').replace(/θ/g,'theta');
    return compact(printable.toLowerCase().replace(/\\(?:dfrac|tfrac|frac)\s*\{([^{}]+)\}\s*\{([^{}]+)\}/g,'$1/$2')
      .replace(/\\(?:left|right|,|!|;|qquad|quad)\s*/g,'').replace(/\\(?:cdot|times)|[×·*]/g,''));
  }
  const entries = JSON.parse(byId('search-index').textContent).map(item => ({
    item, title:normalize(item.title), terms:normalize(item.terms), topic:normalize(item.topic),
    body:normalize(item.body), math:formulaText(item.tex), full:normalize(item.title+' '+item.topic+' '+item.terms+' '+item.body)
  }));
  let matches = [];
  let shown = 0;
  function rank(entry, term, words, mathTerm) {
    const exactFormula = mathTerm && entry.math.includes(mathTerm);
    if (mathTerm && !exactFormula) return 0;
    if (!exactFormula && !words.every(w => entry.full.includes(w) || entry.math.includes(compact(w)))) return 0;
    let score = exactFormula ? 90 : 0;
    if (entry.title === term) score += 160;
    else if (entry.title.includes(term)) score += 80;
    if (entry.terms.includes(term)) score += 55;
    if (entry.topic.includes(term)) score += 20;
    if (entry.body.includes(term)) score += 12;
    for (const word of words) {
      if (entry.title.includes(word)) score += 14;
      if (entry.terms.includes(word)) score += 5;
    }
    const preferred=active===sheet ? 'Formula Sheet' : 'Notes';
    return score + (entry.item.type===preferred ? 40 : entry.item.type==='Problem' ? 1 : 18);
  }
  function appendResults() {
    const more = byId('more-results');
    if (more) more.remove();
    const part = document.createDocumentFragment();
    for (const {entry} of matches.slice(shown,shown+20)) {
      const row = document.createElement('a');
      row.className = 'result'; row.href = '#' + entry.item.id;
      const meta = document.createElement('small');
      if (entry.item.type === 'Problem' && entry.item.id.startsWith('problem-')) {
        meta.textContent = entry.item.topic+' · '+entry.item.title;
        const preview = document.createElement('div');
        preview.className = 'result-preview';
        const prompt = byId(entry.item.id).querySelector('.problem-prompt');
        for (const node of Array.from(prompt.children).slice(0, 2)) preview.append(node.cloneNode(true));
        row.append(meta, preview);
      } else {
        meta.textContent = entry.item.type+' · '+entry.item.topic;
        const title = document.createElement('strong');
        title.textContent = entry.item.title;
        row.append(meta, title);
      }
      part.append(row);
    }
    shown = Math.min(shown+20,matches.length);
    results.append(part);
    if (shown < matches.length) {
      const button = document.createElement('button');
      button.id='more-results'; button.type='button';
      button.textContent = 'Show more results';
      button.addEventListener('click',() => {
        const oldCount=shown;
        appendResults();
        results.querySelectorAll('a')[oldCount]?.focus();
      });
      results.append(button);
    }
  }
  function search() {
    const raw = input.value;
    const hasMath = /[=+'^\\′″²³]/.test(raw) && !/^[A-Za-z]+['’]s\b/i.test(raw)
      || /\b(?:d[a-z]\s*\/\s*d[a-z]|[tyxrz]\s*\/\s*[tyxrz0-9])\b/i.test(raw);
    const term = normalize(hasMath ? raw : raw.replaceAll('/',' '));
    shown=0; results.replaceChildren();
    if (!term) {
      matches=[]; status.textContent='Search formulas, notes, and original problems.'; return;
    }
    const words=term.split(' ').filter(Boolean);
    const mathTerm=hasMath ? formulaText(raw) : '';
    matches=entries.map(entry=>({entry,score:rank(entry,term,words,mathTerm)})).filter(match=> match.score>0)
      .sort((a,b)=>b.score-a.score);
    status.textContent = matches.length ? matches.length+' '+(matches.length===1?'result':'results') : 'No matches. Try a topic name or a shorter expression.';
    appendResults();
  }
  function openSearch() {
    if (dialog.open || printDialog.open) return;
    dialog.showModal(); input.focus(); input.select();
  }
  launcher.addEventListener('click',openSearch);
  byId('close-search').addEventListener('click',()=>dialog.close());
  dialog.addEventListener('click',event=>{
    if (event.target!==dialog) return;
    const r=dialog.getBoundingClientRect();
    if (event.clientX<r.left || event.clientX>r.right || event.clientY<r.top || event.clientY>r.bottom) dialog.close();
  });
  input.addEventListener('input',search);
  document.addEventListener('keydown',event=>{
    if ((event.ctrlKey || event.metaKey) && event.key.toLowerCase()==='k') {
      event.preventDefault(); openSearch(); return;
    }
    if (event.key==='/' && !event.ctrlKey && !event.metaKey && !event.altKey &&
        !event.target.matches('input,textarea,[contenteditable="true"]')) {
      event.preventDefault(); openSearch(); return;
    }
    if (dialog.open && event.target===input && (event.key==='Enter' || event.key==='ArrowDown')) {
      const first=results.querySelector('a');
      if (first) {
        event.preventDefault();
        if (event.key==='Enter') first.click();
        else first.focus();
      }
    }
  });

  const printTopic=byId('print-topic');
  const printMaterial=byId('print-material');
  const printAnswers=byId('print-answers');
  let printState=null;
  let requested=null;

  function selectedTopics(topic) {
    return pages.filter(p=>p.classList.contains('notes-page') && (topic==='all' || p.id===topic));
  }
  function updatePrintFields() {
    const isSheet=active===sheet;
    const selected=selectedTopics(printTopic.value);
    const hasProblems=selected.some(p=>p.querySelector('.practice'));
    const hasAnswers=selected.some(p=>p.querySelector('.solution'));
    byId('material-field').hidden=isSheet || !hasProblems;
    if (!hasProblems) printMaterial.value='notes';
    byId('answers-field').hidden=isSheet || printMaterial.value==='notes' || !hasAnswers;
    if (byId('answers-field').hidden) printAnswers.checked=false;
  }
  function openPrintOptions() {
    byId('print-title').textContent=active===sheet ? 'Print formulas' : 'Print topics';
    printTopic.value=active===sheet || active===overview ? 'all' : active.id;
    printMaterial.value='notes';
    printAnswers.checked=false;
    updatePrintFields();
    printDialog.showModal();
    printTopic.focus();
  }
  printTopic.addEventListener('change',updatePrintFields);
  printMaterial.addEventListener('change',updatePrintFields);
  byId('close-print').addEventListener('click',()=>printDialog.close());
  byId('cancel-print').addEventListener('click',()=>printDialog.close());
  document.addEventListener('click',event=>{
    if (event.target.closest('[data-open-print]')) openPrintOptions();
  });
  byId('print-form').addEventListener('submit',event=>{
    event.preventDefault();
    endPrint();
    requested={scope:active===sheet?'formulas':printMaterial.value,topic:printTopic.value,answers:printAnswers.checked};
    printDialog.close();
    preparePrint();
    window.print();
  });

  function preparePrint() {
    if (printState) return;
    const settings=requested || {scope:active===sheet?'formulas':'notes',topic:active.classList.contains('notes-page')?active.id:'all',answers:false};
    const {scope,topic,answers}=settings;
    const selected=scope==='formulas' ? [sheet] : selectedTopics(topic).filter(p=>scope!=='practice' || p.querySelector('.practice'));
    printState={details:[]};
    document.body.dataset.printScope=scope;
    document.body.classList.toggle('with-answers',answers);
    for (const page of selected) {
      page.classList.add('printing');
      if (page===sheet) {
        for (const block of sheet.querySelectorAll('.sheet-block')) {
          block.classList.toggle('print-omit',topic!=='all' && block.dataset.topic!==topic);
        }
      } else if (scope!=='notes') {
        for (const detail of page.querySelectorAll('.practice,.solution')) {
          printState.details.push([detail,detail.open]);
          detail.open=detail.classList.contains('practice') || answers;
        }
      }
    }
  }
  function endPrint() {
    if (printState) {
      for (const [detail,wasOpen] of printState.details) detail.open=wasOpen;
    }
    for (const el of document.querySelectorAll('.printing,.print-omit')) el.classList.remove('printing','print-omit');
    delete document.body.dataset.printScope;
    document.body.classList.remove('with-answers');
    requested=null;
    printState=null;
  }
  window.addEventListener('beforeprint',preparePrint);
  window.addEventListener('afterprint',endPrint);
  // Some system print dialogs omit afterprint when cancelled.
  for (const type of ['pointerdown','keydown']) {
    document.addEventListener(type,()=>{
      if (printState && !window.matchMedia('print').matches) endPrint();
    },true);
  }
  navigate(false);
})();
