#!/usr/bin/env python3
"""Erzeugt die Lern-PDF: Stoff bis KW41 + Fragen."""

from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER, TA_JUSTIFY, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import cm, mm
from reportlab.platypus import (
    KeepTogether,
    ListFlowable,
    ListItem,
    PageBreak,
    Paragraph,
    Preformatted,
    SimpleDocTemplate,
    Spacer,
    Table,
    TableStyle,
)

OUT = Path(__file__).resolve().parent / "SWP_Python_Lernzusammenfassung_KW41.pdf"


def styles():
    base = getSampleStyleSheet()
    s = {
        "title": ParagraphStyle(
            "T",
            parent=base["Title"],
            fontName="Helvetica-Bold",
            fontSize=20,
            leading=24,
            spaceAfter=8,
            textColor=colors.HexColor("#1a365d"),
        ),
        "subtitle": ParagraphStyle(
            "ST",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=11,
            leading=14,
            alignment=TA_CENTER,
            textColor=colors.HexColor("#4a5568"),
            spaceAfter=18,
        ),
        "h1": ParagraphStyle(
            "H1",
            parent=base["Heading1"],
            fontName="Helvetica-Bold",
            fontSize=14,
            leading=18,
            spaceBefore=16,
            spaceAfter=8,
            textColor=colors.HexColor("#1a365d"),
            borderPadding=3,
        ),
        "h2": ParagraphStyle(
            "H2",
            parent=base["Heading2"],
            fontName="Helvetica-Bold",
            fontSize=12,
            leading=15,
            spaceBefore=12,
            spaceAfter=6,
            textColor=colors.HexColor("#2b6cb0"),
        ),
        "h3": ParagraphStyle(
            "H3",
            parent=base["Heading3"],
            fontName="Helvetica-Bold",
            fontSize=11,
            leading=14,
            spaceBefore=8,
            spaceAfter=4,
            textColor=colors.HexColor("#2d3748"),
        ),
        "body": ParagraphStyle(
            "B",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=13,
            alignment=TA_JUSTIFY,
            spaceAfter=6,
        ),
        "bullet": ParagraphStyle(
            "Bu",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=10,
            leading=13,
            leftIndent=12,
            spaceAfter=3,
        ),
        "code": ParagraphStyle(
            "C",
            parent=base["Code"],
            fontName="Courier",
            fontSize=8.5,
            leading=11,
            backColor=colors.HexColor("#f7fafc"),
            borderPadding=6,
            spaceBefore=4,
            spaceAfter=8,
        ),
        "q": ParagraphStyle(
            "Q",
            parent=base["Normal"],
            fontName="Helvetica-Bold",
            fontSize=10,
            leading=13,
            spaceBefore=10,
            spaceAfter=4,
            textColor=colors.HexColor("#1a202c"),
        ),
        "a": ParagraphStyle(
            "A",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=9.5,
            leading=12.5,
            leftIndent=8,
            spaceAfter=6,
            textColor=colors.HexColor("#2d3748"),
        ),
        "tag": ParagraphStyle(
            "Tag",
            parent=base["Normal"],
            fontName="Helvetica-Oblique",
            fontSize=8,
            leading=10,
            textColor=colors.HexColor("#718096"),
            spaceAfter=2,
        ),
        "footer": ParagraphStyle(
            "F",
            parent=base["Normal"],
            fontName="Helvetica",
            fontSize=8,
            textColor=colors.HexColor("#718096"),
            alignment=TA_CENTER,
        ),
    }
    return s


def bullets(items, style):
    return [
        Paragraph(f"• {item}", style) for item in items
    ]


def add_header_footer(canvas, doc):
    canvas.saveState()
    canvas.setFont("Helvetica", 8)
    canvas.setFillColor(colors.HexColor("#718096"))
    canvas.drawString(2 * cm, 1.2 * cm, "SWP-Python 5B · Lernzusammenfassung bis KW 41")
    canvas.drawRightString(A4[0] - 2 * cm, 1.2 * cm, f"Seite {doc.page}")
    canvas.restoreState()


def build():
    s = styles()
    story = []

    # ---- Titel ----
    story.append(Paragraph("SWP-Python 5BHWII", s["title"]))
    story.append(
        Paragraph(
            "Lernzusammenfassung bis einschließlich KW 41<br/>"
            "Theorie · passende Testfragen · Zusatzfragen",
            s["subtitle"],
        )
    )
    story.append(
        Paragraph(
            "Quellen: <b>5B_SWP_python_2026.pdf</b>, "
            "<b>Python_Syntax_Kontrollstrukturen.pdf</b>, "
            "<b>Python_Testfragen_Sammlung</b> (nur Fragen zum Stoff bis KW 41).",
            s["body"],
        )
    )

    # ========== TEIL 1: STOFF ==========
    story.append(Paragraph("Teil 1 — Stoffübersicht bis KW 41", s["h1"]))

    story.append(Paragraph("Rahmenbedingungen (Kurz)", s["h2"]))
    for b in bullets(
        [
            "Drei oder vier Tests; jeder Test muss positiv sein (sonst P5).",
            "Mitarbeit 30 % · Tests 70 %; 1. HJ 45 % · 2. HJ 55 %.",
            "Mitarbeit startet bei Befriedigend; Plus −0,25 · Minus +0,5.",
            "HUs gehören in ein eigenes Git-Repo; Folien: github.com/htlinnrain/python",
            "Stoff allgemein: Python-Theorie + Aufgaben → verkettete Listen → 2. HJ Projekt.",
        ],
        s["bullet"],
    ):
        story.append(b)

    # ---- KW38 ----
    story.append(Paragraph("KW 38 — Warum Grundlagen trotz KI?", s["h2"]))
    story.append(
        Paragraph(
            "Kernaussage: Wer den Code nicht versteht, steuert nicht – er fliegt blind.",
            s["body"],
        )
    )
    for b in bullets(
        [
            "<b>Debugging &amp; Verifikation:</b> KI liefert schnell laufenden Code, "
            "baut aber oft subtile Logikfehler, Race Conditions oder Sicherheitslücken ein. "
            "Ohne Grundlagen, Datenstrukturen und Systemverständnis kann man KI-Code "
            "weder prüfen noch reparieren.",
            "<b>Pilot-Analogie:</b> Ein Jet fliegt oft auf Autopilot – der Pilot muss das "
            "Flugzeug trotzdem im Detail verstehen, um bei Ausfällen die Kontrolle zu übernehmen.",
            "<b>Programmieren = Problemübersetzung</b>, nicht Syntax-Tippen. "
            "Architektur, Schnittstellen, Skalierung und echte Problemstellung sind die "
            "eigentliche Ingenieursleistung.",
            "<b>Präzise Anforderungen:</b> Gute Prompts brauchen technische Durchdringung. "
            "Vage Eingaben → unbrauchbarer Code.",
            "<b>Haftung:</b> Bei Fehlern in kritischen Systemen (Medizin, Automotive, Finanzen) "
            "haftet der Entwickler, nicht das Sprachmodell.",
            "<b>Rollenwandel:</b> KI ersetzt mechanische Tipparbeit. Entwickler mit soliden "
            "Informatikgrundlagen + KI als Werkzeug werden produktiver, nicht arbeitslos.",
        ],
        s["bullet"],
    ):
        story.append(b)

    # ---- KW39 ----
    story.append(Paragraph("KW 39 — Einführung &amp; Python-Grundlagen", s["h2"]))

    story.append(Paragraph("Praktischer Einstieg", s["h3"]))
    for b in bullets(
        [
            "Einführung, Folien via Git, eigenes Repo für SWP-Python anlegen.",
            "Python installieren, Hallo-Welt programmieren.",
            "Lernressourcen: learnpython.org, programiz.com/python-programming.",
            "KI als Recherchehilfe erlaubt – Nutzung in Git protokollieren.",
        ],
        s["bullet"],
    ):
        story.append(b)

    story.append(Paragraph("Python 2 vs. Python 3", s["h3"]))
    story.append(
        Paragraph(
            "Python 3 hat die Abwärtskompatibilität zu Python 2 bewusst gebrochen "
            "(z. B. <font face='Courier'>print</font> als Funktion, "
            "Division <font face='Courier'>/</font> liefert float, Unicode-Strings). "
            "Heute arbeitet man praktisch nur noch mit Python 3.",
            s["body"],
        )
    )

    story.append(Paragraph("Iterativ vs. rekursiv", s["h3"]))
    story.append(
        Paragraph(
            "<b>Iterativ:</b> Lösung mit Schleifen (for/while), Zustand in Variablen. "
            "<b>Rekursiv:</b> Funktion ruft sich selbst auf, braucht Abbruchbedingung. "
            "Rekursion ist oft eleganter bei Baum-/Teile-und-Herrsche-Problemen, "
            "braucht aber Stack und kann bei großer Tiefe overflowen.",
            s["body"],
        )
    )
    story.append(
        Preformatted(
            "def fak_iter(n):\n"
            "    r = 1\n"
            "    for i in range(2, n + 1):\n"
            "        r *= i\n"
            "    return r\n\n"
            "def fak_rek(n):\n"
            "    if n <= 1:\n"
            "        return 1\n"
            "    return n * fak_rek(n - 1)",
            s["code"],
        )
    )

    story.append(Paragraph("Prozesse vs. Threads", s["h3"]))
    for b in bullets(
        [
            "<b>Prozess:</b> eigenständiges Programm mit eigenem Adressraum (Speicher). "
            "Kommunikation nur über IPC (Pipes, Sockets, …). Isoliert, aber schwerer.",
            "<b>Thread:</b> Ausführungspfad innerhalb eines Prozesses; Threads teilen sich "
            "Speicher. Leichtgewichtiger, aber Race Conditions möglich.",
            "In CPython begrenzt der GIL oft echte Parallelität bei CPU-lastigem Code "
            "(Threads gut für I/O; Prozesse für CPU).",
        ],
        s["bullet"],
    ):
        story.append(b)

    story.append(Paragraph("Typisierung &amp; Type Hints", s["h3"]))
    for b in bullets(
        [
            "Python ist <b>dynamisch typisiert</b>: Variablen haben keinen festen Typ "
            "zur Compile-Zeit; der Typ hängt am Objekt zur Laufzeit.",
            "Gegenstück: <b>statische Typisierung</b> (z. B. Java) – Typen werden "
            "vor dem Lauf geprüft.",
            "<b>Type Hints</b> (ab 3.5+): optionale Annotationen für Lesbarkeit und "
            "statische Checker (mypy, pyright) – zur Laufzeit oft ignoriert.",
        ],
        s["bullet"],
    ):
        story.append(b)
    story.append(
        Preformatted(
            "def addiere(a: int, b: int) -> int:\n"
            "    return a + b\n\n"
            "namen: list[str] = [\"Ana\", \"Ben\"]",
            s["code"],
        )
    )

    story.append(Paragraph("Paradigmen, Interpreter, Speicher", s["h3"]))
    for b in bullets(
        [
            "Python unterstützt <b>funktional</b> und <b>objektorientiert</b>.",
            "<b>Interpretersprachen</b> (Python, JS): Quellcode wird zur Laufzeit "
            "interpretiert/JIT. <b>Compilersprachen</b> (C, C++, oft Java→Bytecode): "
            "Übersetzung vor dem Lauf.",
            "<b>Instanz:</b> konkretes Objekt im Speicher. "
            "<b>Referenz:</b> Name/Zeiger auf diese Instanz. "
            "<b>Referenzzähler:</b> zählt, wie viele Referenzen auf ein Objekt zeigen. "
            "<b>Garbage Collection:</b> freigibt Speicher, wenn nichts mehr darauf zeigt "
            "(+ Zyklus-GC). <b>del</b>: entfernt einen Namen/Referenz (Objekt erst weg, "
            "wenn Zähler 0).",
        ],
        s["bullet"],
    ):
        story.append(b)

    story.append(Paragraph("Syntax &amp; Kontrollstrukturen", s["h3"]))
    story.append(
        Paragraph(
            "Blöcke über <b>Einrückung</b> (4 Leerzeichen, keine Tabs) und Doppelpunkt. "
            "Logik: <font face='Courier'>and / or / not</font> (nicht &amp;&amp; || !). "
            "<font face='Courier'>True / False / None</font> (groß).",
            s["body"],
        )
    )
    story.append(
        Preformatted(
            "# if / elif / else\n"
            "note = 78\n"
            "if note >= 90:\n"
            "    print(\"sehr gut\")\n"
            "elif note >= 75:\n"
            "    print(\"gut\")\n"
            "else:\n"
            "    print(\"nicht genügend\")\n\n"
            "# bedingter Ausdruck (ternär)\n"
            "status = \"ok\" if note >= 50 else \"fail\"\n\n"
            "# match/case (viele Fälle – analog switch)\n"
            "match note // 10:\n"
            "    case 10 | 9:\n"
            "        print(\"1\")\n"
            "    case 8 | 7:\n"
            "        print(\"2\")\n"
            "    case _:\n"
            "        print(\"andere\")\n\n"
            "# Schleifen\n"
            "for i in range(5):          # 0..4\n"
            "    print(i)\n"
            "while n > 0:\n"
            "    n -= 1                  # kein ++/--\n\n"
            "# break / continue / pass\n"
            "for i in range(10):\n"
            "    if i == 3:\n"
            "        continue\n"
            "    if i == 7:\n"
            "        break\n"
            "    print(i)\n"
            "def noch_offen():\n"
            "    pass                    # leerer Block\n\n"
            "# try / except / else / finally\n"
            "try:\n"
            "    ergebnis = a / b\n"
            "except ZeroDivisionError:\n"
            "    print(\"Division durch 0\")\n"
            "else:\n"
            "    print(\"ok\")             # nur ohne Exception\n"
            "finally:\n"
            "    print(\"fertig\")         # immer",
            s["code"],
        )
    )
    for b in bullets(
        [
            "<b>if-elif-else:</b> gut für Bereiche/Bedingungen. "
            "<b>match/case:</b> gut, wenn viele konkrete Werte/Muster eines Inhalts geprüft werden.",
            "Schleifen-<b>else</b>: läuft nur, wenn die Schleife <i>nicht</i> per break endet.",
            "Exceptions: <font face='Courier'>raise ValueError(\"...\")</font>",
        ],
        s["bullet"],
    ):
        story.append(b)

    # ---- KW40 ----
    story.append(Paragraph("KW 40 — Arrays, Listen, Dictionaries, Lotto", s["h2"]))
    story.append(
        Paragraph(
            "Wiederholung + Vergleich Assembler/C++ (Abbildung in den Folien): "
            "hohe Abstraktion in Python vs. maschinennahe Sprachen.",
            s["body"],
        )
    )
    story.append(Paragraph("Datenstrukturen", s["h3"]))
    for b in bullets(
        [
            "<b>list</b> (Python): dynamisch, gemischte Typen möglich, "
            "ähnlich Java <font face='Courier'>ArrayList</font>.",
            "<b>array</b> (Modul <font face='Courier'>array</font>) / "
            "<b>numpy.ndarray</b>: echte Arrays – homogener Typ, speichereffizient, "
            "schneller bei Zahlenrechnungen.",
            "Java-Arrays: feste Länge, fester Typ. Python-Listen: flexibel.",
            "<b>dict</b>: Zuordnung Schlüssel → Wert (Hash-Map). Ideal für Zähler/Statistik.",
            "Binary Search (programiz): Algorithmus + Python-Syntax der Schleifen/Indizes.",
        ],
        s["bullet"],
    ):
        story.append(b)

    story.append(Paragraph("Aufgabe: Lottoziehung", s["h3"]))
    for b in bullets(
        [
            "Methode, die 6 Zahlen aus 1–45 zieht und ausgibt.",
            "Wichtig: <b>keine Zahl doppelt</b>. Algorithmus so, dass der RNG "
            "bei 45 gezogenen Zahlen nur 45-mal aufgerufen wird "
            "(z. B. Fisher-Yates / Liste mischen und erste 6 nehmen – "
            "nicht „solange neu würfeln bis unique“).",
            "Statistik: 1000 / 10 000 / 100 000 Ziehungen; Dictionary zählt, "
            "wie oft jede Zahl vorkommt; nach jeder Ziehung Zähler erhöhen.",
        ],
        s["bullet"],
    ):
        story.append(b)
    story.append(
        Preformatted(
            "import random\n\n"
            "def lottoziehung() -> list[int]:\n"
            "    zahlen = list(range(1, 46))\n"
            "    random.shuffle(zahlen)       # RNG-Aufrufe begrenzt\n"
            "    gezogen = sorted(zahlen[:6])\n"
            "    return gezogen\n\n"
            "def statistik(n: int) -> dict[int, int]:\n"
            "    zaehler = {i: 0 for i in range(1, 46)}\n"
            "    for _ in range(n):\n"
            "        for z in lottoziehung():\n"
            "            zaehler[z] += 1\n"
            "    return zaehler",
            s["code"],
        )
    )

    # ---- KW41 ----
    story.append(Paragraph("KW 41 — Datentypen, Division, Stil, Schlüsselwörter", s["h2"]))
    for b in bullets(
        [
            "Type-Hints, Data-Validation, Datentypen vertiefen "
            "(int, float, str, list, dict).",
            "<b>Division:</b> <font face='Courier'>/</font> → float; "
            "<font face='Courier'>//</font> → Floor Division (abrunden Richtung −∞); "
            "<font face='Courier'>%</font> Rest; "
            "<font face='Courier'>divmod(a,b)</font>.",
            "Strings: mit <font face='Courier'>+</font> konkatenieren; "
            "immutable (neu erzeugt).",
            "Variablennamen sind <b>case-sensitiv</b> (<font face='Courier'>Name ≠ name</font>).",
            "Schlüsselwörter reserviert (<font face='Courier'>if, for, def, class, "
            "True, None, …</font>) – siehe Rheinwerk OpenBook.",
            "Logische Ausdrücke: <font face='Courier'>and / or / not</font>, "
            "Vergleiche <font face='Courier'>&lt; &lt;= == != &gt;= &gt;</font>.",
            "Dateien enden auf <font face='Courier'>*.py</font>.",
            "Shebang (UNIX): <font face='Courier'>#!/usr/bin/env python3</font>",
            "Stil: keine Tabs, 4 Spaces; lange Zeilen max. ~80 Zeichen, "
            "Umbruch mit Backslash <font face='Courier'>\\</font>.",
            "Kommentare: <font face='Courier'># …</font> oder Docstrings "
            "<font face='Courier'>\"\"\"…\"\"\"</font>; Platzhalter: <font face='Courier'>pass</font>.",
        ],
        s["bullet"],
    ):
        story.append(b)

    story.append(
        Preformatted(
            "print(7 / 2)    # 3.5\n"
            "print(7 // 2)   # 3\n"
            "print(-7 // 2)  # -4  (Floor!)\n"
            "print(7 % 2)    # 1\n\n"
            "#!/usr/bin/env python3\n"
            "# kommentar\n"
            "def hilfe():\n"
            "    \"\"\"Kurze Doku.\"\"\"\n"
            "    pass",
            s["code"],
        )
    )

    story.append(Paragraph("Schnellvergleich Python vs. Java (bis KW 41)", s["h2"]))
    data = [
        [Paragraph("<b>Thema</b>", s["body"]),
         Paragraph("<b>Python</b>", s["body"]),
         Paragraph("<b>Java</b>", s["body"])],
        [Paragraph("Blöcke", s["body"]),
         Paragraph("Einrückung", s["body"]),
         Paragraph("{ }", s["body"])],
        [Paragraph("Typen", s["body"]),
         Paragraph("dynamisch + optionale Hints", s["body"]),
         Paragraph("statisch, Pflicht", s["body"])],
        [Paragraph("Logik", s["body"]),
         Paragraph("and / or / not", s["body"]),
         Paragraph("&& || !", s["body"])],
        [Paragraph("Boolean/Null", s["body"]),
         Paragraph("True False None", s["body"]),
         Paragraph("true false null", s["body"])],
        [Paragraph("else if", s["body"]),
         Paragraph("elif / match", s["body"]),
         Paragraph("else if / switch", s["body"])],
        [Paragraph("for", s["body"]),
         Paragraph("über Iterable / range", s["body"]),
         Paragraph("C-Style oder for-each", s["body"])],
        [Paragraph("++ / --", s["body"]),
         Paragraph("gibt es nicht", s["body"]),
         Paragraph("ja", s["body"])],
        [Paragraph("Exceptions", s["body"]),
         Paragraph("except (+ else)", s["body"]),
         Paragraph("catch", s["body"])],
        [Paragraph("Listen/Arrays", s["body"]),
         Paragraph("list flexibel; array/np fest", s["body"]),
         Paragraph("Array fest; ArrayList dynamisch", s["body"])],
    ]
    t = Table(data, colWidths=[3.2 * cm, 6.5 * cm, 6.5 * cm])
    t.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#ebf8ff")),
                ("GRID", (0, 0), (-1, -1), 0.4, colors.HexColor("#a0aec0")),
                ("VALIGN", (0, 0), (-1, -1), "TOP"),
                ("LEFTPADDING", (0, 0), (-1, -1), 4),
                ("RIGHTPADDING", (0, 0), (-1, -1), 4),
                ("TOPPADDING", (0, 0), (-1, -1), 3),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 3),
                ("ROWBACKGROUNDS", (0, 1), (-1, -1),
                 [colors.white, colors.HexColor("#f7fafc")]),
            ]
        )
    )
    story.append(t)

    # ========== TEIL 2: FRAGEN ==========
    story.append(PageBreak())
    story.append(Paragraph("Teil 2 — Fragen aus der Testfragen-Sammlung", s["h1"]))
    story.append(
        Paragraph(
            "Nur Fragen, die zum Stoff <b>bis einschließlich KW 41</b> passen. "
            "Spätere Themen (List Comprehensions, mutable/immutable Vertiefung, OOP, "
            "Lambda, unittest, verkettete Listen, …) sind bewusst weggelassen. "
            "Musterantworten zum Lernen – beim Test können Formulierungen abweichen.",
            s["body"],
        )
    )

    fragen_sammlung = [
        (
            "Erklären Sie Instanz, Referenz, Referenzzähler, Garbage Collection und del.",
            "Eine <b>Instanz</b> ist ein konkretes Objekt im Speicher. Eine <b>Referenz</b> "
            "ist ein Name/Zeiger darauf. Der <b>Referenzzähler</b> zählt, wie viele Referenzen "
            "auf das Objekt zeigen. Die <b>Garbage Collection</b> gibt Speicher frei, wenn "
            "nichts mehr darauf zeigt (plus Erkennung von Referenzzyklen). "
            "<b>del name</b> entfernt die Referenz; das Objekt verschwindet erst, wenn der "
            "Zähler 0 ist.",
        ),
        (
            "Was sind Type Hints?",
            "Optionale Typannotationen an Parametern, Rückgaben und Variablen "
            "(z. B. <font face='Courier'>def f(x: int) -> str:</font>). Sie dokumentieren "
            "Erwartungen und ermöglichen statische Prüfung (mypy), ändern aber zur Laufzeit "
            "meist nichts am dynamischen Verhalten.",
        ),
        (
            "Erklären Sie den Unterschied zwischen Compiler- und Interpretersprachen.",
            "<b>Compiler:</b> Quellcode wird vor dem Ausführen in Maschinencode/Bytecode "
            "übersetzt (C, C++, Java→Bytecode). <b>Interpreter:</b> Quellcode wird zur "
            "Laufzeit zeilen-/blockweise ausgeführt (Python, oft JS). Vorteil Interpreter: "
            "schneller Start/Portabilität; Vorteil Compiler: oft höhere Laufzeitleistung.",
        ),
        (
            "Unterschiede zwischen Java und Assembler.",
            "Assembler ist maschinennah (Register, Befehle der CPU), kaum Abstraktion. "
            "Java ist hochsprachlich: Objekte, GC, JVM-Bytecode, Plattformunabhängigkeit. "
            "Assembler: maximale Kontrolle/Leistung, wenig Portabilität; Java: Produktivität "
            "und Sicherheit auf Kosten von Abstraktionsschichten.",
        ),
        (
            "Unterschied if-elif-else und match case.",
            "<b>if-elif-else:</b> beliebige Bedingungen/Bereiche. "
            "<b>match/case:</b> Musterabgleich auf einen Wert (viele konkrete Fälle, "
            "Zerlegung von Strukturen). Für „viele Möglichkeiten eines Inhalts“ oft "
            "match/case klarer.",
        ),
        (
            "Was sind Kontrollstrukturen? Welche eignet sich, um viele Möglichkeiten "
            "eines Inhalts zu überprüfen?",
            "Kontrollstrukturen steuern den Programmfluss: Verzweigungen (if/match), "
            "Schleifen (for/while), Sprünge (break/continue), Ausnahmebehandlung "
            "(try/except). Für viele Möglichkeiten eines Inhalts: <b>match/case</b> "
            "(früher oft lange if-elif-Ketten).",
        ),
        (
            "Unterschied zwischen iterativer und rekursiver Programmierung.",
            "Iterativ: Schleifen + Zustandsvariablen. Rekursiv: Funktion ruft sich selbst "
            "mit kleinerem Teilproblem auf, braucht Basisfall. Rekursion oft eleganter bei "
            "Bäumen; Iteration oft speicher-/stackschonender.",
        ),
        (
            "Nennen Sie drei fachliche Unterschiede zwischen Java und Python.",
            "1) Typisierung: Java statisch / Python dynamisch (+ optionale Hints). "
            "2) Blöcke: Java { } / Python Einrückung. "
            "3) Ausführung: Java Compiler→Bytecode+JVM / Python Interpreter. "
            "(Weitere: kein ++ in Python; True/None vs. true/null; list vs. Array/ArrayList.)",
        ),
        (
            "Prozesse und Threads allgemein in Betriebssystemen.",
            "Ein <b>Prozess</b> ist ein laufendes Programm mit eigenem Adressraum. "
            "<b>Threads</b> sind parallele Ausführungspfade im selben Prozess und teilen "
            "sich Speicher. Prozesse: Isolation; Threads: leicht, aber Sync nötig.",
        ),
        (
            "Unterschied zwischen Arrays in Python und Java.",
            "Java-Arrays: feste Länge, einheitlicher Typ. In Python ist die Standard-"
            "Sequenz die <b>list</b> (dynamisch, gemischte Typen). „Echte“ Arrays gibt es "
            "über das Modul <font face='Courier'>array</font> oder NumPy – homogener Typ, "
            "fester/effizienter Speicher.",
        ),
        (
            "Unterschied zwischen array und list in Python sowie die Vorteile von Arrays.",
            "<b>list:</b> flexibel, beliebig typisiert, allgemein. "
            "<b>array/np.array:</b> ein Elementtyp, dichter Speicher, schneller bei "
            "großen Zahlenmengen und numerischen Operationen.",
        ),
        (
            "Nennen Sie drei Vorteile von Python gegenüber C-ähnlichen Sprachen.",
            "1) Hohe Produktivität / knappe Syntax. "
            "2) Dynamische Typen + großer Standard-/Library-Ökosystem. "
            "3) Automatische Speicherverwaltung (GC). "
            "(Auch: plattformübergreifend, gut zum Prototyping/Scripting.)",
        ),
        (
            "Drei Gemeinsamkeiten zwischen Java und Python.",
            "Beide: objektorientiert möglich; automatische Garbage Collection; "
            "Exceptions zur Fehlerbehandlung; große Standardbibliotheken; "
            "plattformübergreifend (JVM bzw. Interpreter).",
        ),
        (
            "Erklären Sie die pass-Anweisung in Python.",
            "<font face='Courier'>pass</font> ist eine No-Op-Anweisung: sie macht nichts "
            "und hält einen Block syntaktisch gültig (leere Funktion/Klasse/if-Zweig), "
            "wo Java leere { } hätte.",
        ),
        (
            "Unterschied im Umgang mit Datentypen zwischen Java und Python, "
            "einschließlich Type Hints.",
            "Java verlangt Deklaration und prüft Typen zur Compile-Zeit. "
            "Python bindet Typen an Objekte zur Laufzeit. Type Hints bringen optionale "
            "statische Hinweise ohne das dynamische Modell abzuschaffen.",
        ),
        (
            "Floor Division in Python 3.",
            "<font face='Courier'>//</font> teilt und rundet Richtung −∞ (Floor). "
            "Beispiele: <font face='Courier'>7 // 2 == 3</font>, "
            "<font face='Courier'>-7 // 2 == -4</font>. "
            "Dagegen liefert <font face='Courier'>/</font> immer float "
            "(<font face='Courier'>7 / 2 == 3.5</font>).",
        ),
        (
            "Garbage Collection allgemein.",
            "Automatische Freigabe nicht mehr erreichbarer Objekte. In CPython vor allem "
            "Referenzzählung; zusätzlich ein Zyklus-Collector für zirkuläre Referenzen.",
        ),
        (
            "Beispiel für den ternären Operator / bedingten Ausdruck.",
            "Konventionell: <font face='Courier'>if x &gt; 0: s = \"pos\"\\nelse: s = \"neg\"</font>. "
            "Ternär: <font face='Courier'>s = \"pos\" if x &gt; 0 else \"neg\"</font>.",
        ),
        (
            "Erläutern Sie den ternären Operator und geben Sie ein konventionelles "
            "Beispiel sowie die Umsetzung als ternären Operator an.",
            "Kurzform von if/else für Ausdrücke. "
            "Konventionell: if note &gt;= 50: status = \"ok\" else: status = \"fail\". "
            "Ternär: status = \"ok\" if note &gt;= 50 else \"fail\".",
        ),
        (
            "Exceptions anhand eines kompletten Code-Beispiels erklären "
            "(alle Exception-Teile).",
            "try: riskanter Code · except Typ as e: Behandlung · else: nur ohne Fehler · "
            "finally: immer (Aufräumen). Zusätzlich raise zum Auslösen.",
        ),
        (
            "Arten von Exceptions erklären; vier Exception-Kombis demonstrieren.",
            "Strategien: LBYL (vorher prüfen) vs. EAFP (try/except). "
            "Fehlerarten: neu erzeugt vs. „hochgeblubbert“; behebbar vs. nicht behebbar. "
            "Vier Kombis: (a) neuer + behebbar → Default setzen; "
            "(b) hochgeblubbert + behebbar → except und Alternative; "
            "(c) neuer + nicht behebbar → raise; "
            "(d) hochgeblubbert + nicht behebbar → nicht schlucken, nach oben lassen "
            "bzw. am Einstieg loggen und exit.",
        ),
    ]

    for i, (frage, antwort) in enumerate(fragen_sammlung, 1):
        block = [
            Paragraph(f"F{i}. {frage}", s["q"]),
            Paragraph(f"<b>Antwort:</b> {antwort}", s["a"]),
        ]
        story.append(KeepTogether(block))

    # ========== TEIL 3: ZUSATZ ==========
    story.append(PageBreak())
    story.append(Paragraph("Teil 3 — Zusatzfragen (Stoff bis KW 41)", s["h1"]))
    story.append(
        Paragraph(
            "Weitere Fragen, die man mit dem behandelten Stoff beantworten können sollte.",
            s["body"],
        )
    )

    zusatz = [
        (
            "Warum reicht „der Code läuft“ laut KW 38 nicht als Qualitätskriterium?",
            "Weil KI/schnell geschriebener Code subtile Logik- und Sicherheitsfehler "
            "enthalten kann. Nur wer Grundlagen beherrscht, kann verifizieren und reparieren.",
        ),
        (
            "Was bedeutet die Pilot-Analogie im Kontext von KI-generiertem Code?",
            "Autopilot (KI) erledigt Routine; der Pilot (Entwickler) muss System und "
            "Grundlagen kennen, um bei Ausfällen die Kontrolle zu übernehmen und zu haften.",
        ),
        (
            "Nennen Sie zwei konkrete Python-2→3-Brüche.",
            "print ist Funktion; / bei ints liefert float; str ist Unicode; "
            "viele Standardbibliotheks-Umbenennungen.",
        ),
        (
            "Wann würden Sie Rekursion vermeiden?",
            "Bei sehr großer Rekursionstiefe (Stack Overflow), engen Performance-/Speicher-"
            "Anforderungen oder wenn die iterative Form klarer ist.",
        ),
        (
            "Warum sind Threads im selben Prozess riskanter als getrennte Prozesse?",
            "Gemeinsamer Speicher → Race Conditions, wenn Synchronisation fehlt. "
            "Prozesse sind isolierter.",
        ),
        (
            "Ändern Type Hints das Laufzeitverhalten von Python?",
            "In der Regel nein – sie sind Hinweise für Menschen und Checker. "
            "(Ausnahmen: Tools/Libraries, die Annotations aktiv auswerten, z. B. zur Validierung.)",
        ),
        (
            "Was passiert bei del x, wenn noch eine andere Variable auf dasselbe Objekt zeigt?",
            "Nur der Name x verschwindet; der Referenzzähler sinkt um 1. Das Objekt bleibt, "
            "solange andere Referenzen existieren.",
        ),
        (
            "Schreiben Sie ein match/case für Wochentage (1–7) mit Default.",
            "match tag: case 1: … case 7: … case _: print(\"ungültig\")",
        ),
        (
            "Was macht for-else in Python?",
            "Der else-Zweig einer for-Schleife läuft, wenn die Schleife <b>nicht</b> mit "
            "break beendet wurde (typisch: „kein Treffer gefunden“).",
        ),
        (
            "Warum ist „solange random, bis 6 unique Zahlen“ für die Lotto-Aufgabe ungeeignet?",
            "Weil die Vorgabe lautet: bei 45 gezogenen Zahlen den RNG nur 45-mal nutzen. "
            "Wiederholtes Nachwürfeln verletzt das und kann theoretisch endlos laufen.",
        ),
        (
            "Wie speichern Sie in der Lotto-Statistik die Häufigkeiten am sinnvollsten?",
            "Als dict mit Schlüsseln 1…45 und Zählwerten; nach jeder Ziehung die sechs "
            "gezogenen Zahlen inkrementieren.",
        ),
        (
            "Was ist der Unterschied zwischen / und // bei negativen Zahlen?",
            "/ liefert float-Ergebnis der Division. // floored Richtung −∞, daher "
            "-7 // 2 == -4, nicht -3.",
        ),
        (
            "Warum sind Variablen in Python case-sensitiv – Beispiel?",
            "Score und score sind verschiedene Namen; Zuweisung an einen ändert den anderen nicht.",
        ),
        (
            "Wozu dient die Shebang-Zeile?",
            "Unter UNIX sagt sie dem System, mit welchem Interpreter die Datei ausgeführt "
            "werden soll, z. B. #!/usr/bin/env python3.",
        ),
        (
            "Welche Einrückungsregel gilt laut Stoff / Stil?",
            "Keine Tabs, genau 4 Leerzeichen; Zeilen möglichst ≤ 80 Zeichen, Umbruch mit \\.",
        ),
        (
            "Wann verwenden Sie pass?",
            "Als Platzhalter, wenn Syntax einen Block verlangt, aber noch keine Logik "
            "existiert (Stub-Funktion, leerer except vorübergehend – vorsichtig!).",
        ),
        (
            "Nennen Sie drei Python-Schlüsselwörter.",
            "z. B. if, else, elif, for, while, def, class, return, import, try, except, "
            "True, False, None, pass, break, continue, …",
        ),
        (
            "Wie lösen Sie eine Exception selbst aus?",
            "raise ValueError(\"Beschreibung\") – oder einen anderen Exception-Typ.",
        ),
        (
            "Was ist der Unterschied zwischen list und dict in einem Satz?",
            "list: geordnete Sequenz indexiert ab 0; dict: Abbildung Schlüssel → Wert.",
        ),
        (
            "Warum eignet sich ein Dictionary besonders für die Lotto-Statistik?",
            "Direkter Zugriff „Zahl → Häufigkeit“ in amortisiert O(1), ohne jedes Mal "
            "eine Liste zu durchsuchen.",
        ),
    ]

    for i, (frage, antwort) in enumerate(zusatz, 1):
        block = [
            Paragraph(f"Z{i}. {frage}", s["q"]),
            Paragraph(f"<b>Antwort:</b> {antwort}", s["a"]),
        ]
        story.append(KeepTogether(block))

    story.append(Spacer(1, 12))
    story.append(
        Paragraph(
            "Viel Erfolg beim Lernen. Beim echten Test können auch andere/weitere Fragen kommen.",
            s["body"],
        )
    )

    doc = SimpleDocTemplate(
        str(OUT),
        pagesize=A4,
        leftMargin=2 * cm,
        rightMargin=2 * cm,
        topMargin=1.8 * cm,
        bottomMargin=2 * cm,
        title="SWP-Python Lernzusammenfassung bis KW 41",
        author="Lernmaterial 5BHWII",
    )
    doc.build(story, onFirstPage=add_header_footer, onLaterPages=add_header_footer)
    print(f"Wrote {OUT}")


if __name__ == "__main__":
    build()
