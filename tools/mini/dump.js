// Dumpt die Lerndaten einer App als JSON für das Training der Mini-KI
const fs=require('fs');const set=process.argv[2];
const files={id:["head.js","data_a1.js","data_a2.js","data_b1.js","data_b2.js","extra_id.js"],en:["head_plain.js","data_en_a1.js","data_en_a2.js","data_en_b1.js","data_en_b2.js","extra_en.js"],de:["head_plain.js","data_de_a1.js","data_de_a2.js","data_de_b1.js","data_de_b2.js","extra_de.js"]}[set];
let code=files.map(f=>fs.readFileSync(f,"utf8")).join("\n").replace(/^"use strict";/gm,"");
const UNITS=(new Function(code+";return UNITS;"))();
const strip=t=>String(t).split(" – ")[0].trim();
const out={vocab:[],sent:[],lines:[],grammar:[]};
for(const u of UNITS){
 u.vocab.forEach(v=>out.vocab.push([strip(v[0]),v[1]]));
 u.sent.forEach(v=>out.sent.push([v[0],v[1]]));
 u.dlg.lines.forEach(l=>out.lines.push([l[1],l[2]]));
 out.grammar.push(u.grammar.t);
}
fs.writeFileSync("mini/data_"+set+".json",JSON.stringify(out));
console.log(set,out.vocab.length,out.sent.length,out.lines.length);
