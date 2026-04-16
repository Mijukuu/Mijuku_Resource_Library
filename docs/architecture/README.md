# Mijuku System Architecture

## Overview

This repository is not just a website.

It is a **content system + processing pipeline + presentation layer** that turns daily work into a structured, living site.

The goal is to create a system where:

- Content is created daily (notes, writing, code, experiments)
- Content is stored in a consistent structure
- Content is processed into structured data
- The website reflects that data automatically

This is a **living system of progress**, not a static portfolio.

---

## Core Philosophy

This project follows a layered architecture:

1. **Content Layer (Data)**
2. **Processing Layer**
3. **Presentation Layer (Website)**

Each layer has a clear responsibility and should remain decoupled.

---

## Folder Structure

### `data/`

The **source of truth** for all authored content.

#### `data/content/`
Mijuku Created Content

- `notes/` → programming, calculus, machine learning, etc.
- `writing/` → poems, stories, essays
- `projects/` → project entries and metadata
- `experiments/` → diagrams, animations, visualizations

Each item in this folder is a **publishable unit**.

#### `data/generated/`
Machine-generated data.

- `indexes/` → content indexes
- `recent/` → recent activity feeds
- `tags/` → tag mappings
- `manifests/` → structured content outputs

Nothing here is manually edited.

---

### `processing/`

The **pipeline layer**.

Responsible for:

- Loading content
- Validating schemas
- Transforming content
- Generating derived data
- Building indexes

Subfolders:

- `schemas/` → definitions of content structures
- `loaders/` → file readers (markdown, json, etc.)
- `transforms/` → content transformations
- `validators/` → schema validation
- `indexers/` → tag + category indexing
- `utils/` → shared helpers

---

### `website/`

The **presentation layer**.

Responsible for:

- Rendering pages
- Layouts and components
- Navigation
- Styling

This layer should not contain raw content logic.

It consumes processed data.

---

### `config/`

Global configuration for the system.

- Navigation structure
- Taxonomy (tags, categories)
- Site-level settings
- Defaults for content

---

### `assets/`

Static files:

- images
- diagrams
- animations
- previews

---

### `docs/`

Internal documentation for the system.

- architecture decisions
- schema definitions
- design notes

---

## Content Model

Each piece of content is treated as a **structured object**.

Examples:

- A note
- A poem
- A project entry
- An experiment

Each object:

- lives in `data/content/`
- has metadata (frontmatter or JSON)
- has a consistent schema
- is independently publishable

---

## Content Types (Initial)

### Notes
- Technical and conceptual learning
- Organized by domain (programming, calculus, ML)

### Writing
- Poems, stories, essays
- More expressive, less structured than notes

### Projects
- Work artifacts
- May link to external repositories

### Experiments
- Visual or interactive work
- Diagrams, animations, demos

---

## Pipeline Vision

The system will eventually:

1. Load all content from `data/content/`
2. Validate it against schemas
3. Extract metadata
4. Build indexes (tags, categories, recent activity)
5. Output structured data to `data/generated/`
6. Feed that data into the website layer

---

## Publishing Model

- Content is created as files (primarily Markdown)
- Each file represents a **single unit of progress**
- A commit = a visible update to the system
- The site reflects new content automatically after processing

---

## Design Principles

- **Separation of concerns**
  - Content, processing, and presentation are independent

- **Consistency over cleverness**
  - Schemas should be simple and predictable

- **Incremental growth**
  - Start small, expand over time

- **Human-readable content**
  - Raw content should always be understandable without tooling

- **System over pages**
  - The goal is not to build pages, but a structured knowledge system

---

## Current Phase

Phase 1:
- Repository structure
- Content model definition
- Initial schemas
- Sample content

Later phases:
- Processing pipeline implementation
- Automated data generation
- Website integration
- Deployment

---

## Long-Term Vision

A system where:

- Daily work becomes structured output
- Knowledge is accumulated and navigable
- Code, writing, and thinking coexist in one place
- The site reflects growth over time

This is not just a site.

It is a **map of thought, work, and progress**.
