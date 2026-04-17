# Content Flow

## Overview

This document describes how content moves through the Mijuku system.

The system is designed to take human-authored content and transform it into structured data that can be consumed by the website.

The core idea is:

> Markdown content in `data/content/` becomes structured output in `data/generated/`, which is then used by the website layer.

This creates a pipeline with clear responsibilities and separation between authorship, processing, and presentation.

---
## High-Level Flow

The system follows this general flow:

```text
Author writes content
    ↓
Content is stored in data/content/
    ↓
Processing layer reads files
    ↓
Frontmatter and body are parsed
    ↓
Metadata is validated against schema
    ↓
Structured objects are created
    ↓
Derived outputs are generated
    ↓
Website consumes generated data
```
---
## Core Layers

### 1. Content Layer

The content layer is the source of truth.

Location:
> data/content/
This contains human-authored files such as:
- notes
- writing
- projects
- experiments

At the beginning of the system, notes are the first supported content type.

example:
> data/content/notes/programming/binary-search-md

Each content file contains:
- YAML frontmatter
- Markdown body content

### 2. Processing Layer

The processing layer interprets content.

Location:
> processing/

its job is to:
- locate content files
- load file contents
- parse frontmatter
- validate schema
- transform content into structured objects
- generate derived outputs

**This layer should not be responsible for visual rendering.**

### 3. Generated Data Layer

The generated data layer contains machine-produced outputs.

Location:
> data/generated/

Examples of generated outputs:
- all-notes.json
- recent-notes.json
- tags.json
- content-manifest.json

**These outputs are *derived* from raw content and should not be edited manually**.

### 4. Website Layer

The website layer consumes generated data.

Location:
> website/

Its role is to:
- render pages
- display content
- provide navigation
- surface recent updates
- organize material for browsing

The website should consume processed data instead of directly depending on raw Markdown files when possible.

---

## Detailed Flow for Notes

The first implemented content type is the note.

A note follows this path:

### Step 1: Authoring
A note is written as a Markdown file inside:
> data/content/notes/

Example:
> data/content/notes/machine-learning/autoencoder-suitcase.md

The note contains required metadeta such as:
- `id`
- `title`
- `date`
- `category`
- `tags`
- `summary`
- `status`

and a Markdown body.

### Step 2: Discovery
The processing layer scans hte notes directory and finds all note files.

This may later include:
- recursive directory scanning
- filtering by file extension
- ignoring temporary or hidden files

### Step 3: Loading
Each note file is loaded into memory as raw text.

At this point, the system only knows:
- file path
- raw file contents

### Step 4: Parsing
The file is split into:
- frontmatter
- body content
The front matter is parsed into structured metadata.

The body remains Markdown text.

### Step 5: Validation
The parsed note is checked against the note schema.

Validation confirms:
- required fields exist
- field types are correct
- formatting rules are respected
- allowed values are valid

If validation fails, the system should report useful errors.

# Step 6: Normalization
After validation, the note may be normalized.

Examples:
- trimming whitespace
- standardizing tag format
- confirming category names
- resolving missing optional values
- deriving slug from filename or id if needed

This step ensures consistency.

# Step 7: Structured Object Creation

The note is converted into a structured object.

Example:

```json
{
    "id": "autoencoder-suitcase",
    "title": "Autoencoders: Compression, Loss, and the Suitcase",
    "date": "2026-04-16",
    "category": "machine-learning",
    "tags": ["autoencoders", "neural-networks", "representation-learning"],
    "summary": "Understanding autoencoders through compression and reconstruction.",
    "status": "draft",
    "content": "full markdown body here"
}
```
This object becomes the canonical machine-readable version of the note.

### Step 8: Indexing and Derived Output
Once all notes are structured, the system can generate additional outputs.

Examples:

`all-notes.json`

Contains every structured note.

`recent-notes.json`

Contains notes sorted by most recent date.

`tags.json`

Maps tags to associated notes.

`categories.json`

Groups notes by category.

These derived outputs make the weebsite easier to build.

### Step 9: Website Consumption
The website layer reads generated data and renders it into pages or sections.

Examples:

- notes homepage
- note detail page
- recent notes feed
- category pages
- tag pages

This keeps the presentation layer simple and focused.

### Why This Flow Exists
This architecture exists to separate concerns.

#### Content stays human-first
Writers should be able to create notes without thinking about rendering details.

#### Processing stays machine-focused
The processing layer handles strucutre, validation, and data generation.

#### Website stays presentation-focused
The website displays already-structured information insttead of reinventing parsing logic.

This makes the system easier to grow.

### Current Scope
At the current stage of the project, only part of the full flow is implemented.

Completed so far:
- repository structure
- content folders
- initial note files
- note schema documentation
- VS Code snippet for notes

Planned next:

- parser for Markdown notes
- schema validation
- generated JSON outputs
- website integration

### Future Extensions

This same flow can later supoport other content types:
- writing
- projects
- experiments

Each type may have its own schema, but the same high-level pipeline can apply:
> raw file -> parse -> validate -> normalize -> structure -> generate -> render

This keeps the system consistent across domains.










