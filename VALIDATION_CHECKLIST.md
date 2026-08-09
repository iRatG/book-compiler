# Validation Checklist: Pass 4 Architecture Implementation

**Purpose:** Validate that the Pass 4 (LLM-driven JSON generation) architecture is correctly implemented and ready for actual book processing.

**Date Created:** 2026-08-09  
**Status:** Ready for validation in next session  
**Validator:** A fresh LLM (no prior context from implementation session)

---

## How to Use This Checklist

1. Read this entire file
2. Execute each validation task below (in order)
3. Mark as ✅ (pass) or ❌ (fail)
4. For any ❌, note the issue and stop (don't proceed to next items)
5. If all ✅, the architecture is ready for Part B (JSON regeneration)

---

## SECTION A: Documentation Structure Validation

### A1. Check SKILL.md has been updated with Pass 4

**File:** `SKILL.md` (repo root)

**What to verify:**
- [ ] Frontmatter description mentions "6 files: 5 markdown + 1 JSON"
- [ ] "## The Three Passes" has been renamed to "## The Four Passes"
- [ ] A new section "### Pass 4: Generate LLM Instructions (05_llm_instructions.json)" exists after Pass 3
- [ ] Pass 4 section contains:
  - [ ] Goal statement (transform to actionable JSON, always English)
  - [ ] Input description (00-04 in any language, any header convention)
  - [ ] Output description (05_llm_instructions.json, always English)
  - [ ] "How it works" section with 5+ numbered steps (read, identify, link, translate, write)
  - [ ] Rules section forbidding truncation and requiring source tracking
  - [ ] Reference to `reference/pass-4-json-generation.md`
- [ ] "## Output Structure" section updated to mention both 00-04 (markdown, native language) and 05 (JSON, always English)
- [ ] References section lists `reference/pass-4-json-generation.md` and `reference/pipeline-complete.md`

**Pass Criteria:** All items above are checked ✅

---

### A2. Check that reference/pass-4-json-generation.md exists and is complete

**File:** `reference/pass-4-json-generation.md` (this file should exist; the old `pass-6-...md` should NOT exist)

**What to verify:**
- [ ] File exists at `reference/pass-4-json-generation.md`
- [ ] File does NOT exist at `reference/pass-6-json-generation.md` (it should have been renamed)
- [ ] Title is "# Pass 4: Generate LLM Instructions JSON (LLM-Driven Procedure)"
- [ ] File contains exactly these major sections (in order):
  - [ ] Purpose, Input, Output, Key Principle
  - [ ] PROCEDURE (with steps 1-6: read, identify, extract, translate, metadata, tags)
  - [ ] JSON SCHEMA (with full schema in code block, including new `source_language` field)
  - [ ] SCOPE NOTE (explicitly stating what's OUT of scope: metrics, formulas, scenarios, anti-patterns)
  - [ ] SPECIAL HANDLING for martin-clean-code (chapter-based extraction)
  - [ ] PROCESSING ORDER (lists all 6 books)
  - [ ] QUALITY GATES (checklist for validation)
  - [ ] Versioning (v4.0 current)
  - [ ] Usage section
- [ ] Schema includes:
  - [ ] `metadata.source_language` field (new, records actual language of book's 00-04)
  - [ ] Lean fields only: principle, statement, tags, source, source_line, supporting_arguments[], related_implications[], related_questions[]
  - [ ] NO rich fields: no practical_metrics, scenarios, anti_patterns, code_review_checklist, etc.
- [ ] SCOPE NOTE section explicitly forbids fabrication:
  - [ ] "❌ practical_metrics with formulas"
  - [ ] "❌ code_review_checklists"
  - [ ] "❌ scenarios with estimated hours"
  - [ ] "❌ anti_patterns derived by inverting"

**Pass Criteria:** All items above are checked ✅, and file is >200 lines (not a stub)

---

### A3. Check reference/pipeline-complete.md Pass numbering is fixed

**File:** `reference/pipeline-complete.md`

**What to verify:**
- [ ] Overview diagram shows 4 passes (not 5), with Pass 4 labeled as "PASS 4: GENERATE LLM INSTRUCTIONS (always English)"
- [ ] NO mention of "Pass 5: Validate" as a separate pass (validation is part of Pass 4 now)
- [ ] "## Pass 4" section (not "Pass 4" and "Pass 5" separately) contains:
  - [ ] "LLM-Driven" in the header/subtitle
  - [ ] Input describes "any language, any header convention"
  - [ ] Output describes "v4.0 lean schema"
  - [ ] Time estimate is "30-60 minutes per book for an LLM"
  - [ ] "What Pass 4 Does" section describes LLM procedure (5+ steps)
  - [ ] Lists lean schema fields (NOT rich v3.0 fields)
- [ ] "## Running the Pipeline" section:
  - [ ] Does NOT show `python scripts/build_all_llm_instructions.py` as recommended
  - [ ] Shows LLM-driven procedure as the current approach
  - [ ] Has a "### Legacy (Deprecated)" subsection explaining old script is superseded
- [ ] "## Versioning" section includes v4.0 entry:
  - [ ] Mentions "LLM-driven"
  - [ ] Mentions "lean schema"
  - [ ] Mentions "6 books"
  - [ ] Mentions "no fabricated data"

**Pass Criteria:** All items checked ✅

---

### A4. Check that json-generation-spec.md is marked superseded (not deleted)

**File:** `reference/json-generation-spec.md`

**What to verify:**
- [ ] File still exists (not deleted)
- [ ] First 10 lines contain a "Superseded" banner with:
  - [ ] Warning icon and "Superseded" label
  - [ ] Explanation that it describes rich v3.0 schema (never implemented)
  - [ ] Reference to `reference/pass-4-json-generation.md` as the authoritative doc
  - [ ] Note that it's kept for historical reference
- [ ] Rest of file is unchanged (old spec still there for history)

**Pass Criteria:** Banner present, file intact ✅

---

### A5. Check LLM_INSTRUCTIONS_TEMPLATE.md is marked superseded

**File:** `LLM_INSTRUCTIONS_TEMPLATE.md`

**What to verify:**
- [ ] Title updated to include "(v2.0) — SUPERSEDED"
- [ ] First section (before "## Structure Overview") contains:
  - [ ] Note that this template describes a richer schema no longer implemented
  - [ ] Reference to `reference/pass-4-json-generation.md` as current
  - [ ] Note that it's kept for historical reference
- [ ] A new divider "## Historical Reference (Kept for Documentation)"
- [ ] Rest of file is unchanged

**Pass Criteria:** Superseded marker present ✅

---

## SECTION B: Deprecation of Legacy Scripts

### B1. Check that legacy scripts have been moved and marked

**Directory:** `scripts/legacy/` (should exist and contain 5 files)

**What to verify:**
- [ ] Directory `scripts/legacy/` exists
- [ ] Contains exactly these 5 files (renamed/moved from scripts/ root):
  - [ ] `generate_llm_instructions.py`
  - [ ] `generators_clean_architecture.py`
  - [ ] `generator_real_data.py`
  - [ ] `generator_smart_links.py`
  - [ ] `parser_real_data.py`
- [ ] Each file still exists (not deleted), but moved to legacy/ subfolder
- [ ] A new file `scripts/legacy/README.md` exists with:
  - [ ] Explanation that these targeted v3.0 rich schema (never implemented)
  - [ ] Note that they're superseded by LLM-driven Pass 4
  - [ ] Warning: "Do not use these to regenerate 05_llm_instructions.json"
  - [ ] List of files and brief one-liner per file

**Pass Criteria:** All 5 files moved to legacy/, README.md present ✅

---

### B2. Check universal_pass6_generator.py has deprecation banner

**File:** `scripts/universal_pass6_generator.py`

**What to verify:**
- [ ] File still exists (not deleted)
- [ ] Top docstring (after #!/usr/bin/env python3) contains:
  - [ ] "DEPRECATED" label
  - [ ] "⚠️" warning icon
  - [ ] Explanation that it's superseded by LLM-driven procedure
  - [ ] List of limitations (English-only, can't parse Russian headers, can't handle chapter-based structures)
  - [ ] Note: "Kept for historical reference / emergency fallback only"
  - [ ] Strong statement: "Do NOT use to regenerate 05_llm_instructions.json going forward"
  - [ ] Reference to `reference/pass-4-json-generation.md`
- [ ] Actual script code is unchanged (only docstring added)

**Pass Criteria:** Deprecation banner present ✅

---

### B3. Check scripts/README.md deprecation notice

**File:** `scripts/README.md`

**What to verify:**
- [ ] Very first section (after title) has a prominent deprecation banner:
  - [ ] "⚠️ DEPRECATED:" label
  - [ ] Explanation of why (English-only regex, can't handle Russian/chapters, doesn't translate)
  - [ ] Reference to `reference/pass-4-json-generation.md` as current
  - [ ] "Do NOT use them going forward"
- [ ] "## Quick Start" section has been updated (or replaced with "## Legacy Usage")
- [ ] "## References" section:
  - [ ] Points to `reference/pass-4-json-generation.md` as authoritative
  - [ ] NOT to `reference/json-generation-spec.md` (or if it mentions it, marks as superseded)

**Pass Criteria:** Deprecation banner + reference updates ✅

---

## SECTION C: README and LLM_USAGE_GUIDE Updates

### C1. Check README.md mentions 6 books (not 5)

**File:** `README.md` (repo root)

**What to verify:**
- [ ] Title/intro mentions "6 technical books" (not 5)
- [ ] Books section includes 6 entries:
  - [ ] 1. Clean Architecture
  - [ ] 2. Ideal Work / Clean Coder
  - [ ] 3. Pragmatic Programmer
  - [ ] 4. Parallel Programming
  - [ ] 5. Code That Fits in Your Head
  - [ ] 6. Clean Code (NEW)
- [ ] Each book entry has:
  - [ ] Author name
  - [ ] Short description
  - [ ] Principles count (even if "TBD" for now)
  - [ ] Tags
  - [ ] Link to JSON file
- [ ] "## Quick Start" section under "I want to regenerate the JSON files" contains:
  - [ ] Reference to `reference/pass-4-json-generation.md` (not a python script command)
  - [ ] Explanation that it's LLM-driven
  - [ ] Note that legacy script is deprecated
- [ ] "## Files" section tree includes:
  - [ ] 6 book directories (including martin-clean-code)
  - [ ] Reference files (especially `reference/pass-4-json-generation.md`)
  - [ ] Note about SKILL.md and LLM_USAGE_GUIDE.md
- [ ] "## Versioning" section includes v4.0:
  - [ ] Mentions "LLM-driven"
  - [ ] Mentions "6 books"
  - [ ] Mentions "lean schema"
  - [ ] Explains language asymmetry (00-04 per-book, 05 always English)

**Pass Criteria:** All items checked ✅

---

### C2. Check LLM_USAGE_GUIDE.md includes 6th book

**File:** `LLM_USAGE_GUIDE.md`

**What to verify:**
- [ ] "## Books Available" table has 6 rows (not 5):
  - [ ] Clean Architecture | 15 | English
  - [ ] Ideal Work (Clean Coder) | 15 | English
  - [ ] Pragmatic Programmer | 7 | Russian
  - [ ] Parallel Programming | 15 | English
  - [ ] Code That Fits in Head | 8 | Russian
  - [ ] Clean Code | 15 | Russian (NEW)
- [ ] Table has a "Source Language" column showing which books are English vs Russian
- [ ] A note below table states: "All 05_llm_instructions.json files are always in English, regardless of 00-04 language"

**Pass Criteria:** All 6 books in table, source language column present ✅

---

## SECTION D: Structural Readiness of Source Books

### D1. Verify all 6 books have complete markdown layers (00-04)

**Books:** clean-architecture, parallel-programming, pragmatic-programmer, ideal-work, code-fits-in-head, martin-clean-code

**For each book, verify:**
- [ ] `Books/{slug}/00_purpose.md` exists and contains:
  - [ ] Title, author, publication info
  - [ ] Problem statement
  - [ ] Intent/goal
- [ ] `Books/{slug}/01_questions.md` exists and contains:
  - [ ] Central questions (at least 5+)
  - [ ] Questions organized clearly
- [ ] `Books/{slug}/02_ideas.md` exists and contains:
  - [ ] Principles/ideas (at least 6+)
  - [ ] Clear principle statements
  - [ ] Tags marked with #
- [ ] `Books/{slug}/03_reasoning.md` exists and contains:
  - [ ] Arguments/reasoning (at least 6+)
  - [ ] Evidence or explanations
- [ ] `Books/{slug}/04_consequences.md` exists and contains:
  - [ ] Implications/applications (at least 6+)
  - [ ] Practical usage or outcomes
- [ ] **Special check for martin-clean-code/02_ideas.md:**
  - [ ] Contains chapter sections (## Глава N:)
  - [ ] Each chapter has inline principle items (##C-NNN:`)
  - [ ] Total principle count is ~15+

**Pass Criteria:** All 6 books have all 5 layers (00-04) ✅

---

### D2. Verify current (broken) JSON structure is as expected

**Check:** `Books/*/05_llm_instructions.json` (all 6 files)

**For each book, verify:**
- [ ] File exists
- [ ] File is valid JSON (can be parsed)
- [ ] Contains metadata, system_instruction, quick_reference, principles[], decision_guide, faq, tags, version_info fields
- [ ] `metadata.language` is hardcoded as "English" (this is expected to be correct after Pass 4)
- [ ] `metadata.source_language` field does NOT exist yet (should be added by Pass 4)

**Current expected state (BEFORE Pass 4):**
- [ ] clean-architecture, parallel-programming: have `principles[]` count > 0, but most/all statements are empty ("")
- [ ] pragmatic-programmer, ideal-work, code-fits-in-head, martin-clean-code: have `principles[]` count = 0 (empty)

**Pass Criteria:** All 6 JSON files exist, are syntactically valid, match expected (broken) structure ✅

---

## SECTION E: Documentation Completeness

### E1. Check PASS_4_REGENERATION_GUIDE.md exists and is comprehensive

**File:** `PASS_4_REGENERATION_GUIDE.md`

**What to verify:**
- [ ] File exists at repo root
- [ ] Contains a clear introduction
- [ ] Lists all 6 books with:
  - [ ] Current state (English vs Russian, expected vs actual principle counts)
  - [ ] Special notes (especially for martin-clean-code)
  - [ ] Task description (what Pass 4 should do for this book)
- [ ] "## Execution Checklist" section with per-book verification items:
  - [ ] Principle count
  - [ ] Statement completeness
  - [ ] Arguments/implications/questions linkage
  - [ ] Metadata correctness
  - [ ] JSON validity
  - [ ] No truncation
  - [ ] No invented data
- [ ] "## Expected Results (Spot Check)" table showing:
  - [ ] Expected principle counts per book
  - [ ] Total: 66 principles across 6 books
- [ ] "## Validation After Regeneration" section with bash commands to verify
- [ ] "## How to Execute This" section with multiple options (Claude manual, API batch, etc.)

**Pass Criteria:** All sections present ✅

---

## SUMMARY: Can We Proceed to Part B?

If ALL sections (A, B, C, D, E) are ✅, then:

**✅ YES — Architecture is ready for Part B (JSON regeneration)**

Proceed to: For each of the 6 books, execute the LLM-driven Pass 4 procedure from `reference/pass-4-json-generation.md`:
1. Read 00-04
2. Identify principles
3. Translate to English
4. Write 05_llm_instructions.json

---

If ANY section is ❌:

**❌ NO — Architecture has issues**

Stop. Document the issue and notify the user. Do not proceed to JSON regeneration until architecture is fixed.

---

## Validation Report Template

After running through all checks, fill in this report:

```
# Validation Report: Pass 4 Architecture

Date: [date]
Validator: [name/ID]

## Results

- [ ] Section A (Documentation Structure): PASS / FAIL
- [ ] Section B (Deprecation): PASS / FAIL
- [ ] Section C (README/LLM_USAGE_GUIDE): PASS / FAIL
- [ ] Section D (Source Books): PASS / FAIL
- [ ] Section E (Regeneration Guide): PASS / FAIL

## Issues Found

[If any FAIL, list them here]

## Recommendation

[READY FOR PART B or NEEDS FIXES]

## Spot Check Samples

[If doing random spot checks, note findings here]
```

---

**END OF CHECKLIST**

This document is self-contained and can be used in a new session by a fresh LLM context.
