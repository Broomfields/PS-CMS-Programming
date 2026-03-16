---
title: "Builds CMS"
parent: "forge-and-fable"
---

Same structural pattern as the programming CMS, but for physical builds — mostly CAD work and 3D printed things. The metadata reflects that: CAD tools in place of programming languages, links out to Printables or Thingiverse where relevant, and support for downloadable STL and SCAD files alongside the images.

The manifest pipeline is identical. Push, generate, publish, fetch.

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

    U->>S: Visit builds section
    S->>CDN: Fetch manifest (if cache miss)
    CDN-->>S: manifest.json
    S->>U: Render build cards

    U->>S: Click a build
    S->>CDN: Fetch build folder content
    CDN-->>S: Markdown + images + files
    S->>U: Render build page
```

[View the repository](https://github.com/Broomfields/PS-CMS-Builds)
