# Research Portfolio

Public source for [AnhND3 Research Notes](https://anhnd3.github.io/research-portfolio/), an independently maintained technical portfolio focused on compact AI models, ranking, calibration, and evaluation.

## Publication

The website is authored in **Quarto (.qmd)** and rendered to **HTML**, with responsive tables and SVG charts. Source Markdown is not the presentation format shown to readers.

- Homepage: `index.qmd`
- Articles: `articles/*/index.qmd`
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

This public repository contains only material selected for publication. It intentionally does **not** contain proprietary datasets, internal source code, raw experiment traces, checkpoints, or confidential project metadata. Charts reuse the aggregate results of the corresponding published article.

See [Publication Policy](policy.qmd). No open content/code license is granted implicitly.
