---
title: "Programming CMS"
parent: "forge-and-fable"
---

The programming CMS is the most straightforward of the three. Each project gets a folder with a markdown file and an images directory. Frontmatter handles the metadata — title, description, languages, dependencies, status, and so on. A GitHub Actions workflow processes it on push and publishes a manifest to a release tag, which the site fetches at runtime.

That's it. No database, no backend beyond what GitHub provides. Just structured markdown and a CI pipeline.

**Publishing pipeline — triggered on commit:**

```mermaid
graph LR
    A[Markdown + frontmatter] --> B[Push to main]
    B --> C[GitHub Actions]
    C --> D[manifest.json]
    D --> E[GitHub Release / CDN]
```

**Site consumption — triggered by the user:**

```mermaid
sequenceDiagram
    participant U as User
    participant S as Forge & Fable
    participant CDN as GitHub CDN

    U->>S: Visit programming section
    S->>CDN: Fetch manifest (if cache miss)
    CDN-->>S: manifest.json
    S->>U: Render project cards

    U->>S: Click a project
    S->>CDN: Fetch project folder content
    CDN-->>S: Markdown + images + files
    S->>U: Render project page
```

[View the repository](https://github.com/Broomfields/PS-CMS-Programming)
