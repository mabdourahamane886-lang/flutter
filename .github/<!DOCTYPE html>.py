<!DOCTYPE html>
<html lang="fr">
  <head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Bickri Agency | Création Digitale</title>
    <meta
      name="description"
      content="Bickri Agency accompagne les marques dans leur création digitale, branding, sites web, marketing et contenus visuels."
    />
    <style>
      :root {
        --bg: #07111f;
        --bg-soft: #0d1d2f;
        --panel: rgba(17, 30, 44, 0.8);
        --card: #101e2d;
        --muted: #9cb0c8;
        --text: #edf5ff;
        --primary: #7c5cff;
        --secondary: #00d4ff;
        --accent: #ffb703;
        --success: #7ef0b0;
        --border: rgba(255, 255, 255, 0.08);
        --shadow: 0 30px 60px rgba(5, 10, 18, 0.4);
      }

      * { box-sizing: border-box; }

      html {
        scroll-behavior: smooth;
      }

      body {
        margin: 0;
        font-family: Inter, "Segoe UI", sans-serif;
        background:
          radial-gradient(circle at top left, rgba(124, 92, 255, 0.25), transparent 20%),
          radial-gradient(circle at right, rgba(0, 212, 255, 0.18), transparent 25%),
          var(--bg);
        color: var(--text);
      }

      a {
        color: inherit;
        text-decoration: none;
      }

      img {
        max-width: 100%;
        display: block;
      }

      .container {
        width: min(1180px, calc(100% - 32px));
        margin: 0 auto;
      }

      .topbar {
        position: sticky;
        top: 0;
        z-index: 20;
        backdrop-filter: blur(18px);
        background: rgba(7, 17, 31, 0.72);
        border-bottom: 1px solid var(--border);
      }

      .nav {
        display: flex;
        align-items: center;
        justify-content: space-between;
        min-height: 80px;
      }

      .brand {
        display: flex;
        align-items: center;
        gap: 12px;
        font-weight: 800;
        letter-spacing: 0.06em;
        text-transform: uppercase;
      }

      .brand-mark {
        width: 36px;
        height: 36px;
        border-radius: 12px;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        display: grid;
        place-items: center;
        font-size: 1rem;
        box-shadow: var(--shadow);
      }

      .nav-links {
        display: flex;
        align-items: center;
        gap: 28px;
        color: var(--muted);
      }

      .nav-links a:hover {
        color: var(--text);
      }

      .nav-actions {
        display: flex;
        align-items: center;
        gap: 14px;
      }

      .button {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 14px 22px;
        border-radius: 999px;
        border: 1px solid transparent;
        font-weight: 700;
        transition: 0.25s ease;
        cursor: pointer;
      }

      .button.primary {
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        color: white;
        box-shadow: 0 20px 40px rgba(124, 92, 255, 0.35);
      }

      .button.primary:hover {
        transform: translateY(-2px);
      }

      .button.secondary {
        border-color: var(--border);
        background: rgba(255, 255, 255, 0.02);
        color: var(--text);
      }

      .hero {
        padding: 90px 0 70px;
      }

      .hero-grid {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        align-items: center;
        gap: 44px;
      }

      .eyebrow {
        display: inline-flex;
        align-items: center;
        gap: 10px;
        padding: 8px 14px;
        border: 1px solid rgba(124, 92, 255, 0.32);
        border-radius: 999px;
        background: rgba(124, 92, 255, 0.08);
        color: #d9d2ff;
        font-size: 0.76rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
      }

      .eyebrow::before {
        content: "";
        width: 8px;
        height: 8px;
        border-radius: 50%;
        background: var(--success);
        box-shadow: 0 0 18px rgba(126, 240, 176, 0.8);
      }

      h1 {
        margin: 22px 0 18px;
        font-size: clamp(2.7rem, 5vw, 5rem);
        line-height: 1.02;
        letter-spacing: -0.05em;
      }

      .lead {
        font-size: 1.08rem;
        line-height: 1.8;
        color: var(--muted);
        max-width: 620px;
      }

      .hero-actions {
        display: flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 16px;
        margin-top: 26px;
      }

      .stats {
        display: grid;
        grid-template-columns: repeat(3, minmax(120px, 1fr));
        gap: 18px;
        margin-top: 34px;
      }

      .stat {
        padding: 18px 14px;
        border: 1px solid var(--border);
        border-radius: 18px;
        background: rgba(255, 255, 255, 0.02);
      }

      .stat strong {
        display: block;
        font-size: 1.6rem;
        margin-bottom: 6px;
      }

      .stat span {
        color: var(--muted);
        font-size: 0.9rem;
      }

      .hero-visual {
        position: relative;
        padding: 24px;
      }

      .visual-card {
        position: relative;
        border: 1px solid var(--border);
        border-radius: 28px;
        background: linear-gradient(180deg, rgba(16, 30, 45, 0.9), rgba(13, 29, 47, 0.9));
        box-shadow: var(--shadow);
        overflow: hidden;
      }

      .mini-window {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 18px 18px 0;
      }

      .window-dots {
        display: flex;
        gap: 8px;
      }

      .window-dots span {
        width: 10px;
        height: 10px;
        border-radius: 50%;
        display: inline-block;
      }

      .window-dots span:nth-child(1) { background: #ff5f57; }
      .window-dots span:nth-child(2) { background: #ffbd2e; }
      .window-dots span:nth-child(3) { background: #28c840; }

      .dashboard {
        padding: 20px 18px 18px;
      }

      .dashboard-top {
        display: grid;
        grid-template-columns: 1.2fr 0.8fr;
        gap: 18px;
      }

      .panel {
        background: rgba(255, 255, 255, 0.02);
        border: 1px solid var(--border);
        border-radius: 20px;
        padding: 18px;
      }

      .chart-bars {
        display: flex;
        align-items: end;
        gap: 10px;
        height: 130px;
        margin-top: 22px;
      }

      .chart-bars span {
        flex: 1;
        border-radius: 10px 10px 0 0;
        background: linear-gradient(180deg, var(--secondary), var(--primary));
        box-shadow: 0 8px 28px rgba(0, 212, 255, 0.2);
      }

      .chart-bars span:nth-child(1) { height: 40%; }
      .chart-bars span:nth-child(2) { height: 60%; }
      .chart-bars span:nth-child(3) { height: 55%; }
      .chart-bars span:nth-child(4) { height: 80%; }
      .chart-bars span:nth-child(5) { height: 100%; }
      .chart-bars span:nth-child(6) { height: 70%; }

      .ring {
        display: grid;
        place-items: center;
        width: 110px;
        height: 110px;
        border-radius: 50%;
        background: conic-gradient(var(--primary) 0 70%, rgba(255,255,255,0.08) 70% 100%);
        margin: 18px auto 0;
      }

      .ring-inner {
        width: 74px;
        height: 74px;
        border-radius: 50%;
        display: grid;
        place-items: center;
        background: var(--bg-soft);
        font-weight: 800;
        color: var(--text);
      }

      .floating-card {
        position: absolute;
        right: -12px;
        bottom: 30px;
        background: rgba(11, 25, 39, 0.92);
        border: 1px solid var(--border);
        border-radius: 18px;
        padding: 16px 18px;
        box-shadow: var(--shadow);
      }

      .floating-card strong {
        display: block;
        font-size: 1.5rem;
        margin-top: 10px;
      }

      section {
        padding: 34px 0;
      }

      .section-header {
        display: flex;
        align-items: end;
        justify-content: space-between;
        gap: 18px;
        margin-bottom: 32px;
      }

      .section-header h2 {
        margin: 0;
        font-size: clamp(2rem, 3vw, 3rem);
        letter-spacing: -0.045em;
      }

      .section-header p {
        color: var(--muted);
        margin: 0;
        max-width: 540px;
        line-height: 1.7;
      }

      .services {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 22px;
      }

      .service-card {
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 28px 22px;
      }

      .icon-box {
        width: 52px;
        height: 52px;
        border-radius: 16px;
        display: grid;
        place-items: center;
        font-size: 1.5rem;
        background: linear-gradient(135deg, rgba(124,92,255,0.24), rgba(0,212,255,0.18));
        margin-bottom: 18px;
      }

      .service-card h3 {
        margin: 0 0 12px;
        font-size: 1.35rem;
      }

      .service-card p {
        margin: 0;
        color: var(--muted);
        line-height: 1.8;
      }

      .showcase {
        display: grid;
        grid-template-columns: 1.15fr 0.85fr;
        gap: 24px;
        align-items: stretch;
      }

      .showcase-large,
      .showcase-small {
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--border);
        border-radius: 24px;
        overflow: hidden;
      }

      .showcase-large {
        padding: 28px;
      }

      .project-visual {
        margin-top: 18px;
        border-radius: 18px;
        overflow: hidden;
        background: linear-gradient(180deg, rgba(124,92,255,0.18), rgba(0,212,255,0.08));
        min-height: 280px;
        position: relative;
      }

      .project-visual::before {
        content: "";
        position: absolute;
        inset: 24px;
        border-radius: 18px;
        background: linear-gradient(135deg, rgba(124,92,255,0.18), rgba(0,212,255,0.08));
        border: 1px solid var(--border);
      }

      .project-visual::after {
        content: "";
        position: absolute;
        left: 56px;
        right: 56px;
        bottom: 34px;
        height: 120px;
        border-radius: 22px 22px 0 0;
        background: linear-gradient(180deg, rgba(124,92,255,0.75), rgba(0,212,255,0.82));
        box-shadow: 0 30px 60px rgba(124,92,255,0.28);
      }

      .showcase-small {
        padding: 24px;
      }

      .mini-list {
        display: grid;
        gap: 16px;
        margin-top: 20px;
      }

      .mini-item {
        display: flex;
        justify-content: space-between;
        gap: 12px;
        padding: 14px 0;
        border-bottom: 1px solid var(--border);
        color: var(--muted);
      }

      .mini-item strong {
        color: var(--text);
      }

      .process {
        display: grid;
        grid-template-columns: repeat(4, minmax(0, 1fr));
        gap: 22px;
      }

      .step {
        position: relative;
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 26px 18px 20px;
      }

      .step-number {
        width: 42px;
        height: 42px;
        border-radius: 12px;
        display: grid;
        place-items: center;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        font-weight: 800;
        margin-bottom: 18px;
      }

      .step h3 {
        margin: 0 0 8px;
        font-size: 1.2rem;
      }

      .step p {
        margin: 0;
        color: var(--muted);
        line-height: 1.8;
      }

      .testimonial-wrap {
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 22px;
      }

      .quote {
        background: rgba(255,255,255,0.02);
        border: 1px solid var(--border);
        border-radius: 22px;
        padding: 22px;
      }

      .stars {
        color: var(--accent);
        letter-spacing: 0.14em;
        margin-bottom: 14px;
      }

      .quote p {
        margin: 0 0 20px;
        color: var(--muted);
        line-height: 1.8;
      }

      .person {
        display: flex;
        align-items: center;
        gap: 12px;
      }

      .avatar {
        width: 42px;
        height: 42px;
        border-radius: 50%;
        background: linear-gradient(135deg, var(--primary), var(--secondary));
        display: grid;
        place-items: center;
        font-weight: 700;
      }

      .person small {
        display: block;
        color: var(--muted);
      }

      .cta {
        margin: 48px 0 0;
      }

      .cta-box {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 24px;
        padding: 30px 34px;
        border: 1px solid var(--border);
        border-radius: 28px;
        background: linear-gradient(135deg, rgba(124,92,255,0.12), rgba(0,212,255,0.06));
      }

      .cta-box h3 {
        margin: 0 0 8px;
        font-size: clamp(1.7rem, 2vw, 2.4rem);
      }

      .cta-box p {
        margin: 0;
        color: var(--muted);
      }

      footer {
        padding: 36px 0 80px;
        color: var(--muted);
      }

      .footer-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 16px;
        border-top: 1px solid var(--border);
        padding-top: 22px;
      }

      .footer-links {
        display: flex;
        gap: 18px;
      }

      @media (max-width: 980px) {
        .hero-grid,
        .showcase,
        .services,
        .process,
        .testimonial-wrap {
          grid-template-columns: 1fr;
        }

        .nav-links {
          display: none;
        }

        .cta-box,
        .section-header,
        .footer-row {
          flex-direction: column;
          align-items: flex-start;
        }
      }

      @media (max-width: 640px) {
        .nav-actions .button.secondary {
          display: none;
        }

        .stats {
          grid-template-columns: 1fr;
        }

        h1 {
          letter-spacing: -0.04em;
        }
      }
    </style>
  </head>
  <body>
    <header class="topbar">
      <div class="container nav">
        <a href="#accueil" class="brand" aria-label="Bickri Agency">
          <span class="brand-mark">B</span>
          <span>Bickri</span>
        </a>

        <nav class="nav-links" aria-label="Navigation principale">
          <a href="#services">Services</a>
          <a href="#projets">Projets</a>
          <a href="#process">Process</a>
          <a href="#avis">Avis</a>
          <a href="#contact">Contact</a>
        </nav>

        <div class="nav-actions">
          <a class="button secondary" href="#contact">Parler à un expert</a>
          <a class="button primary" href="#contact">Démarrer</a>
        </div>
      </div>
    </header>

    <main id="accueil">
      <section class="hero">
        <div class="container hero-grid">
          <div>
            <span class="eyebrow">Agency digitale</span>
            <h1>On donne vie à votre marque en ligne.</h1>
            <p class="lead">
              Bickri conçoit des expériences numériques qui attirent, convertissent et
              fidélisent. Branding, sites web, stratégie marketing et contenu — tout est
              pensé pour faire grandir votre business.
            </p>

            <div class="hero-actions">
              <a class="button primary" href="#contact">Obtenir un devis</a>
              <a class="button secondary" href="#projets">Voir nos réalisations</a>
            </div>

            <div class="stats" aria-label="Chiffres clés">
              <div class="stat">
                <strong>120+</strong>
                <span>projets livrés</span>
              </div>
              <div class="stat">
                <strong>4.9/5</strong>
                <span>satisfaction</span>
              </div>
              <div class="stat">
                <strong>+186%</strong>
                <span>croissance média</span>
              </div>
            </div>
          </div>

          <div class="hero-visual" aria-label="Aperçu du tableau de bord digital">
            <div class="visual-card">
              <div class="mini-window">
                <div class="window-dots"><span></span><span></span><span></span></div>
                <span style="color: var(--muted); font-size: 0.8rem;">bickri.ai</span>
              </div>

              <div class="dashboard">
                <div class="dashboard-top">
                  <div class="panel">
                    <div style="color: var(--muted); font-size: 0.8rem;">Performance</div>
                    <div class="chart-bars" aria-hidden="true">
                      <span></span>
                      <span></span>
                      <span></span>
                      <span></span>
                      <span></span>
                      <span></span>
                    </div>
                  </div>

                  <div class="panel">
                    <div style="color: var(--muted); font-size: 0.8rem; margin-bottom: 8px;">Croissance</div>
                    <div class="ring" aria-label="70% de croissance">
                      <div class="ring-inner">70%</div>
                    </div>
                  </div>
                </div>
              </div>
            </div>

            <div class="floating-card">
              <div style="color: var(--muted); font-size: 0.8rem;">CA généré</div>
              <strong>€84K</strong>
              <small style="color: var(--success);">+32% ce mois</small>
            </div>
          </div>
        </div>
      </section>

      <section id="services">
        <div class="container">
          <div class="section-header">
            <h2>Des services qui font la différence</h2>
            <p>
              Nous combinons stratégie, design et performance pour transformer votre image
              numérique en croissance durable.
            </p>
          </div>

          <div class="services">
            <article class="service-card">
              <div class="icon-box">✦</div>
              <h3>Branding & Positionnement</h3>
              <p>
                Identité visuelle, voix de marque, messaging et storytelling qui donnent
                du sens à votre présence digitale.
              </p>
            </article>

            <article class="service-card">
              <div class="icon-box">◎</div>
              <h3>Sites & Applications</h3>
              <p>
                Landing pages, sites vitrines, boutiques et interfaces premium conçues pour
                convertir et améliorer l’expérience client.
              </p>
            </article>

            <article class="service-card">
              <div class="icon-box">▣</div>
              <h3>Marketing Digital</h3>
              <p>
                Stratégies SEO, social media, publicité et automatisation pour capter plus
                de leads et augmenter votre visibilité.
              </p>
            </article>
          </div>
        </div>
      </section>

      <section id="projets">
        <div class="container">
          <div class="section-header">
            <h2>Nos dernières réalisations</h2>
            <p>
              Nous aidons les marques à se distinguer avec des projets à la fois beaux,
              utiles et orientés résultats.
            </p>
          </div>

          <div class="showcase">
            <div class="showcase-large">
              <div style="color: var(--muted); text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.72rem;">Cas client</div>
              <h3 style="margin: 14px 0 8px; font-size: 2rem;">Nova Studio</h3>
              <p style="margin: 0; color: var(--muted); line-height: 1.8; max-width: 650px;">
                Refonte complète de l’identité digitale d’une agence de création visuelle,
                avec un site premium et une stratégie de génération de leads.
              </p>
              <div class="project-visual" aria-label="Aperçu du projet Nova Studio"></div>
            </div>

            <div class="showcase-small">
              <div style="color: var(--muted); text-transform: uppercase; letter-spacing: 0.12em; font-size: 0.72rem;">Impact</div>
              <div class="mini-list">
                <div class="mini-item"><span>Leads générés</span><strong>+240%</strong></div>
                <div class="mini-item"><span>Temps moyen</span><strong>3.2s</strong></div>
                <div class="mini-item"><span>Retour visuel</span><strong>DX/UX</strong></div>
                <div class="mini-item"><span>ROI marketing</span><strong>4.8x</strong></div>
              </div>
            </div>
          </div>
        </div>
      </section>

      <section id="process">
        <div class="container">
          <div class="section-header">
            <h2>Une méthodologie claire</h2>
            <p>
              Nous travaillons de manière stratégique et collaborative pour livrer des
              solutions efficaces sans perdre de vue vos objectifs business.
            </p>
          </div>

          <div class="process">
            <div class="step">
              <div class="step-number">01</div>
              <h3>Audit</h3>
              <p>Analyse de votre marché, concurrence, positioning et opportunités.</p>
            </div>
            <div class="step">
              <div class="step-number">02</div>
              <h3>Stratégie</h3>
              <p>Définition de l’offre, du message et des canaux les plus performants.</p>
            </div>
            <div class="step">
              <div class="step-number">03</div>
              <h3>Création</h3>
              <p>Design, UX, contenu et production de votre présence digitale premium.</p>
            </div>
            <div class="step">
              <div class="step-number">04</div>
              <h3>Optimisation</h3>
              <p>Suivi des performances, tests et améliorations continues pour sécuriser la croissance.</p>
            </div>
          </div>
        </div>
      </section>

      <section id="avis">
        <div class="container">
          <div class="section-header">
            <h2>Ils nous font confiance</h2>
            <p>
              Nos clients nous rejoignent pour transformer leur visibilité et accélérer leur business.
            </p>
          </div>

          <div class="testimonial-wrap">
            <article class="quote">
              <div class="stars">★★★★★</div>
              <p>
                “Bickri a redessiné notre image et notre site en quelques semaines. Le résultat
                est premium, clair et convertit vraiment mieux.”
              </p>
              <div class="person">
                <div class="avatar">AR</div>
                <div>
                  <strong>Amélie R.</strong>
                  <small>Founder • Luma Studio</small>
                </div>
              </div>
            </article>

            <article class="quote">
              <div class="stars">★★★★★</div>
              <p>
                “Une équipe à l’écoute, ultra pro et très orientée résultats. Notre audience a
                grossi et notre image de marque s’est considérablement renforcée.”
              </p>
              <div class="person">
                <div class="avatar">KD</div>
                <div>
                  <strong>Kévin D.</strong>
                  <small>CEO • Atlas Commerce</small>
                </div>
              </div>
            </article>

            <article class="quote">
              <div class="stars">★★★★★</div>
              <p>
                “Leur approche stratégique nous a permis de mieux vendre, de mieux communiquer et de
                gagner du temps sur les tâches quotidiennes.”
              </p>
              <div class="person">
                <div class="avatar">SM</div>
                <div>
                  <strong>Sara M.</strong>
                  <small>Marketing • Nexo Lab</small>
                </div>
              </div>
            </article>
          </div>
        </div>
      </section>

      <section class="cta" id="contact">
        <div class="container">
          <div class="cta-box">
            <div>
              <h3>Prêt à faire grandir votre marque ?</h3>
              <p>Discutons de votre projet digital et de la meilleure façon de le lancer.</p>
            </div>
            <a class="button primary" href="mailto:hello@bickri.agency">hello@bickri.agency</a>
          </div>
        </div>
      </section>
    </main>

    <footer>
      <div class="container footer-row">
        <div class="brand" aria-label="Bickri Agency footer brand">
          <span class="brand-mark">B</span>
          <span>Bickri</span>
        </div>
        <div class="footer-links">
          <a href="#services">Services</a>
          <a href="#projets">Projets</a>
          <a href="#contact">Contact</a>
        </div>
        <span>© <span id="year"></span> Bickri Agency</span>
      </div>
    </footer>

    <script>
      document.getElementById('year').textContent = new Date().getFullYear();
    </script>
  </body>
</html>
