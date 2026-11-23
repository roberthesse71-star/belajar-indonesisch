/* ---------- Groq-Anbindung (nur Indonesisch-App): Spracherkennung (Whisper groß) + ausführlicher Lehrer ---------- */
const GQ={
  base:"https://api.groq.com/openai/v1",
  key(){try{return localStorage.getItem("gq_key")||"";}catch(e){return "";}},
  setKey(k){try{k?localStorage.setItem("gq_key",k.trim()):localStorage.removeItem("gq_key");}catch(e){}},
  get(n,d){try{return localStorage.getItem("gq_"+n)||d;}catch(e){return d;}},
  put(n,v){try{localStorage.setItem("gq_"+n,v);}catch(e){}},
  ok(){return !!GQ.key();},
  last:"",
  async call(path,opt){
    const r=await fetch(GQ.base+path,Object.assign({headers:{"Authorization":"Bearer "+GQ.key()}},opt,{headers:Object.assign({"Authorization":"Bearer "+GQ.key()},(opt&&opt.headers)||{})}));
    if(!r.ok){let m="";try{const j=await r.json();m=(j&&j.error&&j.error.message)||"";}catch(e){}
      const err=new Error("Groq "+r.status+(m?": "+m:""));err.status=r.status;err.msg=m;throw err;}
    return r;
  },
  async models(){const r=await GQ.call("/models");const j=await r.json();return (j.data||[]).map(m=>m.id);},
  async pickModel(){
    const ids=await GQ.models();
    const bad=/whisper|guard|tts|playai|distil|embed|vision-preview|orpheus/i;
    const pref=["llama-3.3-70b-versatile","openai/gpt-oss-120b","meta-llama/llama-4-scout-17b-16e-instruct","qwen/qwen3-32b","llama-3.1-8b-instant","openai/gpt-oss-20b"];
    const chat=ids.filter(x=>!bad.test(x));
    const m=pref.find(p=>chat.includes(p))||chat[0];
    if(m){GQ.put("model",m);tlog("Groq: Modell "+m);}
    return m;
  },
  model(){return GQ.get("model","llama-3.3-70b-versatile");},
  /* Chat-Antwort; bei unbekanntem Modell automatisch neues wählen */
  async chat(messages,o){
    o=o||{};
    const go=async()=>{
      const body={model:GQ.model(),messages,temperature:o.temp==null?.4:o.temp,max_tokens:o.max||650};
      const r=await GQ.call("/chat/completions",{method:"POST",headers:{"Content-Type":"application/json"},body:JSON.stringify(body)});
      const j=await r.json();return String((j.choices&&j.choices[0]&&j.choices[0].message&&j.choices[0].message.content)||"").replace(/<think>[\s\S]*?<\/think>/g,"").trim();
    };
    try{return await go();}
    catch(e){
      if(e.status===404||e.status===400&&/model|decommission/i.test(e.msg||"")){const m=await GQ.pickModel();if(m)return await go();}
      throw e;
    }
  },
  /* Spracherkennung: Whisper groß über Groq (rohe 16-kHz-Samples → WAV) */
  async stt(pcm){
    const wav=pmWav(pcm);
    const mk=model=>{const f=new FormData();f.append("file",wav,"aufnahme.wav");f.append("model",model);f.append("language",CFG.tl==="id"?"id":CFG.tl);f.append("response_format","json");f.append("temperature","0");return f;};
    const t0=Date.now();let model=GQ.get("stt","whisper-large-v3-turbo"),r;
    try{r=await GQ.call("/audio/transcriptions",{method:"POST",body:mk(model)});}
    catch(e){if(e.status===404||e.status===400){model="whisper-large-v3";r=await GQ.call("/audio/transcriptions",{method:"POST",body:mk(model)});GQ.put("stt",model);}else throw e;}
    const j=await r.json();const t=String(j.text||"").replace(/\s+/g," ").trim();
    tlog("Groq "+model+": \""+t+"\" ("+Math.round((Date.now()-t0)/100)/10+" s)");return t;
  },
  /* Lehrer-Kontext der aktuellen Lektion */
  ctx(){
    let u=null;try{u=otUnit();}catch(e){}
    if(!u)return "";
    const v=ITEMS.filter(x=>x.u===u.id&&x.k==="v").slice(0,30).map(x=>stripG(x.idn)+" = "+x.de).join("; ");
    const s=ITEMS.filter(x=>x.u===u.id&&x.k==="s").slice(0,8).map(x=>stripG(x.idn)+" = "+x.de).join("; ");
    let g="";try{g=stripHtml(u.grammar.html).slice(0,900);}catch(e){}
    return "Aktuelle Lektion "+u.n+" („"+u.t+"“, Niveau "+(S.level||"A1")+").\nGrammatik: "+(u.grammar&&u.grammar.t||"")+" – "+g+"\nWörter: "+v+"\nSätze: "+s;
  },
  sys(){
    return "Du bist ein geduldiger, warmherziger Indonesisch-Lehrer für deutschsprachige Lernende (Niveau "+(S.level||"A1")+"). "+
    "Antworte immer auf Deutsch. Indonesische Beispiele stehen in „…“ und bekommen direkt die deutsche Übersetzung. "+
    "Erkläre klar und konkret, mit 2–4 Beispielsätzen, typischen Fehlern deutscher Lernender und einer Eselsbrücke, wenn sie passt. "+
    "Sprich so, wie ein Lehrer im Unterricht redet (kein Markdown, keine Sternchen, keine Überschriften, keine Tabellen). "+
    "Halte dich kurz genug für ein Handy (höchstens ca. 170 Wörter). Erfinde keine Wörter; wenn du unsicher bist, sag es. "+
    "Gib nur Indonesisch in der heutigen Standardsprache (Bahasa Indonesia) an.\n\n"+GQ.ctx();
  },
  hist(){
    const C=V.chat;return C.msgs.slice(-8).filter(m=>m.text&&!m.opts0).map(m=>({role:m.role==="assistant"?"assistant":"user",content:String(m.text).slice(0,600)}));
  },
  clean(t){return String(t||"").replace(/\*\*|__|^#+\s*/gm,"").replace(/^\s*[-*]\s+/gm,"• ").trim();},
  async answer(q){
    const msgs=[{role:"system",content:GQ.sys()}].concat(GQ.hist().slice(0,-1),[{role:"user",content:q}]);
    return GQ.clean(await GQ.chat(msgs,{max:520}));
  },
  async explain(text){
    const msgs=[{role:"system",content:GQ.sys()},{role:"user",content:"Erkläre mir diesen Unterrichtsstoff ausführlicher, als wäre ich bei dir im Unterricht. Gehe auf Aussprache, Gebrauch und typische Fehler ein und gib 3 neue Beispielsätze mit Übersetzung:\n\n"+text}];
    return GQ.clean(await GQ.chat(msgs,{max:700}));
  },
  async why(target,heard,de){
    const msgs=[{role:"system",content:GQ.sys()},{role:"user",content:"Die richtige Antwort war „"+target+"“ ("+de+"), ich habe „"+heard+"“ gesagt. Erkläre mir in höchstens 3 Sätzen, was ich falsch gemacht habe und wie ich es mir merke."}];
    return GQ.clean(await GQ.chat(msgs,{max:230}));
  },
  errText(e){
    const s=e&&e.status;
    if(s===401)return "Der Groq-Schlüssel wurde abgelehnt (401). Prüfe den Schlüssel im Lehrer-Bereich unter „🔑 Groq-KI“.";
    if(s===429)return "Groq-Limit erreicht (429). Warte kurz und versuche es noch einmal – bis dahin hilft der einfache Lehrer.";
    if(e&&/Failed to fetch|NetworkError|Load failed/i.test(e.message||""))return "Keine Verbindung zu Groq. Prüfe das Internet (oder einen Adblocker).";
    return "Groq-Fehler: "+((e&&e.message)||e);
  },
  card(){
    const k=GQ.key(),mask=k?("…"+k.slice(-4)):"";
    return `<div class="card" id="gqcard"><b>🔑 Groq-KI (optional)</b>
     <div class="small" style="margin:6px 0">${k?"Verbunden ("+esc(mask)+"). Der Lehrer erklärt jetzt ausführlicher und die Spracherkennung läuft über Whisper groß.":"Mit einem Groq-Schlüssel erklärt der Lehrer ausführlicher, beantwortet freie Fragen und die Spracherkennung wird deutlich genauer. Der Schlüssel bleibt nur in deinem Browser. Kostenlos erhältlich auf console.groq.com/keys."}</div>
     <input id="gqk" type="password" autocomplete="off" placeholder="gsk_…" style="width:100%;box-sizing:border-box;margin-bottom:8px;padding:10px;border-radius:10px;border:1px solid var(--line);background:var(--card,#fff);color:inherit;font-size:16px">
     <div class="row"><button class="btn sm pri" data-act="gqSave">Speichern &amp; testen</button>${k?`<button class="btn sm" data-act="gqOff">Entfernen</button>`:""}</div>
     <div class="small" id="gqst" style="margin-top:6px">${esc(GQ.last)}</div></div>`;
  },
  async save(){
    const el=$("#gqk"),v=el&&el.value.trim();const st=$("#gqst");const say=t=>{GQ.last=t;if(st)st.textContent=t;};
    if(!v){say("Bitte zuerst den Schlüssel eintragen.");return;}
    GQ.setKey(v);say("Teste die Verbindung …");
    try{const m=await GQ.pickModel();const t=await GQ.chat([{role:"user",content:"Antworte nur mit dem Wort: Halo"}],{max:12,temp:0});
      GQ.last="✅ Verbunden – Modell "+(m||GQ.model())+" antwortet: "+t.slice(0,30);toast("Groq verbunden ✅");}
    catch(e){GQ.setKey("");GQ.last="❌ "+GQ.errText(e);}
    render();
  },
  off(){GQ.setKey("");GQ.last="";render();}
};

/* ---------- Groq-Lehrer: führt durch die Lektion, erklärt Grammatik, spricht alles vor ---------- */
GQ.spoken="Dein Text wird laut vorgelesen: keine Aufzählungszeichen, keine Klammern, keine Sternchen, keine Tabellen; Indonesisch immer in „…“; kurze, klare Sätze wie im Unterricht. ";
GQ.rate=function(){const r=parseFloat(GQ.get("rate","1"));return r>0?r:1;};
GQ.setRate=function(r){GQ.put("rate",String(r));};
GQ.msgs=function(user,max){return [{role:"system",content:GQ.sys()+" "+GQ.spoken},{role:"user",content:user}];};
GQ.intro=async function(u){
  return GQ.clean(await GQ.chat(GQ.msgs("Begrüße mich herzlich und starte Lektion "+u.n+" („"+u.t+"“). Sag in 3–5 Sätzen, was wir heute lernen, wozu es im Alltag nützt und wie wir vorgehen (erst Grundlagen, dann Wörter, Sätze, Übungen, Dialog, Abfrage). Keine Lernziel-Liste.",1),{max:260}));
};
/* Grammatik in 2–3 Teilen, Teile durch eine Zeile mit --- getrennt */
GQ.grammar=async function(u){
  let g="";try{g=stripHtml(u.grammar.html).slice(0,3200);}catch(e){}
  const t=await GQ.chat(GQ.msgs("Bring mir jetzt die Grammatik dieser Lektion bei: „"+(u.grammar&&u.grammar.t||u.t)+"“.\nVorlage (Stoff):\n"+g+"\n\nErkläre sie in 2 oder 3 Teilen, jeder Teil höchstens 110 Wörter. Jeder Teil behandelt EINEN Gedanken: Regel in einfachen Worten, dann 2–3 Beispiele („Indonesisch“ – Deutsch), dann ein typischer Fehler deutscher Lerner. Der letzte Teil endet mit einer kurzen Merkhilfe. Trenne die Teile mit einer Zeile, die nur --- enthält. Keine Überschriften, kein „Teil 1“.",1),{max:900,temp:.35});
  const parts=GQ.clean(t).split(/\n\s*-{3,}\s*\n/).map(x=>x.trim()).filter(x=>x.length>20);
  return parts.length?parts.slice(0,3):[GQ.clean(t)];
};
GQ.words=async function(u,blk,first){
  const list=blk.map(it=>"„"+stripG(it.idn)+"“ = "+it.de+(it.ph?" (Aussprache: "+it.ph+")":"")).join("; ");
  return GQ.clean(await GQ.chat(GQ.msgs((first?"Wir beginnen mit dem Wortschatz. ":"")+"Stelle mir diese neuen Wörter vor: "+list+".\nSag zu jedem Wort in 1–2 Sätzen: Bedeutung, wie man es benutzt (mit einem kurzen Beispielsatz) oder eine Eselsbrücke – insgesamt höchstens 80 Wörter. Danach sage ich sie dir nach.",1),{max:300}));
};
GQ.mistake=async function(target,heard,de,kind){
  return GQ.clean(await GQ.chat(GQ.msgs("Ich habe bei der Übung ("+kind+") „"+heard+"“ gesagt, richtig wäre „"+target+"“"+(de?" ("+de+")":"")+". Erkläre mir in höchstens 2 kurzen Sätzen, was der Unterschied ist, und gib eine Merkhilfe. Nicht schimpfen, freundlich bleiben.",1),{max:170,temp:.3}));
};
GQ.wrap=async function(u,fr,fn,weak){
  return GQ.clean(await GQ.chat(GQ.msgs("Wir haben Lektion "+u.n+" („"+u.t+"“) beendet. Abfrage: "+fr+" von "+fn+" richtig."+(weak.length?" Schwach waren: "+weak.join(", ")+".":"")+" Fasse in 3–4 Sätzen zusammen, was ich gelernt habe, lobe konkret und sag, was ich als Nächstes üben sollte.",1),{max:220}));
};
/* Lektionstext vorlesen: Deutsch normal, Indonesisch langsamer; gibt true zurück, wenn bis zum Ende gelesen wurde */
