"""Generate the three ANKA pages. Static assets are served from dist/assets."""
from pathlib import Path
from html import escape

P = Path(__file__).parent
D = P
LOGO = 'assets/anka-brand-reference.png'
NAV = [('index.html', 'Start'), ('festeinsatz.html', 'Fahrzeuge & Festeinsatz'), ('unternehmen.html', 'Unternehmen & Kontakt')]
CLASSES = [
    ('7-5', '7,5 t', '7,5-Tonner mit Fahrer', 'Für Ihre regelmäßigen Transporte – mit Einsatzzeiten und Touren nach Vereinbarung.', 'Regelmäßige Transporte'),
    ('12', '12 t', '12-Tonner mit Fahrer', 'Für Ihre täglichen Transportaufgaben – fest in Ihre Abläufe eingeplant.', 'Tägliche Transportaufgaben'),
    ('18', '18 t', '18-Tonner mit Fahrer', 'Für Ihre laufenden Aufträge – als Ergänzung Ihrer Transportkapazitäten.', 'Zusätzliche Kapazität'),
    ('Sattelzug', 'Sattelzug', 'Sattelzüge mit Fahrer', 'Für Transporte mit großem Platzbedarf – im langfristigen Festeinsatz.', 'Großer Platzbedarf'),
]


def header(page):
    links = ''.join(f'<a href="{url}"'+(' aria-current="page"' if url == page else '')+f'>{label}</a>' for url, label in NAV)
    return f'''<a class="skip" href="#main">Zum Inhalt</a>
<header class="header"><a class="brand" href="index.html" aria-label="ANKA TRANSPORT Startseite"><span class="brand-icon"><img src="{LOGO}" alt="" width="352" height="510"></span><span class="brand-name"><img src="{LOGO}" alt="" width="352" height="510"></span></a>
<button class="menu-toggle" type="button" aria-expanded="false" aria-controls="navigation"><span>Menü</span><i aria-hidden="true"></i></button>
<nav id="navigation" aria-label="Hauptnavigation">{links}<a class="button button-small" href="unternehmen.html#anfrage">Festeinsatz anfragen</a></nav></header>'''


def footer():
    legal = (P/'content/legal.html').read_text().replace('class="eyebrow"', 'class="kicker"')
    return '''<footer class="footer"><div class="footer-top"><a class="footer-brand" href="index.html" aria-label="ANKA TRANSPORT Startseite"><span class="brand-lockup"><img src="assets/anka-brand-reference.png" alt="" width="352" height="510" loading="lazy"></span></a><p>LKW mit Fahrer.<br>Fest in Ihre Abläufe eingeplant.</p></div>
<div class="footer-columns"><div><span class="footer-label">Ihr Ansprechpartner</span><strong>Zafer Beyazdogan</strong><span>Inhaber · ANKA TRANSPORT</span></div><div><span class="footer-label">Unser Standort</span><address>Rheinhessenstraße 102<br>55545 Bad Kreuznach</address></div><div><span class="footer-label">Entdecken</span><a href="festeinsatz.html">Fahrzeuge & Festeinsatz</a><a href="unternehmen.html">Unternehmen & Kontakt</a></div></div>
<div class="footer-bottom"><span>© <span data-year>2026</span> ANKA TRANSPORT</span><div><button type="button" data-dialog="impressum">Impressum</button><button type="button" data-dialog="datenschutz">Datenschutz</button><button type="button" data-dialog="bildnachweise">Bildnachweise</button></div><a href="#top">Nach oben</a></div></footer>'''+legal


def cta():
    return '''<section class="closing section"><div><span class="kicker">Ihr nächster Festeinsatz</span><h2>WAS STEHT<br>BEI IHNEN AN?</h2></div><div class="closing-action"><p>Sprechen wir über Ihre Touren, Ihre Einsatzzeiten und das passende Fahrzeug.</p><a class="button button-dark" href="unternehmen.html#anfrage">Festeinsatz anfragen</a></div></section>'''


def truck_svg(key):
    # Stylised class illustrations; neither dimensions nor vehicle equipment specifications.
    long = key == 'Sattelzug'
    width = {'7-5': 240, '12': 290, '18': 325, 'Sattelzug': 325}[key]
    left = 75 if long else 130
    cabin = 415 if long else left + width + 5
    wheel_positions = [left+50, cabin+42]
    if key == '18': wheel_positions.insert(1, left+88)
    if long: wheel_positions = [left+38, left+74, left+110, cabin+9, cabin+47]
    wheels = ''.join(f'<circle cx="{x}" cy="205" r="22" fill="#151a20"/><circle cx="{x}" cy="205" r="10" fill="#c7d0d8"/><circle cx="{x}" cy="205" r="3" fill="#151a20"/>' for x in wheel_positions)
    body = f'<rect x="{left}" y="62" width="{width}" height="119" rx="2" fill="#e5eaf0"/><rect x="{left}" y="164" width="{width}" height="17" fill="#a9bac9"/><rect x="{left+14}" y="76" width="5" height="77" fill="#c7d1db"/>'
    if long: body += '<rect x="362" y="190" width="100" height="10" fill="#151a20"/>'
    return f'''<svg class="truck-illustration" data-truck="{key}" viewBox="0 0 600 250" aria-hidden="true">{body}<path d="M{cabin} 103h60l31 55v41h-91z" fill="#fff"/><path d="M{cabin+10} 112h43l23 40h-66z" fill="#2b3037"/><path d="M{cabin+57} 117v35" stroke="#fff" stroke-width="4"/><rect x="{left}" y="182" width="{cabin-left+91}" height="17" fill="#292e35"/><rect x="{cabin+61}" y="166" width="26" height="8" fill="#f38a24"/>{wheels}</svg>'''


def fleet_picker(prefix):
    tabs = ''.join(f'<button type="button" role="tab" id="{prefix}-tab-{key}" aria-controls="{prefix}-panel" aria-selected="{str(i==0).lower()}" tabindex="{0 if i==0 else -1}" data-fleet="{key}">{short}</button>' for i, (key, short, *_rest) in enumerate(CLASSES))
    illustrations = ''.join(truck_svg(key) for key, *_ in CLASSES)
    return f'''<div class="fleet-picker" data-fleet-picker><div class="fleet-tabs" role="tablist" aria-label="Fahrzeugklasse auswählen">{tabs}</div>
<div class="fleet-stage" id="{prefix}-panel" role="tabpanel" tabindex="0" aria-labelledby="{prefix}-tab-7-5" data-kind="7-5">
<div class="fleet-detail"><span class="kicker">LKW + Fahrer</span><span class="fleet-weight" data-fleet-weight>7,5<small>t</small></span><h3 data-fleet-title>7,5-Tonner mit Fahrer</h3><p data-fleet-description>Für Ihre regelmäßigen Transporte – mit Einsatzzeiten und Touren nach Vereinbarung.</p><div class="fleet-tags"><span data-fleet-use>Regelmäßige Transporte</span><span>Mit Fahrer</span></div><a class="button button-orange" data-fleet-link href="unternehmen.html?fahrzeug=7-5#anfrage">Diesen Festeinsatz anfragen</a></div>
<div class="fleet-visual"><span class="fleet-visual-label">FEST IN IHRE PLANUNG EINGEBUNDEN.</span>{illustrations}<small>Schematische Darstellung der Fahrzeugklasse</small><div class="fleet-availability">Fahrzeugausstattung, Verfügbarkeit und Einsatzbedingungen stimmen wir persönlich mit Ihnen ab.</div></div></div></div>'''


def steps():
    return '''<div class="steps"><article><span class="step-tag">Bedarf</span><h3>Sie sagen,<br>was ansteht.</h3><p>Fahrzeugklasse, Einsatzort, Touren und Starttermin: Wir besprechen Ihren konkreten Bedarf.</p></article><article><span class="step-tag">Abstimmung</span><h3>Wir klären<br>den Einsatz.</h3><p>Touren, Einsatzzeiten, Laufzeit und Konditionen werden gemeinsam vereinbart.</p></article><article><span class="step-tag">Festeinsatz</span><h3>ANKA fährt<br>Ihre Touren.</h3><p>Mit LKW und Fahrer starten wir zum vereinbarten Termin in Ihren abgestimmten Einsatz.</p></article></div>'''


hero_links = ''.join(f'<a href="festeinsatz.html?fahrzeug={key}#fahrzeugauswahl"><strong>{short}</strong><span>Mit Fahrer im Festeinsatz</span></a>' for key, short, *_ in CLASSES)
home = f'''<section class="home-hero"><div class="hero-copy"><span class="kicker">ANKA TRANSPORT · BAD KREUZNACH</span><h1>LKW.<br>FAHRER.<br><span>FESTEINSATZ.</span></h1><p>Ihr Transportauftrag. Unser Einsatz.<br>LKW mit Fahrer für Ihre regelmäßigen Touren.</p><div class="hero-actions"><a class="button button-orange" href="unternehmen.html#anfrage">Festeinsatz anfragen</a><a class="hero-link" href="festeinsatz.html">Fahrzeuge entdecken</a></div><span class="hero-for">Für Speditionen, Logistikdienstleister & Unternehmen</span></div>
<div class="hero-photo"><img src="assets/anka-truck.webp" alt="Mercedes-Benz-LKW von ANKA TRANSPORT am Ladehof" width="1200" height="1600" fetchpriority="high"><span class="photo-label">ANKA IM TRANSPORTALLTAG</span><div class="hero-photo-note"><strong>IHRE TOUREN.<br>UNSER ANTRIEB.</strong><span>LKW + Fahrer · Festeinsatz</span></div></div></section>
<div class="class-strip" aria-label="Unsere Fahrzeugklassen">{hero_links}</div>
<section class="intro section"><div class="intro-copy"><span class="kicker">Ihr Partner für regelmäßige Transporte</span><h2>PLANBARE<br>KAPAZITÄT.<br><span class="accent-text">KLARE ABSPRACHEN.</span></h2><p class="lead">ANKA unterstützt Ihren Transportbetrieb mit LKW und Fahrer im Festeinsatz.</p><p>Fahrzeug, Touren, Einsatzzeiten und Laufzeit stimmen wir auf Ihre Anforderungen ab. Als Subunternehmer arbeiten wir mit Speditionen, Logistikdienstleistern und Unternehmen zusammen.</p><div class="service-facts"><div><strong>LKW + Fahrer</strong><span>Für Ihren vereinbarten Einsatz</span></div><div><strong>Regelmäßige Touren</strong><span>Fest in Ihre Abläufe eingeplant</span></div><div><strong>Direkter Kontakt</strong><span>Mit Inhaber Zafer Beyazdogan</span></div></div><a class="text-link" href="festeinsatz.html">Mehr zum Festeinsatz</a></div><figure class="intro-photo"><img src="assets/anka-loading.webp" alt="Geöffneter ANKA-LKW mit Ladebordwand und palettierter Ladung" width="1200" height="1600" loading="lazy"><figcaption><span>VOM LADEHOF IN IHRE TOUREN.</span><strong>Transport ist unser Alltag.</strong></figcaption></figure></section>
<section class="fleet-section section" id="fahrzeuge"><div class="section-title"><div><span class="kicker">Die passende Fahrzeugklasse</span><h2>IHR BEDARF.<br>UNSER FAHRZEUG.</h2></div><p>7,5 t, 12 t, 18 t oder Sattelzug.<br>Wählen Sie Ihre Fahrzeugklasse.</p></div>{fleet_picker('fleet-home')}</section>
<section class="partner-section section"><div class="partner-photo"><img src="assets/anka-front.webp" alt="Frontansicht des ANKA-LKW am Ladehof" width="1200" height="1600" loading="lazy"><span class="photo-label">ANKA TRANSPORT · BAD KREUZNACH</span></div><div class="partner-copy"><span class="kicker">Inhabergeführt. Persönlich abgestimmt.</span><h2>TRANSPORT<br>IST TEAMARBEIT.</h2><p>Sie kennen Ihre Aufträge. Wir besprechen mit Ihnen, wie unser Festeinsatz Ihre Abläufe unterstützt.</p><p>Ihr Ansprechpartner ist Zafer Beyazdogan, Inhaber von ANKA TRANSPORT. Vom ersten Gespräch bis zur Abstimmung des Einsatzes.</p><div class="owner"><span class="owner-monogram" aria-hidden="true">ZB</span><div><strong>Zafer Beyazdogan</strong><span>Inhaber · ANKA TRANSPORT</span></div></div><a class="button" href="unternehmen.html">Unternehmen kennenlernen</a></div></section>
<section class="process-section section"><div class="section-title"><div><span class="kicker">So starten wir</span><h2>VOM BEDARF<br>AUF DIE STRASSE.</h2></div><p>Drei Schritte zum abgestimmten<br>Festeinsatz mit ANKA.</p></div>{steps()}</section>{cta()}'''

questions = [
 ('Für wen ist der Festeinsatz gedacht?', 'Für Speditionen, Logistikdienstleister und Unternehmen mit regelmäßigen Touren oder langfristigen Transportaufgaben. ANKA TRANSPORT unterstützt Sie als Subunternehmer mit LKW und Fahrer.'),
 ('Ist der Fahrer im Einsatz enthalten?', 'Ja. Das Angebot umfasst LKW mit Fahrer im Festeinsatz. Fahrzeug und Einsatz werden gemeinsam mit Ihnen abgestimmt.'),
 ('Welche Angaben brauchen Sie für eine Anfrage?', 'Hilfreich sind die gewünschte Fahrzeugklasse, der Einsatzort, Ihre Touren, Einsatzzeiten und der geplante Starttermin. Laufzeit und Konditionen klären wir gemeinsam.'),
 ('Wie werden Laufzeit und Konditionen vereinbart?', 'Wir besprechen Ihren konkreten Bedarf und stimmen Touren, Einsatzzeiten, Laufzeit und Konditionen persönlich mit Ihnen ab.'),
]
faq = ''.join(f'<details><summary>{q}<span aria-hidden="true">+</span></summary><p>{a}</p></details>' for q, a in questions)
fleet = f'''<section class="subhero fleet-hero"><div class="subhero-copy"><span class="kicker">Fahrzeuge & Festeinsatz</span><h1>DAS FAHRZEUG<br>FÜR IHRE<br><span>TOUREN.</span></h1><p>Vom 7,5-Tonner bis zum Sattelzug. Mit Fahrer, für den gemeinsam vereinbarten Einsatz.</p><a class="button button-orange" href="#fahrzeugauswahl">Fahrzeugklasse auswählen</a></div><div class="subhero-photo"><img src="assets/anka-cargo.webp" alt="Palettierte Ladung im Laderaum des ANKA-LKW" width="1200" height="1600" fetchpriority="high"><span class="photo-label">EINBLICK IN DEN ANKA-LADERAUM</span></div></section>
<section class="fleet-section section" id="fahrzeugauswahl"><div class="section-title"><div><span class="kicker">Vier Fahrzeugklassen</span><h2>WAS BRAUCHT<br>IHR EINSATZ?</h2></div><p>Wählen Sie Ihre Klasse.<br>Die Details klären wir im Gespräch.</p></div>{fleet_picker('fleet-full')}</section>
<section class="planning-section section"><div class="planning-copy"><span class="kicker">Der Festeinsatz</span><h2>PASSEND ZU<br>IHREN ABLÄUFEN.</h2><p class="lead">LKW und Fahrer für Ihren vereinbarten Einsatz. Die Planung machen wir gemeinsam.</p><dl><div><dt>Fahrzeug</dt><dd>Welche Klasse und Ausstattung brauchen Ihre Transporte?</dd></div><div><dt>Touren</dt><dd>Welche Strecken und Einsatzorte stehen an?</dd></div><div><dt>Einsatzzeiten</dt><dd>Wann und wie regelmäßig soll gefahren werden?</dd></div><div><dt>Laufzeit</dt><dd>Ab wann und wie lange benötigen Sie Unterstützung?</dd></div></dl></div><figure class="planning-photo"><img src="assets/anka-loading.webp" alt="Ladebordwand und Laderaum des ANKA-LKW" width="1200" height="1600" loading="lazy"><figcaption>LKW und Fahrer für Ihre Transportaufgaben.</figcaption></figure></section>
<section class="process-section section"><div class="section-title"><div><span class="kicker">Die Zusammenarbeit</span><h2>KLAR GEPLANT.<br>GEMEINSAM GESTARTET.</h2></div></div>{steps()}</section>
<section class="faq section"><div><span class="kicker">Fragen zum Festeinsatz</span><h2>GUT ZU<br>WISSEN.</h2></div><div class="faq-items">{faq}</div></section>{cta()}'''

form = (P/'content/request-form.html').read_text()
summary = (P/'content/request-summary.html').read_text()
company = f'''<section class="subhero company-hero"><div class="subhero-copy"><span class="kicker">Unternehmen & Kontakt</span><h1>TRANSPORT.<br><span>PERSÖNLICH<br>GEFÜHRT.</span></h1><p>ANKA TRANSPORT aus Bad Kreuznach.<br>Ihr Partner für LKW mit Fahrer im Festeinsatz.</p><a class="button button-orange" href="#anfrage">Einsatz besprechen</a><div class="owner owner-light"><span class="owner-monogram" aria-hidden="true">ZB</span><div><strong>Zafer Beyazdogan</strong><span>Inhaber · ANKA TRANSPORT</span></div></div></div><div class="subhero-photo"><img src="assets/anka-front.webp" alt="Mercedes-Benz-LKW von ANKA TRANSPORT am Ladehof" width="1200" height="1600" fetchpriority="high"><span class="photo-label">BAD KREUZNACH · RHEINLAND-PFALZ</span></div></section>
<section class="about-section section"><div><span class="kicker">Über ANKA TRANSPORT</span><h2>FESTER PARTNER.<br><span class="accent-text">DIREKTER KONTAKT.</span></h2></div><div class="about-copy"><p class="lead">Inhabergeführt von Zafer Beyazdogan. Mit Sitz in Bad Kreuznach.</p><p>Als Subunternehmer unterstützen wir Speditionen, Logistikdienstleister und Unternehmen mit LKW und Fahrer im Festeinsatz. Persönliche Zusammenarbeit und klare Vereinbarungen bilden die Grundlage.</p><p>7,5-Tonner, 12-Tonner, 18-Tonner und Sattelzüge: Welches Fahrzeug für Ihre Touren passt, stimmen wir mit Ihnen ab.</p></div></section>
<section class="credentials section"><div class="section-title"><div><span class="kicker">Lizenz & Versicherung</span><h2>DIE GRUNDLAGE<br>FÜR UNSEREN EINSATZ.</h2></div></div><div class="credential-cards"><article><span class="credential-icon" aria-hidden="true"><svg viewBox="0 0 32 36"><path d="M6 3h13l7 7v23H6zM19 3v8h7M11 18h10M11 23h10M11 28h6"/></svg></span><div><h3>Gemeinschaftslizenz</h3><p>Für den grenzüberschreitenden gewerblichen Güterkraftverkehr liegt eine Gemeinschaftslizenz vor.</p></div></article><article><span class="credential-icon" aria-hidden="true"><svg viewBox="0 0 32 36"><path d="M16 3 28 8v10c0 7-5 12-12 15C9 30 4 25 4 18V8zM10 18l4 4 8-9"/></svg></span><div><h3>Güterschaden-Haftpflicht</h3><p>Es liegt eine Versicherungsbestätigung über eine Güterschaden-Haftpflichtversicherung gemäß § 7a GüKG vor.</p></div></article></div></section>
<section class="contact-section section" id="anfrage"><div class="contact-intro"><span class="kicker">Anfrage vorbereiten</span><h2>IHRE TOUREN.<br><span class="accent-text">UNSER EINSATZ.</span></h2><p>Welche Fahrzeugklasse, welcher Einsatzort, welcher Start? Bereiten Sie Ihren Bedarf für die persönliche Abstimmung vor.</p><div class="contact-address"><span>Ihr Ansprechpartner</span><strong>Zafer Beyazdogan</strong><address>ANKA TRANSPORT<br>Rheinhessenstraße 102<br>55545 Bad Kreuznach</address><a class="text-link" href="https://www.google.com/maps/search/?api=1&query=Rheinhessenstra%C3%9Fe+102+55545+Bad+Kreuznach" target="_blank" rel="noopener noreferrer">Standort auf der Karte ansehen</a></div><div class="contact-service"><strong>LKW + FAHRER</strong><span>7,5 t · 12 t · 18 t · Sattelzüge</span><small>Fahrzeug und Einsatz nach persönlicher Abstimmung.</small></div></div>{form}</section>{summary}'''

pages = [
 ('index.html', 'ANKA TRANSPORT — LKW mit Fahrer im Festeinsatz', 'ANKA TRANSPORT aus Bad Kreuznach unterstützt Speditionen und Unternehmen mit LKW und Fahrer im Festeinsatz. 7,5 t, 12 t, 18 t und Sattelzüge.', home),
 ('festeinsatz.html', 'Fahrzeuge & Festeinsatz — ANKA TRANSPORT', '7,5-Tonner, 12-Tonner, 18-Tonner und Sattelzüge mit Fahrer. Gemeinsam stimmen wir Fahrzeug, Touren, Einsatzzeiten und Laufzeit ab.', fleet),
 ('unternehmen.html', 'Unternehmen & Kontakt — ANKA TRANSPORT', 'Inhabergeführtes Transportunternehmen aus Bad Kreuznach. ANKA TRANSPORT und Zafer Beyazdogan: Ihr Partner für LKW mit Fahrer im Festeinsatz.', company),
]
for filename, title, description, body in pages:
    head = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><meta name="theme-color" content="#ef7d14"><title>{escape(title)}</title><meta name="description" content="{escape(description, quote=True)}"><meta name="robots" content="noindex,nofollow"><meta property="og:title" content="{escape(title, quote=True)}"><meta property="og:description" content="{escape(description, quote=True)}"><meta property="og:type" content="website"><meta property="og:image" content="https://anka-transport.cra4zzy.chatgpt.site/assets/anka-truck.webp"><link rel="icon" href="assets/favicon.svg" type="image/svg+xml"><link rel="preload" href="assets/barlow-condensed-bold.ttf" as="font" type="font/ttf" crossorigin><link rel="stylesheet" href="assets/fonts-v3.css"><link rel="stylesheet" href="assets/style.css?v=5"><script src="assets/app.js?v=5" defer></script></head>'''
    (D/filename).write_text(head+f'<body id="top" class="{filename.split(".")[0]}-page">'+header(filename)+'<main id="main">'+body+'</main>'+footer()+'</body></html>')
print('Generated three ANKA pages, transport design v4, supplied logo and orange/anthracite palette.')
