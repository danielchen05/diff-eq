(() => {
  const fallback=document.currentScript.dataset.dest;
  const query=new URLSearchParams(location.search);
  const target=location.hash.slice(1).replace(/^unit-/,'');
  const oldUnit=target || query.get('unit');
  const remap={'complex-roots':'real-roots','improved-euler':'euler'};
  const problem=query.get('problem');
  const key=problem ? 'problem-'+problem : remap[oldUnit] || oldUnit || fallback;
  location.replace('index.html#'+(/^[a-z0-9-]+$/.test(key) ? key : fallback));
})();
