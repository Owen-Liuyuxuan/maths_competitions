'use strict';
(() => {
  const D = window.MATH_ATLAS;
  const $ = s => document.querySelector(s);
  const esc = v => String(v ?? '').replace(/[&<>"']/g, c => ({'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;',"'":'&#39;'}[c]));
  const safe = url => /^(https?:\/\/|originals\/|derived\/)/.test(url || '') ? esc(url) : '#';
  const link = (url, label) => `<a href="${safe(url)}" target="_blank" rel="noopener noreferrer">${esc(label)} ↗</a>`;
  const comps = Object.fromEntries(D.competitions.map(c => [c.id, c]));
  const rmap = Object.fromEntries(D.resources.map(r => [r.id, r]));
  let view = 'papers', page = 1, selected = null, panel = 'question', blindMask = false;
  const SIZE = 18;
  const authority = {official:'官方来源', 'university-mirror':'大学镜像', 'community-mirror':'社区镜像', 'third-party':'第三方整理'};
  const role = {questions:'试题',solutions:'参考解答',combined:'题解合卷',compilation:'历史汇编'};
  const MATH_OPTS = {delimiters:[{left:'\\[',right:'\\]',display:true},{left:'\\(',right:'\\)',display:false}],throwOnError:false,strict:'ignore'};

  const taughtCount = D.questions.filter(q=>q.has_teaching).length;
  const editedCount = D.questions.filter(q=>q.editorial_status==='model-visual').length;
  $('#stats').innerHTML = [
    [D.competitions.length, '项代表性竞赛'],
    [D.resources.filter(r=>r.status==='downloaded').length, '份下载记录 / 含版本'],
    [D.questions.length, '条逐题索引 / 已合并版本'],
    [D.questions.filter(q=>q.solution||q.has_solution).length, '条逐题解答关联'],
    [taughtCount, '题教学拆解与易错分析']
  ].map(([n,t])=>`<div class="stat"><strong>${n}</strong><span>${t}</span></div>`).join('');
  $('#mode-note').textContent = D.mode === 'public'
    ? `公开索引版 · 含 ${taughtCount} 题教学标签索引`
    : `中文正文已整理 ${editedCount} 题 · 教学拆解与易错分析 ${taughtCount} 题`;

  for (const c of D.competitions) $('#contest').insertAdjacentHTML('beforeend',`<option value="${esc(c.id)}">${esc(c.id)} · ${esc(c.name)}</option>`);
  for (const year of [...D.years].reverse()) $('#year').insertAdjacentHTML('beforeend',`<option>${year}</option>`);
  for (const tag of [...new Set(D.questions.flatMap(q=>q.tags||[]))].sort()) $('#tag').insertAdjacentHTML('beforeend',`<option>${esc(tag)}</option>`);

  const allTeachingTags = [...new Set(D.questions.flatMap(q=>q.teaching_tags||[]))];
  const diffTags = ['训练:基础热身','训练:技巧进阶','训练:压轴攻坚'].filter(t=>allTeachingTags.includes(t));
  const pitfallTags = allTeachingTags.filter(t=>t.startsWith('易错:')).sort();
  const methodTags = allTeachingTags.filter(t=>!t.startsWith('训练:')&&!t.startsWith('易错:')).sort();
  for (const [label, list] of [['训练定位', diffTags], ['核心思维与方法', methodTags], ['典型易错类型', pitfallTags]]) {
    if (!list.length) continue;
    $('#teaching-tag').insertAdjacentHTML('beforeend', `<optgroup label="${esc(label)}">${list.map(t=>`<option value="${esc(t)}">${esc(t)}</option>`).join('')}</optgroup>`);
  }

  function matching(r) {
    const c = $('#contest').value, y = $('#year').value, l = $('#level').value, tag = $('#tag').value;
    const ttag = $('#teaching-tag').value;
    const query = $('#search').value.trim().toLowerCase();
    const edition = $('#edition').value;
    const isQ = Boolean(r.resource_id);
    const edited = r.contest && (isQ ? r.editorial_status==='model-visual' : D.questions.some(q=>q.resource_id===r.id&&q.editorial_status==='model-visual'));
    const taught = r.contest && (isQ ? Boolean(r.has_teaching) : D.questions.some(q=>q.resource_id===r.id&&q.has_teaching));
    const editionMatch = !edition || (edition==='teaching' ? taught : edition==='ready' ? edited : !edited);
    const tagMatch = !tag || (r.tags || []).includes(tag) || (!r.tags && D.questions.some(q=>q.resource_id===r.id&&(q.tags||[]).includes(tag)));
    const ttagMatch = !ttag || (isQ ? (r.teaching_tags||[]).includes(ttag) : D.questions.some(q=>q.resource_id===r.id&&(q.teaching_tags||[]).includes(ttag)));
    const searchable = [
      r.id, r.title, r.name, r.contest, comps[r.contest]?.name, r.year, r.number, r.part,
      ...(r.tags||[]), ...(r.teaching_tags||[]), ...(r.teaching_topics||[]),
      r.text||'', r.teaching?.problem_statement_zh||'', r.teaching?.teaching_takeaway||''
    ].join(' ').toLowerCase();
    return (!c || r.contest===c || (r.id===c && !r.contest)) && (!y || String(r.year)===y) &&
      editionMatch && (!l || (r.level || comps[r.contest]?.level)===l) && tagMatch && ttagMatch &&
      (!query || searchable.includes(query));
  }

  function teachingChips(q) {
    if (!q.has_teaching) return '';
    const diff = q.teaching_difficulty ? `<span class="chip teach-diff">${esc(q.teaching_difficulty)}</span>` : '';
    const meth = (q.teaching_methods||[]).map(t=>`<span class="chip teach-method">${esc(t)}</span>`).join('');
    const pit = (q.teaching_pitfalls||[]).map(t=>`<span class="chip teach-pitfall">${esc(t)}</span>`).join('');
    return diff + meth + pit;
  }

  function paperCard(r) {
    const ready = r.status === 'downloaded';
    const title = r.title.replace(/_+/g,' ');
    return `<article class="card"><div class="card-head"><span class="contest-code">${esc(r.contest)}</span><span>${r.year} / ${esc(role[r.role]||r.role)}</span></div><h3>${esc(title)}</h3><p class="desc">${esc(comps[r.contest]?.name)}${r.pages ? ` · ${r.page_range?r.page_range[1]-r.page_range[0]:r.pages} 页` : ''}</p><div class="chips"><span class="chip">${esc(authority[r.authority]||r.authority)}</span><span class="chip ${ready?'':'warn'}">${ready?'已下载':'下载待补'}</span>${r.completeness?`<span class="chip warn">${esc({'partial-preview':'部分预览','partial-recall':'部分回忆版','needs-review':'完整度待核'}[r.completeness]||r.completeness)}</span>`:''}</div><div class="card-bottom">${ready&&D.mode==='local'?link(r.local_path+(r.page_range?'#page='+(r.page_range[0]+1):''),'打开原卷'):link(r.url,'来源文件')}${link(r.source_url,'来源')}</div></article>`;
  }

  function questionCard(q) {
    const topicList = (q.tags && q.tags.length) ? q.tags : (q.teaching_topics || []);
    const statusParts = [
      q.editorial_status==='model-visual' ? '中文题面' : (q.has_teaching ? '已整理题干' : '原卷资料 · 正文整理中'),
      (q.solution||q.has_solution) ? '附参考解答' : '',
      q.has_teaching ? '含教学拆解' : ''
    ].filter(Boolean);
    return `<article class="card"><div class="card-head"><span class="contest-code">${esc(q.contest)}</span><span>${q.year} / ${esc(q.number)} · ${esc(q.level)}</span></div><h3>${esc(q.title)}</h3><div class="chips">${teachingChips(q)}${topicList.map(t=>`<span class="chip">${esc(t)}</span>`).join('')}<span class="chip">${esc(authority[q.authority]||'原卷资料')}</span></div><p class="desc">${statusParts.join(' · ')}</p><div class="card-bottom"><button data-q="${esc(q.id)}">${q.has_teaching ? '单题训练与教学 →' : '阅读题目 →'}</button></div></article>`;
  }

  function coverage() {
    const rows = D.competitions.filter(c=>(!$('#contest').value||c.id===$('#contest').value)&&(!$('#level').value||c.level===$('#level').value));
    const years = D.years.filter(y=>!$('#year').value||String(y)===$('#year').value);
    $('#results').innerHTML = `<div class="notice">下载份数包含语言版本、试题及解答文件，不表示该年份全部场次齐全。空白仅表示本库尚未归档。Putnam 2026 截至 2026-11-16 尚未举行。</div><div class="coverage"><table><thead><tr><th>竞赛 / 年份</th>${years.map(y=>`<th>${y}</th>`).join('')}</tr></thead><tbody>${rows.map(c=>`<tr><th>${esc(c.id)} · ${esc(c.name)}</th>${years.map(y=>{const rs=D.resources.filter(r=>r.contest===c.id&&r.year===y&&!r.multi_year);const n=rs.filter(r=>r.status==='downloaded').length;return `<td class="${n?'ok':'missing'}">${n?`已下载 ${n} 份`:c.id==='PUTNAM'&&y===2026?'尚未举行':rs.length?'仅线索 / 待下载':'未收集'}</td>`;}).join('')}</tr>`).join('')}</tbody></table></div>`;
    $('#result-count').textContent='收集覆盖，不等于完整度认证';$('#page-info').textContent='';$('#pagination').innerHTML='';
  }

  function render() {
    if(view==='coverage') {coverage();return;}
    let items;
    if(view==='sources') {
      items=D.competitions.filter(c=>(!$('#contest').value||c.id===$('#contest').value)&&(!$('#level').value||c.level===$('#level').value)&&(!$('#search').value||[c.id,c.name,c.description].join(' ').toLowerCase().includes($('#search').value.toLowerCase())));
      $('#results').innerHTML=`<div class="grid">${items.map(c=>`<article class="card"><div class="card-head"><span class="contest-code">${esc(c.id)}</span><span>${esc(c.level)} / ${esc(c.region)}</span></div><h3>${esc(c.name)}</h3><p class="source-desc">${esc(c.description)}</p><div class="card-bottom">${link(c.source,'官方入口')}</div></article>`).join('')}</div>`;
      $('#result-count').textContent=`${items.length} 项竞赛 · 来源权威性逐文件标记`;$('#page-info').textContent='';$('#pagination').innerHTML='';return;
    }
    items = (view==='papers'?D.resources:D.questions).filter(matching).sort((a,b)=>b.year-a.year||a.contest.localeCompare(b.contest)||a.id.localeCompare(b.id,undefined,{numeric:true}));
    const pages = Math.max(1,Math.ceil(items.length/SIZE));page=Math.min(page,pages);
    $('#result-count').textContent=`找到 ${items.length} ${view==='papers'?'份资料记录':'道题目'}`;
    $('#page-info').textContent=`${page} / ${pages}`;
    $('#results').innerHTML = items.length?`<div class="grid">${items.slice((page-1)*SIZE,page*SIZE).map(view==='papers'?paperCard:questionCard).join('')}</div>`:'<div class="empty">没有符合条件的资料。可重置筛选，或查看「年份覆盖」了解收集缺口。</div>';
    $('#pagination').innerHTML=items.length?`<button id="prev" ${page===1?'disabled':''}>← 上一页</button><span>${page} / ${pages}</span><button id="next" ${page===pages?'disabled':''}>下一页 →</button>`:'';
    $('#prev')?.addEventListener('click',()=>{page--;render();});$('#next')?.addEventListener('click',()=>{page++;render();});
    document.querySelectorAll('[data-q]').forEach(b=>b.addEventListener('click',()=>openQuestion(b.dataset.q)));
  }

  function images(segments) {
    return segments.map(s=>`<div class="reader-page"><p>原卷第 ${s.page} 页 · ${link(s.image,'查看大图')}</p><img src="${safe(s.image)}" alt="原卷第 ${s.page} 页切片" loading="lazy"><div class="image-error notice" role="alert" hidden><p>切片加载失败。若使用本地网址，请确认阅读服务仍在运行：<code>python3 scripts/serve.py --background</code>，然后重试。</p><button type="button" data-retry-image>重新加载图片</button> ${link(s.image,'直接打开切片')}</div></div>`).join('');
  }

  $('#reader-body').addEventListener('error',event=>{
    if(!event.target.matches('img'))return;
    event.target.hidden=true;
    event.target.closest('.reader-page').querySelector('.image-error').hidden=false;
  },true);
  $('#reader-body').addEventListener('load',event=>{
    if(!event.target.matches('img'))return;
    event.target.hidden=false;
    event.target.closest('.reader-page').querySelector('.image-error').hidden=true;
  },true);
  $('#reader-body').addEventListener('click',event=>{
    const button=event.target.closest('[data-retry-image]');
    if(!button)return;
    const image=button.closest('.reader-page').querySelector('img');
    image.loading='eager';
    const url=new URL(image.src);url.searchParams.set('retry',Date.now());image.src=url.href;
  });

  function renderTeachingPanel(q) {
    const t = q.teaching;
    if (!t) {
      return `<p class="notice">本题尚未完成盲解与教学拆解记录。你可以先在「题目」页签独立尝试解答，再到「参考解答」核对思路。</p>`;
    }
    const outcomeCls = t.outcome === 'correct' ? 'ok' : t.outcome === 'different_valid_method' ? 'alt' : 'warn';
    return `
      <div class="teach-shell">
        <div class="teach-meta-box">
          <div class="teach-meta-row">
            <span class="teach-badge ${outcomeCls}">${esc(t.outcome_label)}</span>
            <span class="chip">${esc(q.level)}竞赛生教学</span>
            ${(t.topic_tags||[]).map(x=>`<span class="chip">${esc(x)}</span>`).join('')}
          </div>
          <div class="chips">${teachingChips(q)}</div>
          <p class="teach-takeaway"><strong>核心教学收获：</strong>${esc(t.teaching_takeaway)}</p>
        </div>

        <section class="teach-section">
          <h4>一、问题拆解（如何读题与找切入点）</h4>
          <ol class="teach-list">${t.problem_decomposition.map(p=>`<li><strong>${esc(p.step)}</strong><p>${esc(p.detail)}</p></li>`).join('')}</ol>
        </section>

        <section class="teach-section">
          <h4>二、核心难点剖析（卡在哪里）</h4>
          <div class="teach-cards">${t.difficulties.map(d=>`<article class="teach-card diff"><h5>${esc(d.title)}</h5><p>${esc(d.detail)}</p></article>`).join('')}</div>
        </section>

        <section class="teach-section">
          <h4>三、答案拆解（逻辑骨架与每步动机）</h4>
          <ol class="teach-list">${t.solution_breakdown.map(s=>`<li><strong>${esc(s.step)}</strong><p class="motivation"><em>思考动机：</em>${esc(s.motivation)}</p><p>${esc(s.detail)}</p></li>`).join('')}</ol>
        </section>

        <section class="teach-section">
          <h4>四、易错点分析（常见失分与避坑指南）</h4>
          <div class="teach-cards">${t.common_pitfalls.map(e=>`
            <article class="teach-card pitfall">
              <h5>${esc(e.title)}</h5>
              <p><strong>易错做法：</strong>${esc(e.mistake)}</p>
              <p><strong>错因剖析：</strong>${esc(e.why_wrong)}</p>
              <p><strong>避坑检查：</strong>${esc(e.how_to_avoid)}</p>
            </article>`).join('')}
          </div>
        </section>

        <details class="blind-review">
          <summary>展开「只看原题盲解复盘」记录（${esc(t.outcome_label)}）</summary>
          <div class="blind-body">
            <p><strong>对照复盘结论：</strong>${esc(t.comparison_summary)}</p>
            <p><strong>盲解切入思路：</strong>${esc(t.blind_attempt.approach)}</p>
            <p><strong>盲解推演步骤：</strong></p>
            <ul>${t.blind_attempt.steps.map(st=>`<li>${esc(st)}</li>`).join('')}</ul>
            <p><strong>盲解答案 / 结论：</strong></p>
            <div class="blind-answer">${esc(t.blind_attempt.final_answer)}</div>
            ${(t.blind_attempt.uncertainties&&t.blind_attempt.uncertainties.length)?`<p><strong>盲解时的疑虑与风险点：</strong></p><ul>${t.blind_attempt.uncertainties.map(u=>`<li>${esc(u)}</li>`).join('')}</ul>`:''}
          </div>
        </details>
      </div>`;
  }

  function readerRender() {
    const q=selected,r=rmap[q.resource_id];
    $('#reader-kicker').textContent=`${q.contest} / ${q.year} / Q${q.number} · ${q.level}`;
    $('#reader-title').textContent=q.title;
    $('#blind-toggle').textContent = `盲练遮罩：${blindMask ? '开' : '关'}`;
    $('#blind-toggle').classList.toggle('active', blindMask);
    document.querySelectorAll('[data-panel]').forEach(b=>b.classList.toggle('active',b.dataset.panel===panel));
    if(D.mode==='public'&&panel!=='provenance') {
      const tagNotice = panel==='teaching'&&q.teaching_tags?.length ? `<div class="chips">${teachingChips(q)}</div>` : '';
      $('#reader-body').innerHTML=`<p class="notice">公开索引不包含题目正文、解答与完整教学解析。${link(r.source_url,'查看原始来源')}</p>${tagNotice}`;return;
    }
    if(panel==='provenance') {
      const allTags = [authority[r.authority], ...(q.tags||[]), ...(q.teaching_tags||[])].filter(Boolean);
      $('#reader-body').innerHTML=`<dl class="provenance"><dt>来源网页</dt><dd>${link(r.source_url,'打开来源网页')}</dd><dt>来源文件</dt><dd>${link(r.url,'打开来源文件')}</dd><dt>归档位置</dt><dd>${esc(r.archive_member||r.local_path||r.id)}</dd><dt>标签与教学标注</dt><dd>${esc(allTags.join(' / '))}</dd><dt>教学记录方式</dt><dd>${q.has_teaching ? '严格盲解（只看原题尝试）→ 对照参考解答复盘拆解' : '待补充'}</dd></dl>`;return;
    }
    if(panel==='solution') {
      $('#reader-body').innerHTML=q.solution?`${images(q.solution.segments)}`:`<p class="notice">参考解答尚未单独整理。${r.local_path?' '+link(r.local_path,'查看整卷'):''}</p>`;return;
    }
    if(panel==='teaching') {
      $('#reader-body').innerHTML = renderTeachingPanel(q);
      if(window.renderMathInElement)window.renderMathInElement($('#reader-body'),MATH_OPTS);
      return;
    }
    const bodyText = q.body_zh || q.teaching?.problem_statement_zh || '';
    const statement = bodyText ? `<div class="statement">${esc(bodyText)}</div>` : '<p class="notice">本题中文正文正在逐题整理，现可展开查看原卷。</p>';
    const tagBar = q.has_teaching ? (blindMask
      ? `<p class="blind-note">盲练遮罩已开启：方法与易错标签已隐藏，防止提前剧透。</p>`
      : `<div class="chips teach-strip">${teachingChips(q)}</div>`) : '';
    const hintBox = (q.teaching?.problem_decomposition?.length)
      ? `<details class="training-hint"><summary>卡住了？展开「问题拆解引导」（不含答案）</summary><ol class="teach-list">${q.teaching.problem_decomposition.map(p=>`<li><strong>${esc(p.step)}</strong><p>${esc(p.detail)}</p></li>`).join('')}</ol></details>`
      : '';
    $('#reader-body').innerHTML=`${tagBar}${statement}${hintBox}<details class="original"><summary>展开题目原图</summary>${images(q.segments)}</details>`;
    if(window.renderMathInElement)window.renderMathInElement($('#reader-body'),MATH_OPTS);
  }

  function openQuestion(id) {
    selected=D.questions.find(q=>q.id===(D.aliases?.[id]||id));if(!selected)return;
    panel='question';readerRender();if(!$('#reader').open)$('#reader').showModal();
    history.replaceState(null,'',`#q=${encodeURIComponent(id)}`);
  }

  $('#blind-toggle').addEventListener('click',()=>{blindMask=!blindMask;if(selected)readerRender();});
  $('#close-reader').addEventListener('click',()=>$('#reader').close());
  $('#reader').addEventListener('close',()=>{history.replaceState(null,'',location.pathname+location.search+'#explore');});
  document.querySelectorAll('[data-panel]').forEach(b=>b.addEventListener('click',()=>{panel=b.dataset.panel;readerRender();}));
  document.querySelectorAll('[data-view]').forEach(b=>b.addEventListener('click',()=>{view=b.dataset.view;page=1;document.querySelectorAll('[data-view]').forEach(x=>x.classList.toggle('active',x===b));render();}));
  for(const id of ['search','contest','year','level','tag','teaching-tag','edition']) $('#'+id).addEventListener(id==='search'?'input':'change',()=>{page=1;render();});
  $('#reset').addEventListener('click',()=>{for(const id of ['search','contest','year','level','tag','teaching-tag','edition'])$('#'+id).value='';page=1;render();});
  render();
  if(location.hash.startsWith('#q='))openQuestion(decodeURIComponent(location.hash.slice(3)));
})();
