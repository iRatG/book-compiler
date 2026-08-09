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
PASS 3: WRITE (markdown: 00-04)
  ↓
PASS 4: GENERATE JSON (05_llm_instructions.json v3.0)
  ↓
PASS 5: VALIDATE (quality gates)
  ↓
OUTPUT (ready for LLM consumption)
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

## Pass 4: Generate JSON (v3.0)

**Goal:** Transform markdown into actionable LLM instructions JSON.

**Input:** Five markdown files (00-04)

**Output:** `05_llm_instructions.json` (v3.0 format)

**Time:** Automated (< 1 minute)

### What Pass 4 Does

**Extracts:**
- Principles from `02_ideas.md`
- Reasoning from `03_reasoning.md`
- Applications from `04_consequences.md`

**Transforms Into:**
- Practical metrics (with formulas, not guesses)
- Code review checklists
- Real scenarios with quantified costs
- Anti-patterns (what looks right but is wrong)
- Context qualifiers (when to apply, when NOT)
- Implementation roadmaps
- Decision criteria

**Validates:**
- No invented metrics
- Every scenario has quantified cost
- Every anti-pattern is grounded in reality
- All code examples are real language (not pseudo-code)
- Context boundaries filled in
- Quality gates passed

### JSON v3.0 Structure

```json
{
  "metadata": { ... },
  "system_instruction": "Copy-paste prompt for LLM",
  "quick_reference": { ... },
  
  "principles": [
    {
      "id": "principle_1",
      "principle": "Short statement",
      "scope": "system/module/function",
      "severity": "CRITICAL/HIGH/MEDIUM",
      
      "statement": "Expanded statement",
      "reasoning": "Why this matters",
      
      "when_to_use": ["Specific situation 1", ...],
      "when_NOT_to_use": ["Honest boundary 1", ...],
      
      "key_rules": ["Actionable rule 1", ...],
      
      "practical_metrics": [
        {
          "name": "Metric name",
          "formula": "how to calculate",
          "how_to_measure": "where to get data",
          "good_value": "target",
          "bad_value": "warning sign",
          "example": { "scenario": "...", "calculation": "...", "interpretation": "..." }
        }
      ],
      
      "code_review_checklist": ["☐ Concrete check 1", ...],
      "code_review_warnings": ["⚠️ Red flag 1", ...],
      
      "scenarios": [
        {
          "scenario": "Real situation",
          "bad_approach": { "description": "...", "code": "...", "cost": "...", "problem": "..." },
          "good_approach": { "description": "...", "code": "...", "cost": "...", "why_works": "..." }
        }
      ],
      
      "anti_patterns": [
        {
          "name": "Anti-pattern name",
          "looks_right": "Why developers think it's correct",
          "actually_wrong": "The hidden problem",
          "cost": "Real impact",
          "solution": "How to avoid"
        }
      ],
      
      "context_qualifiers": {
        "for_monolith": "...",
        "for_microservices": "...",
        "for_ui_only": "...",
        "for_startup": "...",
        "for_embedded": "..."
      },
      
      "implementation_steps": [
        { "step": 1, "name": "...", "action": "...", "time": "..." }
      ],
      
      "decision_criteria": { "question": "...", "factors": [...], "if_yes_to_any": "..." },
      
      "common_misconceptions": [
        { "myth": "...", "truth": "...", "why_myth_exists": "...", "consequence": "..." }
      ],
      
      "how_to_verify": { "criterion_1": "...", "tool_suggestion": "..." },
      
      "related_principles": [
        { "id": "principle_X", "relationship": "Conflict/Support/Dependency", "explanation": "..." }
      ],
      
      "tags": ["#tag1", "#tag2"],
      "source_sections": ["02_ideas.md: ...", ...]
    }
  ],
  
  "decision_guide": { "when_uncertain_ask": [...] },
  
  "faq": [
    { "scenario": "Real situation", "question": "What's right?", "answer": "...", "principle_refs": [...] }
  ],
  
  "implementation_roadmap": {
    "phase_1": "Start with this",
    "phase_2": "Then this",
    "rationale": "Why this order"
  },
  
  "tags": ["#tag1", "#tag2"],
  
  "version_info": { ... }
}
```

**See:** `reference/json-generation-spec.md` for full specification

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

### Automated (Recommended)

```bash
# Generate JSON for all books
python scripts/build_all_llm_instructions.py Books/

# Generate JSON for single book
python scripts/build_all_llm_instructions.py Books/ --book clean-architecture

# Verbose output
python scripts/build_all_llm_instructions.py Books/ --verbose
```

### Manual (Educational)

```bash
# Step by step
cd Books/clean-architecture/

# Pass 1: Survey (manual, look at structure)
head -50 00_purpose.md

# Pass 2: Reconstruct (manual, understand text)
# (Read the book and create 02_ideas.md, etc)

# Pass 3: Write (manual or guided)
# (Organize nodes into markdown)

# Pass 4: Generate JSON (automated)
python ../../scripts/generate_llm_instructions.py .

# Pass 5: Validate (automated, included in Pass 4)
# (Validation report printed to stdout)
```

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
**v3.0:** JSON redesigned for actionability (no fake metrics, anti-patterns, metrics as formulas)

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
