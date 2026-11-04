# Research Portfolio

Public source for [Aiden Research Notes](https://anhnd3.github.io/research-portfolio/), an independently maintained technical portfolio focused on compact AI models, ranking, calibration, and evaluation.

## Publication

The portfolio pages use **Quarto (.qmd)**. The flagship article is a **self-contained HTML publication** with responsive tables, inline SVG diagrams/charts, and local interactions, copied into `_site` by Quarto. No external JavaScript or CDN is needed for the article.

- Homepage: `index.qmd`
- Flagship article: `articles/compact-domain-reranking/index.html`
- Notes: `notes.qmd`
- Theme: `styles.css`
- Publishing: `.github/workflows/publish.yml`

To preview locally (Quarto required):

```bash
quarto preview
```

To build:

```bash
quarto render
```

## GitHub Pages setup

In **Settings → Pages → Build and deployment**, choose **GitHub Actions** as the source. A push to `main` triggers the workflow and deploys the `_site` output.

## Publication scope

The repository contains the website sources and aggregate visuals of published research findings. Methodological boundaries and evaluation protocols are described within individual articles. Conceptual diagrams are illustrative, not new measurements.

See [Publication Policy](policy.qmd). No open content/code license is granted implicitly.
