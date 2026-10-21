/* Fragen bis KW 41 – Sammlung + Zusatz */
const FRAGEN = [
  {
    quelle: "Sammlung",
    frage: "Was beschreibt eine Instanz in Python am besten?",
    optionen: [
      "Einen Typ-Namen in Type Hints",
      "Ein konkretes Objekt im Speicher",
      "Einen Kommentarblock",
      "Die Shebang-Zeile"
    ],
    korrekt: 1,
    feedback: "Eine Instanz ist ein konkretes Objekt. Referenzen zeigen darauf; der Referenzzähler zählt die Referenzen."
  },
  {
    quelle: "Sammlung",
    frage: "Was macht del name?",
    optionen: [
      "Löscht die Festplatte",
      "Entfernt die Referenz name; Objekt erst weg bei Zähler 0",
      "Beendet das Programm immer",
      "Kompiliert den Code neu"
    ],
    korrekt: 1,
    feedback: "del entfernt einen Namen/eine Referenz. Garbage Collection gibt Speicher frei, wenn nichts mehr darauf zeigt."
  },
  {
    quelle: "Sammlung",
    frage: "Was sind Type Hints?",
    optionen: [
      "Pflichttypen wie in Java zur Laufzeit",
      "Optionale Annotationen für Lesbarkeit und Checker",
      "Nur Kommentare ohne Syntax",
      "Assembler-Befehle"
    ],
    korrekt: 1,
    feedback: "Type Hints dokumentieren Typen und helfen Tools wie mypy – zur Laufzeit meist ohne Effekt."
  },
  {
    quelle: "Sammlung",
    frage: "Unterschied Compiler- vs. Interpretersprachen?",
    optionen: [
      "Compiler = nur Web; Interpreter = nur Desktop",
      "Compiler übersetzt vor dem Lauf; Interpreter führt zur Laufzeit aus",
      "Es gibt keinen Unterschied",
      "Interpreter erzeugen immer .exe-Dateien"
    ],
    korrekt: 1,
    feedback: "C/C++/oft Java→Bytecode: vorher übersetzen. Python: Interpreter (zur Laufzeit)."
  },
  {
    quelle: "Sammlung",
    frage: "Wann eignet sich match/case besonders?",
    optionen: [
      "Nur für Endlosschleifen",
      "Wenn viele Möglichkeiten/Muster eines Inhalts geprüft werden",
      "Nur für Division",
      "Als Ersatz für Garbage Collection"
    ],
    korrekt: 1,
    feedback: "match/case ist ideal für viele konkrete Fälle eines Werts; if-elif für beliebige Bedingungen/Bereiche."
  },
  {
    quelle: "Sammlung",
    frage: "Was sind Kontrollstrukturen?",
    optionen: [
      "Nur Variablennamen",
      "Mittel zur Steuerung des Programmflusses (if, Schleifen, try, …)",
      "Nur Datenbanken",
      "Nur Type Hints"
    ],
    korrekt: 1,
    feedback: "Verzweigungen, Schleifen, break/continue, Exceptions steuern den Ablauf."
  },
  {
    quelle: "Sammlung",
    frage: "Iterativ vs. rekursiv – was stimmt?",
    optionen: [
      "Iterativ = nur mit match; rekursiv = nur mit dict",
      "Iterativ nutzt Schleifen; rekursiv ruft sich die Funktion selbst auf",
      "Rekursion braucht keine Abbruchbedingung",
      "Iteration gibt es in Python nicht"
    ],
    korrekt: 1,
    feedback: "Rekursion braucht einen Basisfall; Iteration hält den Zustand in Variablen/Schleifen."
  },
  {
    quelle: "Sammlung",
    frage: "Prozess vs. Thread – welche Aussage ist richtig?",
    optionen: [
      "Threads haben immer eigenen Adressraum",
      "Prozesse teilen sich immer denselben Speicher",
      "Prozesse: eigener Adressraum; Threads teilen Speicher im Prozess",
      "Es gibt keinen Unterschied"
    ],
    korrekt: 2,
    feedback: "Prozesse sind isolierter; Threads sind leichtgewichtiger, aber anfällig für Race Conditions."
  },
  {
    quelle: "Sammlung",
    frage: "list vs. „echtes“ array in Python?",
    optionen: [
      "list ist immer schneller als NumPy",
      "list ist flexibel/gemischt; array/np.array homogen und speichereffizient",
      "array kann keine Zahlen speichern",
      "Java ArrayList entspricht np.array 1:1"
    ],
    korrekt: 1,
    feedback: "Listen sind dynamisch und allgemein; Arrays (array/NumPy) haben festen Elementtyp und dichteren Speicher."
  },
  {
    quelle: "Sammlung",
    frage: "Drei Vorteile von Python gegenüber C-ähnlichen Sprachen?",
    optionen: [
      "Immer schneller als C, keine Libraries, manuelle Speicherverwaltung",
      "Hohe Produktivität, dynamische Typen/Ökosystem, automatische GC",
      "Nur Assembler-Ausgabe, keine Strings, feste Arrays",
      "Kein Interpreter, kein GC, keine Syntax"
    ],
    korrekt: 1,
    feedback: "Python punktet mit knapper Syntax, Libraries und Garbage Collection – oft auf Kosten von Rohgeschwindigkeit."
  },
  {
    quelle: "Sammlung",
    frage: "Wozu dient pass?",
    optionen: [
      "Beendet die Schleife wie break",
      "Leerer Block / No-Op, wo Syntax einen Körper verlangt",
      "Importiert Module",
      "Startet Threads"
    ],
    korrekt: 1,
    feedback: "pass macht nichts – z. B. Stub-Funktion oder leerer if-Zweig."
  },
  {
    quelle: "Sammlung",
    frage: "Was liefert 7 // 2 und -7 // 2 in Python 3?",
    optionen: [
      "3.5 und -3.5",
      "3 und -3",
      "3 und -4",
      "4 und -4"
    ],
    korrekt: 2,
    feedback: "// ist Floor Division (Richtung −∞): 7 // 2 == 3, -7 // 2 == -4. / liefert float (3.5)."
  },
  {
    quelle: "Sammlung",
    frage: "Garbage Collection – Kernidee?",
    optionen: [
      "Manuelles free() nach jedem print",
      "Automatische Freigabe nicht mehr erreichbarer Objekte",
      "Nur Löschen von .py-Dateien",
      "Kompilieren nach Assembler"
    ],
    korrekt: 1,
    feedback: "CPython: Referenzzählung + Zyklus-Collector."
  },
  {
    quelle: "Sammlung",
    frage: "Ternärer / bedingter Ausdruck – korrekte Form?",
    optionen: [
      "status = note >= 50 ? \"ok\" : \"fail\"",
      "status = \"ok\" if note >= 50 else \"fail\"",
      "status = if note >= 50 then \"ok\"",
      "status := note >= 50 -> \"ok\""
    ],
    korrekt: 1,
    feedback: "Python: wert_wenn_wahr if bedingung else wert_wenn_falsch (nicht der C/Java-?-Operator)."
  },
  {
    quelle: "Sammlung",
    frage: "Welche Teile gehören zu try/except in Python?",
    optionen: [
      "nur catch und throw",
      "try, except, optional else und finally; Fehler mit raise",
      "nur if und else",
      "nur match und case"
    ],
    korrekt: 1,
    feedback: "else läuft nur ohne Exception; finally immer. raise löst aus."
  },
  {
    quelle: "Sammlung",
    frage: "Unterschied Java/Python bei Datentypen inkl. Hints?",
    optionen: [
      "Beide rein statisch ohne Ausnahme",
      "Java statisch/pflichtig; Python dynamisch + optionale Type Hints",
      "Python hat keine Typen",
      "Java hat nur Type Hints"
    ],
    korrekt: 1,
    feedback: "Python prüft Typen zur Laufzeit am Objekt; Hints sind optional."
  },
  {
    quelle: "Sammlung",
    frage: "Arrays in Python vs. Java – was trifft zu?",
    optionen: [
      "Python-Standard ist feste Arrays wie in Java",
      "Java-Arrays fest/typiert; Python nutzt oft list, echte Arrays via array/NumPy",
      "Java hat keine Arrays",
      "Beide sind identisch"
    ],
    korrekt: 1,
    feedback: "Java: Länge und Typ fix. Python-list: flexibel; array/np für homogene Daten."
  },
  {
    quelle: "Sammlung",
    frage: "Drei Gemeinsamkeiten Java und Python?",
    optionen: [
      "Beide ohne GC, ohne Exceptions, nur Assembler",
      "OOP möglich, Garbage Collection, Exception-Handling (u. a.)",
      "Beide ohne Schleifen",
      "Beide erzwingen Einrückung mit Tabs"
    ],
    korrekt: 1,
    feedback: "Beide sind Hochsprachen mit GC und Exceptions; Unterschiede liegen u. a. bei Typen und Syntax."
  },
  {
    quelle: "Sammlung",
    frage: "if-elif-else vs. match/case – Kurzform?",
    optionen: [
      "Beide sind verboten in Python 3",
      "if für Bedingungen/Bereiche; match für Muster/viele Werte eines Inhalts",
      "match ersetzt alle Schleifen",
      "elif gibt es nur in Java"
    ],
    korrekt: 1,
    feedback: "Kontrollstrukturen: für viele Möglichkeiten eines Inhalts oft match/case."
  },
  {
    quelle: "Sammlung",
    frage: "Vier Exception-Kombis (neu/hoch + behebbar/nicht) – was gilt bei „nicht behebbar“?",
    optionen: [
      "Immer mit print verschlucken",
      "Nicht behandeln bzw. raise/nach oben lassen; am Einstieg ggf. loggen + exit",
      "Nur pass verwenden",
      "Immer in eine list speichern"
    ],
    korrekt: 1,
    feedback: "EAFP/LBYL und die vier Kombis: was man nicht beheben kann, soll man nicht „schönreden“."
  },
  {
    quelle: "Zusatz",
    frage: "Kernaussage KW 38 zu KI-Code?",
    optionen: [
      "Laufender Code braucht nie Review",
      "Ohne Grundlagen kann man KI-Code weder prüfen noch reparieren",
      "KI haftet rechtlich immer",
      "Syntax-Tippen ist die ganze Ingenieursleistung"
    ],
    korrekt: 1,
    feedback: "Pilot-Analogie: Autopilot hilft, aber der Entwickler muss verstehen und verantworten."
  },
  {
    quelle: "Zusatz",
    frage: "Python 2 → 3: ein typischer Bruch?",
    optionen: [
      "print bleibt Statement und / bleibt Integer-Division",
      "print ist Funktion; / liefert float",
      "Es gab keine Brüche",
      "Nur die Farbe der Idle-IDE änderte sich"
    ],
    korrekt: 1,
    feedback: "Abwärtskompatibilität wurde bewusst gebrochen."
  },
  {
    quelle: "Zusatz",
    frage: "Warum „nachwürfeln bis unique“ für Lotto (KW 40) ungeeignet?",
    optionen: [
      "Weil random verboten ist",
      "Weil der RNG bei 45 Zahlen nur 45-mal genutzt werden soll",
      "Weil Dictionaries keine ints speichern",
      "Weil match/case Pflicht ist"
    ],
    korrekt: 1,
    feedback: "Besser: Liste 1..45 mischen (z. B. shuffle) und 6 Zahlen nehmen – ohne Doppelte, mit begrenzten RNG-Aufrufen."
  },
  {
    quelle: "Zusatz",
    frage: "Beste Struktur für Lotto-Statistik?",
    optionen: [
      "Nur print ohne Speichern",
      "dict: Zahl → Häufigkeit, nach jeder Ziehung inkrementieren",
      "Nur Type Hints ohne Daten",
      "Ein einzelner Boolean"
    ],
    korrekt: 1,
    feedback: "Dictionary eignet sich als Zuordnung für Zähler (KW 40)."
  },
  {
    quelle: "Zusatz",
    frage: "Shebang #!/usr/bin/env python3 – wozu?",
    optionen: [
      "Nur Windows-Registry",
      "Unter UNIX: Interpreter für ausführbare Skripte festlegen",
      "Ersetzt alle Imports",
      "Startet Garbage Collection"
    ],
    korrekt: 1,
    feedback: "Magic Line / Shebang – Stoff KW 41."
  },
  {
    quelle: "Zusatz",
    frage: "Einrückung laut Stil (KW 41)?",
    optionen: [
      "Tabs beliebig, 2 Spaces",
      "Keine Tabs, 4 Leerzeichen; Zeilen möglichst ≤ 80 Zeichen",
      "Nur geschweifte Klammern",
      "Einrückung ist egal"
    ],
    korrekt: 1,
    feedback: "PEP-8-nah: 4 Spaces, lange Zeilen umbrechen (Backslash)."
  },
  {
    quelle: "Zusatz",
    frage: "Sind Variablennamen case-sensitiv?",
    optionen: [
      "Nein, Name und name sind gleich",
      "Ja, Name und name sind verschieden",
      "Nur in Java",
      "Nur innerhalb von match"
    ],
    korrekt: 1,
    feedback: "Python ist case-sensitiv (KW 41)."
  },
  {
    quelle: "Zusatz",
    frage: "Logische Operatoren in Python?",
    optionen: [
      "&& || !",
      "and / or / not",
      "AND OR NOT als Bits Pflicht",
      "Nur =="
    ],
    korrekt: 1,
    feedback: "Nicht die C/Java-Schreibweise – Stoff KW 39/41 und Syntax-PDF."
  },
  {
    quelle: "Zusatz",
    frage: "Wann läuft der else-Zweig einer for-Schleife?",
    optionen: [
      "Immer nach dem ersten Durchlauf",
      "Nur wenn die Schleife nicht per break endet",
      "Nur bei Exceptions",
      "Nie in Python"
    ],
    korrekt: 1,
    feedback: "Typisch für „kein break = kein Treffer / Primzahl-Muster“."
  },
  {
    quelle: "Zusatz",
    frage: "True / False / None – was gilt vs. Java?",
    optionen: [
      "In Python kleingeschrieben wie in Java",
      "In Python groß: True, False, None (Java: true, false, null)",
      "None heißt null in Python",
      "Es gibt kein None"
    ],
    korrekt: 1,
    feedback: "Wichtiger Syntax-Unterschied Python vs. Java."
  },
  {
    quelle: "Zusatz",
    frage: "Was macht raise ValueError(\"…\")?",
    optionen: [
      "Ignoriert Fehler",
      "Löst eine Exception aus",
      "Startet einen Thread",
      "Löscht das dict"
    ],
    korrekt: 1,
    feedback: "Entspricht grob throw in Java – Stoff Kontrollstrukturen/Exceptions."
  },
  {
    quelle: "Zusatz",
    frage: "list vs. dict in einem Satz?",
    optionen: [
      "Beide sind dasselbe",
      "list: Sequenz per Index; dict: Schlüssel → Wert",
      "dict hat keine Schlüssel",
      "list speichert nur Strings"
    ],
    korrekt: 1,
    feedback: "KW 40: Listen und Zuordnungsstrukturen (dict)."
  }
];
