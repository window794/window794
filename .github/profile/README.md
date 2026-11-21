# Design System Edition

The masthead uses the cream, charcoal, mist blue and pre-dawn surfaces from [Atelier Tools](https://github.com/window794/atelier-tools/blob/main/assets/style.css). The English title is [Cormorant Garamond](https://github.com/google/fonts/tree/main/ofl/cormorantgaramond) and the Japanese spine is [Zen Old Mincho](https://github.com/google/fonts/tree/main/ofl/zenoldmincho). Both families are licensed under SIL OFL 1.1. The SVGs contain the outlines of this lettering. The small labels use a generic monospace face.

The language badges are local, recoloured copies of output from [GitHub Readme Tech Stack](https://github.com/0l1v3rr/github-readme-tech-stack). The Atelier pictures show the public app converting tab-separated sample rows into JSON.

## Activity

The initial 3D images use dates, counts and levels from [the public calendar](https://github.com/users/window794/contributions). The workflow uses [github-profile-3d-contrib v0.9.3](https://github.com/yoshi389111/github-profile-3d-contrib/tree/v0.9.3) and the colour ramps in [calendar.json](calendar.json). After generation, `python .github/profile/calendar.py` extracts the day columns and date range for the wide layout.

The initial images are included on `profile/design-system`. GitHub schedules the Monday 03:17 JST refresh once the workflow exists on the default branch and Actions is enabled. Manual dispatch also requires the workflow to be registered on the default branch. The generator has read access. A separate job commits just the two SVGs to `profile/design-system` if they change. The README points directly to those images so the same references work after adoption. Keep the design branch available for that purpose. The workflow uses the built-in token and requires no personal secret or pull request.

## Recorded AI collaboration

The Claude card is dated separately from the calendar. On 22 November 2026, the `author:window794 is:public` commit search returned 208 distinct indexed commits. Nine had a Claude address in a trailer parsed by `git interpret-trailers --parse`. The monthly bars use commit author dates. Both themes use the [cocommit renderer](https://github.com/yosh1/cocommit/blob/d28ecd882a8127f1a877a6eae2c6a9d6c178af53/src/render.js). The search and local rendering required no credentials. Refresh the counts, date and alternative text together when replacing the snapshot.
