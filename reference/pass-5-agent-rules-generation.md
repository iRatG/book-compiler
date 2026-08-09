# Pass 5: Generate Agent Rules (LLM-Driven Procedure)

**Purpose:** Transform a book's 5-layer markdown model into an operational, pastable rules file (`APPLY <Book>` — When to use / Primary bias to correct / Decision rules / Trigger rules / Final checklist) plus a companion traceability document mapping every rule back to exact source sections.

**Input:**
- `00_purpose.md` through `04_consequences.md` (in the book's native language; any header structure)
- Existing `05_llm_instructions.json` (from Pass 4 — reused as source citations rather than re-deriving them from markdown)

**Output:**
- `06_agent_rules.md` — Public, clean rules file (no rule IDs; directly pastable as agent instructions)
- `06_agent_rules.traceability.md` — Audit trail (rule IDs R#/T#, source citations, section coverage review, intentionally-lost ledger)

**Key Principle:** Compress the book's content into imperative decision/trigger rules suitable for immediate agent use, while maintaining rigorous traceability to source material. No rule exists without a citation back to a specific principle/argument/implication/question from the book.

---

## PROCEDURE (for the LLM executing Pass 5)

### 1. Read all source material fully

Load and read completely:
- All five markdown layers (`00_purpose.md` through `04_consequences.md`)
- Existing `05_llm_instructions.json` (to reuse cited sections and references)

Understand:
- The book's central problem and intent (from `00_purpose.md`)
- The questions it addresses (from `01_questions.md`)
- The principles/ideas it proposes (from `02_ideas.md`)
- The arguments and evidence supporting each (from `03_reasoning.md`)
- The implications and applications (from `04_consequences.md`)

### 2. Classify each principle/argument/implication/question by role

As you read, assign every item in the source layers to one of four categories:

**`decision-rule`** — General operating principle or bias that applies broadly
- Examples: "Functions should be small", "Write for the next reader", "Preserve behavior while improving"
- These become the main imperative rules in the output

**`trigger`** — Conditional heuristic: "When X occurs, do Y"
- Examples: "When a function does both X and Y, separate them", "When a comment explains flow, simplify first"
- These become trigger rules (one-liners starting with "When...")

**`checklist-only`** — Verification question or self-check item that restates a decision/trigger rule
- Examples: "Did I check the coverage?", "Are names clear?"
- These go into the final checklist but don't create new guidance

**`drop`** — Too narrow, context-specific, or duplicate of another rule
- Examples: Specific Java patterns when the book spans multiple languages; detailed metrics that are context-bound
- These are explicitly noted in the traceability file as intentionally lost (with reason)

**Rules for classification:**
- One principle may appear in multiple classifications (e.g., one principle as both a decision rule AND a trigger rule)
- When in doubt, classify as `decision-rule` — let comprehensive coverage be the goal
- `drop` only when the item genuinely duplicates another or adds no guidance beyond context-specific details

### 3. Draft "When to use" and "Primary bias to correct"

From `00_purpose.md` and `01_questions.md`:

**When to use** (1–3 sentences):
- Describe the situations/contexts where this book's guidance applies best
- Example: "Use when prioritizing readability, local reasoning, and maintainable code structure during typical development and code review."

**Primary bias to correct** (one sentence):
- State the single misconception the book corrects
- Example: "The misconception that working code is automatically clean code."

### 4. Draft decision rules

Read through all source material and list every `decision-rule`-classified item. For each:

1. **Reword into imperative English** — not a verbatim quote, but a clear action/principle
   - Source: "Функция должна делать одно и делать его хорошо" → Rule: "Keep functions small, focused, and at a single abstraction level"
   - Source: "Write for the next reader" → Rule: "Write for local reasoning so readers don't reconstruct hidden state"

2. **Merge duplicates** — if two source principles say the same thing, combine them into one rule

3. **Preserve book-specific vocabulary and perspective** — e.g., if the book uses "Boy Scout Rule", keep that term

4. **Do NOT fabricate** — the rule must trace back to content in the source. If you can't find evidence, mark it as `drop`.

Format the output as a bullet list:
```
## Decision rules
- <Imperative rule 1>
- <Imperative rule 2>
- ...
```

### 5. Draft trigger rules

Read through all source material and list every `trigger`-classified item. Format as "When X, do Y" bullets:

```
## Trigger rules
- When <situation>, <action>.
- When <situation>, <action>.
- ...
```

Examples (from the reference repo's clean-code):
- "When a function mixes setup, validation, computation, and side effects, split the phases."
- "When a comment explains control flow, simplify names or structure before keeping the comment."

### 6. Draft final checklist

From the decision and trigger rules, extract the highest-leverage verification questions that an agent can self-check. Restate them as questions that naturally flow from the rules:

```
## Final checklist
- <Verification question>?
- <Verification question>?
- ...
```

**Important:** The checklist does **not** introduce new rules. It restates the decision/trigger rules as self-check questions. Example:

- Rule: "Write for local reasoning" → Checklist: "Can a reader follow the change locally?"
- Rule: "When mutation occurs, make it explicit" → Checklist: "Is mutation explicit?"

### 7. Write the companion traceability file

Create `06_agent_rules.traceability.md` with these sections:

#### Section 7a: Compression Decisions (narrative)

Explain the process: which items were classified as `decision-rule` vs. `trigger` vs. `drop`, and why. This mirrors the reference repo's "Compression decisions" section. Example narrative structure:

```
- `decision-rule` items retain book-thesis principles and micro-decisions agents commonly miss
- Duplicates are merged into single rules
- Context-specific details are compressed into trigger rules
- Detailed code patterns, unless they shift decision-making, are intentionally dropped
```

#### Section 7b: Decision Rules Mapping

Assign rule IDs (`R1`, `R2`, etc.) in file order. For each rule:

```
**R1** <Rule text verbatim from 06_agent_rules.md>
Source: <reference to principle(s) in 02_ideas.md with line numbers>
Citations: <Any supporting_arguments from 05_llm_instructions.json or specific passages from 03_reasoning.md>
```

Example (Clean Code book):
```
**R1** Preserve behavior, write for the next reader, and leave touched code cleaner within scope.
Source: 02_ideas.md C-001, C-002, C-003 (lines 7-9); 00_purpose.md (lines 20-28)
Citations: Arg-001 (03_reasoning.md: "Плохой код замедляет разработку экспоненциально")
```

#### Section 7c: Trigger Rules Mapping

Assign rule IDs (`T1`, `T2`, etc.) in file order. For each trigger:

```
**T1** When <situation>, <action>.
Source: 02_ideas.md <principle IDs> (lines X-Y)
Citations: <Supporting arguments or examples>
```

#### Section 7d: Section Coverage Review

For each major section in `02_ideas.md` (or all principles if structure is different), list:
- **Covered**: Which decision/trigger rules (`R#`/`T#`) address this section
- **Intentionally lost**: Any principles not captured, with brief reason (e.g., "Covered by R5", "Too context-specific", "Duplicate of R3")
- **Count**: Total principles in section, number covered

Example:
```
## Глава 2: Значимые имена
Principles: C-004, C-005, C-006, C-007 (4 total)
- C-004: Covered by R3
- C-005: Covered by R3
- C-006: Covered by R3
- C-007: Covered by R3
Status: 4/4 covered
```

### 8. Build the public-facing 06_agent_rules.md file

Write a clean markdown file suitable for pasting directly into an LLM conversation (CLAUDE.md/AGENTS.md style). It contains only:

```markdown
# APPLY <Book Title> by <Author>

## When to use
<Derived in step 3>

## Primary bias to correct
<Derived in step 3>

## Decision rules
<Derived in step 4>

## Trigger rules
<Derived in step 5>

## Final checklist
<Derived in step 6>
```

**No rule IDs appear in this file** — it stays clean and focused on the content, not the audit trail. Rule IDs live only in the traceability file.

---

## JSON SCHEMA: Traceability File

While the traceability file is markdown (not JSON), here's its conceptual structure:

```
File: 06_agent_rules.traceability.md

Metadata:
  Book: <slug>
  Source: 00_purpose.md through 04_consequences.md
  JSON reference: 05_llm_instructions.json (used for source citations)
  Generated: <ISO 8601 timestamp>

Compression Decisions: <Narrative explaining classification logic>

Decision Rules Mapping: R1...Rn with source citations
Trigger Rules Mapping: T1...Tn with source citations
Final Checklist Mapping: <Checklist items + source rules>

Section Coverage Review:
  For each section in 02_ideas.md:
    - Principles covered by R#/T#
    - Principles intentionally lost (with reason)
    - Coverage percentage
```

---

## QUALITY GATES

Each generated pair (06_agent_rules.md + 06_agent_rules.traceability.md) must satisfy:

- [ ] `06_agent_rules.md` is valid markdown and reads naturally as pastable instructions
- [ ] Every decision rule (`R#`) has ≥1 source citation in the traceability file pointing to specific line(s) in 00-04 markdown or 05 JSON
- [ ] Every trigger rule (`T#`) has ≥1 source citation
- [ ] Every principle/argument/implication/question from the book's 02_ideas.md appears in the coverage review (either covered by a rule ID or marked "intentionally lost" with reason)
- [ ] No rule exists without a source citation (spot-check: pick 5 random rules, verify they cite a real section)
- [ ] No fabricated data (metrics, scenarios, code examples) beyond what appears in the source
- [ ] Language: All text in both files is in English (regardless of source language)
- [ ] Traceability file records any intentionally-lost principles with explicit reason (e.g., "covered by R#", "too narrow", "duplicate of T#")

---

## SCOPE NOTE

This procedure produces **imperative rules distilled from the book**, not:

- ❌ New examples, metrics, or scenarios not in the source
- ❌ Anti-patterns (unless explicitly addressed in the source)
- ❌ Implementation roadmaps or step-by-step guides not present in the source
- ❌ Decision criteria ("when to use") beyond what appears in the source
- ❌ Context-specific guidance ("for microservices", "for startups") unless explicitly stated

**Why?** Rules may compress and reword, but they must not invent. The traceability file's coverage review makes this accountability visible.

---

## PROCESSING ORDER

Apply this procedure to each book independently:

1. `Books/clean-architecture/` → `06_agent_rules.md` + `06_agent_rules.traceability.md`
2. `Books/parallel-programming/` → `06_agent_rules.md` + `06_agent_rules.traceability.md`
3. `Books/pragmatic-programmer/` → `06_agent_rules.md` + `06_agent_rules.traceability.md`
4. `Books/ideal-work/` → `06_agent_rules.md` + `06_agent_rules.traceability.md`
5. `Books/code-fits-in-head/` → `06_agent_rules.md` + `06_agent_rules.traceability.md`
6. `Books/martin-clean-code/` → `06_agent_rules.md` + `06_agent_rules.traceability.md`

**Note:** Only the martin-clean-code pilot is executed in this task; others follow in a separate pass.

---

## USAGE

After executing this procedure for a book:

```bash
# Use the public rules file
1. Open a new LLM conversation
2. Paste Books/<slug>/06_agent_rules.md as system instructions
3. Ask the LLM to apply the book's principles to your code/design

# Example
> Paste: Books/martin-clean-code/06_agent_rules.md
> Ask: "Review this function against Clean Code principles"
> Claude applies the rules and cites specific rules in its reasoning
```

The traceability file is for **project maintainers**, not for agents — it documents how the rules were compressed and ensures nothing was silently fabricated.

---

## LANGUAGE RULE

**All output (06_agent_rules.md and 06_agent_rules.traceability.md) is always in English**, regardless of the source language of layers 00-04. This matches the language rule for Pass 4 JSON.

Why: 
- Agent instructions are most useful in English (LLM-native language)
- Traceability file is for maintainers (typically English-speaking engineers)
- Consistency with Pass 4's English-only policy

Record in metadata: `source_language`: the language of this book's 00-04 layers (e.g., "Russian", "English").

---

**See Also:** SKILL.md (Pass 5 overview), TECHNICAL_REQUIREMENTS.md (language rule), reference/pipeline-complete.md (full pipeline)
