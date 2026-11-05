# Research Portfolio

Public source for [Aiden Research Notes](https://anhnd3.github.io/research-portfolio/), an independently maintained technical portfolio focused on compact AI models, ranking, calibration, and evaluation.

## Publication

The portfolio pages use **Quarto (.qmd)**. The flagship article is a **self-contained HTML publication** with responsive tables, inline SVG diagrams/charts, and local interactions, copied into `_site` by Quarto. No external JavaScript or CDN is needed for the article.

- Homepage: `index.qmd`
- Flagship article: `articles/compact-domain-reranking/index.html`
- Notes: `notes.qmd`
- Theme: `styles.css`
- Publishing: `.github/workflows/publish.yml`
- SEO: `scripts/verify_sitemap.py`, `scripts/generate_social_image.py`
- Social image: `assets/research-reranking-og.png` (generated at build)

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

The article remains **v1.2**. The static HTML article is injected into Quarto's generated sitemap after rendering, because it is published as a resource rather than a `.qmd` page. SEO validation also checks the canonical URL, JSON-LD article metadata, social preview image, and `index,follow` status.

- Public article: https://anhnd3.github.io/research-portfolio/articles/compact-domain-reranking/
- Sitemap: https://anhnd3.github.io/research-portfolio/sitemap.xml
- Google Search Console: verify the URL-prefix property `https://anhnd3.github.io/research-portfolio/`, then inspect and submit the article URL.
- Bing Webmaster Tools: verify the site and submit its sitemap when needed.
- Crawler policy: `robots.txt` is host-root-scoped (`https://anhnd3.github.io/robots.txt`); a `robots.txt` inside this project repository **would not control crawler access** on the shared GitHub Pages hostname.
- GitHub repository metadata is managed in **Settings → General** and **About**: set the description, website homepage, and repository topics.

Search engine indexing and AI-search citations are not guaranteed by this metadata. Sitemap and schema make content discoverable and interpretable; Search Console confirms Google indexing status.
