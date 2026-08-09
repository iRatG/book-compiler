# JSON Generation Specification (v3.0) — SUPERSEDED

> **⚠️ Superseded.** This specification describes the unimplemented "v3.0 rich schema" (practical_metrics with formulas, quantified scenarios, anti-patterns, code review checklists, etc.), which risks inventing data not present in source books.
> 
> **Current procedure:** See `reference/pass-4-json-generation.md` for the authoritative, implemented Pass 4 specification (LLM-driven, lean schema, no invented data).
> 
> This file is kept for historical reference and inspiration for future, well-sourced schema extensions.

**Status:** In Development  
**Purpose:** Transform 5-layer markdown model into actionable LLM instructions JSON  
**Input:** `00_purpose.md` through `04_consequences.md`  
**Output:** `05_llm_instructions.json`

---

## Overview

JSON Generation is **Pass 4** in the book-compiler pipeline. It transforms the reconstructed 5-layer model (in markdown) into a machine-readable format optimized for LLM decision-making and code review.

**Critical difference from v2.0:** No fake metrics, no obvious stories, no philosophical water. Only actionable content.

---

## Design Principles for v3.0

### 1. **Actionability Over Philosophy**
- ❌ "Separation of concerns is important"
- ✅ Code review checklist: "☐ Does this change touch only 1-3 files?"

### 2. **Metrics Are Measured, Not Invented**
- ❌ "v1: 2 weeks, v2: 4 weeks, v3: 8 weeks" (guessed)
- ✅ "Formula: hours_spent / features_delivered. Track per release."

### 3. **Anti-Patterns Over Misconceptions**
- ❌ "myth: architecture means faster code"
- ✅ "Anti-pattern: Premature optimization (looks right, actually wrong)"

### 4. **Real Scenarios With Cost**
- ❌ "A company had tight coupling"
- ✅ "Scenario: Change discount logic. Bad: 4 hours (touches DB, email, analytics). Good: 30 min (isolated function)."

### 5. **Context Boundaries**
- Show when to apply
- Show when NOT to apply
- Show what happens if you ignore

### 6. **Decision Criteria**
- Explicit decision trees
- When to choose option A vs B
- What trade-off you're making

---

## Principle Structure (Per Principle in Ideas Layer)

Each principle from `02_ideas.md` becomes:

```json
{
  "id": "principle_N",
  "principle": "Short, actionable statement",
  "scope": "system/module/function",
  "severity": "CRITICAL/HIGH/MEDIUM",

  // === UNDERSTANDING ===
  "statement": "Expanded but concise statement",
  "reasoning": "Why this matters in practice (1-2 sentences max)",

  // === APPLICATION BOUNDARIES ===
  "when_to_use": [
    "Specific situation 1",
    "Specific situation 2"
  ],
  
  "when_NOT_to_use": [
    "One-off scripts or throwaway prototypes",
    "Hard real-time systems where performance > changeability",
    "Context with constraints that contradict this principle"
  ],

  // === RULES ===
  "key_rules": [
    "Rule 1: Actionable, starts with verb",
    "Rule 2: Measurable outcome",
    "Rule 3: Clear consequence"
  ],

  // === PRACTICAL METRICS ===
  "practical_metrics": [
    {
      "name": "Metric name (e.g., Cost per Feature)",
      "formula": "how to calculate it",
      "how_to_measure": "where to get data",
      "good_value": "target or range",
      "bad_value": "warning signs",
      "example": {
        "scenario": "Real example",
        "calculation": "5 features, 100 hours = 20h/feature",
        "interpretation": "Good" or "Bad"
      }
    }
  ],

  // === CODE REVIEW ===
  "code_review_checklist": [
    "☐ Concrete check 1",
    "☐ Concrete check 2",
    "☐ Concrete check 3"
  ],

  "code_review_warnings": [
    "⚠️ Red flag 1 (e.g., File > 500 LOC)",
    "⚠️ Red flag 2 (e.g., God object pattern)"
  ],

  // === REAL SCENARIOS ===
  "scenarios": [
    {
      "scenario": "Specific real situation (e.g., 'Change discount logic')",
      "bad_approach": {
        "description": "What you might do wrong",
        "code": "Example code (not pseudo-code)",
        "cost": "Quantified: 4 hours, touches 8 files, etc",
        "problem": "Why it fails"
      },
      "good_approach": {
        "description": "What to do instead",
        "code": "Example code",
        "cost": "Quantified: 30 minutes, touches 1-2 files",
        "why_works": "The mechanism"
      }
    }
  ],

  // === ANTI-PATTERNS ===
  "anti_patterns": [
    {
      "name": "Name of anti-pattern",
      "looks_right": "Why developers think it's correct",
      "actually_wrong": "The hidden problem",
      "cost": "Real impact (performance, maintainability, etc)",
      "solution": "How to avoid it"
    }
  ],

  // === CONTEXT & CONSTRAINTS ===
  "context_qualifiers": {
    "for_monolith": "How this applies to monolithic architecture",
    "for_microservices": "Adjustments or caveats",
    "for_ui_only": "Specifics for frontend/UI code",
    "for_startup": "Startup-specific guidance",
    "for_embedded": "Embedded systems constraints"
  },

  // === IMPLEMENTATION ===
  "implementation_steps": [
    {
      "step": 1,
      "name": "Step name",
      "action": "What to do",
      "time": "Estimated effort (e.g., 1-2 sprints)"
    }
  ],

  // === DECISIONS ===
  "decision_criteria": {
    "question": "When to apply this?",
    "factors": [
      "Factor A (yes → apply)",
      "Factor B (yes → apply)"
    ],
    "if_yes_to_any": "Action or recommendation"
  },

  // === COMMON MISTAKES (Reframed) ===
  "common_misconceptions": [
    {
      "myth": "Developers often think...",
      "truth": "Actually...",
      "why_myth_exists": "Explanation",
      "consequence": "What happens if you believe the myth"
    }
  ],

  // === MEASUREMENT ===
  "how_to_verify": {
    "criterion_1": "Specific way to measure if this is working",
    "criterion_2": "Another measurement approach",
    "tool_suggestion": "Tools that help (e.g., code metrics, monitoring, etc)"
  },

  // === RELATIONSHIPS ===
  "related_principles": [
    {
      "id": "principle_X",
      "relationship": "Conflict/Support/Dependency",
      "explanation": "How they interact"
    }
  ],

  // === METADATA ===
  "tags": ["#tag1", "#tag2"],
  "source_sections": [
    "02_ideas.md: Principle section reference"
  ]
}
```

---

## Document-Level Structure

```json
{
  "metadata": {
    "title": "Book Title (from 00_purpose.md)",
    "author": "Author (from metadata)",
    "format_version": "3.0",
    "generated_at": "ISO timestamp",
    "language": "English"
  },

  "system_instruction": "Prompt-ready text for pasting into LLM conversation",

  "quick_reference": {
    "core_goal": "One sentence from 00_purpose.md Intent",
    "top_3_principles": [
      "Most critical 3 from principles array"
    ]
  },

  "principles": [
    // Array of principle objects (per spec above)
  ],

  "decision_guide": {
    "when_uncertain_ask": [
      "Key questions from 00_purpose.md or 01_questions.md"
    ]
  },

  "faq": [
    {
      "scenario": "Real situation (not abstract question)",
      "question": "What's the right approach here?",
      "answer": "Actionable answer with principle references",
      "principle_refs": ["principle_1", "principle_2"]
    }
  ],

  "implementation_roadmap": {
    "phase_1": "Start with this principle",
    "phase_2": "Then this one",
    "phase_3": "Then this",
    "rationale": "Why this order"
  },

  "tags": ["#tag1", "#tag2"],

  "version_info": {
    "book_edition": "Original book edition",
    "json_version": "3.0",
    "generation_date": "Date created",
    "source": "Generated from 5-layer markdown model"
  }
}
```

---

## Generation Algorithm

```
FOR EACH principle in 02_ideas.md:
  1. Extract: id, statement, scope, severity
  2. From 03_reasoning.md: reasoning, examples, evidence
  3. From 04_consequences.md: applications, implications
  4. GENERATE:
     - Actionable key_rules (from statements)
     - practical_metrics (derive from 03/04 or infer)
     - code_review_checklist (derive from key_rules)
     - scenarios (from examples, expand with cost)
     - anti_patterns (infer from contrapositive of principle)
     - context_qualifiers (infer from scope in 03/04)
     - common_misconceptions (from reasoning clarifications)
  5. VALIDATE:
     - No invented metrics (must trace to source or be formula)
     - Each scenario has quantified cost
     - Each anti-pattern is realistic
     - No water (philosophy without action)

AGGREGATE:
  - Extract system_instruction from 00_purpose.md intent
  - Extract FAQ from common applications in 04_consequences.md
  - Create implementation_roadmap based on principle dependencies
```

---

## Quality Gates

**Before output is valid:**

- [ ] Zero invented metrics (all metrics are formulas or traceable)
- [ ] Every scenario has quantified cost (time, files changed, etc)
- [ ] Every anti-pattern is grounded in real developer behavior
- [ ] when_NOT_to_use is never empty (always has boundaries)
- [ ] All code examples are real language (JavaScript, Python, etc), not pseudo-code
- [ ] All context_qualifiers are filled (or marked "N/A")
- [ ] FAQ scenarios are real situations, not abstract questions
- [ ] Every principle has at least 1 practical_metric
- [ ] Every principle has at least 1 code_review checklist item
- [ ] Every principle has at least 1 real scenario

---

## Example: Principle 2 (from Clean Architecture)

**Input:** 02_ideas.md, 03_reasoning.md, 04_consequences.md extracts

**Output:** principle_2 JSON object (see scratchpad/principle_2_refactored.json for full example)

**Key transformations:**
- "Minimize human effort" → practical_metrics (Cost per Feature, Blast Radius, Test Feedback Loop)
- "Architecture enables change" → code_review_checklist (5 specific checks)
- General examples → real_scenarios with quantified costs
- Philosophical discussions → anti_patterns with "looks right / actually wrong" structure

---

## Files

- `reference/json-generation-spec.md` — This file
- `scripts/generate_llm_instructions.py` — Generator implementation
- `Books/<name>/05_llm_instructions.json` — Output

---

## Not In Scope (v3.0)

- Translating to languages other than English
- Extracting from books without proper 5-layer markdown
- Automated metrics collection (user must provide via spec)
- Real-time validation of code examples

---

## Success Criteria

Generated JSON is successful when:

1. ✅ An LLM can paste the system_instruction and immediately apply principles to code
2. ✅ A developer can use code_review_checklist to review PRs
3. ✅ A team lead can use practical_metrics to measure if architecture is working
4. ✅ Anyone can point to a scenario and think "this is literally what we do"
5. ✅ Zero "water" — every section is actionable or reference-able
