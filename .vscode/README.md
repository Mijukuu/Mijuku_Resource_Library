# VS Code Configuration

This folder contains **project-specific editor configuration** for the Mijuku system.

The goal is to make content creation **fast, consistent, and structured**.

---

## Purpose

The `.vscode/` folder defines:

- Custom snippets
- Editor behavior for this project
- A guided workflow for creating content

This ensures that writing notes, projects, and other content follows a consistent format.

---

## Snippets

### `markdown.code-snippets`

Contains reusable templates for Markdown files.

#### Example: `mnote`

Typing: mnote and pressing `Tab` inserts a structured note template with:

- frontmatter (id, title, date, tags, etc.)
- basic section layout

This helps ensure that all notes:

- follow a consistent schema
- are easier to process later
- integrate cleanly into the system pipeline

---

## Philosophy

This is not just editor configuration.

It is part of the system design.

The goal is to turn:

> writing content

into:

> creating structured, consistent data

---

## Usage

1. Open any `.md` file inside the project
2. Type a snippet prefix (e.g. `mnote`)
3. Press `Tab`
4. Fill out fields using `Tab` navigation

---

## Notes

- These settings are **project-scoped**, not global
- They do not affect other projects
- They are committed intentionally to define workflow

---

## Future Additions

This folder may later include:

- Additional snippets (poems, projects, experiments)
- Editor settings specific to content creation
- Formatting rules
- Extensions recommendations

---

## Summary

This folder helps enforce:

- speed
- consistency
- structure

It is a small but important part of the overall system.

