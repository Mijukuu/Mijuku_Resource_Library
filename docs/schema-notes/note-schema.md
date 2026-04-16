# Note Schema

## Overview

A **note** is the fundamental unit of knowledge in the Mijuku system.

Each note is:
- independently readable
- structured with metadata (frontmatter)
- stored as a Markdown file
- processed into a structured object by the pipeline

---

## File Location

All notes must exist within:
> data/content/notes


Subdirectories represent categories or domains:

- `programming/`
- `calculus/`
- `machine-learning/`
- etc.

---

## File Format

Each note must be a `.md` file with:

1. YAML frontmatter
2. Markdown body content

---

## Required Fields

These fields must exist in every note.

### `id`
- Type: `string`
- Description: Unique identifier for the note
- Rules:
  - lowercase
  - hyphen-separated
  - no spaces
- Example:

> autoencoder-suitcase

---

### `title`
- Type: `string`
- Description: Human-readable title
- Example:
> "Autoencoders: Compression, Loss, and the Suitcase"


---

### `date`
- Type: `string` (ISO format)
- Format:
> YYYY-MM-DD

- Description: Creation date of the note

---

### `category`
- Type: `string`
- Description: Primary domain of the note
- Examples:
- `programming`
- `calculus`
- `machine-learning`

---

### `tags`
- Type: `array<string>`
- Description: Keywords describing the note
- Rules:
- lowercase
- no spaces (use hyphens if needed)
- Example:

> [autoencoders, neural-networks, representation-learning]


---

### `summary`
- Type: `string`
- Description: Short description of the note (1–2 sentences)

---

### `status`
- Type: `string`
- Allowed values:
- `draft`
- `complete`
- Description: Indicates whether the note is finished or still evolving

---

## Optional Fields (Future Use)

These are not required yet but may be introduced later.

### `updated`
- Type: `string`
- Description: Last modified date

---

### `difficulty`
- Type: `string`
- Examples:
- `easy`
- `medium`
- `hard`

---

### `related`
- Type: `array<string>`
- Description: IDs of related notes

---

### `series`
- Type: `string`
- Description: Grouping notes into a sequence

---

## Body Content

The body of the note is written in Markdown.

**This structure is flexible and not enforced.**

Suggested structure:
---

## Example Note

```md
---
id: autoencoder-suitcase
title: "Autoencoders: Compression, Loss, and the Suitcase"
date: 2026-04-16
category: machine-learning
tags: [autoencoders, neural-networks, representation-learning]
summary: "Understanding autoencoders through compression and reconstruction."
status: draft
---

## The Idea

Autoencoders compress data into a smaller representation and reconstruct it.

## Insight

Learning is compression.

## Notes on Processing Note Schema:

## Processing Expectations

When processed, a note should be transformed into a structured object:

{
  "id": "autoencoder-suitcase",
  "title": "Autoencoders: Compression, Loss, and the Suitcase",
  "date": "2026-04-16",
  "category": "machine-learning",
  "tags": ["autoencoders", "neural-networks"],
  "summary": "Understanding autoencoders through compression and reconstruction.",
  "status": "draft",
  "content": "full markdown body"
}

## Design Principles

Consistency over flexibility
- Every note follows the same required structure

Human-first
- Notes must be easy to read without tooling

Machine-readable
- Metadata must be predictable for processing

Incremental evolution
- Schema may expand as the system grows
