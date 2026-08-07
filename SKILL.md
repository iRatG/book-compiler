---
name: book-compiler
description: Deep reading skill. Reconstructs books (not summarizes). Use when asked to "read this deeply", "build a book model", "what is this really saying", "reconstruct the ideas". Output is 5 structured markdown files modeling the book's intellectual architecture.
---

# BOOK COMPILER — Deep Reading Skill (v0)

## Manifesto

> This skill does not summarize books. It reads them. It determines why a book exists, identifies the questions it addresses, reconstructs its concepts, claims, principles and reasoning, preserves the distinction between the author's statements and the model's interpretations, traces important conclusions back to the source, and builds a compact but deep model of how the book works as an intellectual system. Only after this reconstruction is complete does the skill transform the model into a human-readable representation optimized for understanding, retention and application.

---

## Core Principles (Three Authors)

- **Povarnin**: Reading is purposeful. Know *why* and *how deep* before you start.
- **Adler**: Reading is active reconstruction of the author's intellectual structure.
- **Foster**: Meaning lives in layers. Attend to what is shown as well as what is said.

---

## The Three Passes

### Pass 1: Survey
- Identify text type (non-fiction, narrative, argument)
- Skim structure: TOC, intro, conclusion, chapter openings
- Identify the problem the book addresses
- Identify the author's intent and central question(s)
- Establish your reading goal and approach

**Output**: One-paragraph orientation + central problem, intent, and questions identified.

### Pass 2: Reconstruct
- Read the text (linear or requested excerpt)
- Extract nodes using the Five-Layer Model:
  1. **PURPOSE** — Problem, Intent
  2. **QUESTIONS** — Questions organizing the inquiry
  3. **IDEAS** — Concepts, Claims, Principles
  4. **REASONING** — Arguments, Evidence, Examples, Assumptions
  5. **CONSEQUENCES** — Implications, Applications, Limitations

- Tag every node with: status (explicit/inferred/interpretation/evaluation), importance (core/important/supporting/detail), confidence (high/medium/low), source (chapter/section/location)
- Identify relations between nodes (ANSWERS, SUPPORTS, DEPENDS_ON, EXPLAINS, ILLUSTRATES, QUALIFIES, CONTRADICTS, LEADS_TO, PART_OF)
- **Critical rule**: Never critique before reconstruction is complete.

**Output**: ~30-100 nodes organized by layer with full metadata.

### Pass 3: Write
- Organize nodes by layer into five markdown files:
  - `00_purpose.md` — Problem and Intent
  - `01_questions.md` — Questions
  - `02_ideas.md` — Concepts, Claims, Principles
  - `03_reasoning.md` — Arguments, Evidence, Examples, Assumptions
  - `04_consequences.md` — Implications, Applications, Limitations

- Use the node template (see `reference/ontology.md`)
- Include relations with explanatory notes
- Preserve qualifications, scope, exceptions

**Output**: Five markdown files in `Books/<slug>/`

---

## Hard Rules (Non-Negotiable)

1. **Do NOT optimize for compression.** Preserve the book's texture.
2. **Do NOT treat chapter summaries as canonical.** Reconstruct from the actual text.
3. **Do NOT equate frequency with importance.** Function in the argument matters.
4. **Do NOT present inferred statements as explicit author claims.** Tag status correctly.
5. **Do NOT treat examples as ideas.** Examples illustrate ideas; they are separate nodes.
6. **Do NOT use quotations as knowledge nodes.** Quotations are evidence supporting claims.

---

## Five-Layer Model (Quick Reference)

| Layer | Node Types | Question |
|-------|-----------|----------|
| **PURPOSE** | Problem, Intent | Why does this book exist? |
| **QUESTIONS** | Question | What does the author ask? |
| **IDEAS** | Concept, Claim, Principle | What ideas does the author introduce? |
| **REASONING** | Argument, Evidence, Example, Assumption | How are ideas supported? |
| **CONSEQUENCES** | Implication, Application, Limitation | What follows? |

---

## Node Metadata

Each node:
```yaml
id: [unique id]
type: [one of 13 types]
title: [short label]
statement: [1-2 sentence core claim]
status: explicit | inferred | interpretation | evaluation
importance: core | important | supporting | detail
confidence: high | medium | low
source:
  chapter: [chapter or section]
  location: [page/passage]
relations:
  - type: [relation type]
    target: [id of related node]
    note: [optional explanation]
```

---

## Output Structure

```
Books/<slug>/
├── 00_purpose.md
├── 01_questions.md
├── 02_ideas.md
├── 03_reasoning.md
└── 04_consequences.md
```

Each file is hierarchically organized, human-readable markdown with full node metadata and relations.

---

## Scope (v0)

**In scope**: Non-fiction (methodology, argument, exposition), narrative non-fiction, philosophy, social science.

**Out of scope**: Deep literary analysis (v1+), poetry, technical proofs, syntopical reading.

---

## References

- **reference/philosophy.md** — The three authors and six foundational principles
- **reference/ontology.md** — Complete specification of node types, relations, and templates
- **reference/process.md** — Detailed step-by-step instructions and examples
- **reference/design-log.md** — Full design conversation and rationale
