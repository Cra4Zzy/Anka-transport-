# ANKA TRANSPORT — Gestaltung Version 4

## Aufgabe

Der vorherige Entwurf wirkte durch Serifenschrift, Bildbögen, warme Naturfarben und eine landschaftliche Bildbühne wie eine Fotografenwebsite. Der neue Auftritt macht die tatsächliche Leistung sofort verständlich: LKW mit Fahrer im Festeinsatz für Speditionen, Logistikdienstleister und Unternehmen.

## Gestaltung

- Die Markenreferenz des Nutzers vom 14.10.2026 zeigt ein orangefarbenes A mit Straßenmotiv und den Schriftzug ANKA TRANSPORT auf dunklem Hintergrund. Die aktuelle Gestaltung verwendet Orange `#ef7d14`, Anthrazit `#171d24`, Schwarz `#070b11` und Hellgrau `#f1f2f3`. Für orange Schrift auf hellen Flächen wird der dunklere Ton `#ac4e08` verwendet.
- Barlow Condensed Bold für kompakte, starke Überschriften. Instrument Sans für Inhalte, Navigation und Formulare. Schriften werden lokal geladen. Barlow-Quelle und Lizenz: [Google Fonts](https://github.com/google/fonts/tree/main/ofl/barlowcondensed), OFL im Asset-Verzeichnis.
- Der Einstieg nennt das Angebot direkt: **LKW. FAHRER. FESTEINSATZ.** Seine dunkle Fläche mit orangefarbener Hervorhebung steht neben der Originalaufnahme des LKW am Ladehof.
- Rechteckige, sachliche Flächen mit verschiedenen Größen und Ausrichtungen. Keine Serifenschrift, Bildbögen, dekorativen Pfeile oder Trennlinienraster.
- Originalbilder von Ladehof, Ladung und Ladebordwand verankern die Seite im Transportalltag. Landschaftsinszenierung und ergänzende Stockbilder werden nicht in die aktuellen Seiten eingebunden.
- Eine kompakte obere Fahrzeugübersicht, dunkle Auswahlfläche, Originalfotos, praktische Ablaufblöcke und ein orangefarbener Anfrageabschluss variieren die Seitenstruktur.
- Die gelieferte Logo-Datei wird unverändert eingebunden. Header: Emblem und Schriftzug mit CSS-Ausschnitten aus derselben Originaldatei. Footer: vollständige Marke mit CSS-Ausschnitt des Leerraums. Favicon: Originalemblem als eingebettetes Bild im SVG-ViewBox. Keine generative Neuzeichnung und keine Änderung der Rasterpixel. Der Nutzer hat den offiziellen Markenstand noch nicht ausdrücklich bestätigt.

## Drei Seiten

**Start:** Leistung im Einstieg, vier Fahrzeugklassen, Nutzen des Festeinsatzes, interaktive Auswahl, persönliche Führung, Ablauf und Anfrage.

**Fahrzeuge & Festeinsatz:** Originalaufnahme des Laderaums, Auswahl der Klassen, vier konkrete Planungspunkte, Ablauf, häufige Fragen und Anfrage.

**Unternehmen & Kontakt:** Inhabergeführtes Transportunternehmen aus Bad Kreuznach, Ansprechpartner Zafer Beyazdogan, bereitgestellte Angaben zu Gemeinschaftslizenz und Güterschaden-Haftpflicht sowie Anfragevorbereitung.

## Funktionen

Die Fahrzeugauswahl bleibt mit Tastatur bedienbar. Jede Klasse zeigt eine eigene schematische LKW-Illustration. Die Illustrationen sind keine verbindlichen Fahrzeug- oder Ausstattungsangaben. Die URL-Auswahl führt zur Fahrzeugauswahl und übernimmt die passende Klasse in den Anfrageweg.

Menü, FAQ, Informationsdialoge, Pflichtfeldvalidierung und kopierbare Anfrageübersicht bleiben erhalten. Das Formular versendet weiterhin keine Anfrage. Es macht diesen Stand unmittelbar im Formular und in der Übersicht sichtbar.

## Prüfungen und offene Punkte

Geprüft: drei Seiten, lokale Dateien und Sprungziele, eindeutige IDs, Überschriftenstruktur, aktive Navigation, ARIA-/Dialogverweise, Alttexte und Bildintegrität, Fontreferenzen und JavaScript-Syntax. Zusätzlich geprüft: identische Logo-Datei, Ausschnittgrenzen für Header und Footer und Textkontraste der Markenfarben. Die längste Hauptheadline wurde mit der tatsächlichen Schrift bei 320 bis 1440 Pixeln auf Breite geprüft.

Ein visueller Browsercheck ist in dieser Umgebung nicht verfügbar. Telefon, E-Mail, der endgültige Versandweg und vollständige Rechtstexte müssen vor dem Kundenlaunch ergänzt werden.

## Referenzen der vorangegangenen Recherche

Die vorhandene Recherche betrachtete Terminal Industries, Emons, LODISNA, M.V.P. Trans-Logistics, PureFreight und Freight Consolidators. Übernommen wurden allgemeine Prinzipien: Transportleistung klar zeigen, Bilder des tatsächlichen Betriebs verwenden und Fahrzeugauswahl und Anfrage verständlich verbinden. Der neue Aufbau und seine Assets sind eigenständig erstellt; fremde Website-Assets wurden nicht übernommen.
