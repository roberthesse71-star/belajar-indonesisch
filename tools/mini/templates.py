# Satzmuster für die Absichtserkennung der Mini-KI. {w}=Wort/Phrase, {n}=Bedeutung, {g}=Grammatikthema, {l}=Sprachname
T = {
 "meaning": {
  "de": ["was bedeutet {w}", "was heißt {w}", "was heisst {w}", "was ist {w}", "bedeutung von {w}", "{w} was heißt das", "{w} was bedeutet das", "was soll {w} heißen",
         "kannst du mir sagen was {w} heißt", "ich weiß nicht was {w} bedeutet", "weißt du was {w} bedeutet", "was heißt {w} auf deutsch", "was ist {w} auf deutsch", "bedeutet {w} etwas",
         "was meint man mit {w}", "sag mir was {w} heißt", "kannst du {w} erklären", "übersetz mir bitte {w} ins deutsche", "wat heisst {w}", "was is {w}", "{w} bedeutung", "{w}?", "was heißt denn {w}", "wie übersetzt man {w}"],
  "en": ["what does {w} mean", "what is {w}", "meaning of {w}", "what is the meaning of {w}", "can you tell me what {w} means", "i dont know what {w} means", "{w} means what",
         "what does {w} mean in english", "what is {w} in english", "translate {w} to english", "whats {w}", "wat is {w}", "explain {w}", "do you know what {w} means", "{w} meaning please", "tell me what {w} means", "what does it mean {w}"],
 },
 "translate": {
  "de": ["wie sagt man {n}", "wie sage ich {n}", "wie heißt {n} auf {l}", "{n} auf {l}", "wie sagt man {n} auf {l}", "übersetze {n} auf {l}", "übersetze {n}", "ich möchte {n} sagen",
         "wie kann ich {n} sagen", "wie sagt man das {n}", "{n} auf {l} bitte", "was heißt {n} auf {l}", "kannst du mir sagen wie man {n} sagt", "wie drückt man {n} aus", "wie sagt man denn {n}", "wie sag ich {n} auf {l}", "{n} in {l}", "wie spricht man {n} auf {l}"],
  "en": ["how do you say {n}", "how to say {n} in {l}", "how do i say {n}", "translate {n} to {l}", "{n} in {l}", "{n} in {l} please", "i want to say {n}", "how can i say {n} in {l}",
         "what is {n} in {l}", "how would you say {n}", "say {n} in {l}", "how do u say {n}", "whats {n} in {l}", "can you tell me how to say {n} in {l}", "translate {n}"],
 },
 "example": {
  "de": ["gib mir ein beispiel mit {w}", "beispiel mit {w}", "beispielsatz für {w}", "beispielsatz mit {w}", "wie benutzt man {w}", "{w} in einem satz", "satz mit {w}", "zeig mir sätze mit {w}",
         "kannst du mir ein beispiel für {w} geben", "wie verwendet man {w}", "ich brauche ein beispiel für {w}", "nenne einen satz mit {w}", "gibt es beispiele mit {w}", "{w} beispiel", "bsp mit {w}", "wie baue ich einen satz mit {w}"],
  "en": ["example with {w}", "give me an example with {w}", "use {w} in a sentence", "show me a sentence with {w}", "sentence with {w}", "example sentence for {w}", "how do you use {w}", "can you give me an example of {w}",
         "i need an example for {w}", "examples of {w}", "{w} example", "how to use {w} in a sentence", "make a sentence with {w}"],
 },
 "grammar": {
  "de": ["erkläre die grammatik", "erkläre mir {g}", "erklär {g}", "wie funktioniert {g}", "regel für {g}", "ich verstehe {g} nicht", "grammatik zu {g}", "was ist die regel bei {g}", "erkläre {g} bitte",
         "kannst du mir {g} erklären", "wie geht {g}", "ich checke {g} nicht", "hilf mir bei {g}", "grammatik {g}", "wie bildet man {g}", "wann benutzt man {g}", "ich habe probleme mit {g}", "wie war das mit {g}", "grammatikregel", "erkläre die grammatik dieser lektion"],
  "en": ["explain the grammar", "explain {g}", "how does {g} work", "what is the rule for {g}", "i dont understand {g}", "grammar for {g}", "help me with {g}", "can you explain {g}", "how do you form {g}",
         "when do i use {g}", "grammar rule", "i have problems with {g}", "{g} please explain", "explain the grammar of this lesson", "what is the rule here"],
 },
 "repeat": {
  "de": ["nochmal", "noch einmal", "noch mal bitte", "wiederhole das", "sag das nochmal", "kannst du das wiederholen", "bitte nochmal", "wie bitte", "was hast du gesagt", "nochmal bitte", "kannst du das noch mal sagen", "wiederholen", "ich habe es nicht verstanden sag es nochmal", "hä nochmal"],
  "en": ["again", "say it again", "repeat please", "once more", "can you repeat that", "one more time", "what did you say", "repeat", "pardon", "say that again", "could you say that once more"],
 },
 "slow": {
  "de": ["langsamer", "sprich langsamer", "sprich langsamer bitte", "kannst du langsam sprechen", "bitte langsam", "das war zu schnell", "etwas langsamer", "sag es langsam", "langsam bitte", "nochmal langsam"],
  "en": ["slower", "speak slowly", "speak slower please", "can you speak slowly", "too fast", "slowly please", "say it slowly", "a bit slower", "slow down"],
 },
 "whatmeant": {
  "de": ["was bedeutet das", "was heißt das", "was heisst das", "übersetze das", "und auf deutsch", "und auf deutsch?", "was soll das heißen", "ich verstehe das nicht", "übersetzung", "was bedeutet das denn", "kannst du das übersetzen", "was hast du damit gemeint", "bedeutung bitte", "was heißt das auf deutsch"],
  "en": ["what does that mean", "what does this mean", "translate that", "translate this", "and in english", "i dont understand", "translation please", "what did you mean", "meaning please", "what is that in english"],
 },
 "dialog": {
  "de": ["dialog", "dialog bitte", "lass uns ein rollenspiel machen", "rollenspiel", "wir spielen ein gespräch", "ich möchte ein gespräch üben", "können wir einen dialog üben", "spielen wir einen dialog", "starte einen dialog", "lass uns sprechen üben", "gespräch üben", "kannst du mit mir ein gespräch führen", "ich will ein rollenspiel", "lass uns reden", "rollenspiel starten"],
  "en": ["dialogue", "dialog please", "lets do a role play", "role play", "start a dialogue", "can we practice a conversation", "lets have a conversation", "i want to practise speaking", "lets talk", "can we play a dialogue", "start role play", "conversation practice"],
 },
 "stop": {
  "de": ["stopp", "stop", "ende", "genug", "hör auf", "abbrechen", "beenden", "ich will aufhören", "das reicht", "lass uns aufhören", "schluss", "dialog beenden", "mach mal pause", "nicht mehr"],
  "en": ["stop", "end", "enough", "quit", "cancel", "i want to stop", "that is enough", "lets stop", "finish", "end dialogue", "stop it", "no more"],
 },
 "help": {
  "de": ["hilfe", "was kannst du", "was kann ich dich fragen", "wie funktioniert das hier", "was kannst du alles", "hilf mir", "was kann ich hier machen", "wie benutze ich dich", "was sind deine funktionen", "ich weiß nicht was ich fragen soll", "was geht hier", "hilfe bitte"],
  "en": ["help", "what can you do", "what can i ask you", "how does this work", "what are your features", "help me", "how do i use you", "i dont know what to ask", "what can i do here", "please help"],
 },
 "whoareyou": {
  "de": ["wer bist du", "bist du eine ki", "bist du ein mensch", "was bist du", "wer hat dich gebaut", "bist du ein roboter", "wie heißt du", "stell dich vor", "bist du chatgpt", "bist du echt", "was für ein programm bist du"],
  "en": ["who are you", "are you an ai", "are you human", "what are you", "who made you", "are you a robot", "whats your name", "introduce yourself", "are you chatgpt", "are you real", "what kind of program are you"],
 },
 "thanks": {
  "de": ["danke dir", "vielen dank", "dankeschön", "super danke", "danke für die hilfe", "ok danke", "das war hilfreich danke", "danke schön", "great danke", "perfekt danke", "cool danke dir", "besten dank"],
  "en": ["thank you very much", "thanks a lot", "thanks for the help", "ok thanks", "that was helpful thanks", "great thank you", "cheers thanks", "many thanks", "perfect thanks", "thanks so much"],
 },
 "quiz": {
  "de": ["frag mich was", "teste mich", "stell mir eine frage", "quiz", "ich will getestet werden", "gib mir eine aufgabe", "prüfe mich", "frag mich ab", "lass uns ein quiz machen", "übungsaufgabe bitte", "frag mich vokabeln ab", "kannst du mich abfragen", "teste mich mal"],
  "en": ["quiz me", "test me", "ask me something", "ask me a question", "give me a task", "i want a quiz", "lets do a quiz", "test my vocabulary", "give me an exercise", "can you quiz me", "examine me"],
 },
 "pronounce": {
  "de": ["wie spricht man {w} aus", "aussprache von {w}", "wie sagt man {w} richtig", "sprich {w} aus", "sag {w}", "wie wird {w} ausgesprochen", "lies {w} vor", "wie klingt {w}", "kannst du {w} vorsprechen", "{w} aussprache", "ich möchte hören wie {w} klingt", "sprich mir {w} vor"],
  "en": ["how do you pronounce {w}", "pronunciation of {w}", "say {w}", "how is {w} pronounced", "read {w} aloud", "how does {w} sound", "can you say {w}", "{w} pronunciation", "i want to hear {w}", "pronounce {w}"],
 },
 "nextlesson": {
  "de": ["nächste lektion", "weiter zur nächsten lektion", "weiter", "ich bin fertig mit der lektion", "was kommt als nächstes", "zur nächsten lektion bitte", "bring mich zur nächsten lektion", "lass uns weitermachen", "ich will weiter lernen", "nächstes thema"],
  "en": ["next lesson", "go to the next lesson", "move on", "i am done with this lesson", "what comes next", "take me to the next lesson", "lets continue", "i want to keep learning", "next topic", "continue"],
 },
 "level": {
  "de": ["welches level habe ich", "was ist mein niveau", "auf welchem level bin ich", "wie gut bin ich", "wie weit bin ich", "mein fortschritt", "wie ist mein stand", "welche stufe bin ich", "wie viel habe ich gelernt"],
  "en": ["what is my level", "which level am i", "how good am i", "how far am i", "my progress", "what is my status", "what level do i have", "how much have i learned"],
 },
}
FILLERS_DE = ["äh", "mal", "bitte", "also", "hey", "sorry", "kurze frage", "du", "hm", "ok", "ey", "sag mal", "ähm", "tutor", "bitte bitte", "?", "mal eben"]
FILLERS_EN = ["uh", "please", "so", "hey", "sorry", "quick question", "um", "ok", "hm", "tutor", "hey tutor", "pls", "plz", "just", "?", "like"]
GRAMMAR = {
 "de": ["plural", "die vergangenheit", "das perfekt", "den artikel", "artikel", "den akkusativ", "den dativ", "die wortstellung", "die verneinung", "modalverben", "trennbare verben", "nebensätze", "die zeiten", "adjektivendungen", "den komparativ", "das passiv", "den konjunktiv", "relativsätze", "fragen", "pronomen", "präpositionen", "die höflichkeitsform", "verben", "die zukunft", "das präteritum", "present perfect", "past simple", "die bedingungssätze", "reflexive verben", "die satzstellung", "die affixe", "die vorsilben", "die endungen"],
 "en": ["the plural", "past tense", "the perfect", "articles", "the accusative", "the dative", "word order", "negation", "modal verbs", "separable verbs", "subordinate clauses", "tenses", "adjective endings", "the comparative", "the passive", "the subjunctive", "relative clauses", "questions", "pronouns", "prepositions", "politeness", "verbs", "the future", "the past simple", "present perfect", "conditionals", "reflexive verbs", "sentence structure", "prefixes", "endings"],
}
LANGNAMES = {
 "id": {"de": ["indonesisch", "auf indonesisch", "bahasa indonesia"], "en": ["indonesian", "bahasa indonesia"]},
 "en": {"de": ["englisch", "auf englisch"], "en": ["english"]},
 "de": {"de": ["deutsch", "auf deutsch"], "en": ["german", "in german"]},
}
OFFTOPIC = {
 "de": ["wie ist das wetter morgen", "was gibt es heute zum essen", "wie viel kostet ein flug nach new york", "wer hat die fußball weltmeisterschaft gewonnen", "erzähl mir einen witz", "was ist der sinn des lebens", "wie spät ist es", "wo ist der nächste supermarkt", "kannst du mir bei meinen hausaufgaben in mathe helfen", "wie alt ist die erde", "welche aktien soll ich kaufen", "ich habe hunger", "mir ist langweilig", "was läuft im kino", "wie wird man reich", "schreib mir ein gedicht", "wer ist der bundeskanzler", "mein handy ist kaputt", "ich bin müde", "was ist 15 mal 12"],
 "en": ["how is the weather tomorrow", "what is for dinner", "how much is a flight to new york", "who won the world cup", "tell me a joke", "what is the meaning of life", "what time is it", "where is the nearest supermarket", "can you help me with my maths homework", "how old is the earth", "which stocks should i buy", "i am hungry", "i am bored", "what is on at the cinema", "how do i get rich", "write me a poem", "who is the president", "my phone is broken", "i am tired", "what is 15 times 12"],
}

PRE = {
 "de": ["kannst du mir sagen", "ich würde gern wissen", "weißt du", "könntest du mir helfen", "ich frage mich", "sag mir mal", "sag mal", "hey tutor", "tutor", "entschuldigung", "also", "ich hätte eine frage", "ich wollte fragen", "kurze frage", "ganz kurz", "du", "bitte erkläre mir", "ich brauche hilfe"],
 "en": ["can you tell me", "i would like to know", "do you know", "could you help me", "i wonder", "tell me", "hey tutor", "tutor", "excuse me", "so", "i have a question", "i wanted to ask", "quick question", "just quickly", "please", "i need help"],
}
POST = {
 "de": ["bitte", "danke", "kannst du das", "wenn du kannst", "ok", "mal", "nur kurz", "danke dir"],
 "en": ["please", "thanks", "if you can", "ok", "just quickly", "thank you", "pls"],
}
# Begriffs-Lexikon: sprachübergreifende Konzepte (normalisierte Wörter). Hilft bei umformulierten Fragen.
CONCEPTS = {
 "meaning": "bedeutet bedeutung bedeuten heisst heist heissen heisen meint meinen mean means meaning definition definiert soll sinn bdeutet".split(),
 "translate": "sagt sage sag uebersetze uebersetzen uebersetzung uebersetz translate translation say ausdruecken ausdrueckt wort vokabel".split(),
 "example": "beispiel beispiele beispielsatz bsp example examples satz saetze sentence sentences benutzt benutzen verwendet verwenden verwendung use using".split(),
 "grammar": "grammatik grammar regel regeln rule rules erklaere erklaer erklaeren erklarung explain explanation verstehe funktioniert work works wie bildet form formen".split(),
 "repeat": "nochmal einmal wiederhole wiederholen wiederholung again repeat once more pardon bitte hae".split(),
 "slow": "langsam langsamer slow slower slowly schnell fast tempo".split(),
 "dialog": "dialog dialogue rollenspiel role roleplay gespraech gespraechs conversation talk reden unterhalten ueben practice practise".split(),
 "stop": "stopp stop ende end genug enough quit cancel abbrechen beenden schluss aufhoeren finish".split(),
 "help": "hilfe help hilf funktionen features kannst koennen".split(),
 "who": "wer who bist are ki ai roboter robot mensch human chatgpt programm program".split(),
 "thanks": "danke dank dankeschoen thanks thank cheers merci".split(),
 "quiz": "quiz test teste testen abfragen abfrage pruefe pruefen aufgabe exercise task examine frag ask".split(),
 "pronounce": "aussprache aussprechen ausgesprochen pronounce pronounced pronunciation klingt sound vorsprechen vorlesen aloud".split(),
 "next": "naechste naechstes naechsten next weiter weitermachen continue move fertig done".split(),
 "level": "level niveau stufe fortschritt progress status stand lernstand".split(),
}

# ---- weitere, umgangssprachliche / unvollständige Formulierungen (erweitert T) ----
MORE = {
 "meaning": {
  "de": ["wasn das {w}", "was is das {w}", "{w} heißt was", "was heisst eigentlich {w}", "was ist denn {w} auf englisch", "{w} was soll das sein", "ich check nicht was {w} heißt", "was bedeutet das wort {w}", "sag mir die bedeutung von {w}", "was genau heißt {w}", "bedeutet {w} das gleiche wie", "hä was ist {w}", "{w} was ist das", "kannst du mir {w} übersetzen", "was meint {w}", "ich hab {w} gelesen was heißt das", "heißt {w} so viel wie"],
  "en": ["wat does {w} mean", "whats the meaning of {w}", "{w} means what", "what does the word {w} mean", "i dont get {w}", "what is {w} called", "can u tell me meaning of {w}", "what does {w} stand for", "i read {w} what does that mean", "does {w} mean the same as"],
 },
 "translate": {
  "de": ["wie nennt man {n}", "wie heist {n}", "wie sagt mann {n}", "ich möchte sagen {n} aber wie", "wie sag ich {n}", "was ist das wort für {n}", "{n} wie sagt man das", "wie heißt {n}", "wie nennt man {n} auf {l}", "gibt es ein wort für {n}", "und {n} wie sagt man das", "wie würde man {n} sagen", "{n} heißt auf {l} wie"],
  "en": ["what is {n} called", "how u say {n}", "how do i say {n}", "what is the word for {n}", "{n} how do you say that", "whats the word for {n} in {l}", "i want to say {n} but how", "how would i say {n}", "is there a word for {n}"],
 },
 "example": {
  "de": ["zeig mal sätze wo {w} drin vorkommt", "kannst du mir ne beispiel geben mit {w}", "wie benutz ich das wort {w}", "satz bitte mit {w}", "brauche beispiele für {w}", "in welchen sätzen kommt {w} vor", "bau mir einen satz mit {w}", "wie verwende ich {w} richtig", "zeig mir {w} im satz", "{w} in einem beispiel", "mehr sätze mit {w}", "ein satz mit {w} bitte"],
  "en": ["show me sentences where {w} appears", "give example using {w}", "how do i use the word {w}", "sentence with {w} pls", "need examples for {w}", "put {w} in a sentence", "{w} in context", "more sentences with {w}", "one sentence with {w} please"],
 },
 "grammar": {
  "de": ["warum ist die wortstellung so komisch", "wieso heißt es so und nicht anders", "wie geht das mit {g}", "erklär mal kurz {g}", "ich verstehe {g} nicht", "grammatik hilfe bitte", "warum {g}", "ich raffe {g} nicht", "kannst du {g} nochmal erklären", "was ist bei {g} zu beachten", "hilfe bei {g}", "wieso ist das so grammatisch", "erkläre mir die regeln", "wie funktioniert die grammatik hier"],
  "en": ["why is the word order so weird", "why is it like that and not different", "how does {g} work", "explain {g} quickly", "i dont get {g}", "grammar help please", "why {g}", "can you explain {g} again", "what do i need to know about {g}", "explain the rules", "how does the grammar work here"],
 },
 "stop": {
  "de": ["ich hab keine lust mehr", "genug für heute", "ok das reicht für heute", "ich muss jetzt los", "lass mich in ruhe", "nee jetzt nicht", "für heute ist schluss", "ich möchte nicht mehr", "mir reichts", "stopp jetzt", "das war's"],
  "en": ["i dont want to anymore", "enough for today", "ok thats enough for today", "i have to go now", "leave me alone", "not now", "thats it for today", "i dont feel like it anymore", "i am done", "stop now"],
 },
 "help": {
  "de": ["hilfe ich weiß nicht weiter", "ich komm nicht klar", "was mach ich hier", "wie geht das hier", "wie funktioniert das alles", "ich blicke nicht durch", "was soll ich tun", "ich bin überfordert", "erklär mir wie du funktionierst", "was kann man mit dir machen"],
  "en": ["help i dont know what to do", "i am lost", "what do i do here", "how does this go", "how does all this work", "i dont get it all", "what should i do", "i am overwhelmed", "explain how you work", "what can one do with you"],
 },
 "repeat": {
  "de": ["hä wie bitte", "kannst nochmal", "ich hab nix verstanden wiederhol", "was war das", "bitte wiederholen", "nochmal von vorn", "sag nochmal", "hör nicht verstanden nochmal"],
  "en": ["what? pardon", "repeat that pls", "i didnt catch that", "what was that", "please repeat", "again from the start", "say again", "i missed that"],
 },
 "slow": {
  "de": ["zu schnell langsamer", "bitte etwas langsamer reden", "kannst du das in langsam", "ganz langsam bitte", "du sprichst zu schnell", "mach mal langsamer"],
  "en": ["too fast slower please", "can you talk slowly", "can you do that slowly", "very slowly please", "you speak too fast", "slow it down"],
 },
 "dialog": {
  "de": ["lass uns mal dialog üben", "ich will mit dir ein gespräch führen", "spielen wir was rollenspiel", "lass uns ein gespräch simulieren", "ich möchte sprechen üben", "unterhalten wir uns", "ein dialog bitte", "wollen wir ein rollenspiel machen"],
  "en": ["lets practice a dialog", "i wanna have a conversation with you", "role play time", "lets simulate a conversation", "i want to practise speaking", "lets chat", "a dialog please", "shall we do a role play"],
 },
 "quiz": {
  "de": ["frag mich mal was", "kannst du mich testen", "ich will vokabeln abgefragt werden", "teste mein wissen", "stell mir aufgaben", "ich will üben frag mich", "mach ein quiz mit mir"],
  "en": ["ask me something", "can you test me", "i want a vocab quiz", "test my knowledge", "give me tasks", "i want to practise ask me", "do a quiz with me"],
 },
 "pronounce": {
  "de": ["wie spricht man {w} aus", "sprich mir mal {w} vor", "wie klingt das wort {w}", "wie sagt man {w} laut", "ich will {w} hören", "kannst du {w} sagen", "wie betont man {w}", "betonung von {w}"],
  "en": ["how do you pronounce {w}", "say {w} for me", "how does the word {w} sound", "i want to hear {w}", "can you say {w} out loud", "how do you stress {w}", "stress of {w}"],
 },
 "nextlesson": {
  "de": ["nächste lektion bitte", "ich bin fertig weiter", "das war leicht nächstes", "ich bin bereit für mehr", "gib mir die nächste lektion", "weiter geht's"],
  "en": ["next lesson please", "im done lets move on", "that was easy next", "i am ready for more", "give me the next lesson", "lets go on"],
 },
 "level": {
  "de": ["wo stehe ich gerade", "wo stehe ich", "wo bin ich gerade im kurs", "wie läuft es bei mir", "wie gut bin ich", "was habe ich schon gelernt", "wo stehen wir gerade", "mein stand bitte", "wie ist mein fortschritt", "auf welchem niveau bin ich", "wie weit bin ich schon", "wie fit bin ich", "was ist mein stand", "zeig mir meinen fortschritt", "wie viele lektionen habe ich geschafft"],
  "en": ["where do i stand", "where am i right now", "how am i doing", "how good am i", "what have i learned so far", "which level am i on", "how far am i already", "how fit am i", "whats my standing", "show me my progress", "how many lessons have i done"],
 },
}
for _k, _d in MORE.items():
    for _l, _lst in _d.items():
        T[_k][_l] = T[_k][_l] + _lst
OFFTOPIC["de"] += ["erzähl mir was lustiges", "wo gibts pizza", "wie wird das wetter", "wer ist der beste fußballer", "kannst du singen", "ich liebe dich", "was denkst du über politik", "wie kocht man nudeln", "wie komme ich zum bahnhof", "was kostet ein auto", "ich bin traurig", "welcher tag ist heute", "empfiehl mir einen film", "wie funktioniert ein motor", "kennst du musik von taylor swift"]
OFFTOPIC["en"] += ["tell me something funny", "where is pizza", "how will the weather be", "who is the best football player", "can you sing", "i love you", "what do you think about politics", "how do you cook pasta", "how do i get to the station", "how much is a car", "i am sad", "what day is today", "recommend me a movie", "how does an engine work", "do you know taylor swift songs"]
