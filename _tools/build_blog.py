#!/usr/bin/env python3
"""Genera el blog (/blog/), el feed RSS y el sitemap.xml completo.

Uso:  python3 _tools/build_blog.py
Para publicar un artículo nuevo, crea _tools/blog/<slug>.html con la cabecera
(title, description, date, tag, related) seguida de '---' y el cuerpo en HTML,
y vuelve a ejecutar el script.
"""
import json
from datetime import date
from email.utils import format_datetime
from datetime import datetime, timezone
from pathlib import Path

from build_landings import PAGES, PHONE, SITE, WA, esc

ROOT = Path(__file__).resolve().parent.parent
POSTS_DIR = Path(__file__).resolve().parent / "blog"
MONTHS = ["enero", "febrero", "marzo", "abril", "mayo", "junio", "julio",
          "agosto", "septiembre", "octubre", "noviembre", "diciembre"]


def load_posts():
    posts = []
    for f in sorted(POSTS_DIR.glob("*.html")):
        head, body = f.read_text(encoding="utf-8").split("\n---\n", 1)
        meta = dict(line.split(": ", 1) for line in head.strip().splitlines())
        meta["slug"] = f.stem
        meta["body"] = body.strip()
        meta["d"] = date.fromisoformat(meta["date"])
        posts.append(meta)
    return sorted(posts, key=lambda p: (p["d"], p["title"]), reverse=True)


def human(d):
    return f"{d.day} de {MONTHS[d.month - 1]} de {d.year}"


def shell(title, description, url, body, ld, og_type="website"):
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Generado por _tools/build_blog.py: no editar a mano -->
<title>{esc(title)}</title>
<meta name="description" content="{esc(description)}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#08121e">
<meta property="og:type" content="{og_type}">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Visionatec">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(description)}">
<meta property="og:image" content="{SITE}/og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="alternate" type="application/rss+xml" title="Blog de Visionatec" href="{SITE}/blog/feed.xml">
<script type="application/ld+json">
{json.dumps(ld, ensure_ascii=False, indent=1)}
</script>
<link rel="shortcut icon" type="image/x-icon" href="/favicon.ico">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,300..700;1,9..144,400..600&family=Hanken+Grotesk:wght@300;400;500;600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/assets/site.css">
</head>
<body>

<header id="hdr">
  <div class="wrap">
    <nav>
      <a class="brand" href="/"><img src="/logo.png" alt="Visionatec"></a>
      <div class="nav-links">
        <a href="/#servicios">Servicios</a>
        <a href="/#sectores">Sectores</a>
        <a href="/blog/">Blog</a>
        <a href="/#faq">FAQ</a>
      </div>
      <div class="nav-cta">
        <a class="btn" href="/#contacto">Agendar reunión</a>
        <button class="burger" id="burger" aria-label="Abrir menú" aria-expanded="false" aria-controls="mnav">≡</button>
      </div>
    </nav>
  </div>
</header>
<div class="mnav" id="mnav">
  <a href="/">Inicio</a>
  <a href="/#servicios">Servicios</a>
  <a href="/#sectores">Sectores</a>
  <a href="/blog/">Blog</a>
  <a class="btn" href="/#contacto">Agendar reunión gratis</a>
</div>

{body}

<footer>
  <div class="wrap">
    <div class="foot">
      <img src="/logo.png" alt="Visionatec">
      <div class="foot-links">
        <a href="/">Inicio</a>
        <a href="/blog/">Blog</a>
{chr(10).join(f'        <a href="/{p["slug"]}/">{p["nav"]}</a>' for p in PAGES)}
      </div>
    </div>
    <p class="copy">© <span id="yr"></span> Visionatec · Consultoría de inteligencia artificial en Murcia.</p>
    <div class="legal"><a href="/aviso-legal.html">Aviso legal</a><a href="/privacidad.html">Política de privacidad</a></div>
  </div>
</footer>
<a class="wa" href="{WA}" target="_blank" rel="noopener" aria-label="Escríbenos por WhatsApp"><svg viewBox="0 0 24 24" aria-hidden="true"><use href="/assets/whatsapp.svg#i"/></svg></a>
<script src="/assets/site.js" defer></script>
</body>
</html>
'''


ORG = {"@type": "Organization", "name": "Visionatec", "url": SITE + "/", "logo": SITE + "/logo.png"}


def cta():
    return f'''<div class="post-cta">
      <h2>¿Lo vemos para tu empresa?</h2>
      <p>Primera reunión gratis y sin compromiso, en Murcia o por videollamada. Te decimos con franqueza si la IA te compensa y por dónde empezar.</p>
      <div class="hero-actions">
        <a class="btn" href="/#contacto">Pedir diagnóstico gratis →</a>
        <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
    </div>'''


def render_post(p, others):
    url = f'{SITE}/blog/{p["slug"]}/'
    related = next((l for l in PAGES if f'/{l["slug"]}/' == p.get("related")), None)
    rel_html = ""
    if related:
        rel_html = f'<p class="post-related">Te puede interesar: <a href="/{related["slug"]}/">{esc(related["title"])}</a></p>'
    more = "\n".join(
        f'        <a class="card" href="/blog/{o["slug"]}/"><span class="post-tag">{esc(o["tag"])}</span><h3>{esc(o["title"])}</h3></a>'
        for o in others[:3])
    body = f'''<main class="post">
  <div class="wrap">
    <div class="crumbs"><a href="/">Inicio</a> / <a href="/blog/">Blog</a></div>
    <article>
      <div class="post-head">
        <span class="post-tag">{esc(p["tag"])}</span>
        <h1>{esc(p["title"])}</h1>
        <p class="post-meta"><time datetime="{p["date"]}">{human(p["d"])}</time> · Equipo Visionatec</p>
      </div>
      <div class="post-body">
{p["body"]}
      </div>
      {rel_html}
    </article>
    {cta()}
    <section class="post-more">
      <h2>Más artículos</h2>
      <div class="grid-serv">
{more}
      </div>
    </section>
  </div>
</main>'''
    ld = [
        {
            "@context": "https://schema.org", "@type": "BlogPosting",
            "headline": p["title"], "description": p["description"],
            "datePublished": p["date"], "dateModified": p["date"],
            "mainEntityOfPage": url, "url": url, "image": SITE + "/og.png",
            "inLanguage": "es-ES", "author": ORG, "publisher": ORG,
        },
        {
            "@context": "https://schema.org", "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": "Blog", "item": SITE + "/blog/"},
                {"@type": "ListItem", "position": 3, "name": p["title"], "item": url},
            ],
        },
    ]
    return shell(f'{p["title"]} · Visionatec', p["description"], url, body, ld, "article")


def render_index(posts):
    url = SITE + "/blog/"
    cards = "\n".join(
        f'''      <a class="card post-card" href="/blog/{p["slug"]}/">
        <span class="post-tag">{esc(p["tag"])}</span>
        <h3>{esc(p["title"])}</h3>
        <p>{esc(p["description"])}</p>
        <span class="post-meta">{human(p["d"])}</span>
      </a>''' for p in posts)
    body = f'''<section class="hero hero-sm">
  <div class="wrap">
    <div class="hero-inner">
      <span class="eyebrow"><span class="pulse"></span>Blog</span>
      <h1>IA práctica para <em>pymes y autónomos</em></h1>
      <p class="lead">Guías sin jerga sobre automatización, inteligencia artificial y cómo ahorrar horas en el día a día de tu empresa.</p>
    </div>
  </div>
</section>
<section class="sec" style="padding-top:0">
  <div class="wrap">
    <div class="grid-serv">
{cards}
    </div>
  </div>
</section>'''
    ld = {
        "@context": "https://schema.org", "@type": "Blog", "name": "Blog de Visionatec",
        "url": url, "inLanguage": "es-ES", "publisher": ORG,
        "blogPost": [{"@type": "BlogPosting", "headline": p["title"], "url": f'{SITE}/blog/{p["slug"]}/', "datePublished": p["date"]} for p in posts],
    }
    return shell("Blog de inteligencia artificial para pymes · Visionatec",
                 "Guías prácticas sobre inteligencia artificial y automatización para pymes y autónomos: WhatsApp, citas, facturas, ayudas, RGPD y costes.",
                 url, body, ld)


def render_feed(posts):
    now = format_datetime(datetime.now(timezone.utc))
    items = "\n".join(f'''  <item>
    <title>{esc(p["title"])}</title>
    <link>{SITE}/blog/{p["slug"]}/</link>
    <guid>{SITE}/blog/{p["slug"]}/</guid>
    <pubDate>{format_datetime(datetime(p["d"].year, p["d"].month, p["d"].day, 9, tzinfo=timezone.utc))}</pubDate>
    <description>{esc(p["description"])}</description>
  </item>''' for p in posts)
    return f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
<channel>
  <title>Blog de Visionatec</title>
  <link>{SITE}/blog/</link>
  <atom:link href="{SITE}/blog/feed.xml" rel="self" type="application/rss+xml"/>
  <description>Inteligencia artificial práctica para pymes y autónomos.</description>
  <language>es-es</language>
  <lastBuildDate>{now}</lastBuildDate>
{items}
</channel>
</rss>
'''


def render_sitemap(posts):
    today = date.today().isoformat()
    urls = [("/", today, "1.0")]
    urls += [(f'/{p["slug"]}/', today, "0.8") for p in PAGES]
    urls += [("/blog/", posts[0]["date"] if posts else today, "0.8")]
    urls += [(f'/blog/{p["slug"]}/', p["date"], "0.7") for p in posts]
    urls += [("/aviso-legal.html", today, "0.2"), ("/privacidad.html", today, "0.2")]
    rows = "\n".join(f"  <url><loc>{SITE}{u}</loc><lastmod>{m}</lastmod><priority>{pr}</priority></url>" for u, m, pr in urls)
    return f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n'


def main():
    posts = load_posts()
    for p in posts:
        out = ROOT / "blog" / p["slug"] / "index.html"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(render_post(p, [o for o in posts if o is not p]), encoding="utf-8")
        print("ok", out.relative_to(ROOT))
    (ROOT / "blog" / "index.html").write_text(render_index(posts), encoding="utf-8")
    (ROOT / "blog" / "feed.xml").write_text(render_feed(posts), encoding="utf-8")
    (ROOT / "sitemap.xml").write_text(render_sitemap(posts), encoding="utf-8")
    home = ROOT / "index.html"
    h = home.read_text(encoding="utf-8")
    start, end = "<!-- BLOG:START -->\n", "<!-- BLOG:END -->"
    cards = "".join(
        f'      <a class="card reveal" href="/blog/{p["slug"]}/"><span class="post-tag">{esc(p["tag"])}</span><h3>{esc(p["title"])}</h3></a>\n'
        for p in posts[:3])
    h = h[:h.index(start) + len(start)] + cards + h[h.index(end):]
    home.write_text(h, encoding="utf-8")
    print("ok blog/index.html, blog/feed.xml, sitemap.xml")


if __name__ == "__main__":
    main()
