# Differential Equations Review

Daniel Chen’s review for AS.110.302 opens on the Formula Sheet. Topics & Practice contains ten chapters with searchable notes, original practice problems, and selected worked solutions.

## Preview the included site

Open `dist/index.html` in a modern browser with MathML support. The included distribution is the complete version 6 reader, from source commit `c634fc0c05071a5d40ee5df134947f1e841579be`.

## Edit the review

| Material | Source |
| --- | --- |
| Formula Sheet | `content/reference/cheatsheet.md` |
| Lesson notes and examples | Chapter Markdown files in `content/reference/` |
| Problems, hints, and solutions | `content/reference/problems.json` |
| Chapter titles, summaries, and order | `content/reference/catalog.json` |
| Page template, navigation behavior, typography, and print styles | `ui/` |
| Diagram generation | `scripts/figures.py` |

The formula sheet and chapter notes are separate. Update both when correcting shared material. The font license is included with its source and distributed copies.

## Build locally

Install Python 3.12, Pandoc 3.1.11.1, and Node.js. With your Python environment active, run these commands at the repository root.

```sh
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/verify.py
```

The build writes the site to `dist/` and a summary to `review/build-summary.json`. Verification checks links, search entries, math, practice content, JavaScript syntax, and the standalone export. Some checks encode specific wording and course content. Update those assertions when intentionally revising that material. To produce a single offline HTML file, run `python scripts/export.py Differential_Equations.html`.

## Publish with GitHub Pages

Place the extracted files at the root of `danielchen05/diff-eq`, including `.github/workflows/pages.yml`. Use `main` as the default branch. When ready to publish, select **Settings → Pages → Build and deployment → Source → GitHub Actions**. Run **Build and publish course review** from the Actions tab, or push a change to `main`. The workflow rebuilds from source, verifies the result, and deploys `dist/` to `https://danielchen05.github.io/diff-eq/`.

For subsequent edits, the workflow builds from source on each push to `main`. To keep the checked-in offline preview current too, rebuild locally and commit the updated `dist/` files with the source.
