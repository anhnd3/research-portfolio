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

## Experimental-data policy

This public repository contains only material selected for publication. It intentionally does **not** contain proprietary datasets, internal source code, raw experiment traces, checkpoints, or confidential project metadata. Charts visualize the aggregate results of the corresponding published article. Experimental diagrams are illustrative, not new measurements.

See [Publication Policy](policy.qmd). No open content/code license is granted implicitly.
