# Research Portfolio

Public source for [Aiden Research Portfolio](https://anhnd3.github.io/research-portfolio/), an independently maintained technical portfolio documenting applied AI research and empirical evaluation.

## Publication

The supplementary pages use **Quarto (.qmd)**. The homepage and four research articles are **self-contained HTML publications** with responsive tables, inline SVG diagrams/charts, and local interactions, copied into `_site` by Quarto. No external JavaScript or CDN is needed for the article.

- Homepage: `index.html` (static resource; `index.qmd` is excluded from rendering)
- Reranking article: `articles/compact-domain-reranking/index.html`
- Vision Transformer retrospective: `articles/vision-transformers-facial-expression-recognition/index.html`
- GDEM reproduction study: `articles/gdem-graph-distillation-reproduction/index.html`
- UFCE thesis retrospective (defended September 2026): `articles/verified-counterfactual-explanations-ufce-ff/index.html`
- About page: moved to the root site https://anhnd3.github.io/ (repo `anhnd3/anhnd3.github.io`, canonical `Person` at `https://anhnd3.github.io/#person`); `about/index.html` is a redirect stub
- AI/LLM discovery: `llms.txt`; Atom feed built by `scripts/build_discovery.py`; IndexNow ping by `scripts/indexnow.py` after deploy
- Theme: `styles.css`
- Publishing: `.github/workflows/publish.yml`
- SEO: `scripts/verify_sitemap.py`, `scripts/generate_social_image.py`
- Social images: `assets/research-reranking-og.png` and `assets/research-gdem-og.png` (generated at build)

To preview locally (Quarto required):

```bash
python scripts/generate_social_image.py
quarto preview
```

To build:

```bash
python scripts/generate_social_image.py
quarto render
python scripts/verify_sitemap.py
```

## GitHub Pages setup

In **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source. A push to `main` triggers the workflow and deploys the `_site` output.

## Publication scope

The repository contains the website sources and aggregate visuals of published research findings. Methodological boundaries and evaluation protocols are described within individual articles. Conceptual diagrams are illustrative, not new measurements.

See [Publication Policy](policy.qmd). No open content/code license is granted implicitly.

## Discovery and indexing

The reranking article has been updated to **v3.1** (re-architected research narrative and balanced takeaways, published 22 November 2026). The ViT and GDEM retrospectives were published on **22 November 2026**; GDEM research dates to **December 2025**. The UFCE thesis retrospective was published **23 November 2026** and reports thesis defense in **September 2026**, with distinct defense-appendix experiments. The static HTML article is injected into Quarto's generated sitemap after rendering, because it is published as a resource rather than a `.qmd` page. SEO validation also checks the canonical URL, JSON-LD article metadata, social preview image, and `index,follow` status.

- Reranking article: https://anhnd3.github.io/research-portfolio/articles/compact-domain-reranking/
- Vision Transformer article: https://anhnd3.github.io/research-portfolio/articles/vision-transformers-facial-expression-recognition/
- GDEM reproduction: https://anhnd3.github.io/research-portfolio/articles/gdem-graph-distillation-reproduction/
- UFCE thesis retrospective: https://anhnd3.github.io/research-portfolio/articles/verified-counterfactual-explanations-ufce-ff/
- Sitemap: https://anhnd3.github.io/research-portfolio/sitemap.xml
- Google Search Console: verify the URL-prefix property `https://anhnd3.github.io/research-portfolio/`, then inspect and submit the article URL.
- Bing Webmaster Tools: verify the site and submit its sitemap when needed.
- Crawler policy: `robots.txt` is host-root-scoped (`https://anhnd3.github.io/robots.txt`); a `robots.txt` inside this project repository **would not control crawler access** on the shared GitHub Pages hostname.
- GitHub repository metadata is managed in **Settings → General** and **About**: set the description, website homepage, and repository topics.

Search engine indexing and AI-search citations are not guaranteed by this metadata. Sitemap and schema make content discoverable and interpretable; Search Console confirms Google indexing status.
