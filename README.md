# book-compiler

A Claude skill for deep reading—not summarization.

**book-compiler** reconstructs books as knowledge systems. When you ask it to read a text, it identifies the author's problem, traces the reasoning, reconstructs the ideas and their connections, and produces a machine-readable model of the book's intellectual architecture.

The output is five structured markdown files containing nodes (concepts, claims, arguments, evidence, implications, etc.) with metadata (status, importance, source, relations).

## What It Does

- ✓ Reconstructs intellectual structure before summarizing
- ✓ Separates explicit statements from inference from interpretation
- ✓ Traces claims back to their sources
- ✓ Preserves nuance, scope, qualifications, and exceptions
- ✓ Models relationships between ideas
- ✓ Produces machine-readable knowledge files

## What It Does NOT Do

- ✗ Does not compress books into short summaries
- ✗ Does not treat chapter summaries as the main output
- ✗ Does not prioritize frequency over structural importance
- ✗ Does not present inferences as facts
- ✗ Does not treat examples as knowledge

## Installation & Use

This is a Claude skill. To use it:

1. **Via Claude Web (claude.ai):**
   - You need to set up a custom skill. Follow Anthropic's documentation on skill creation.
   - Copy the SKILL.md frontmatter and instructions into your skill configuration.

2. **Via Claude Code:**
   - Use `/book-compiler` to invoke (once registered).
   - Paste text or upload a document, then ask: "Read this book deeply" or "Reconstruct the ideas in this text."

3. **Manually:**
   - Copy the instructions from `SKILL.md` into a prompt to Claude.
   - Provide the text you want read.
   - Claude will generate the five output files as markdown.

## The Three-Pass Process

1. **Survey** — Identify the text type, central problem, questions, and structure.
2. **Reconstruct** — Read and extract the five-layer model: Purpose, Questions, Ideas, Reasoning, Consequences.
3. **Write** — Render as five markdown files with full metadata and relationships.

## Output Format

For each book analyzed, you get:
```
Books/<slug>/
├── 00_purpose.md       # Problem & Intent
├── 01_questions.md     # Central questions
├── 02_ideas.md         # Concepts, Claims, Principles
├── 03_reasoning.md     # Arguments, Evidence, Examples, Assumptions
└── 04_consequences.md  # Implications, Applications, Limitations
```

Each file contains nodes with:
- id, type, title, statement
- status (explicit/inferred/interpretation/evaluation)
- importance (core/important/supporting/detail)
- confidence (high/medium/low)
- source (chapter, location)
- relations (answers, supports, depends_on, leads_to, etc.)

## Philosophy & Design

- **philosophy.md** — The three-author foundation (Povarnin, Adler, Foster) and six core principles
- **ontology.md** — Complete specification of node types, relations, metadata contract, and output templates
- **design-log.md** — Full design process, rationale, and decision history

## Quick Start Example

Prompt:
```
Read this book deeply:
[paste opening chapter of a book]

Create the five output files.
```

Output:
```
Books/example-book/
├── 00_purpose.md
├── 01_questions.md
├── 02_ideas.md
├── 03_reasoning.md
└── 04_consequences.md
```

---

## Version

**v0 (Minimum Viable Reconstruction)**

- Core 5-layer model
- 13 node types
- 9 relation types
- Markdown file output
- No database, no external dependencies
- Designed for non-fiction; fiction support is future work

## Author & License

Created as a thoughtful alternative to summary-based reading.

See `reference/design-log.md` for the full development conversation and design rationale.
