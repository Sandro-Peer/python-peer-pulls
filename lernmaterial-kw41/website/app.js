(() => {
  const $ = (id) => document.getElementById(id);

  const screens = {
    start: $("start"),
    stoff: $("stoff"),
    quiz: $("quiz"),
    ende: $("ende"),
  };

  let order = [];
  let index = 0;
  let richtig = 0;
  let beantwortet = false;

  function show(name) {
    Object.entries(screens).forEach(([key, el]) => {
      el.classList.toggle("hidden", key !== name);
    });
  }

  function shuffle(arr) {
    const a = [...arr];
    for (let i = a.length - 1; i > 0; i--) {
      const j = Math.floor(Math.random() * (i + 1));
      [a[i], a[j]] = [a[j], a[i]];
    }
    return a;
  }

  function startQuiz() {
    order = shuffle(FRAGEN.map((_, i) => i));
    index = 0;
    richtig = 0;
    beantwortet = false;
    $("score").textContent = "0 richtig";
    show("quiz");
    renderFrage();
  }

  function renderFrage() {
    const q = FRAGEN[order[index]];
    beantwortet = false;
    $("progress").textContent = `${index + 1} / ${order.length}`;
    $("quelle").textContent = q.quelle;
    $("frage-text").textContent = q.frage;
    $("feedback").className = "feedback hidden";
    $("feedback").textContent = "";
    $("btn-next").classList.add("hidden");
    $("btn-next").textContent =
      index + 1 === order.length ? "Ergebnis anzeigen" : "Weiter";

    const box = $("optionen");
    box.innerHTML = "";
    q.optionen.forEach((text, i) => {
      const btn = document.createElement("button");
      btn.type = "button";
      btn.className = "opt";
      btn.textContent = text;
      btn.addEventListener("click", () => choose(i, btn));
      box.appendChild(btn);
    });
  }

  function choose(wahl, btn) {
    if (beantwortet) return;
    beantwortet = true;
    const q = FRAGEN[order[index]];
    const buttons = [...$("optionen").querySelectorAll(".opt")];
    buttons.forEach((b) => {
      b.disabled = true;
    });

    const feedback = $("feedback");
    if (wahl === q.korrekt) {
      richtig += 1;
      btn.classList.add("correct");
      feedback.className = "feedback ok";
      feedback.textContent = "Richtig. " + q.feedback;
    } else {
      btn.classList.add("wrong");
      buttons[q.korrekt].classList.add("correct");
      feedback.className = "feedback bad";
      feedback.textContent =
        "Leider falsch. Richtig wäre: „" +
        q.optionen[q.korrekt] +
        "“. " +
        q.feedback;
    }
    $("score").textContent = `${richtig} richtig`;
    $("btn-next").classList.remove("hidden");
  }

  function next() {
    if (index + 1 >= order.length) {
      finish();
      return;
    }
    index += 1;
    renderFrage();
  }

  function finish() {
    const total = order.length;
    const pct = Math.round((richtig / total) * 100);
    $("ergebnis").textContent = `${richtig} / ${total} (${pct} %)`;
    let text = "Noch üben – PDF + Kurzstoff helfen.";
    if (pct >= 90) text = "Sehr stark – Stoff bis KW 41 sitzt.";
    else if (pct >= 75) text = "Gut – offene Lücken nochmal nachlesen.";
    else if (pct >= 50) text = "Solide Basis – schwache Themen wiederholen.";
    $("wertung").textContent = text;
    show("ende");
  }

  $("anzahl").textContent = String(FRAGEN.length);
  $("btn-start").addEventListener("click", startQuiz);
  $("btn-stoff").addEventListener("click", () => show("stoff"));
  $("btn-stoff-back").addEventListener("click", () => show("start"));
  $("btn-next").addEventListener("click", next);
  $("btn-restart").addEventListener("click", startQuiz);
  $("btn-home").addEventListener("click", () => show("start"));
})();
