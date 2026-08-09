# 📚 Deep Reading System v2.0

Complete analysis of 5 technical books with **6 layers per book**:

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

## Books

### 1. Clean Architecture ← [Learn More](Books/clean-architecture/)
**Robert C. Martin** — How to structure systems that minimize change cost

- 15 principles extracted
- Tags: #architecture, #cost-of-change, #paradigms
- JSON: [05_llm_instructions.json](Books/clean-architecture/05_llm_instructions.json)

### 2. Ideal Work / The Clean Coder ← [Learn More](Books/ideal-work/)
**Robert C. Martin** — Professionalism as ethical commitment and long-term thinking

- 15 principles extracted
- Tags: #craftsmanship, #tdd, #professionalism, #ethics
- JSON: [05_llm_instructions.json](Books/ideal-work/05_llm_instructions.json)

### 3. The Pragmatic Programmer ← [Learn More](Books/pragmatic-programmer/)
**Thomas & Hunt** — Sustainable pace and managing technical risk

- 5 principles extracted
- Tags: #dry, #automation, #risk-management
- JSON: [05_llm_instructions.json](Books/pragmatic-programmer/05_llm_instructions.json)

### 4. Parallel Programming Models ← [Learn More](Books/parallel-programming/)
**R.E. Fedotov** — Choosing the right concurrency model

- 15 principles extracted
- Tags: #concurrency, #synchronization, #performance
- JSON: [05_llm_instructions.json](Books/parallel-programming/05_llm_instructions.json)

### 5. Code That Fits in Your Head ← [Learn More](Books/code-fits-in-head/)
**Mark Seeman** — Cognitive load as an architectural constraint

- 12 principles extracted
- Tags: #readability, #cognitive-load, #simplicity
- JSON: [05_llm_instructions.json](Books/code-fits-in-head/05_llm_instructions.json)

---

## What's New (v2.0)

### Layer 5: LLM Instructions

Every book now outputs a **machine-readable JSON file** with:
- ✅ Structured principles (title, reasoning, tags, severity)
- ✅ System instructions for Claude/GPT/other LLMs
- ✅ FAQ for common questions
- ✅ Cross-references between principles

**Use case:** Load JSON into your LLM conversations to apply book principles automatically.

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
# Regenerate all llm_instructions.json files
python generate-llm-instructions.py Books/clean-architecture
python generate-llm-instructions.py Books/ideal-work
# ... etc
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
- No prose ambiguity
- Ready for system prompts
- Optimized for Claude/GPT comprehension

### Why Not Library/ Yet?

v1.0 focuses on **standalone books**. Each book is independent and useful on its own.

v2.0 (future): Optional cross-book network at `Library/` level (if you choose to build it).

---

## Files

```
Books/
├─ clean-architecture/
│  ├─ 00_purpose.md
│  ├─ 01_questions.md
│  ├─ 02_ideas.md
│  ├─ 03_reasoning.md
│  ├─ 04_consequences.md
│  ├─ 05_llm_instructions.json  ← NEW
│  └─ README.md
├─ ideal-work/ (same structure)
├─ pragmatic-programmer/ (same structure)
├─ parallel-programming/ (same structure)
└─ code-fits-in-head/ (same structure)

generate-llm-instructions.py    ← Script to generate JSON layer
LLM_USAGE_GUIDE.md              ← How to use the JSON files
README.md                        ← This file
```

---

## Next Steps (v2.1+)

- [ ] Auto-update JSON when book layers change
- [ ] Cross-book concept mapping (optional Library/)
- [ ] Tags registry across all books
- [ ] Integration with Obsidian graph
- [ ] Version control for principles (detect changes between editions)

---

**Status:** ✅ v2.0 Complete  
**Last Updated:** 2026-08-09  
**License:** Personal knowledge base
