---
title: "Audible Library Data Export"
description: "A Python tool for exporting metadata from your Audible library — started as a quick cover image grab, ended up as something more complete."
date: 2026-03-05
status: "complete"
repo: "https://github.com/Broomfields/Audible-Library-Data-Export"
languages: ["Python"]
dependencies: ["audible", "Playwright"]
tags: ["tool", "audible", "cli", "python", "OAuth"]
---

Started because I was putting together a tier list after a conversation with a friend. I had a load of Audible books to rank and wanted the cover images to go with them. Rather than pulling them one by one, I wrote something to do it for me.

That ended up becoming this. What started as a cover image grabber is now a full export tool — titles, authors, narrators, series, genres, descriptions, ratings, listening progress, companion PDFs, the lot. Handles libraries over a thousand books through paginated API calls.

Authentication is handled properly too. OAuth tokens only, stored in a git-ignored directory. No passwords are ever touched.
