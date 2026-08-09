# Pass 4 Regeneration Guide: Generate 05_llm_instructions.json for All 6 Books

**Status:** Ready for execution  
**Date:** 2026-08-09  
**Procedure:** Follow `reference/pass-4-json-generation.md` exactly

---

## What to Do

For each book listed below, execute Pass 4 using the LLM-driven procedure in `reference/pass-4-json-generation.md`:

1. **Read** `00_purpose.md` through `04_consequences.md` for the book
2. **Identify** every principle, argument, implication, question (by understanding, not regex)
3. **Link** supporting content within the same book by meaning
4. **Translate** everything into faithful, complete English
5. **Write** `05_llm_instructions.json` matching the lean schema

---

## Books to Regenerate

### 1. ✅ clean-architecture
- **Source Language:** English (00-04 are already in English)
- **Structure:** `## PRINCIPLE N: Title` in 02_ideas.md
- **Current State:** 15 principles recognized, but most have empty `statement` fields (paragraph bug)
- **Task:** Fix empty statements; write real, untruncated explanations for all 15 principles

**Special Notes:**
- English source makes this a good warm-up test
- Verify that fixing the paragraph-split bug produces full statements for all 15 principles
- Check that statement lengths are NOT truncated (current script limits to 150 chars, should be full text)

---

### 2. ✅ parallel-programming
- **Source Language:** English (00-04 are already in English)
- **Structure:** `## PRINCIPLE N: Title` in 02_ideas.md
- **Current State:** 15 principles recognized, but ALL have empty `statement` fields
- **Task:** Write real, untruncated statements for all 15 principles

**Special Notes:**
- Same structure as clean-architecture, so same approach
- All 15 statements are currently empty (worse than clean-arch), so the fix is critical

---

### 3. ✅ pragmatic-programmer
- **Source Language:** Russian (00-04 are in Russian)
- **Structure:** `### Идея N: Title` (h3, mixed-case "Идея") in 02_ideas.md
- **Current State:** 0 principles extracted (regex doesn't recognize Russian headers)
- **Task:** Extract 7 principles from Russian markdown, translate to English

**Special Notes:**
- First Russian-language book
- Header pattern is h3 with "Идея" — different from other Russian books
- Verify count: source markdown should have ~7 distinct "Идея N:" entries
- Translate each principle's statement faithfully into English

---

### 4. ✅ ideal-work
- **Source Language:** Russian (00-04 are in Russian)
- **Structure:** `## ИДЕЯ N: Title` (h2, all-caps "ИДЕЯ") in 02_ideas.md
- **Current State:** 0 principles extracted (regex doesn't recognize Russian headers)
- **Task:** Extract 6 principles from Russian markdown, translate to English

**Special Notes:**
- Different Russian header convention than pragmatic-programmer (h2, all-caps)
- Verify count: should have ~6 distinct "ИДЕЯ N:" entries
- Translate each principle faithfully

---

### 5. ✅ code-fits-in-head
- **Source Language:** Russian (00-04 are in Russian)
- **Structure:** `## ПРИНЦИП N: Title` (h2, all-caps "ПРИНЦИП") in 02_ideas.md
- **Current State:** 0 principles extracted (regex doesn't recognize Russian headers)
- **Task:** Extract 8 principles from Russian markdown, translate to English

**Special Notes:**
- Another Russian header convention (h2, all-caps, but "ПРИНЦИП" instead of "ИДЕЯ")
- Verify count: should have ~8 distinct "ПРИНЦИП N:" entries
- Note: 02_ideas.md is longer than the other Russian books; make sure all principles are extracted

---

### 6. ✅ martin-clean-code
- **Source Language:** Russian (00-04 are in Russian)
- **Structure:** Chapter-based: `## Глава N: Title` sections containing inline `**C-NNN:**` principle items (NOT top-level principle headers)
- **Current State:** 0 principles extracted (regex cannot handle chapter-based structure)
- **Task:** Extract ~15 principles from chapter-based structure, translate to English

**Special Notes:**
- **This is the structural challenge:** Unlike other books, principles are NOT marked as `## PRINCIPLE N:` or `### Идея N:` headers at the top level. Instead, they're inline bold items like `**C-001:** Код пишется для людей...` nested inside chapter sections.
- Example structure:
  ```markdown
  ## Глава 1: Чистый код
  **C-001:** Код пишется для людей, прежде всего
  **C-002:** Чистый код - это долг разработчика
  ...
  ## Глава 2: Значимые имена
  **C-004:** Имя переменной должно отвечать...
  ...
  ```
- **Procedure:** For each chapter section, read the text and extract each `**C-NNN:**` item as a separate principle. No markdown restructuring needed — the LLM-driven approach extracts by understanding, not by requiring specific header syntax.
- Verify count: should have ~15 distinct `**C-NNN:**` entries across all chapters
- Translate each principle's statement faithfully to English
- **Note:** This book was historically excluded from the "official 5 books" list precisely because the regex script couldn't parse its structure. Adding it back (with LLM-driven extraction) demonstrates that the new procedure handles format variation.

---

## Execution Checklist

For **each** book, verify:

- [ ] Read all five markdown files (00_purpose.md through 04_consequences.md) completely
- [ ] Extracted principle count matches expected count (see table below)
- [ ] Every principle has:
  - [ ] `id` (principle_1, principle_2, ...)
  - [ ] `number` (1, 2, ...)
  - [ ] `principle` (short statement)
  - [ ] `statement` (full, untruncated explanation)
  - [ ] `tags` (extracted from markdown)
  - [ ] `source` (reference like "02_ideas.md: PRINCIPLE 1")
  - [ ] `source_line` (actual line number)
- [ ] Supporting arguments (from 03_reasoning.md):
  - [ ] Each argument has `id`, `name`, `claim` (full, NOT truncated), `source`
  - [ ] Linked to principles by content matching (not tag overlap)
- [ ] Related implications (from 04_consequences.md):
  - [ ] Each implication has `id`, `name`, `what_means` (full, NOT truncated), `source`
  - [ ] Linked to principles by content matching
- [ ] Related questions (from 01_questions.md):
  - [ ] Each question has `id`, `text`, `source`
  - [ ] Linked to principles by content matching
- [ ] Metadata is complete:
  - [ ] `title`, `author`, `publication` from 00_purpose.md
  - [ ] `language` = "English" (always)
  - [ ] `source_language` = actual language of this book's 00-04 (English or Russian)
- [ ] JSON parses as valid JSON
- [ ] No truncated text (spot-check 2-3 principle statements against source)
- [ ] No invented data (metrics, scenarios, anti-patterns, checklists, etc.)

---

## Expected Results (Spot Check)

| Book | Source Language | Expected Principles | Current Count |
|------|---|---|---|
| clean-architecture | English | 15 | 15 (fix empty statements) |
| parallel-programming | English | 15 | 15 (fix empty statements) |
| pragmatic-programmer | Russian | 7 | 0 → **7** |
| ideal-work | Russian | 6 | 0 → **6** |
| code-fits-in-head | Russian | 8 | 0 → **8** |
| martin-clean-code | Russian (chapters) | 15 | 0 → **15** |
| **TOTAL** | - | **66** | 30 → **66** |

After regeneration: **All 6 books should have non-zero, non-empty principle counts.**

---

## How to Execute This

### Option 1: Use Claude with the Procedure Doc

1. Open `reference/pass-4-json-generation.md`
2. For each book:
   - Open a **new Claude conversation**
   - Paste the entire `reference/pass-4-json-generation.md` doc
   - Say: "Please follow this procedure exactly to generate the JSON for [Book Name]"
   - Paste: all five markdown files from `Books/[slug]/`
   - Have Claude output the generated JSON
   - Save the JSON to `Books/[slug]/05_llm_instructions.json`
   - (Or use the API if you want to automate this)

### Option 2: Batch with a Script

If you want to script this (e.g., using Claude API), the algorithm is:

```python
for book in ["clean-architecture", "parallel-programming", "pragmatic-programmer", 
             "ideal-work", "code-fits-in-head", "martin-clean-code"]:
    markdown_00_04 = read_all_layers(f"Books/{book}/")
    json_output = llm.generate_json_for_book(
        markdown_content=markdown_00_04,
        procedure=read_file("reference/pass-4-json-generation.md")
    )
    write_file(f"Books/{book}/05_llm_instructions.json", json_output)
```

### Option 3: Manual + Claude

Run Claude on each book's layers one at a time, manually copying JSON files.

---

## Validation After Regeneration

After all 6 JSONs are written, run this verification:

```bash
# Count principles per book
for book in clean-architecture parallel-programming pragmatic-programmer ideal-work code-fits-in-head martin-clean-code; do
  count=$(jq '.quick_reference.principles_count' "Books/$book/05_llm_instructions.json")
  echo "$book: $count principles"
done

# Check for empty statements (should be 0)
for book in clean-architecture parallel-programming pragmatic-programmer ideal-work code-fits-in-head martin-clean-code; do
  empty=$(jq '.principles[] | select(.statement == "") | .id' "Books/$book/05_llm_instructions.json" | wc -l)
  echo "$book: $empty empty statements"
done

# Verify all files are valid JSON
for book in clean-architecture parallel-programming pragmatic-programmer ideal-work code-fits-in-head martin-clean-code; do
  jq empty "Books/$book/05_llm_instructions.json" 2>&1 && echo "$book: ✓ valid JSON" || echo "$book: ✗ INVALID"
done
```

---

## Timeline Expectation

- **Per-book generation:** 15-30 minutes (LLM reads 00-04, extracts, translates, writes JSON)
- **6 books total:** 1.5-3 hours (can be parallelized if running via API)
- **Verification:** 15-30 minutes

---

## Notes for the Person Executing This

- ✅ All documentation is in place (`reference/pass-4-json-generation.md` is authoritative)
- ✅ All 6 books' markdown layers (00-04) exist and are complete
- ✅ Legacy script is deprecated and documented as such
- ⏳ Next step: Execute Pass 4 for all 6 books following the procedure
- ⏳ Then: Commit regenerated JSONs to git
- ⏳ Then: Update any per-book principle counts if they changed (README.md already has placeholders)

---

**Everything is ready. Follow `reference/pass-4-json-generation.md` step by step for each book.**
