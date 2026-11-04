# ANKA TRANSPORT

Statische Unternehmenswebsite für ANKA TRANSPORT aus Bad Kreuznach.

- `index.html`: Transportangebot, Fahrzeugauswahl, Unternehmen und Ablauf
- `festeinsatz.html`: Fahrzeugklassen, Festeinsatz, Planung und häufige Fragen
- `unternehmen.html`: Unternehmen, Lizenz/Versicherung, Kontakt und Anfragevorbereitung
- `impressum.html`, `datenschutz.html`: direkt verlinkte Rechtstexte, auch ohne JavaScript

Die Seiten werden mit `python3 build_pages.py` erzeugt. Gestaltung und Interaktionen liegen in `assets/style.css` und `assets/app.js`. Rechtstexte, Anfrageformular und Anfrageübersicht werden aus `content/` eingebunden. Alle Schriften und Bilder werden lokal geladen. Es gibt keine Laufzeitabhängigkeiten.

Version 4 richtet den Auftritt klar auf Transport und LKW-Festeinsatz aus: Barlow Condensed Bold und Instrument Sans, Orange, Anthrazit und Schwarz entsprechend der vom Nutzer bereitgestellten Markenreferenz, kantige Flächen und ausschließlich Originalfotos von ANKA. Das bereitgestellte Logo ist als Originaldatei eingebunden: Emblem und Schriftzug im Header, vollständige Marke im Footer und Emblem als Favicon. Der Bildausschnitt wird über CSS beziehungsweise den SVG-ViewBox gesteuert; die Pixel der Vorlage wurden nicht verändert. Die Referenz gilt als vom Nutzer bereitgestellter, noch nicht ausdrücklich bestätigter Markenstand. Die interaktive Fahrzeugauswahl ergänzt eigene schematische LKW-Illustrationen. Die vorhandene generierte Landschaftsaufnahme und ältere Symbolbilder werden nicht mehr in die Seiten eingebunden.

Die Fahrzeugklasse lässt sich per Tab-Auswahl, Tastatur oder URL-Parameter `fahrzeug` auswählen. Anfragelinks übernehmen die Auswahl in das Formular. Die Anfragevorbereitung validiert Pflichtfelder und erstellt eine kopierbare Übersicht. Sie sendet keine Daten und nutzt keinen dauerhaften Browserspeicher.

## Rechtstexte

- Geschäftsanschrift, Telefonnummer, E-Mail und USt-IdNr. werden über `content/legal-details.json` gepflegt. Optionale Registerdaten und Wirtschafts-Identifikationsnummer nur eintragen, wenn sie vorliegen.
- Die Aufsicht für den gewerblichen Güterkraftverkehr ist der [Landesbetrieb Mobilität Rheinland-Pfalz](https://lbm.rlp.de/wichtigelinks/kontakt), wie in der vorgelegten Gemeinschaftslizenz angegeben. Lizenz- und Versicherungsunterlagen selbst gehören nicht ins öffentliche Repository.
- Die Datenschutzhinweise beschreiben GitHub Pages, Outlook.com als E-Mail-Dienst, lokale Assets, den externen Kartenlink und die lokale Anfragevorbereitung ohne Versand. Bei einem Wechsel der Dienste bitte entsprechend aktualisieren.
- Mit `python3 build_pages.py` neu erzeugen. `noindex,nofollow` bleibt bis zur Freigabe der endgültigen Domain gesetzt; das ist keine Zugangssperre.

Validierung für Version 4: JavaScript-Syntax, interne Dateien und Sprungziele, eindeutige IDs, Überschriftenstruktur, aktive Navigation, ARIA-/Dialogverweise, Alttexte, Bildintegrität, Fontreferenzen, unveränderte Logo-Datei, Logo-Ausschnittgrenzen, Textkontraste und mobile Hauptheadline mit tatsächlichen Schriftmetriken bei 320 bis 1440 Pixeln. Ein visueller Browsercheck war in dieser Umgebung nicht verfügbar und bleibt vor dem Kundenlaunch erforderlich.

## Hosting

Die fertigen HTML-Seiten liegen im Repository-Hauptverzeichnis und können direkt statisch gehostet werden. Ein Build-Schritt ist nicht erforderlich. Änderungen am Generator können mit `python3 build_pages.py` in die drei HTML-Seiten übernommen werden.
