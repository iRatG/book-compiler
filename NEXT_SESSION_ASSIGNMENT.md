# Next Session Assignment: Pass 5 v2.0 Rollout to 5 Books

**Goal:** Apply Pass 5 v2.0 methodology independently to 5 remaining books  
**Status:** Ready for execution  
**Scope:** `Books/clean-architecture/`, `Books/ideal-work/`, `Books/pragmatic-programmer/`, `Books/code-fits-in-head/`, `Books/parallel-programming/`

---

## Quick Start (60 seconds)

1. **Open:** `SESSION_2026_08_10_PASS_5_V2_COMPLETE.md` (what we did last session)
2. **Reference:** `Books/martin-clean-code/06_agent_rules.md` (copy structure from here)
3. **Reference:** `Books/martin-clean-code/06_agent_rules.traceability.md` (copy audit format from here)
4. **Process:** For each of 5 books, apply the 3-step procedure below
5. **Commit:** After each book (5 commits total)

---

## For Each Book: 4-Step Process

### Step 1: Read All Layers (15 minutes)

Read these files for the book completely:
- `Books/{name}/00_purpose.md` — purpose, intent, problem
- `Books/{name}/01_questions.md` — central questions
- `Books/{name}/02_ideas.md` — principles/ideas (main content)
- `Books/{name}/03_reasoning.md` — arguments, evidence, examples
- `Books/{name}/04_consequences.md` — implications, applications
- `Books/{name}/05_llm_instructions.json` — existing extraction (reuse source citations)

**Why:** You need to understand the book before synthesizing rules.

---

### Step 2: Create 06_agent_rules.md (25 minutes)

**Format:** Copy structure from `Books/martin-clean-code/06_agent_rules.md`

**Structure to follow:**
```markdown
# APPLY [Book Title] by [Author]

## When to use
[1-3 sentences]

## Primary bias to correct
[1 sentence — the misconception book corrects]

## Decision Rules
### R1: [Title]
Quality: [85-95]%
[Conditions, Fail Signals, Examples, Sources]

### R2: [Title]
...
[14 total decision rules]

## Trigger Rules
### T1: When [condition] → [action]
Quality: [85-95]%
[Example]

[8 total trigger rules]

## Final Checklist
[7 items, restate highest-leverage rules as questions]
```

**For each Decision Rule (R1-R14):**

1. **Identify core principles** from `02_ideas.md`
   - Group related principles together
   - Look for natural clusters

2. **Synthesize into imperative statement**
   - NOT a quote, but clear restatement
   - Should be actionable (not abstract)
   - Example: "Keep functions small, focused, single abstraction level"

3. **Add Conditions section**
   - 3-5 testable conditions
   - Each starts with ✓
   - Checkable by agent or human
   ```markdown
   Conditions to verify:
   - ✓ Condition 1: [specific check]
   - ✓ Condition 2: [specific check]
   ```

4. **Add Fail Signals section**
   - 3-5 signals of violation
   - Each starts with ✗
   - Shows when to stop and revise
   ```markdown
   Fail signals — stop and revise if:
   - ✗ Signal 1: [what to avoid]
   - ✗ Signal 2: [what to avoid]
   ```

5. **Add Sources**
   - Cite which principles (C-NNN, P-NNN, etc.)
   - Cite line numbers from source files
   - Be specific

6. **Add Quality Score**
   - Estimate 0-100% based on:
     * Source Integrity (100% if fully from source)
     * Necessity (100% if core, 70% if context-dependent)
     * Actionability (0-100% can agent check this?)
     * Cross-Book Consistency (100% if matches other books)
   - Use formula from SESSION report
   - Result: 85-95% (rarely <85%, rarely >95%)

7. **Add Examples (optional but recommended)**
   ```markdown
   Example:
   ✓ GOOD: [good code]
   ✗ BAD: [bad code]
   ```

**For each Trigger Rule (T1-T8):**

1. **Format:** "When [condition] → [action]"
   - Condition is specific (not abstract)
   - Action is concrete (not vague)

2. **Add Quality Score** (85-95%)

3. **Add Example** (shows detection + action)
   ```markdown
   Example:
   Before: [bad pattern]
   After: [good pattern]
   ```

4. **Add Source** (which principle triggers this)

---

### Step 3: Create 06_agent_rules.traceability.md (20 minutes)

**Format:** Copy structure from `Books/martin-clean-code/06_agent_rules.traceability.md`

**Sections to include:**

1. **Metadata**
   ```markdown
   Book: {name}
   Pass: 5 (Agent Rules) - Version 2.0
   Quality: {decision rules avg}% {trigger rules avg}%
   Generated: 2026-08-{date}
   ```

2. **Methodology** (can reuse text from martin-clean-code file, adapt as needed)
   - Explain Extract → Synthesize → Validate → Optimize
   - Mention Quality Scoring formula

3. **Decision Rules Mapping** (R1-R14)
   ```markdown
   ### R1: [Title]
   Quality Score: {X}%
   - Source Integrity: {0-100%}
   - Necessity: {0-100%}
   - Actionability: {0-100%}
   - Cross-Book Consistency: {0-100%}

   Sources:
   - 02_ideas.md: [principle names/IDs and line numbers]
   - 03_reasoning.md: [argument IDs and line numbers]
   - 04_consequences.md: [application IDs and line numbers]

   Citation: [quote from source explaining why this rule exists]
   ```

4. **Trigger Rules Mapping** (T1-T8)
   ```markdown
   ### T1: [Title]
   Quality Score: {X}%
   Source: [which principles trigger this]
   ```

5. **Section Coverage Review**
   - For each chapter/section in `02_ideas.md`:
     ```markdown
     | Principle | Covered By | Status | Quality |
     |-----------|-----------|--------|---------|
     | [name] | R# | ✓ | 90% |
     | [name] | Intentionally Dropped | ⚠ | — |
     ```

6. **Grand Total**
   ```markdown
   Total principles in book: {X}
   Covered: {X}/{total} ({%})
   Intentionally dropped: {X}/{total} ({%})
   [explain why dropped]
   ```

---

### Step 4: Quality Checks & Commit (10 minutes)

**Before committing, verify:**

- [ ] All 14 decision rules have:
  - [ ] Quality Score (85-95%)
  - [ ] Conditions (3-5 testable checks)
  - [ ] Fail Signals (3-5 violation signs)
  - [ ] Sources (line numbers)

- [ ] All 8 trigger rules have:
  - [ ] Quality Score (85-95%)
  - [ ] Example (before/after)
  - [ ] Sources

- [ ] Traceability file has:
  - [ ] Quality Score breakdown (4 factors)
  - [ ] Complete section coverage audit
  - [ ] Intentionally-dropped principles explained

- [ ] 06_agent_rules.md is:
  - [ ] ~500+ lines
  - [ ] Pastable into Claude as system instructions
  - [ ] Free of personal notes/TODOs

- [ ] File sizes reasonable:
  - [ ] 06_agent_rules.md: 400-600 lines
  - [ ] 06_agent_rules.traceability.md: 600-800 lines

**Commit message template:**
```
Pass 5 v2.0: Agent Rules for {Book Title}

- 14 decision rules with Conditions + Fail Signals + Quality Scores
- 8 trigger rules with examples and Quality Scores
- Complete audit trail: {X}/46 principles covered ({%}), Y intentionally dropped
- Quality: {decision avg}% + {trigger avg}% = {overall}%

This follows Pass 5 v2.0 methodology:
Extract → Synthesize → Validate → Optimize (for LLM)
See reference/pass-5-agent-rules-generation.md for procedure.

Co-Authored-By: Claude <you>
```

---

## Expected Output per Book

| File | Size | Content |
|------|------|---------|
| 06_agent_rules.md | 500-600 lines | R1-R14, T1-T8, checklist, pastable |
| 06_agent_rules.traceability.md | 600-800 lines | Quality Scores, coverage audit, sources |

**Total time per book:** 60-70 minutes (including checks)  
**Total time all 5 books:** ~5-6 hours

---

## Tips & Tricks

### Tip 1: Use martin-clean-code as Template

Don't start from scratch. Copy structure from martin-clean-code files:

```bash
# Copy structure
cp Books/martin-clean-code/06_agent_rules.md Books/{newbook}/06_agent_rules.md.template
# Then edit, replace content

# Copy traceability structure
cp Books/martin-clean-code/06_agent_rules.traceability.md Books/{newbook}/06_agent_rules.traceability.md.template
```

### Tip 2: Reuse Quality Scoring Explanations

The methodology text from martin-clean-code traceability can be reused/adapted:
- Extract → Synthesize → Validate → Optimize (same for all books)
- Quality Scoring formula (same for all books)
- Just update "book name" references

### Tip 3: Cross-Book Consistency Check

As you process 5 books, note when rules appear across books:
- R2 in Clean Code ("Write for readers") ← also in Architecture, Pragmatic, etc.
- R6 in Clean Code ("Separate concerns") ← also in Architecture, Design
- This will help identify "Shared Rules" later

**Mark in notes but don't create "Shared Rules" yet** — wait until all 6 books done.

### Tip 4: Quality Scores

**Target: 85-95% for all rules**

If a rule is <85%, it might be:
- Too context-specific (should drop)
- Too abstract (should rewrite with conditions)
- Too actionable (actionability is high, but necessity/integrity low)

If a rule is >95%, verify it's actually that good (rarely are).

Typical distribution:
- 90-95%: Most rules (high quality)
- 85-89%: Some rules (good but context-dependent)
- <85%: Rare (probably should reconsider)

---

## When to Ask Questions

**Ask if:**
- A principle doesn't fit into decision/trigger/drop categories
- A book has unusual structure (non-standard headers, etc.)
- Quality Scores come out weird (<80% or >96%)
- You disagree with martin-clean-code's approach for this book

**Don't ask about:**
- How to rewrite specific rules (you decide based on source)
- Exact wording (your phrasing is fine if it traces to source)
- Whether to commit (yes, always commit completed work)

---

## Reference Materials

**In this repo:**
- `SESSION_2026_08_10_PASS_5_V2_COMPLETE.md` — what we did, lessons learned
- `reference/pass-5-agent-rules-generation.md` — full procedure
- `IMPROVEMENTS_FOR_LLM_GENERATION.md` — methodology overview
- `Books/martin-clean-code/06_agent_rules.md` — etalon (copy structure)
- `Books/martin-clean-code/06_agent_rules.traceability.md` — audit template

---

## Success Criteria

**Per book:**
- ✅ 14 decision rules (Quality 85-95%)
- ✅ 8 trigger rules (Quality 85-95%)
- ✅ Traceability file complete (audit trail)
- ✅ Coverage: principles covered or explicitly dropped
- ✅ Sources: line numbers cited
- ✅ Pastable: can paste 06_agent_rules.md into Claude

**Overall (5 books):**
- ✅ 5 commits (one per book)
- ✅ 5 × 06_agent_rules.md (25 total rule definitions + triggers)
- ✅ 5 × 06_agent_rules.traceability.md (complete audit)
- ✅ Ready for: Context Levels (NANO/MINI/FULL) in future session

---

## Order of Processing (Recommended)

1. **clean-architecture** first
   - Similar structure to martin-clean-code
   - Clear separation of concerns
   - Good to start with

2. **ideal-work** next
   - Russian source (like martin-clean-code)
   - Similar principles, ethics focus
   - Familiar translation patterns

3. **pragmatic-programmer** next
   - English source (different pattern)
   - Practice-oriented
   - Shorter, more specific rules

4. **code-fits-in-head** next
   - Cognitive-focused
   - Unique principles
   - Good to end with before final book

5. **parallel-programming** last
   - Most technical/specialized
   - Unique domain (concurrency)
   - Good for final stretch

**No hard rule — you can do in any order, but above sequence flows naturally.**

---

## After Completion: Next Steps (Not This Session)

**Future sessions will handle:**
- Phase 2: Validation Loop (automatic Quality Score calculation)
- Phase 3: Context Levels (generate NANO/MINI versions)
- Phase 4+: Cross-Book Synthesis, Actionability Scoring

**For now:** Just focus on Phase 1 (Structured Synthesis + Agent-Specific Optimization)

---

## Questions Before You Start?

**Ask if unclear about:**
- Process (Extract → Synthesize → Validate → Optimize)
- Structure (Conditions, Fail Signals, Quality Score format)
- Coverage (how many decision rules, how many triggers)
- Sources (how detailed should citations be)

**Then start with clean-architecture and go step by step.**

---

## Last Notes

- ✅ Everything is documented, no guessing needed
- ✅ Template exists (martin-clean-code) — copy format, change content
- ✅ Methodology is clear (reference docs)
- ✅ Quality metrics are quantified (85-95% range)
- ✅ Sources must be cited (traceability matters)

**You're independent now. Go for it. 🚀**

---

**Status:** Ready to execute  
**Time estimate:** 5-6 hours for all 5 books  
**Quality target:** 90% average (same as pilot)  
**Deliverables:** 5 books × (06_agent_rules.md + 06_agent_rules.traceability.md)
