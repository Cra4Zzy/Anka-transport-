# ANKA TRANSPORT

Statische Unternehmenswebsite für ANKA TRANSPORT aus Bad Kreuznach.

- `index.html`: Transportangebot, Fahrzeugauswahl, Unternehmen und Ablauf
- `festeinsatz.html`: Fahrzeugklassen, Festeinsatz, Planung und häufige Fragen
- `unternehmen.html`: Unternehmen, Lizenz/Versicherung, Kontakt und Anfragevorbereitung
- `impressum.html`, `datenschutz.html`: direkt verlinkte Rechtstexte, auch ohne JavaScript

Die Seiten werden mit `python3 build_pages.py` erzeugt. Gestaltung und Interaktionen liegen in `assets/style.css` und `assets/app.js`. Rechtstexte, Anfrageformular und Anfrageübersicht werden aus `content/` eingebunden. Alle Schriften und Bilder werden lokal geladen. Es gibt keine Laufzeitabhängigkeiten.

Version 4 richtet den Auftritt klar auf Transport und LKW-Festeinsatz aus: Barlow Condensed Bold und Instrument Sans, Orange, Anthrazit und Schwarz entsprechend der vom Nutzer bereitgestellten Markenreferenz, kantige Flächen und ausschließlich Originalfotos von ANKA. Das bereitgestellte Logo ist als Originaldatei eingebunden: Emblem und Schriftzug im Header, vollständige Marke im Footer und Emblem als Favicon. Der Bildausschnitt wird über CSS beziehungsweise den SVG-ViewBox gesteuert; die Pixel der Vorlage wurden nicht verändert. Die Referenz gilt als vom Nutzer bereitgestellter, noch nicht ausdrücklich bestätigter Markenstand. Die interaktive Fahrzeugauswahl ergänzt eigene schematische LKW-Illustrationen. Die vorhandene generierte Landschaftsaufnahme und ältere Symbolbilder werden nicht mehr in die Seiten eingebunden.

Die Fahrzeugklasse lässt sich per Tab-Auswahl, Tastatur oder URL-Parameter `fahrzeug` auswählen. Anfragelinks übernehmen die Auswahl in das Formular. Die Anfragevorbereitung validiert Pflichtfelder und erstellt eine kopierbare Übersicht. Sie sendet keine Daten und nutzt keinen dauerhaften Browserspeicher.

## Vor der Freigabe

- Geschäftliche E-Mail-Adresse in `content/legal-details.json` ergänzen. Dieselbe Adresse erscheint im Impressum, im Datenschutz und bei den Kontaktdaten. Telefonnummer: [öffentliche Stellenanzeige von ANKA TRANSPORT](https://de.linkedin.com/jobs/view/lkw-fahrer-m-w-d-f%C3%BCr-den-nahverkehr-at-anka-transport-herrn-zafer-beyazdogan-4482345038).
- Falls vorhanden, Register und Registernummer, USt-IdNr. bzw. Wirtschafts-Identifikationsnummer in derselben Datei ergänzen. Aufsichtsbehörde mit der Lizenz abgleichen; die [Stadt Bad Kreuznach](https://www.bad-kreuznach.de/buergerservice/buergerservice/abteilungen/RLP:department:268447/sachgebiet-strassenverkehrsangelegenheiten/) führt den gewerblichen Güterkraftverkehr für diesen Standort in ihrem Zuständigkeitsbereich.
- Datenschutzhinweise anpassen, falls der Hosting- oder Kontaktweg vom dokumentierten Stand abweicht. Die Erklärung basiert auf GitHub Pages, lokalen Assets, einem externen Kartenlink und der reinen Anfragevorbereitung ohne Versand.
- Mit `python3 build_pages.py` neu erzeugen. `noindex,nofollow` bleibt bis zur Freigabe gesetzt; das ist keine Zugangssperre.

Validierung für Version 4: JavaScript-Syntax, interne Dateien und Sprungziele, eindeutige IDs, Überschriftenstruktur, aktive Navigation, ARIA-/Dialogverweise, Alttexte, Bildintegrität, Fontreferenzen, unveränderte Logo-Datei, Logo-Ausschnittgrenzen, Textkontraste und mobile Hauptheadline mit tatsächlichen Schriftmetriken bei 320 bis 1440 Pixeln. Ein visueller Browsercheck war in dieser Umgebung nicht verfügbar und bleibt vor dem Kundenlaunch erforderlich.

## Hosting

Die fertigen HTML-Seiten liegen im Repository-Hauptverzeichnis und können direkt statisch gehostet werden. Ein Build-Schritt ist nicht erforderlich. Änderungen am Generator können mit `python3 build_pages.py` in die drei HTML-Seiten übernommen werden.
