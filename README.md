# 📚 Deep Reading System v4.0

Complete analysis of **11 technical and philosophy books** with **6+ layers per book**:

## Layers

| Layer | File | Purpose |
|-------|------|---------|
| 0 | `00_purpose.md` | Why this book matters — problem, goal, audience |
| 1 | `01_questions.md` | 12-15 central questions the book answers |
| 2 | `02_ideas.md` | 12-15 core principles and concepts |
| 3 | `03_reasoning.md` | Arguments and evidence supporting each idea |
| 4 | `04_consequences.md` | Practical applications and how to use each idea |
| 5 | `05_llm_instructions.json` | **NEW:** Machine-readable principles for LLM system prompts |

---

## Books (11 Total)

### Core Technical Books

1. **Clean Architecture** — Robert C. Martin  
   How to structure systems that minimize change cost  
   JSON: [05_llm_instructions.json](Books/clean-architecture/05_llm_instructions.json)

2. **Ideal Work / The Clean Coder** — Robert C. Martin  
   Professionalism as ethical commitment and long-term thinking  
   JSON: [05_llm_instructions.json](Books/ideal-work/05_llm_instructions.json)

3. **The Pragmatic Programmer** — Thomas & Hunt  
   Sustainable pace and managing technical risk  
   JSON: [05_llm_instructions.json](Books/pragmatic-programmer/05_llm_instructions.json)

4. **Parallel Programming Models** — R.E. Fedotov  
   Choosing the right concurrency model  
   JSON: [05_llm_instructions.json](Books/parallel-programming/05_llm_instructions.json)

5. **Code That Fits in Your Head** — Mark Seeman  
   Cognitive load as an architectural constraint  
   JSON: [05_llm_instructions.json](Books/code-fits-in-head/05_llm_instructions.json)

6. **Clean Code** — Robert C. Martin  
   Writing code that reads as prose  
   JSON: [05_llm_instructions.json](Books/martin-clean-code/05_llm_instructions.json)

7. **A Philosophy of Software Design** — John Ousterhout  
   Design thinking applied to systems and code  
   JSON: [05_llm_instructions.json](Books/philosophy-software-design/05_llm_instructions.json)

8. **Domain-Driven Design Patterns** — Various Authors  
   Modeling complex business domains  
   JSON: [05_llm_instructions.json](Books/domain-modeling-functional/05_llm_instructions.json)

9. **Concepts of Programming Languages** — Various  
   Language design principles and paradigms  
   JSON: [05_llm_instructions.json](Books/concepts-programming-languages/05_llm_instructions.json)

10. **The Architect Elevator** — Gregor Hohpe  
    Bridging technical and business architecture  
    JSON: [05_llm_instructions.json](Books/architect-elevator/05_llm_instructions.json)

11. **Refactoring: Improving the Design of Existing Code** — Martin Fowler (2nd Edition)  
    Behavior-preserving design improvement through systematic transformation  
    JSON: [05_llm_instructions.json](Books/refactoring/05_llm_instructions.json)

---

## What's New (v4.0)

### Layer 5: LLM Instructions (JSON)

Every book outputs a **machine-readable JSON file** with:
- ✅ Structured principles (statement, tags, source citations)
- ✅ Supporting arguments and evidence
- ✅ Related principles and questions
- ✅ Full traceability back to source material

**Use case:** Parse JSON programmatically or paste into LLM conversations.

### Layer 6: Agent Rules (NEW — Pass 5)

Each book can generate **agent-ready rules** with:
- **When to use** — Situations where this book's guidance applies
- **Primary bias to correct** — The misconception the book fixes
- **Decision rules** — General operating principles (7-10)
- **Trigger rules** — Conditional heuristics: "When X, then Y" (3-5)
- **Final checklist** — Verification questions (4-6)

**Example:** [Books/martin-clean-code/06_agent_rules.md](Books/martin-clean-code/06_agent_rules.md)

**Use case:** Paste into Claude/GPT instructions, or use in agent frameworks (MCP, Cursor rules, etc.).

**Traceability:** Every rule includes a companion [06_agent_rules.traceability.md](Books/martin-clean-code/06_agent_rules.traceability.md) proving each rule traces back to exact source material. No fabricated data.

### Example

```bash
# In Claude, at conversation start:
@paste content of Books/clean-architecture/05_llm_instructions.json

# Claude now understands Clean Architecture principles
# and applies them to any code review you ask
```

See [**LLM_USAGE_GUIDE.md**](LLM_USAGE_GUIDE.md) for full examples.

---

## Quick Start

### I want to understand a book

Choose a layer:
- **5 minutes?** Read `00_purpose.md`
- **30 minutes?** Read `02_ideas.md`
- **2 hours?** Read all layers in order (00 → 04)

### I want LLM to apply principles

```bash
# Open conversation with Claude
# At the start, paste:

cat Books/clean-architecture/05_llm_instructions.json

# Then ask Claude to review your code
```

### I want to combine multiple books

See [LLM_USAGE_GUIDE.md → Advanced section](LLM_USAGE_GUIDE.md#advanced-combining-multiple-books)

### I want to regenerate the JSON files

```bash
# Follow the LLM-driven Pass 4 procedure in reference/pass-4-json-generation.md
# For each book, an LLM reads 00_purpose.md through 04_consequences.md,
# identifies principles/arguments/implications/questions by understanding (not regex),
# translates everything to complete, faithful English,
# and writes 05_llm_instructions.json in the lean schema.

# Legacy (deprecated) script (English-only, cannot handle Russian headers):
# python scripts/universal_pass6_generator.py Books/
#
# ⚠️ Do NOT use the legacy script. Use the LLM-driven procedure instead.
```

---

## Architecture Decision

### Why 6 Layers?

Layers 0-4 serve **humans** reading books:
- Progressive deepening (summary → full understanding)
- Each layer is self-contained
- Can skip layers based on time/need

Layer 5 serves **LLMs**:
- Structured, parseable format (JSON)
- Always in English (regardless of the language of layers 0-4)
- Ready to paste into Claude/GPT conversations as system prompts
- No invented data — every principle/argument/implication traces to the source book

### Why Not Library/ Yet?

v1.0 focuses on **standalone books**. Each book is independent and useful on its own.

v2.0 (future): Optional cross-book network at `Library/` level (if you choose to build it).

---

## Files

```
Books/
├─ clean-architecture/
│  ├─ 00_purpose.md              (English)
│  ├─ 01_questions.md            (English)
│  ├─ 02_ideas.md                (English)
│  ├─ 03_reasoning.md            (English)
│  ├─ 04_consequences.md         (English)
│  ├─ 05_llm_instructions.json   (English, generated from 00-04)
│  └─ README.md
├─ ideal-work/ (00-04 English; 05 English)
├─ pragmatic-programmer/ (00-04 Russian; 05 English)
├─ parallel-programming/ (00-04 English; 05 English)
├─ code-fits-in-head/ (00-04 Russian; 05 English)
└─ martin-clean-code/ (00-04 Russian; 05 English)

reference/
├─ pass-4-json-generation.md     ← Authoritative spec for generating JSON layer
├─ pipeline-complete.md           ← Full pipeline documentation (Pass 1-4)
└─ ...

SKILL.md                           ← Deep reading skill (Pass 1-4)
LLM_USAGE_GUIDE.md                 ← How to use the JSON files
README.md                           ← This file
```

---

## Next Steps (v2.1+)

- [ ] Auto-update JSON when book layers change
- [ ] Cross-book concept mapping (optional Library/)
- [ ] Tags registry across all books
- [ ] Integration with Obsidian graph
- [ ] Version control for principles (detect changes between editions)

---

**Status:** ✅ v4.1 Complete (11 books analyzed; all Layer 5 JSON ready; Refactoring added)  
**Books:** Clean Architecture, Ideal Work, Pragmatic Programmer, Parallel Programming, Code That Fits in Head, Clean Code, Philosophy of Software Design, Domain-Driven Design, Concepts in Programming Languages, Architect Elevator, **Refactoring** ⭐  
**Last Updated:** 2026-08-09 (Session 11)  
**License:** Personal knowledge base

---

## How This Compares to Similar Projects

See [QUICKSTART_AUDIT_SUMMARY.md](QUICKSTART_AUDIT_SUMMARY.md) for a quick comparison with mattpocock/agent-rules-books.

Full audit available in [AUDIT_REPORT_2026-08-09.md](AUDIT_REPORT_2026-08-09.md).

## Versioning

- **v1.0:** Markdown layers (00-04) only, Russian language
- **v2.0:** Added JSON layer (05) with basic structure, English
- **v3.0 (Abandoned):** Designed rich JSON schema (metrics, scenarios, anti-patterns) — never implemented, risked inventing data
- **v4.0 (Current):** Pass 4 is LLM-driven; layers 00-04 stay in their original language (2 English, 4 Russian); layer 05 always English with lean schema (no fabricated data). Includes all 6 books (added martin-clean-code).
