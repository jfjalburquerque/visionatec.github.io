#!/usr/bin/env python3
"""Genera las landings por sector/ciudad en /<slug>/index.html.

Uso:  python3 _tools/build_landings.py
Edita PAGES y vuelve a ejecutar. Jekyll ignora las carpetas que empiezan por "_",
así que este script no se publica.
"""
import html
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://visionatec.com"
PHONE = "+34624844363"
WA = "https://wa.me/34624844363?text=Hola%2C%20me%20interesa%20una%20consultor%C3%ADa%20de%20IA"

PAGES = [
    {
        "slug": "consultoria-ia-murcia",
        "nav": "Murcia",
        "title": "Consultoría de inteligencia artificial en Murcia para pymes",
        "description": "Consultoría de IA y automatización de procesos en Murcia. Visitamos tu empresa, detectamos tareas repetitivas y las automatizamos con inteligencia artificial. Primera reunión gratis.",
        "eyebrow": "Consultoría de IA · Murcia",
        "h1": "Consultoría de inteligencia artificial en <em>Murcia</em>",
        "lead": "Somos de Murcia y trabajamos con pymes, autónomos y profesionales de la Región. Nos sentamos contigo, presencialmente o en remoto, estudiamos cómo trabajáis y automatizamos lo que hoy os roba horas.",
        "pains_title": "Lo que solemos automatizar en <em>empresas murcianas</em>",
        "pains": [
            ("Atención al cliente por WhatsApp y email", "Respuestas automáticas a las preguntas de siempre, filtrado de consultas y aviso al equipo solo cuando hace falta una persona."),
            ("Citas, reservas y recordatorios", "Agenda online conectada a tu calendario, confirmaciones y recordatorios automáticos para reducir ausencias."),
            ("Presupuestos y documentos", "Generación de presupuestos, contratos e informes a partir de plantillas y de los datos que ya tienes."),
            ("Datos que se copian a mano", "Conectamos tus herramientas (email, hojas de cálculo, ERP, CRM) para que la información viaje sola."),
            ("Facturas y gastos", "Lectura automática de facturas y tickets, clasificación y envío a tu gestoría."),
            ("Formación del equipo en IA", "Talleres prácticos para que tu equipo use ChatGPT, Claude y otras herramientas con criterio y de forma segura."),
        ],
        "faq": [
            ("¿Os desplazáis a mi empresa en Murcia?", "Sí. En Murcia capital y alrededores hacemos la primera reunión y el diagnóstico de forma presencial si lo prefieres. También trabajamos en remoto con toda España."),
            ("¿Cuánto cuesta una consultoría de IA?", "Depende del alcance. La primera reunión es gratuita y, tras el diagnóstico, te damos una propuesta cerrada con precio, plazos y el ahorro de tiempo esperado, sin sorpresas."),
            ("Soy autónomo o una empresa pequeña, ¿me compensa?", "Muchas veces es donde más se nota: una sola persona que recupera 4 o 5 horas a la semana gana casi un día de trabajo. Te diremos con honestidad si merece la pena."),
            ("¿Hay ayudas o subvenciones para implantar IA?", "Ahora mismo no hay ninguna convocatoria estatal abierta (Kit Digital y Kit Consulting están cerrados). Si se abre una nueva, te avisamos y te ayudamos a aprovecharla."),
        ],
    },
    {
        "slug": "ia-para-clinicas",
        "nav": "Clínicas",
        "title": "IA y automatización para clínicas y consultas en Murcia",
        "description": "Automatiza citas, recordatorios, WhatsApp y tareas administrativas de tu clínica de psicología, fisioterapia, dental o estética con inteligencia artificial. Murcia y toda España.",
        "eyebrow": "IA para clínicas y consultas",
        "h1": "Menos administración, <em>más tiempo para tus pacientes</em>",
        "lead": "Para clínicas de psicología, fisioterapia, dentales, nutrición o estética. Automatizamos la agenda, los recordatorios y las consultas repetitivas para que el equipo se dedique a atender.",
        "pains_title": "Tareas que <em>dejan de hacerse a mano</em>",
        "pains": [
            ("Agenda y reservas online", "Tus pacientes reservan, cambian o cancelan su cita solos, conectado a tu calendario."),
            ("Recordatorios automáticos", "Avisos por WhatsApp, SMS o email antes de cada cita para reducir las ausencias."),
            ("WhatsApp que responde solo", "Precios, horarios, ubicación, primera visita: las preguntas de siempre se contestan al momento, a cualquier hora."),
            ("Formularios de primera visita", "El paciente rellena sus datos antes de llegar y la información entra directamente en su ficha."),
            ("Resúmenes y notas", "Ayuda de IA para redactar informes y notas de sesión, siempre revisados por el profesional."),
            ("Seguimiento y reseñas", "Mensajes de seguimiento tras la sesión y petición de reseñas en Google a pacientes satisfechos."),
        ],
        "case": ("Cano Psicología", "Creamos su página web y automatizamos la gestión de su agenda, liberando tiempo administrativo para dedicarlo a los pacientes."),
        "faq": [
            ("¿Qué pasa con los datos de salud de mis pacientes?", "Son datos especialmente protegidos por el RGPD. Diseñamos cada solución para que esos datos se traten solo donde deben, con proveedores que cumplen la normativa, y nunca se usan para entrenar modelos de IA."),
            ("¿Tengo que cambiar mi software de gestión?", "Normalmente no. Nos integramos con tu calendario y tus herramientas actuales siempre que sea posible."),
            ("¿El paciente notará que habla con una IA?", "Lo indicamos siempre de forma transparente, y cualquier consulta delicada pasa directamente a una persona de tu equipo."),
        ],
    },
    {
        "slug": "ia-para-academias",
        "nav": "Academias",
        "title": "IA para academias y centros de formación en Murcia",
        "description": "Inteligencia artificial para academias, autoescuelas y centros de formación: matrículas, atención a alumnos, creación de tests y material, seguimiento. Murcia y toda España.",
        "eyebrow": "IA para academias y formación",
        "h1": "Tu academia, con un asistente que <em>no se cansa</em>",
        "lead": "Para academias de oposiciones, idiomas, refuerzo escolar, autoescuelas y centros de formación. Automatizamos la parte administrativa y usamos la IA para crear material y acompañar mejor a cada alumno.",
        "pains_title": "Dónde la IA <em>ayuda a una academia</em>",
        "pains": [
            ("Información y matrículas", "Respuesta inmediata a interesados por WhatsApp o web: horarios, precios, plazas, y matrícula online."),
            ("Generación de tests y ejercicios", "Creación de preguntas tipo test, resúmenes y esquemas a partir de tu temario, revisados por tus profesores."),
            ("Seguimiento de alumnos", "Avisos de faltas, progreso y recordatorios de pago automáticos a alumnos o familias."),
            ("Corrección asistida", "Apoyo de IA para corregir ejercicios abiertos y dar feedback personalizado más rápido."),
            ("Gestión de grupos y horarios", "Altas, bajas, listas y cambios de grupo sincronizados sin hojas de cálculo duplicadas."),
            ("Captación", "Campañas y seguimiento de interesados que piden información y no llegan a matricularse."),
        ],
        "case": ("Testealo", "App de preparación de oposiciones con inteligencia artificial integrada, desarrollada por nuestro equipo, que personaliza el estudio de cada opositor."),
        "faq": [
            ("¿La IA puede crear tests de mi temario?", "Sí. Partimos de tu propio temario para generar preguntas y material, y tus profesores los revisan antes de usarlos."),
            ("¿Sirve para una academia pequeña?", "Sí. Empezamos por lo que más tiempo os quita, normalmente la atención a interesados y la parte administrativa."),
            ("¿Necesito una app propia?", "No necesariamente. Muchas mejoras funcionan con las herramientas que ya usáis; si tiene sentido una app, sabemos hacerla."),
        ],
    },
    {
        "slug": "ia-para-asesorias",
        "nav": "Asesorías",
        "title": "IA para asesorías, gestorías y despachos en Murcia",
        "description": "Automatiza la recogida de documentación, la lectura de facturas, las consultas repetitivas y la redacción de documentos en tu asesoría, gestoría o despacho con IA. Murcia y toda España.",
        "eyebrow": "IA para asesorías y despachos",
        "h1": "Menos papeleo para tu despacho, <em>más asesoramiento</em>",
        "lead": "Para asesorías fiscales y laborales, gestorías y despachos de abogados. La IA se encarga de clasificar, extraer y redactar; tu equipo revisa y asesora.",
        "pains_title": "Lo que <em>se automatiza</em> en un despacho",
        "pains": [
            ("Recogida de documentación", "Los clientes suben facturas y documentos en un único sitio y reciben recordatorios automáticos de lo que falta."),
            ("Lectura de facturas y tickets", "Extracción automática de datos para la contabilidad, con revisión humana de los casos dudosos."),
            ("Consultas repetitivas", "Un asistente responde a las preguntas frecuentes de tus clientes (plazos, modelos, documentación) y deriva el resto."),
            ("Borradores de documentos", "Primeros borradores de escritos, contratos o informes a partir de tus propias plantillas."),
            ("Búsqueda en tu archivo", "Encuentra al momento cualquier dato dentro de tus documentos internos con un buscador inteligente privado."),
            ("Calendario fiscal", "Avisos automáticos a cada cliente según sus obligaciones y vencimientos."),
        ],
        "faq": [
            ("¿Es seguro usar IA con documentación de clientes?", "Sí, si se hace bien. Usamos proveedores con garantías RGPD, configurados para no entrenar con tus datos, y definimos contigo qué información se procesa y dónde."),
            ("¿Funciona con mi programa de contabilidad?", "En la mayoría de casos podemos exportar o integrar los datos con tu software actual. Lo revisamos en el diagnóstico."),
            ("¿La IA sustituye la revisión del profesional?", "No. La IA prepara y propone; el profesional revisa y decide."),
        ],
    },
    {
        "slug": "ia-para-inmobiliarias",
        "nav": "Inmobiliarias",
        "title": "IA para inmobiliarias en Murcia: leads, anuncios y visitas",
        "description": "Inteligencia artificial para inmobiliarias: respuesta inmediata a leads, redacción de anuncios, agenda de visitas y seguimiento de clientes. Murcia y toda España.",
        "eyebrow": "IA para inmobiliarias",
        "h1": "Responde a cada interesado <em>en minutos, no en horas</em>",
        "lead": "Para agencias inmobiliarias y gestores de alquiler. Automatizamos la atención a leads de los portales, la agenda de visitas y la redacción de anuncios para que tus agentes se centren en cerrar operaciones.",
        "pains_title": "Lo que tu agencia <em>puede automatizar</em>",
        "pains": [
            ("Respuesta inmediata a leads", "Cada contacto de Idealista, Fotocasa o la web recibe respuesta al momento y se cualifica antes de llegar al agente."),
            ("Agenda de visitas", "El interesado elige hueco disponible y recibe confirmación y recordatorio automáticos."),
            ("Anuncios en minutos", "Descripciones atractivas y traducidas a varios idiomas a partir de los datos y fotos del inmueble."),
            ("Seguimiento de clientes", "Recordatorios y mensajes automáticos para que ningún comprador o propietario se quede sin respuesta."),
            ("Cruce de demanda y oferta", "Aviso automático a los clientes cuando entra un inmueble que encaja con lo que buscan."),
            ("Documentación de operaciones", "Recogida y control de documentos de compradores, vendedores e inquilinos."),
        ],
        "faq": [
            ("¿Se conecta con los portales inmobiliarios?", "Sí, podemos recoger los leads que llegan por email o integración de los portales y centralizarlos en un único sitio."),
            ("¿Y si ya uso un CRM inmobiliario?", "Lo aprovechamos. La idea es conectar y automatizar lo que ya tienes, no cambiarlo."),
            ("¿Puede atender en inglés a compradores extranjeros?", "Sí. Las respuestas y anuncios pueden generarse en varios idiomas, algo muy útil en la costa de Murcia."),
        ],
    },
]


def esc(t):
    return html.escape(t, quote=True)


def strip_tags(t):
    import re
    return re.sub(r"<[^>]+>", "", t)


def nav_links(current):
    return "\n".join(
        f'        <a href="/{p["slug"]}/"{" aria-current=\"page\"" if p["slug"] == current else ""}>{p["nav"]}</a>'
        for p in PAGES
    )


def render(p):
    url = f'{SITE}/{p["slug"]}/'
    pains = "\n".join(
        f'''      <div class="card reveal">
        <span class="num">{i:02d}</span>
        <h3>{esc(t)}</h3>
        <p>{esc(d)}</p>
      </div>''' for i, (t, d) in enumerate(p["pains"], 1))
    faqs = "\n".join(
        f'      <details class="faq reveal"><summary>{esc(q)}</summary><div class="faq-a">{esc(a)}</div></details>'
        for q, a in p["faq"])
    case = ""
    if p.get("case"):
        n, d = p["case"]
        case = f'''
<section class="sec clients">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="tag">Caso real</span>
      <h2>Ya lo hemos <em>hecho antes</em></h2>
    </div>
    <div class="grid-cli">
      <div class="cli reveal">
        <div class="cli-name"><span class="dotmark"></span>{esc(n)}</div>
        <p>{esc(d)}</p>
      </div>
    </div>
  </div>
</section>
'''
    ld = [
        {
            "@context": "https://schema.org",
            "@type": "Service",
            "name": strip_tags(p["h1"]),
            "serviceType": p["eyebrow"],
            "url": url,
            "description": p["description"],
            "areaServed": [{"@type": "City", "name": "Murcia"}, {"@type": "Country", "name": "España"}],
            "provider": {"@type": "ProfessionalService", "name": "Visionatec", "url": SITE + "/", "telephone": PHONE},
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in p["faq"]],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "Inicio", "item": SITE + "/"},
                {"@type": "ListItem", "position": 2, "name": p["nav"], "item": url},
            ],
        },
    ]
    return f'''<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<!-- Generado por _tools/build_landings.py: no editar a mano -->
<title>{esc(p["title"])} · Visionatec</title>
<meta name="description" content="{esc(p["description"])}">
<link rel="canonical" href="{url}">
<meta name="theme-color" content="#08121e">
<meta property="og:type" content="website">
<meta property="og:locale" content="es_ES">
<meta property="og:site_name" content="Visionatec">
<meta property="og:url" content="{url}">
<meta property="og:title" content="{esc(p["title"])}">
<meta property="og:description" content="{esc(p["description"])}">
<meta property="og:image" content="{SITE}/og.png">
<meta name="twitter:card" content="summary_large_image">
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
        <a href="/#proceso">Cómo trabajamos</a>
        <a href="/#sectores">Sectores</a>
        <a href="/blog/">Blog</a>
        <a href="#faq">FAQ</a>
      </div>
      <div class="nav-cta">
        <a class="btn" href="#contacto">Agendar reunión</a>
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
  <a href="#faq">FAQ</a>
  <a class="btn" href="#contacto">Agendar reunión gratis</a>
</div>

<section class="hero hero-sm">
  <div class="wrap">
    <div class="hero-inner">
      <span class="eyebrow reveal"><span class="pulse"></span>{esc(p["eyebrow"])}</span>
      <h1 class="reveal">{p["h1"]}</h1>
      <p class="lead reveal">{esc(p["lead"])}</p>
      <div class="hero-actions reveal">
        <a class="btn" href="#contacto">Pedir diagnóstico gratis →</a>
        <a class="btn btn-ghost" href="{WA}" target="_blank" rel="noopener">Escribir por WhatsApp</a>
      </div>
    </div>
  </div>
</section>

<section class="sec">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="tag">Qué automatizamos</span>
      <h2>{p["pains_title"]}</h2>
      <p>Cada empresa es distinta: en el diagnóstico gratuito vemos cuáles de estas tareas te compensan y en qué orden.</p>
    </div>
    <div class="grid-serv">
{pains}
    </div>
  </div>
</section>

<section class="sec proc">
  <div class="wrap">
    <div class="sec-head reveal">
      <span class="tag">Cómo trabajamos</span>
      <h2>Tres pasos, <em>sin compromiso</em></h2>
    </div>
    <div class="grid-serv">
      <div class="card reveal"><span class="num">i</span><h3>Reunión gratuita</h3><p>30 minutos, en persona en Murcia o por videollamada. Nos cuentas cómo trabajáis y qué os quita tiempo.</p></div>
      <div class="card reveal"><span class="num">ii</span><h3>Propuesta cerrada</h3><p>Te decimos qué automatizaríamos, con qué herramientas, cuánto tiempo esperamos ahorrar y cuánto cuesta.</p></div>
      <div class="card reveal"><span class="num">iii</span><h3>Implantación y formación</h3><p>Lo ponemos en marcha con tus herramientas, formamos a tu equipo y seguimos a tu lado.</p></div>
    </div>
  </div>
</section>
{case}
<section class="sec" id="faq">
  <div class="wrap">
    <div class="sec-head reveal" style="margin:0 auto 60px;text-align:center">
      <span class="tag" style="justify-content:center">Preguntas frecuentes</span>
      <h2>Lo que sueles <em>preguntarnos</em></h2>
    </div>
    <div class="faq-wrap">
{faqs}
    </div>
  </div>
</section>

<section class="sec cta" id="contacto">
  <div class="wrap">
    <div class="cta-card reveal">
      <div class="glow"></div>
      <div class="cta-grid">
        <div>
          <h2>Cuéntanos qué te <em>roba tiempo</em></h2>
          <p class="lead">Primera reunión gratis y sin compromiso. Te decimos con franqueza si la IA puede ayudarte y por dónde empezar.</p>
          <ul class="contact-list">
            <li><a href="mailto:info@visionatec.com">info@visionatec.com</a></li>
            <li><a href="tel:{PHONE}">624 844 363</a> · <a href="{WA}" target="_blank" rel="noopener">WhatsApp</a></li>
            <li>Murcia · presencial en la Región y en remoto en toda España</li>
          </ul>
        </div>
        <div>
          <form id="form" action="https://formspree.io/f/xzdwloop" method="POST" novalidate>
            <div class="field"><label for="n">Nombre y empresa</label><input id="n" name="nombre" type="text" required></div>
            <div class="field"><label for="e">Email</label><input id="e" name="email" type="email" placeholder="tu@empresa.com" required></div>
            <div class="field"><label for="t">Teléfono <small>(opcional)</small></label><input id="t" name="telefono" type="tel" autocomplete="tel"></div>
            <div class="field"><label for="m">¿Qué proceso te gustaría mejorar?</label><textarea id="m" name="mensaje" rows="3"></textarea></div>
            <input type="hidden" name="_subject" value="Nueva solicitud · {esc(p["nav"])} · Visionatec">
            <input type="hidden" name="origen" value="/{p["slug"]}/">
            <input type="text" name="_gotcha" style="display:none !important" tabindex="-1" autocomplete="off">
            <label class="consent"><input type="checkbox" name="acepta_privacidad" value="si" required><span>He leído y acepto la <a href="/privacidad.html" target="_blank">política de privacidad</a>. Usaremos tus datos solo para responder a tu solicitud.</span></label>
            <button class="btn" type="submit">Solicitar diagnóstico gratis →</button>
            <div class="form-ok" id="ok">¡Gracias! Hemos recibido tu mensaje. Te escribiremos muy pronto.</div>
            <div class="form-err" id="err">Ups, algo ha fallado. Escríbenos directamente a info@visionatec.com</div>
          </form>
        </div>
      </div>
    </div>
  </div>
</section>

<footer>
  <div class="wrap">
    <div class="foot">
      <img src="/logo.png" alt="Visionatec">
      <div class="foot-links">
        <a href="/blog/">Blog</a>
{nav_links(p["slug"])}
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


def main():
    for p in PAGES:
        out = ROOT / p["slug"] / "index.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(render(p), encoding="utf-8")
        print("ok", out.relative_to(ROOT))


if __name__ == "__main__":
    main()
