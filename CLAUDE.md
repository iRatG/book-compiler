# book-compiler: Deep Reading System

**Version:** 4.1  
**Status:** Production-ready  
**11 books analyzed** | **86+ files** | **6-8 layers each**

---

## What is this project?

A systematic deep-reading framework that reconstructs technical books into structured, actionable knowledge layers optimized for both human understanding and LLM consumption.

**Not a summary tool.** A reconstruction tool: understands why the book exists, what questions it answers, what principles it proposes, what evidence supports them, and how to apply each principle in real work.

---

## Core Files (What to Read First)

| File | Purpose | Read Time |
|------|---------|-----------|
| **README.md** | Project overview, 11 books, quick examples | 5 min |
| **SKILL.md** | Skill specification (Pass 1-5 methodology) | 10 min |
| **WORKFLOW.md** | How to add new books to the system | 5 min |
| **LLM_USAGE_GUIDE.md** | How to use JSON files in Claude/GPT | 10 min |

---

## Project Structure

```
book-compiler/
├── Books/                    ← 11 analyzed books (86+ files in git)
│   ├── clean-architecture/
│   ├── ideal-work/
│   ├── pragmatic-programmer/
│   ├── parallel-programming/
│   ├── code-fits-in-head/
│   ├── martin-clean-code/
│   ├── philosophy-software-design/
│   ├── domain-modeling-functional/
│   ├── concepts-programming-languages/
│   ├── architect-elevator/
│   └── refactoring/
│
├── reference/                ← Technical specs (in git)
│   ├── philosophy.md         (Three authors: Povarnin, Adler, Foster)
│   ├── ontology.md           (Node types, relations, metadata)
│   ├── process.md            (Pass 1-3 detailed instructions)
│   ├── pass-4-json-generation.md
│   ├── pass-5-agent-rules-generation.md
│   ├── pipeline-complete.md
│   ├── decisions.md
│   ├── design-log.md
│   └── specification.md
│
├── source/                   ← Input materials (NOT in git)
│   └── my-new-book/
│       ├── README.md         (Book metadata)
│       └── book.pdf          (Source material)
│
├── reports/                  ← Processing logs (NOT in git)
│   └── my-new-book-PASS-1-5.md
│
├── CLAUDE.md                 ← This file (developer guide)
├── SKILL.md                  ← Skill specification
├── README.md                 ← Project overview
├── WORKFLOW.md               ← How to add new books
├── LLM_USAGE_GUIDE.md        ← How to use JSON in LLM
├── .gitignore                ← Excludes source/ and reports/
└── .git/
```

---

## The Five Passes (Methodology)

Every book goes through 5 sequential passes:

### **Pass 1: Survey**
- Read text structure (TOC, intro, conclusion)
- Identify central problem and author's intent
- **Output:** Orientation paragraph (why read this book?)

### **Pass 2-3: Reconstruct & Write**
- Extract principles, questions, arguments, implications using Five-Layer Model
- Preserve original language (Russian, English, or other)
- Tag with epistemic status (explicit, inferred, interpretation, evaluation)
- **Output:** 5 markdown files
  - `00_purpose.md` — Problem and intent
  - `01_questions.md` — Central questions
  - `02_ideas.md` — Core principles
  - `03_reasoning.md` — Arguments and evidence
  - `04_consequences.md` — Practical applications

### **Pass 4: Generate LLM Instructions (JSON)**
- Transform 00-04 layers into machine-readable JSON
- **Always English** (regardless of source language)
- Each principle includes: supporting arguments, implications, related questions
- Full source citations (source + source_line)
- **Output:** `05_llm_instructions.json` (ready to paste into Claude/GPT)

### **Pass 5: Generate Agent Rules**
- Compress principles into operational decision rules + trigger rules + checklist
- Synthesize: multiple principles → one coherent rule
- Rigorous traceability: every rule → source principle → source material
- Two files:
  - `06_agent_rules.md` (clean, pastable)
  - `06_agent_rules.traceability.md` (audit trail)
- **Output:** Ready for agent frameworks (MCP, Cursor, Claude instructions)

---

## Key Architectural Decisions

### **Why 6 Layers?**

Layers 0-4 serve **humans** reading books (progressive depth):
- 5 min: Layer 0 (purpose)
- 30 min: Layer 2 (principles)
- 2 hours: Layers 0-4 (full understanding)

Layers 5-6 serve **LLMs** and agents:
- Structured JSON (parseable)
- Always English (universal compatibility)
- No invented data (only sourced from 00-04)

### **Why English for Layers 5-6?**

**Layer 5 (JSON):** LLM consumption requires consistency
- Enables programmatic processing (tag extraction, principle linking)
- Works with any LLM (Claude, GPT, others)
- Translation ≠ invention (every field traces to source)

**Layer 6 (Agent Rules):** Agent frameworks use English
- Better for cross-team guidance
- More reliable for instruction-following

**Layers 0-4 stay in original language** for native readers.

### **Why LLM-Driven Passes 4-5?**

Not scripts, not templates, but **LLM-driven procedures**:
- LLM reads 00-04 **completely** (not regex matching)
- Identifies principles by **understanding**, not keywords
- Links arguments/implications by **meaning**, not tags
- Translates **faithfully** (preserves intent)
- Never invents (every field traceable to source)

Each pass has a **formal procedure** (see reference/pass-4-json-generation.md and reference/pass-5-agent-rules-generation.md).

### **Why No Auto-Summary?**

❌ We do NOT:
- Truncate principle statements
- Invent examples beyond source
- Create metrics the book doesn't mention
- Compress to "essence" (lose nuance)

✅ We DO:
- Extract word-for-word or faithfully paraphrase
- Preserve scope and qualifications
- Trace every claim to source material
- Maintain intellectual integrity

---

## How to Use

### **As a reader (understand a book)**

Pick a depth:

```bash
# 5 minutes
cat Books/clean-architecture/00_purpose.md

# 30 minutes
cat Books/clean-architecture/02_ideas.md

# 2 hours
cat Books/clean-architecture/{00,01,02,03,04}_*.md
```

### **With LLM (apply principles)**

```bash
# Open Claude or GPT
# Paste this at the start:

cat Books/clean-architecture/05_llm_instructions.json

# Now ask Claude to review your code/design
# Claude will apply principles with source citations
```

### **For agent instructions**

```bash
# Option 1: Single book
cat Books/clean-architecture/06_agent_rules.md
# Paste into CLAUDE.md or agent framework

# Option 2: Multiple books
cat Books/clean-architecture/06_agent_rules.md
cat Books/refactoring/06_agent_rules.md
# Combine and paste
```

### **To add a new book**

See **WORKFLOW.md** for step-by-step instructions.

---

## Key Assumptions

1. **Fidelity over compression:** Preserve book texture; don't optimize for brevity
2. **Source-first:** Every claim must trace to source material
3. **Language flexibility:** Layers 0-4 preserve original language; layers 5-6 are English
4. **LLM-driven:** Passes 4-5 use LLM understanding, not scripts or templates
5. **No fabrication:** If field can't be populated from source, leave empty (not invented)
6. **Traceability:** Every rule/principle/argument includes source reference + line number

---

## For Developers Adding Features

### Before you add something, ask:

- ✅ **Does it help readers understand the book?** (Layers 0-4)
- ✅ **Does it help LLMs apply principles?** (Layer 5)
- ✅ **Does it help agents make decisions?** (Layer 6)
- ❌ **Does it invent data beyond source?** (Don't add)
- ❌ **Does it expand scope indefinitely?** (Don't add)

### Scope boundaries

**In scope:**
- Deep non-fiction (methodology, argument, exposition)
- Technical books (software design, engineering, architecture)
- Philosophy, social science (if they influence engineering thinking)

**Out of scope:**
- Literary analysis (novels, poetry)
- Technical proofs (formal math)
- Syntopical reading across unrelated domains

---

## Quality Criteria

### For Pass 1-3 (Markdown)

Each layer should:
- ✅ Preserve original language
- ✅ Reflect book structure accurately
- ✅ Tag every statement with epistemic status
- ✅ Include full reasoning/evidence
- ✅ Show relationships between ideas

### For Pass 4 (JSON)

Each principle should have:
- ✅ Complete statement (no truncation)
- ✅ Supporting arguments (from 03_reasoning.md)
- ✅ Related implications (from 04_consequences.md)
- ✅ Related questions (from 01_questions.md)
- ✅ Full source citations (source + source_line)

### For Pass 5 (Agent Rules)

Each rule should have:
- ✅ Clear decision rule or trigger rule
- ✅ Actionable conditions (testable)
- ✅ Fail signals (when to revise)
- ✅ Source references (traced to specific principle/argument/implication)
- ✅ Quality score (reflects actual confidence)

---

## Common Questions

### "Why not auto-generate from PDFs?"
LLMs can misread structure; human reconstruction ensures accuracy and fidelity.

### "Why two output files for Pass 5?"
- `06_agent_rules.md` is clean, pastable, production-ready
- `06_agent_rules.traceability.md` is audit trail proving every rule

Separation of concerns: agent uses one; auditor uses the other.

### "Can I use these in my own projects?"
Yes. Every principle is sourced and traceable. Cite the original book + the principle ID.

### "What if I disagree with a principle?"
The system reconstructs what the **book says**, not what we believe. Disagreement is valid — argue with the author, not the reconstruction.

### "How do I add a book?"
See **WORKFLOW.md**. Quick version:
1. Create `source/my-book/README.md` (metadata)
2. Run `/book-compiler my-book` (in Claude Code)
3. System does Pass 1-5 automatically
4. Result: `Books/my-book/00-06`

---

## Project Status

| Component | Status | Coverage |
|-----------|--------|----------|
| **Architecture & Design** | ✅ Complete | 100% |
| **Pass 1-3 (Markdown)** | ✅ Complete | 11 books |
| **Pass 4 (JSON)** | ✅ Complete | 11 books (6012 lines) |
| **Pass 5 (Agent Rules)** | ✅ Complete | 10 books (3654 lines); Refactoring in progress |
| **Documentation** | ✅ Complete | 5400+ lines |
| **LLM Integration** | ✅ Complete | Ready-to-use examples |
| **Workflow for new books** | ✅ Complete | Tested, automated |

---

## License & Use

Personal knowledge base. Use freely for your own projects. If you share or extend, cite the original books and maintain traceability.

---

## Questions or Issues?

Check:
1. **README.md** — Project overview
2. **WORKFLOW.md** — How to add books
3. **SKILL.md** — Technical specification
4. **reference/** — Detailed procedures and design decisions
5. **LLM_USAGE_GUIDE.md** — How to use JSON with LLMs

---

**Last updated:** 2026-08-09  
**Maintained by:** Claude Code (Anthropic)
