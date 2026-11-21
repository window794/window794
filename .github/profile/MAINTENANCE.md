# Maintaining the profile artwork

## Cover and toolbox

The two cover drawings use the cream and mist blue from [Atelier Tools](https://github.com/window794/atelier-tools#デザイン). Edit the SVGs together to keep the two windows aligned. The moving sun respects the visitor's reduced-motion preference.

The five personal-development badges came from [GitHub Readme Tech Stack](https://github.com/0l1v3rr/github-readme-tech-stack). The [card request](https://github-readme-tech-stack.vercel.app/api/cards?hideTitle=true&hideBg=true&showBorder=false&width=340&align=left&gap=8&lineCount=2&badge=%23364956&line1=html5,HTML,bbd6e0;css,CSS,bbd6e0;javascript,JavaScript,bbd6e0;&line2=typescript,TypeScript,bbd6e0;python,Python,bbd6e0;) returns a self-contained SVG with embedded logos. The checked-in copy has a tighter viewBox and an accessible title. Profile views load every image from this repository.

## Contribution calendar

The initial images use the days, levels and counts from [window794's public calendar](https://github.com/users/window794/contributions). Both images were rendered with [github-profile-3d-contrib v0.9.3](https://github.com/yoshi389111/github-profile-3d-contrib/tree/v0.9.3). The profile script keeps the day columns, period and contribution total and lays them out in a wide figure. The initial range is 16 November 2025 through 21 November 2026, as served by GitHub.

Once the workflow is on the default branch and Actions is enabled, it runs on Mondays at 03:17 Japan time, or manually through **Actions → Refresh contribution calendar → Run workflow** on the default branch. The render job reads GitHub's calendar using the automatic repository token. A separate job proposes changes to the two calendar SVGs on the `automation/contribution-calendar` branch. Merging that PR updates the profile.

The PR step requires **Settings → Actions → General → Workflow permissions → Allow GitHub Actions to create and approve pull requests**. The workflow only creates or updates a PR. No PAT or repository secret is needed. The workflow file requests write access to contents and pull requests only for the PR job.

To reframe existing upstream output locally, place the two generated files under `profile-3d-contrib/` and run `python .github/profile/calendar.py` from the repository root. The input filenames and colour ramps are in [calendar.json](calendar.json).

## Claude co-author snapshot

On 22 November 2026, the unauthenticated [public commit search](https://github.com/search?q=author%3Awindow794+is%3Apublic&type=commits) returned 207 distinct indexed commits. All three result pages were checked. Nine messages had a Claude trailer recognized by `git interpret-trailers --parse` with the address `noreply@anthropic.com`. None had either Codex address recognized by this release. The totals cover the indexed history. The bars group the most recent twelve calendar months by author date.

Both cards use the [pinned cocommit renderer](https://github.com/yosh1/cocommit/blob/d28ecd882a8127f1a877a6eae2c6a9d6c178af53/src/render.js) with a blue palette and static bars. They are dated snapshots. To refresh them, query the public commit search again, check the trailer addresses against the [agent definitions](https://github.com/yosh1/cocommit/blob/d28ecd882a8127f1a877a6eae2c6a9d6c178af53/src/fetch.js), and pass the verified counts to `renderCard`. Update both SVGs, the date and the README's alternative text together. If the search exceeds GitHub's 1,000-result retrieval limit, split it into non-overlapping author-date ranges before counting. The public search and local renderer require no credentials.
