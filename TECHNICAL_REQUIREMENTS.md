# Technical Requirements — Book Compiler v2.0

**Status:** AUTHORITATIVE  
**User Requirement:** Core principle, repeated every session  
**Priority:** CRITICAL — affects all future work

---

## REQUIREMENT 1: Five-Layer Language Asymmetry

### LAYERS 00-04: Russian Language (User-Readable)

**Purpose:** User reads these layers to understand book content

**Files:**
- `00_purpose.md` — **Russian**
- `01_questions.md` — **Russian**
- `02_ideas.md` — **Russian**
- `03_reasoning.md` — **Russian**
- `04_consequences.md` — **Russian**

**Content Owner:** User (reads directly)  
**Quality Gate:** Readability in Russian for human comprehension

---

### LAYER 05: English Language (LLM-Ready)

**Purpose:** Consume by Claude/GPT for code reviews and guidance

**File:**
- `05_llm_instructions.json` — **ALWAYS ENGLISH**

**Content Source:** Extract + TRANSLATE from layers 00-04  
**Translation Rule:** Faithful English translation of Russian source (preserve meaning, idioms, context)  
**Quality Gate:** English clarity suitable for LLM consumption

**Why English for LLM:**
1. ✓ Better token efficiency (LLM understands English natively)
2. ✓ Reduced hallucination (clearer instructions = better following)
3. ✓ Lower context consumption (English often more concise)
4. ✓ Cross-language compatibility (any LLM can understand)

---

## REQUIREMENT 2: No Translation in Layers 00-04

**Rule:** DO NOT translate layers 00-04 to English.

**Reason:** User reads these layers in Russian to understand content naturally. Forcing English breaks the workflow.

**Example of WRONG approach:**
```
Books/ideal-work/02_ideas.md (Russian-source book):
## ИДЕЯ 1: Мастерство...
```
→ Should STAY in Russian, not be translated to:
```
## IDEA 1: Craftsmanship...
```

**Correct approach:**
- Keep markdown 00-04 in Russian
- Translate content INTO layer 05 JSON (English)
- User benefits: reads Russian naturally, gives LLM English for efficiency

---

## REQUIREMENT 3: JSON Layer 05 Structure

### English Content Only

Every field in 05_llm_instructions.json MUST be in English:

```json
{
  "metadata": {
    "language": "English",              ← Always "English"
    "source_language": "Russian",       ← What 00-04 are written in
    ...
  },
  "system_instruction": "...",         ← English instructions
  "principles": [
    {
      "principle": "...",              ← English
      "statement": "...",              ← English (translated from Russian markdown)
      "supporting_arguments": [
        {
          "claim": "...",              ← English (translated)
          ...
        }
      ],
      "related_implications": [
        {
          "what_means": "...",         ← English (translated)
          ...
        }
      ],
      "related_questions": [
        {
          "text": "...",               ← English (translated)
          ...
        }
      ]
    }
  ]
}
```

### Translation Quality

**NOT:** Copy Russian text into JSON  
**NOT:** Hardcode `"language": "English"` while keeping Russian content  
**YES:** Translate Russian → English faithfully, preserving meaning

---

## REQUIREMENT 4: All 6 Books Follow This Pattern

| Book | 00-04 Source | 05 Output | Status |
|------|---|---|---|
| clean-architecture | English | English (pass-through) | ✓ |
| parallel-programming | English | English (pass-through) | ✓ |
| ideal-work | Russian | English (translate) | **FIX NEEDED** |
| pragmatic-programmer | Russian | English (translate) | **FIX NEEDED** |
| code-fits-in-head | Russian | English (translate) | **FIX NEEDED** |
| martin-clean-code | Russian | English (translate) | **FIX NEEDED** |

---

## REQUIREMENT 5: Generator Must Enforce This

**Generator rule:** When extracting from markdown (any language), output JSON layer 05 ALWAYS in English.

**Algorithm:**
```
FOR each book in Books/:
  Read layers 00-04 in ANY language (Russian, English, etc.)
  
  FOR each principle/argument/implication/question:
    Extract content from markdown
    
    IF markdown is in Russian:
      TRANSLATE to English
    ELSE IF markdown is already English:
      USE as-is
    
    Write to 05_llm_instructions.json in English
  
  Verify: "language": "English" in metadata
  Verify: All text fields are in English
  Commit
```

---

## REQUIREMENT 6: Validation Must Check Language

**Validator rule:** When validating 05_llm_instructions.json, check:

```
✓ metadata.language == "English"
✓ metadata.source_language == actual language of 00-04
✓ All principle.statement fields are in English (not Russian/mix)
✓ All argument.claim fields are in English
✓ All implication.what_means fields are in English
✓ All question.text fields are in English
✗ FAIL if any field contains Cyrillic (Russian) text when should be English
```

---

## REQUIREMENT 7: Documentation Must Reflect This

**All docs must state clearly:**

> "Layers 00-04 are in the book's native language (Russian, English, etc.)  
> Layer 05 is ALWAYS in English, regardless of source language."

**Files that need this:**
- SKILL.md
- README.md
- LLM_USAGE_GUIDE.md
- reference/pass-4-json-generation.md
- This file (TECHNICAL_REQUIREMENTS.md)

---

## IMPLEMENTATION CHECKLIST

### Books that need fixing (Russian source → English JSON)

- [ ] ideal-work: Translate all principles/arguments/implications to English
- [ ] pragmatic-programmer: Translate all to English
- [ ] code-fits-in-head: Translate all to English
- [ ] martin-clean-code: Translate all to English

### Generator must be updated

- [ ] Add translation step (Russian → English)
- [ ] Add language detection (mark source_language)
- [ ] Add validation (ensure JSON is 100% English)

### Validator must check

- [ ] All text fields are in target language (English for 05)
- [ ] No Cyrillic mixed in English JSON
- [ ] metadata.language matches actual content

---

## RATIONALE

**Why this matters:**

1. **User Experience:** Native Russian content is readable for user in layers 00-04
2. **LLM Efficiency:** English layer 05 reduces token count + hallucination
3. **Maintainability:** Clear separation (native lang for humans, English for LLM)
4. **Consistency:** All 6 books follow same pattern (no special cases)
5. **Scalability:** New books follow this rule from day 1

**This is not optional.** It's the core design principle of the system.

---

## HISTORY

**Who said this:** User (multiple times, every session)  
**First mentioned:** Session 2 planning  
**Repeated:** Sessions 2, 3, and current session  
**Why it matters:** User was clear that this is non-negotiable

**Session 4 action item:** Fix all 4 Russian books to have English JSON layer 05.

---

**SIGNED:** User requirement  
**STATUS:** Must implement before system is production-ready
