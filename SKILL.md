---
name: book-compiler
description: Use when asked to deeply read, analyze, or reconstruct a book, article, or paper. Triggers on "read this deeply", "build a book model", "reconstruct the ideas", "what is this really saying", "deep reading". Does NOT summarize—reconstructs intellectual structure.
---

# Book Compiler Skill

This skill does not summarize books. **It reads them.**

When you ask it to read a text deeply, the skill:
1. Identifies why the text exists and what problem it addresses
2. Reconstructs the author's intellectual structure—the questions, ideas, reasoning, and conclusions
3. Preserves the distinction between what is explicitly stated, what is inferred, and what is interpretation
4. Traces important conclusions back to their source
5. Transforms the reconstruction into a knowledge model optimized for understanding, memory, and application

## The Three-Pass Process

### Pass 1: Survey
Before detailed reading:
- Identify the text type (non-fiction, narrative, argument, exploration)
- Identify the central problem the author addresses and the author's intent
- Skim structure: table of contents, introduction, conclusion, chapter openings
- Identify the central question(s) that organize the text
- Determine your reading goal—what depth is needed?

Do not read linearly yet. Build an orientation.

### Pass 2: Reconstruct
Read the text (or the section you're asked to analyze) and populate the Five-Layer Model:

1. **PURPOSE** — Problem and Intent. Why was this written?
2. **QUESTIONS** — Central and subsidiary questions organizing the inquiry
3. **IDEAS** — Concepts, claims, principles the author introduces
4. **REASONING** — How ideas are supported: arguments, evidence, examples, assumptions
5. **CONSEQUENCES** — Implications, applications, limitations

For each node:
- Write a clear, concise statement
- Tag its status: explicit (directly stated), inferred (clearly implied), interpretation (requires judgment), or evaluation (your assessment)
- Record its importance: core (essential), important (significant), supporting (reinforces), or detail (illustrative)
- Note the source: chapter, section, passage, page
- Identify relations to other nodes (supports, answers, depends_on, leads_to, contradicts, etc.)

**Critical rule:** Never critique before reconstruction is complete. Do not evaluate the author's argument until you understand it fully.

### Pass 3: Write
Render the reconstructed model as five markdown files:
- `00_purpose.md` — Problem and Intent
- `01_questions.md` — Questions
- `02_ideas.md` — Concepts, Claims, Principles
- `03_reasoning.md` — Arguments, Evidence, Examples, Assumptions
- `04_consequences.md` — Implications, Applications, Limitations

Organize each file hierarchically. Include node metadata (status, importance, confidence, source). Preserve qualifications, exceptions, and scope. Follow the templates in `reference/ontology.md`.

## Hard Rules (Non-Negotiable)

- **Do NOT optimize primarily for compression.** Preserve the full structure.
- **Do NOT treat chapter summaries as the canonical representation.** Go deeper.
- **Do NOT equate frequency of mention with importance.** Some ideas are structurally central even if mentioned once.
- **Do NOT present inferred statements as explicit author claims.** Tag status correctly.
- **Do NOT treat examples as ideas.** Examples illustrate; they do not constitute knowledge nodes.
- **Do NOT use quotations as knowledge nodes.** Quotations are evidence that support claims, not claims themselves.

## Output Structure

Create a folder `Books/<slug>/` where `<slug>` is a short identifier (e.g., `gogol-dead-souls`, `adler-how-to-read`).

Inside, place the five files as described above. Each file contains nodes with their metadata and relationships.

The output is a *machine-readable, human-interpretable knowledge structure* of the book. It is not a summary. It is not an outline. It is a reconstruction of the author's intellectual system.

## Philosophy

See `reference/philosophy.md` for the three-author foundation (Povarnin, Adler, Foster) and the six core principles.

See `reference/ontology.md` for the complete node types, relation definitions, and metadata contract.

See `reference/design-log.md` for the full design process and rationale.
