---
name: book-compiler
description: Deep reading skill. Reconstructs books (not summarizes). Use when asked to "read this deeply", "build a book model", "what is this really saying", "reconstruct the ideas". Output is 6 files: 5 structured markdown files modeling the book's intellectual architecture (in the book's native language), plus 1 English JSON file for LLM consumption.
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

## The Four Passes

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

### Pass 4: Generate LLM Instructions (05_llm_instructions.json)

**Goal:** Transform the reconstructed 5-layer model into actionable JSON for LLM consumption, always in English.

**Input:** The book's own `00_purpose.md` through `04_consequences.md` (in whatever language they are written; do not assume or require any specific header convention).

**Output:** One `05_llm_instructions.json` file in `Books/<slug>/`, always in English, regardless of the source language of layers 00-04.

**How it works:**
1. Read `00_purpose.md` through `04_consequences.md` completely.
2. Identify every principle, argument, implication, and question by *reading and understanding* the content — not by regex-matching a specific keyword or heading level.
   - For chapter-organized sources (principles embedded as list items inside chapter sections, like `martin-clean-code`), extract by semantic meaning: each `**C-NNN:**` item is one principle.
   - For header-per-principle sources, extract each principle heading the same way.
3. For each principle, locate its supporting arguments (in `03_reasoning.md`), related implications (in `04_consequences.md`), and related questions (in `01_questions.md`) by **content matching**, not by tag-overlap heuristics.
4. **Translate everything into faithful, complete English.** Translation is not invention: every field in the JSON must trace to a specific passage in the source text. Do not add metrics, scenarios, checklists, anti-patterns, or examples that are not present in the source.
5. Write `05_llm_instructions.json` matching the lean schema in `reference/pass-4-json-generation.md`.

**Rules:**
- No truncation of text (unlike the legacy regex generator, which limited claims to 150 chars and implications to 100 chars).
- Every element must include `source` and `source_line` so the LLM can verify against the original book.
- No invented data. If a field cannot be populated from the source, leave it empty rather than fabricate.

**See:** `reference/pass-4-json-generation.md` for the complete schema and detailed specification.

### Pass 5: Generate Agent Rules (06_agent_rules.md + 06_agent_rules.traceability.md)

**Goal:** Compress the book's 5-layer model into an operational, pastable rules file suitable for agent instruction, with rigorous traceability back to source material.

**Input:** 
- `00_purpose.md` through `04_consequences.md` (native language)
- Existing `05_llm_instructions.json` (reused for source citations)

**Output:** 
- `06_agent_rules.md` — Public, clean rules file (when to use / primary bias to correct / decision rules / trigger rules / final checklist)
- `06_agent_rules.traceability.md` — Audit trail (rule IDs R#/T#, source citations, section coverage review, intentionally-lost ledger)

**How it works:**
1. Read all five markdown layers and the 05 JSON completely.
2. Classify each principle/argument/implication/question as `decision-rule` (general bias), `trigger` (conditional "when X do Y"), `checklist-only` (verification), or `drop` (too narrow, duplicate, or out of scope).
3. Synthesize decision rules into imperative, compressed statements (not verbatim quotes). Merge duplicates.
4. Synthesize trigger rules from conditional items ("When X occurs, do Y").
5. Build final checklist by restating highest-leverage rules as self-check questions.
6. Assign rule IDs (R#, T#) and build traceability file with source citations, coverage review, and explicit ledger of intentionally-lost principles with reasons.

**Rules:**
- No rule exists without a source citation (R# or T# must cite a specific principle/argument/implication/question with line number).
- No fabricated data (metrics, scenarios, examples beyond source).
- All output is in English, regardless of source language (same rule as Pass 4).
- Traceability file must account for every principle in 02_ideas.md — either covered by a rule ID or marked "intentionally lost" with explicit reason.

**See:** `reference/pass-5-agent-rules-generation.md` for the complete procedure and detailed specification.

---

## Hard Rules (Non-Negotiable)

1. **Preserve the book's texture and intellectual architecture.** Do not optimize for compression.
2. **Reconstruct from the actual text, not chapter summaries.** Author fidelity is non-negotiable.
3. **Prioritize structural function in the argument, not frequency of mention.** Importance depends on role.
4. **Tag every statement with epistemic status** (explicit/inferred/interpretation/evaluation). Never present inference as fact.
5. **Separate examples from concepts with ILLUSTRATES relations.** Examples clarify ideas but are not ideas.
6. **Use quotations as Evidence supporting claims, not as knowledge nodes.** Distinguish sources from concepts.

---

## Five-Layer Model (Quick Reference)

See **reference/ontology.md** for the complete Five-Layer Model diagram and detailed specifications for all node types.

---

## Node Metadata

Each node includes: id, type, title, statement, status, importance, confidence, source, and relations. See **reference/ontology.md** for the complete node template and metadata definitions.

---

## Output Structure

Output is up to eight files in `Books/<slug>/`:

**Layers 00-04 (markdown):** `00_purpose.md`, `01_questions.md`, `02_ideas.md`, `03_reasoning.md`, `04_consequences.md` — always in the original language of the book (Russian, English, or other). See **reference/process.md** for detailed structure and examples.

**Layer 05 (JSON):** `05_llm_instructions.json` — always in English, regardless of the language of layers 00-04. Literal, non-synthesized extraction of principles, arguments, implications, and questions with full source citations. Ready to paste into an LLM conversation for expert guidance on applying the book's principles to real work. See **reference/pass-4-json-generation.md** for schema and specification.

**Layer 06 (Markdown + Traceability):** `06_agent_rules.md` + `06_agent_rules.traceability.md` — (optional; new as of Pass 5) Compressed, operational rules distilled from the book, with rigorous audit trail. Ready to paste directly into an LLM conversation as agent instructions (CLAUDE.md/AGENTS.md style). See **reference/pass-5-agent-rules-generation.md** for procedure and specification. Traceability file documents every rule's source and accounts for all principles covered or intentionally excluded.

---

## Scope (v0)

**In scope**: Non-fiction (methodology, argument, exposition), narrative non-fiction, philosophy, social science.

**Out of scope**: Deep literary analysis (v1+), poetry, technical proofs, syntopical reading.

---

## References

- **reference/philosophy.md** — The three authors (Povarnin, Adler, Foster) and six foundational principles that guide all work
- **reference/ontology.md** — Complete specification of node types, relations, templates, and metadata definitions
- **reference/process.md** — Detailed step-by-step instructions, examples, and verification checklists (Pass 1-3)
- **reference/pass-4-json-generation.md** — Specification for Pass 4 (LLM-driven JSON generation, lean schema)
- **reference/specification.md** — Formal specification with implementation decisions and testing criteria
- **reference/design-log.md** — Full design conversation and rationale (historical record)
- **reference/pipeline-complete.md** — Complete pipeline documentation (Pass 1-4) and versioning history
