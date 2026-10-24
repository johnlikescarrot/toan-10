#!/usr/bin/env node
/* Render one TeX expression per JSON input line to SVG.
 * The Python build script owns this short-lived process.
 */
const fs = require('fs');
const path = require('path');
const readline = require('readline');
const {mathjax} = require('mathjax-full/js/mathjax.js');
const {TeX} = require('mathjax-full/js/input/tex.js');
const {SVG} = require('mathjax-full/js/output/svg.js');
const {liteAdaptor} = require('mathjax-full/js/adaptors/liteAdaptor.js');
const {RegisterHTMLHandler} = require('mathjax-full/js/handlers/html.js');
const {AllPackages} = require('mathjax-full/js/input/tex/AllPackages.js');

const outputDir = process.argv[2];
if (!outputDir) throw new Error('Missing SVG output directory');
fs.mkdirSync(outputDir, {recursive: true});

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);
const tex = new TeX({packages: AllPackages});
const svg = new SVG({fontCache: 'none'});
const html = mathjax.document('', {InputJax: tex, OutputJax: svg});

const rl = readline.createInterface({input: process.stdin, crlfDelay: Infinity});
rl.on('line', (line) => {
  if (!line.trim()) return;
  try {
    const request = JSON.parse(line);
    const node = html.convert(request.tex, {display: !!request.display});
    const container = adaptor.outerHTML(node);
    const match = container.match(/<svg\b[\s\S]*<\/svg>/);
    if (!match) throw new Error('MathJax did not return SVG');
    let markup = match[0].replace(/currentColor/g, '#16324F');
    const file = `${request.key}.svg`;
    fs.writeFileSync(path.join(outputDir, file), markup);
    const svgTag = markup.slice(0, markup.indexOf('>') + 1);
    const viewBox = (svgTag.match(/viewBox="([^"]+)"/) || [])[1];
    const height = (svgTag.match(/height="([0-9.]+)ex"/) || [])[1];
    const valign = (container.match(/vertical-align:\s*(-?[0-9.]+)ex/) || [])[1];
    const parts = viewBox.split(/\s+/).map(Number);
    process.stdout.write(JSON.stringify({
      file,
      viewWidth: parts[2],
      viewHeight: parts[3],
      heightEx: Number(height || 0),
      depthEx: Math.abs(Number(valign || 0))
    }) + '\n');
  } catch (error) {
    process.stdout.write(JSON.stringify({error: String(error && error.stack || error)}) + '\n');
  }
});
