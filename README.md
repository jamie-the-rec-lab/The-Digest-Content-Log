# TheRecLab digest

A weekly job that keeps a library of recruiting content up to date, then builds
and publishes a digest from it.

## Start here

**`docs/RUN.md`** is the map: what happens, in what order, and which document
covers each part. Everything else is one level down from there.

## The folders

| Folder | What is in it |
|---|---|
| `docs/` | Every guide. How it runs, how items are picked, how it is written, what to do when it breaks. |
| `config/` | The lists. Every podcast, newsletter and vendor tracked, and where it publishes. |
| `scripts/` | The code. Fetching, indexing, the duplicate sweep, the health report, the email builder. |
| `library/` | The archive. Podcasts, tech, agency, newsletters, reports, news, adhoc. This is the asset. |
| `digest/` | The output. The template, every dated build, and every edition exactly as it went live. |
| `_state/` | Working files the job writes: the two weekly handover files and the run log. |
| `_to_delete/` | Where unwanted files go. Nothing in this project deletes, because the weekly run cannot answer a permission prompt at 6am. Empty it whenever. |

## Quick answers

- **Change something?** The table at the bottom of `docs/RUN.md` says which file to open.
- **Something broken?** `docs/TROUBLESHOOTING.md`.
- **What does that word mean?** `docs/GLOSSARY.md`.
- **Search the library?** `docs/HOW_TO_QUERY.md`.

## The one rule worth knowing

The email to subscribers is never sent automatically. Jamie reviews the live
page, then a test email, and only then does it go to the list. See
`docs/SEND_NEWSLETTER.md`.
