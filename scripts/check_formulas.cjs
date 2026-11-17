#!/usr/bin/env node
// Validate the exact visual editions and teaching records served by the reader, without network/CDN.
const fs = require('node:fs');
const path = require('node:path');
const katex = require('../web/vendor/katex/katex.js');
const root = path.resolve(__dirname, '..');
let questions = 0, teachingQuestions = 0, formulas = 0;
const errors = [];

function checkText(label, body) {
  if (typeof body !== 'string') return;
  const matches = [...body.matchAll(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g)];
  const rest = body.replace(/\\\(([\s\S]*?)\\\)|\\\[([\s\S]*?)\\\]/g, '');
  if (/\\[()[\]]/.test(rest)) errors.push(`${label}: unmatched math delimiter`);
  for (const match of matches) {
    formulas++;
    try { katex.renderToString(match[1] ?? match[2], {throwOnError:true, strict:'error', displayMode:match[2]!==undefined}); }
    catch (error) { errors.push(`${label}: ${error.message}`); }
  }
}

function walkStrings(label, val) {
  if (typeof val === 'string') checkText(label, val);
  else if (Array.isArray(val)) val.forEach((v, i) => walkStrings(`${label}[${i}]`, v));
  else if (val && typeof val === 'object') Object.entries(val).forEach(([k, v]) => walkStrings(`${label}.${k}`, v));
}

for (const name of fs.readdirSync(path.join(root, 'catalog/editorial')).filter(n=>n.endsWith('.json'))) {
  const edition = JSON.parse(fs.readFileSync(path.join(root, 'catalog/editorial', name), 'utf8'));
  for (const q of edition.questions) {
    questions++;
    checkText(`${name} #${q.number}`, q.body_zh);
  }
}

const teachingDir = path.join(root, 'catalog/teaching');
if (fs.existsSync(teachingDir)) {
  for (const name of fs.readdirSync(teachingDir).filter(n=>n.endsWith('.json'))) {
    const pack = JSON.parse(fs.readFileSync(path.join(teachingDir, name), 'utf8'));
    for (const q of pack.questions) {
      teachingQuestions++;
      walkStrings(`${name} ${q.id}`, q.blind_attempt);
      walkStrings(`${name} ${q.id}`, q.analysis);
    }
  }
}

console.log(JSON.stringify({questions, teachingQuestions, formulas, errors}, null, 2));
process.exitCode = errors.length ? 1 : 0;
