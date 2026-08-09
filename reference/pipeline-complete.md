# Book Compiler Complete Pipeline (v3.0)

**Status:** Specification Complete  
**Version:** 3.0  
**Last Updated:** 2026-08-09

---

## Overview

Book Compiler transforms books into structured, actionable knowledge for LLMs.

```
BOOK (linear text)
  ↓
PASS 1: SURVEY (understand structure)
  ↓
PASS 2: RECONSTRUCT (extract 5-layer model)
  ↓
PASS 3: WRITE (markdown: 00-04, in book's native language)
  ↓
PASS 4: GENERATE LLM INSTRUCTIONS (05_llm_instructions.json, always English)
  ↓
OUTPUT (6-layer model ready for LLM consumption)
```

---

## Pass 1: Survey

**Goal:** Establish orientation before deep reading.

**Input:** Book (any format)

**Output:** 
- One-paragraph orientation
- Problem statement (1-2 sentences)
- Author's intent (1-2 sentences)
- Central questions (1-3 questions)
- Reading scope and depth decision

**Time:** 10-20 minutes for a book

### Steps

1. **Identify text type**
   - Non-fiction (exposition, argument, methodology)?
   - Narrative (story, memoir)?
   - Reference material?

2. **Skim structure**
   - Title, subtitle, front matter
   - Table of contents
   - Introduction
   - Conclusion
   - 2-3 chapter openings

3. **Identify problem**
   - What difficulty/gap prompted author?
   - Extract from intro, title, or infer

4. **Identify intent**
   - To convince?
   - To teach?
   - To explore?
   - To provide reference?

5. **Identify central questions**
   - What questions does author answer?
   - Usually in introduction or structure

6. **Determine reading goal**
   - Full reconstruction or overview?
   - Entire text or sections?
   - Time available?

**Example (Clean Architecture):**
- Problem: "Developers often treat architecture as separate from code, leading to unmaintainable systems"
- Intent: "Teach how architecture and implementation are one continuous process"
- Central Questions:
  - How does architecture affect software cost over time?
  - What makes architecture 'clean'?
  - How do paradigms constrain and enable change?

**See:** `reference/process.md` for detailed instructions

---

## Pass 2: Reconstruct

**Goal:** Extract 5-layer knowledge model from text.

**Input:** Book text (full or chapter)

**Output:** Graph of ~30-100 nodes organized by layer with metadata

**Time:** 2-8 hours depending on book length and complexity

### Five-Layer Model

| Layer | Node Types | Meaning | Driving Question |
|-------|-----------|---------|------------------|
| **PURPOSE** | Problem, Intent | Why does this book exist? | What gap does author address? |
| **QUESTIONS** | Question | What does author ask? | What inquiry organizes this text? |
| **IDEAS** | Concept, Claim, Principle | What intellectual content? | What ideas does author propose? |
| **REASONING** | Argument, Evidence, Example, Assumption | How are ideas supported? | Why should we accept these ideas? |
| **CONSEQUENCES** | Implication, Application, Limitation | What follows? | What can we do with this? |

### Node Types

**PURPOSE Layer:**
- **Problem:** The difficulty, gap, or challenge the book addresses
- **Intent:** What the author aims to accomplish

**QUESTIONS Layer:**
- **Question:** Central inquiries that organize the text

**IDEAS Layer:**
- **Concept:** A defined term or building block
- **Claim:** An assertion the author makes as true
- **Principle:** A general rule or law that applies broadly

**REASONING Layer:**
- **Argument:** Premises linked to conclusion
- **Evidence:** Data, observations, or quotations supporting a claim
- **Example:** Concrete instance illustrating a general idea
- **Assumption:** Unstated premise the argument depends on

**CONSEQUENCES Layer:**
- **Implication:** What logically follows from an idea
- **Application:** How to use or apply an idea
- **Limitation:** Conditions, scope, or exceptions

### Node Admission Rule

A node earns a place if:
- ✓ Necessary for understanding central ideas
- ✓ A dependency of other important nodes
- ✓ Represents significant original contribution
- ✓ Required for application or use
- ✓ Losing it would distort author's position

Drop a node if:
- ✗ Purely illustrative (use ILLUSTRATES relation instead)
- ✗ Detail of a detail
- ✗ Already covered by another node
- ✗ Not needed for understanding

### Relations

Nodes are connected by typed edges:
- **ANSWERS:** Q1 answered by idea X
- **SUPPORTS:** Evidence E supports claim C
- **DEPENDS_ON:** Idea B depends on concept A
- **EXPLAINS:** Argument explains claim
- **ILLUSTRATES:** Example illustrates principle
- **QUALIFIES:** Limitation qualifies principle scope
- **CONTRADICTS:** Idea X contradicts idea Y
- **LEADS_TO:** Principle P leads to implication I
- **PART_OF:** Node is part of broader concept

### Node Metadata

Every node includes:
- **id:** Unique identifier
- **type:** One of node types above
- **title:** Short label
- **statement:** Full statement
- **status:** explicit | inferred | interpretation | evaluation
- **importance:** core | important | supporting | detail
- **confidence:** high | medium | low
- **source:** Chapter/section/page reference
- **relations:** Typed edges to other nodes

### Pass 2 Completion Criteria

Pass 2 is complete when:
1. **Node Saturation:** Every node passes admission rule; nothing missed
2. **Relation Saturation:** All important connections identified
3. **Fixed-Point Convergence:** Re-read test discovers no new nodes
4. **Status Honesty:** Every node's status is accurate

**See:** `reference/process.md` and `reference/ontology.md` for full specifications

---

## Pass 3: Write

**Goal:** Transform node graph into human-readable markdown files.

**Input:** 5-layer graph with nodes and relations

**Output:** Five markdown files
- `00_purpose.md` — Problem and Intent
- `01_questions.md` — Central Questions
- `02_ideas.md` — Concepts, Claims, Principles
- `03_reasoning.md` — Arguments, Evidence, Examples, Assumptions
- `04_consequences.md` — Implications, Applications, Limitations

**Time:** 4-6 hours

### File Structure

Each file organizes nodes by layer:

```
# Layer Name (Purpose/Questions/Ideas/etc)

## Section 1: [Top concept or theme]

### Node 1: [Title]

[Statement]

**Type:** Principle  
**Status:** Explicit  
**Importance:** Core  
**Confidence:** High  
**Source:** Chapter 2

[Full content]

**Relations:**
- ANSWERS → question_1
- SUPPORTS → claim_3
- PART_OF → broader_principle

### Node 2: [Title]

...
```

### Guidelines

- **Preserve texture:** Don't compress or oversimplify
- **Include qualifications:** Scope, exceptions, conditions
- **Quote when needed:** Use evidence to support claims
- **Link relations:** Show how ideas depend on each other
- **Maintain fidelity:** Match author's actual argument

**See:** `reference/process.md` for detailed structure and examples

---

## Pass 4: Generate LLM Instructions JSON (LLM-Driven)

**Goal:** Transform the book's 5-layer markdown model into actionable JSON for LLM consumption, always in English.

**Input:** Five markdown files (00-04) in the book's native language (English, Russian, or other); any header convention.

**Output:** `05_llm_instructions.json` (v4.0 lean schema)

**Time:** Typically 30-60 minutes per book for an LLM to read, extract, and translate faithfully.

### What Pass 4 Does

An LLM executes this procedure:

1. **Reads** the book's own 00-04 markdown completely
2. **Identifies** every principle, argument, implication, and question by understanding the content (not regex-matching)
3. **Links** supporting content within the same book by meaning (content-matching, not tag-overlap heuristics)
4. **Translates** everything into faithful, complete English (if source is Russian or another language)
5. **Writes** JSON in the lean schema: metadata, system_instruction, quick_reference, principles[], decision_guide, faq, tags, version_info

**Lean schema fields:**
- `principle`: short statement
- `statement`: full explanation (untruncated)
- `supporting_arguments[]`: {id, name, claim, source}
- `related_implications[]`: {id, name, what_means, source}
- `related_questions[]`: {id, text, source}
- `tags`: book-specific tags
- `source` and `source_line`: every element is traceable

**Out of scope** (never invented, even if tempting):
- Practical metrics with formulas
- Quantified-cost scenarios
- Anti-patterns derived by inverting principles
- Context qualifiers not in the source
- Implementation roadmaps
- Checklists or step-by-step guidance not present in the source

**Validates:**
- No invented data (every field traces to source)
- No truncation of text
- All principles/arguments/implications/questions are real (count matches source)
- Source references are accurate and verifiable

### JSON v4.0 Structure (Lean Schema)

```json
{
  "metadata": {
    "title": "Book Title",
    "author": "Author Name",
    "publication": "Publication info",
    "book_name": "slug",
    "format_version": "4.0",
    "generated_at": "ISO 8601",
    "language": "English",
    "source_language": "English|Russian|...",
    "generation_pass": "Pass 4: Generate LLM Instructions (LLM-driven)"
  },

  "system_instruction": "Paste-in prompt for LLM",

  "quick_reference": {
    "book": "slug",
    "principles_count": N,
    "top_3_principles": ["Principle 1", "Principle 2", "Principle 3"],
    "questions_count": N,
    "arguments_count": N,
    "implications_count": N
  },

  "principles": [
    {
      "id": "principle_1",
      "number": 1,
      "principle": "Short statement",
      "statement": "Full explanation (untruncated)",
      "tags": ["#tag1", "#tag2"],
      "source": "02_ideas.md: PRINCIPLE 1",
      "source_line": 3,
      
      "supporting_arguments": [
        {
          "id": "arg_001",
          "name": "Argument Name",
          "claim": "Full claim (untruncated)",
          "source": "03_reasoning.md: Argument 1"
        }
      ],
      
      "related_implications": [
        {
          "id": "impl_001",
          "name": "Implication Name",
          "what_means": "Full explanation (untruncated)",
          "source": "04_consequences.md: Implication 1"
        }
      ],
      
      "related_questions": [
        {
          "id": "question_01",
          "text": "Full question text",
          "source": "01_questions.md: Question 1"
        }
      ]
    }
  ],

  "decision_guide": { "when_uncertain_ask": [...], "framework": "..." },

  "faq": [{ "question": "...", "answer": "...", "principle_refs": [...] }],

  "tags": ["#tag1", "#tag2"],

  "version_info": {
    "json_version": "4.0",
    "pass": "Pass 4: Generate LLM Instructions (LLM-driven)",
    "generation_date": "ISO 8601",
    "book": "slug",
    "principles": N,
    "arguments": N,
    "implications": N,
    "questions": N,
    "tags": N,
    "data_quality": "No invented data. All sourced from markdown."
  }
}
```

**See:** `reference/pass-4-json-generation.md` for detailed schema and procedure. ~~`reference/json-generation-spec.md` is superseded (documented the unimplemented rich v3.0 schema).~~

### Quality Gates (Must Pass)

- [ ] Zero invented metrics (all are formulas or traceable)
- [ ] Every scenario has quantified cost
- [ ] Every anti-pattern is grounded in reality
- [ ] `when_NOT_to_use` never empty (always has boundaries)
- [ ] All code examples are real language, not pseudo-code
- [ ] All context_qualifiers filled
- [ ] FAQ scenarios are real, not abstract
- [ ] Every principle has ≥1 practical_metric
- [ ] Every principle has ≥1 code_review_checklist item
- [ ] Every principle has ≥1 real scenario

---

## Pass 5: Validate

**Goal:** Ensure JSON meets quality standards.

**Input:** Generated JSON

**Output:** Validation report + approved JSON

**Time:** Automated (< 1 second)

### Validation Checks

1. **Structure:**
   - ✓ Metadata complete
   - ✓ Principles array non-empty
   - ✓ Each principle has required fields

2. **Content Quality:**
   - ✓ No invented metrics (formulas present)
   - ✓ Scenarios quantified (cost specified)
   - ✓ Anti-patterns realistic (no hand-waving)
   - ✓ Context qualifiers filled
   - ✓ Code examples are real language

3. **Completeness:**
   - ✓ Each principle has metrics
   - ✓ Each principle has checklist items
   - ✓ Each principle has scenarios
   - ✓ FAQ populated
   - ✓ Implementation roadmap present

4. **Consistency:**
   - ✓ IDs consistent (principle_1, principle_2, ...)
   - ✓ Tags consistent (no duplicate or conflicting tags)
   - ✓ Relations reference valid principles

### Validation Output

```
✓ Books/clean-architecture/05_llm_instructions.json
  • 6 principles
  • 18 metrics
  • 12 anti-patterns
  • 15 scenarios
  • All quality gates PASSED
```

---

## End-to-End Example: Clean Architecture

### Pass 1: Survey (10 min)
**Problem:** "Developers treat architecture as separate from code"  
**Intent:** "Teach how architecture = implementation"  
**Questions:** "What is architecture?", "How does it affect cost?"

### Pass 2: Reconstruct (6 hours)
**Extracted:** 45 nodes (6 principles, 8 claims, 12 examples, 8 evidence)  
**Identified:** 60+ relations (ANSWERS, SUPPORTS, ILLUSTRATES)  
**Status:** All nodes pass admission rule

### Pass 3: Write (4 hours)
**Output:** Five markdown files
- `00_purpose.md` — 3 KB (Problem, Intent)
- `01_questions.md` — 4 KB (12 central questions)
- `02_ideas.md` — 8 KB (6 principles, 12 concepts)
- `03_reasoning.md` — 15 KB (arguments, evidence, examples)
- `04_consequences.md` — 12 KB (applications, implications)

### Pass 4: Generate JSON (< 1 min)
**Specialized Generator:** CleanArchitectureGenerator  
**Input:** Five markdown files  
**Transformations:**
- 6 principles → full objects with metrics, checklists, scenarios
- Examples → anti-patterns (contrapositive)
- Applications → code review checklists
- Reasoning → practical metrics

**Output:** `05_llm_instructions.json`
- 6 principles (full detail)
- 18 practical metrics (3 per principle on average)
- 12 anti-patterns (2 per principle)
- 18 scenarios (3 per principle)
- 5 contexts (monolith, microservices, UI, startup, embedded)

### Pass 5: Validate (< 1 sec)
**Checks:** All 10 quality gates  
**Result:** ✓ PASSED

**Ready for:** Paste into Claude/GPT and use for code review

---

## Running the Pipeline

### Pass 1-3: Deep Reading (Manual + LLM-Guided)

Use the `book-compiler` skill in Claude:
1. Ask Claude to "read this book deeply" using SKILL.md as the procedure guide
2. Claude executes Pass 1 (survey), Pass 2 (reconstruct), Pass 3 (write) 
3. Output: five markdown files in `Books/<slug>/`

### Pass 4: Generate LLM Instructions JSON (LLM-Driven)

For each book, have an LLM follow `reference/pass-4-json-generation.md`:
1. Read `00_purpose.md` through `04_consequences.md` from the book
2. Identify principles, arguments, implications, questions by understanding (not regex)
3. Translate everything into complete, faithful English
4. Write `05_llm_instructions.json` matching the lean schema

**Output:** Each book now has a 6th file: `05_llm_instructions.json`

### Legacy (Deprecated)

> The previous approach used `scripts/universal_pass6_generator.py` (an English-only regex script). That script is superseded by the LLM-driven Pass 4 procedure above. Scripts are kept for historical reference only — do not use to regenerate 05_llm_instructions.json going forward. See `scripts/README.md` for why.

---

## File Locations

```
book-compiler/
├── Books/
│   ├── clean-architecture/
│   │   ├── 00_purpose.md
│   │   ├── 01_questions.md
│   │   ├── 02_ideas.md
│   │   ├── 03_reasoning.md
│   │   ├── 04_consequences.md
│   │   └── 05_llm_instructions.json ← Generated
│   ├── ideal-work/
│   │   ├── ...
│   │   └── 05_llm_instructions.json ← Generated
│   └── ... (more books)
│
├── reference/
│   ├── philosophy.md (Povarnin, Adler, Foster)
│   ├── ontology.md (Five-layer model, node types)
│   ├── process.md (Detailed Pass 1-3 instructions)
│   ├── specification.md (Problem statement, design)
│   ├── decisions.md (Design decisions)
│   ├── json-generation-spec.md (Pass 4 specification)
│   └── pipeline-complete.md (This file)
│
├── scripts/
│   ├── generate_llm_instructions.py (Core generator)
│   ├── generators_clean_architecture.py (Specialized)
│   └── build_all_llm_instructions.py (Orchestrator)
│
└── README.md (Project overview)
```

---

## Key Principles

### 1. Fidelity
- Reconstruct author's argument on its own terms
- Preserve qualifications and exceptions
- Don't compress; preserve nuance

### 2. Actionability (v3.0)
- No invented metrics (formulas or traced)
- Every scenario quantified
- Every anti-pattern grounded
- Real code examples (not pseudo-code)

### 3. Traceability
- Every node knows its source
- Claims traceable to evidence
- Relations clear and typed

### 4. Usability
- LLM can paste system_instruction immediately
- Developer can use checklist on PR
- Team lead can measure metrics

### 5. Maintainability
- Consistent structure across books
- Specialized generators for domain-specific content
- Clear validation gates

---

## Versioning

**v1.0:** Markdown layers (00-04) only, Russian language  
**v2.0:** Added JSON layer (05) with basic structure, English  
**v3.0 (Abandoned):** JSON designed for actionability (practical_metrics with formulas, quantified scenarios, anti-patterns, checklists, etc.). This rich schema was never implemented, as it risked inventing data not present in the source books, violating the project's "no invented data" principle.  
**v4.0 (Current):** Pass 4 becomes LLM-driven (replacing the English-only regex script). Layers 00-04 keep whatever language they are already in per book (no back-translation). Layer 05 is always English using the lean schema (principle/statement/reasoning/arguments/implications/questions) — genuinely populated via translation, not regex-extracted or fabricated.

---

## Next Steps

1. ✅ Specification complete (this document)
2. ⏳ Run generators on all 5 books
3. ⏳ Validate all outputs
4. ⏳ Create usage guides for each book
5. ⏳ Integrate with LLM workflows

---

**See Also:**
- `reference/process.md` — Detailed Pass 1-3 instructions
- `reference/ontology.md` — Node types and metadata
- `reference/json-generation-spec.md` — Pass 4 specification
- `SKILL.md` — Book Compiler skill documentation
- `LLM_USAGE_GUIDE.md` — How to use generated JSON with LLMs
