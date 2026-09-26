# Pinchy — GitHub and Pages

- Repository: [pablo-mano/Pinchy](https://github.com/pablo-mano/Pinchy)
- Interactive explorer: [pablo-mano.github.io/Pinchy](https://pablo-mano.github.io/Pinchy/)
- Deployment runs: [Publish Pinchy explorer](https://github.com/pablo-mano/Pinchy/actions/workflows/pages.yml)

The workflow publishes only `site/` from `main`. `index.html` bundles the model, renderer and styles; no Node build, API key or backend is required. Print files and videos remain repository downloads. Firmware is [TODO](../TODO.md), with no device source code or binaries included.

## Update the published page

1. Update `site/index.html`, preserving its embedded assets and attribution.
2. Commit and push the update to `main`.
3. Check the Pages workflow above. A successful deployment updates the same public URL.

Pages uses **Settings → Pages → Build and deployment → Source: GitHub Actions**. To redeploy without another content change, open **Actions → Publish Pinchy explorer → Run workflow** on `main`.

The [standalone HTML](../site/index.html) also opens from disk. A GitHub `blob` link shows the file rather than running the explorer; use the Pages URL for the interactive view.

## Publish a fork

Enable GitHub Actions as the Pages source in your fork, run the workflow, and replace the original repository/site URLs with those of your fork. Keep `.github/workflows/pages.yml` and the complete `site/` folder. The workflow expects `main`; adapt its branch filter if your default branch differs.

Configuration follows the [GitHub Pages custom workflow documentation](https://docs.github.com/en/pages/getting-started-with-github-pages/using-custom-workflows-with-github-pages).
