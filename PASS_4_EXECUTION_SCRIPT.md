# Pass 4 Execution Script — LLM Instruction для Улучшения JSON

**Назначение:** Точные инструкции для LLM агента при обработке каждой книги

**Применить для:** ideal-work, pragmatic-programmer, code-fits-in-head, martin-clean-code

---

## СИСТЕМА ИНСТРУКЦИЙ ДЛЯ LLM

### INPUT FILES (читать полностью)

```
Books/{book_name}/
  ├─ 02_ideas.md (список всех принципов с ID)
  ├─ 03_reasoning.md (все аргументы с доказательствами)
  ├─ 04_consequences.md (все применения/следствия)
  ├─ 01_questions.md (центральные вопросы)
  └─ 05_llm_instructions.json (текущее состояние - ЧТО УЛУЧШАТЬ)
```

### TASK: Для каждого principle в JSON

#### STEP 1: Identify the principle ID
- Find in 02_ideas.md 
- Match with principle in JSON
- Confirm source_line

#### STEP 2: Extract supporting_arguments
For each argument listed in JSON:
1. Find argument name in 03_reasoning.md (e.g., "АРГУМЕНТ 1: История Авиации...")
2. Read the FULL argument (all subsections)
3. Extract 2-3 key claims/evidence points
4. **Translate to faithful English** (preserve meaning, not literal)
5. Structure as:
   ```json
   {
     "id": "arg_001",
     "name": "Aviation History As Mirror for Software",
     "claim": "[TRANSLATED claim statement - 1-2 sentences]",
     "evidence": "[TRANSLATED evidence + data points - 3-5 sentences]",
     "source": "03_reasoning.md: Argument 1, line XX-YY",
     "source_line": XX
   }
   ```

#### STEP 3: Extract related_implications
For each implication listed in JSON:
1. Find implication name in 04_consequences.md (e.g., "СЛЕДСТВИЕ 1...")
2. Read the FULL implication section
3. Extract:
   - What it means (practical action)
   - When to apply (contexts)
   - Why it matters (result)
4. **Translate to faithful English**
5. Structure as:
   ```json
   {
     "id": "impl_001",
     "name": "For Developer, Every Day Should Start with TDD",
     "what_means": "[TRANSLATED practical action - 2-3 sentences]",
     "when_applies": "[TRANSLATED contexts - where/when - 2-3 sentences]",
     "why_matters": "[TRANSLATED results - what improves - 2-3 sentences]",
     "source": "04_consequences.md: Consequence 1, line XX-YY",
     "source_line": XX
   }
   ```

#### STEP 4: Verify related_questions
1. Check if related_questions are filled (should be from 01_questions.md)
2. If empty or incomplete:
   - Find related questions in 01_questions.md that match principle
   - Add as:
     ```json
     {
       "id": "question_XX",
       "text": "[TRANSLATED question text]",
       "source": "01_questions.md: Question XX, line YY"
     }
     ```

---

## CRITICAL RULES (Non-Negotiable)

### Rule 1: Language
- **INPUT:** Russian text from 03_reasoning.md and 04_consequences.md
- **OUTPUT:** Faithful English translation (preserve meaning, idioms, intent)
- **NOT:** Literal word-for-word OR invented details
- **Translation Quality:** Would Claude understand the nuance? If no, adjust.

### Rule 2: Source Tracing
- EVERY field must have `source` citation
- EVERY citation must include line numbers from source file
- **Verifiable:** Someone can jump to source_line and find the exact passage

### Rule 3: No Invention
- **Allowed:** Extract + translate + reformat
- **Not Allowed:** Add examples, scenarios, or details not in source
- **Pattern:** If source has "X", JSON must say "X"; if source doesn't mention Y, don't add it
- **Test:** Read your JSON claim, then read source. Do they match in meaning?

### Rule 4: Completeness
- EVERY supporting_argument in JSON must have: id, name, claim, evidence, source, source_line
- EVERY related_implication must have: id, name, what_means, when_applies, why_matters, source, source_line
- **Do NOT leave fields empty or as stubs like "Thesis:" or "Practical Action:"**

### Rule 5: Structure Consistency
- All supporting_arguments follow same JSON structure
- All related_implications follow same JSON structure
- All related_questions follow same JSON structure
- **Uniformity matters for downstream parsing**

---

## METADATA FIXES (apply to ALL 4 books)

### For ideal-work/05_llm_instructions.json:
```json
"metadata": {
  "title": "The Clean Coder: A Code of Conduct for Professional Programmers",
  "author": "Robert C. Martin (\"Uncle Bob\")",
  "publication": "2011",
  "book_name": "ideal-work",
  "format_version": "4.0",
  "generated_at": "2026-08-10T...", ← UPDATE TIMESTAMP
  "language": "English",
  "source_language": "Russian",
  "generation_pass": "Pass 4 v2.0: Generate LLM Instructions (Improved)"
}
```

### For pragmatic-programmer/05_llm_instructions.json:
```json
"metadata": {
  "title": "The Pragmatic Programmer: From Journeyman to Master",
  "author": "Andrew Hunt, David Thomas",
  "publication": "1999 (1st ed), 2019 (2nd ed)",
  ...
}
```

### For code-fits-in-head/05_llm_instructions.json:
```json
"metadata": {
  "title": "Code That Fits in Your Head: Heuristics for Software Engineering",
  "author": "Mark Seemann",
  "publication": "2021",
  ...
}
```

### For martin-clean-code/05_llm_instructions.json:
```json
"metadata": {
  "title": "Clean Code: A Handbook of Agile Software Craftsmanship",
  "author": "Robert C. Martin (\"Uncle Bob\")",
  "publication": "2008",
  ...
}
```

---

## WORKFLOW FOR EACH BOOK

```
1. READ all source files completely:
   ├─ 00_purpose.md (for context)
   ├─ 01_questions.md (all questions)
   ├─ 02_ideas.md (all principles + source lines)
   ├─ 03_reasoning.md (all arguments + source lines)
   ├─ 04_consequences.md (all implications + source lines)
   └─ 05_llm_instructions.json (current structure)

2. FOR EACH PRINCIPLE in 02_ideas.md:
   ├─ Find matching principle_N in JSON
   ├─ FOR EACH supporting_argument:
   │   ├─ Locate in 03_reasoning.md
   │   ├─ Extract claim + evidence
   │   ├─ Translate to English
   │   ├─ Add source + source_line
   │   └─ Fill JSON fields completely
   ├─ FOR EACH related_implication:
   │   ├─ Locate in 04_consequences.md
   │   ├─ Extract what_means + when_applies + why_matters
   │   ├─ Translate to English
   │   ├─ Add source + source_line
   │   └─ Fill JSON fields completely
   └─ FOR EACH related_question:
       ├─ Find in 01_questions.md
       ├─ Translate to English
       ├─ Add source + source_line
       └─ Fill JSON field

3. VALIDATE:
   ├─ JSON is valid (json.loads() OK)
   ├─ Every principle has supporting_arguments (not empty)
   ├─ Every principle has related_implications (not empty)
   ├─ Every field has source citations
   ├─ Every source_line is accurate (spot-check 5 random)
   └─ Every translation is faithful to source

4. OUTPUT:
   └─ Write updated 05_llm_instructions.json
```

---

## QUALITY GATES (before committing)

```
VALIDATION CHECKLIST for {book_name}/05_llm_instructions.json:

❏ Metadata correct:
  ❏ title ≠ "Unknown"
  ❏ author ≠ "Unknown"
  ❏ publication ≠ "Unknown"
  ❏ language = "English"
  ❏ source_language = "Russian" (or correct source)

❏ Principles count matches 02_ideas.md:
  ❏ Total principles in JSON = Total ИДЕЯ in 02_ideas.md

❏ Supporting arguments:
  ❏ EVERY principle has ≥2 arguments
  ❏ NO empty supporting_arguments arrays
  ❏ EVERY argument has: id, name, claim, evidence, source, source_line

❏ Related implications:
  ❏ EVERY principle has ≥2 implications
  ❏ NO empty related_implications arrays
  ❏ EVERY implication has: id, name, what_means, when_applies, why_matters, source, source_line

❏ Related questions:
  ❏ Most principles have ≥1 question
  ❏ EVERY question has: id, text, source, source_line (source is optional if no match found)

❏ Translation quality (spot-check 5 random):
  ❏ Argument 1 claim: Does translation match meaning in Russian original? YES/NO
  ❏ Implication 1 what_means: Does translation preserve intent? YES/NO
  ❏ Argument 3 evidence: Is the data accurate? YES/NO
  ❏ Implication 4 why_matters: Does it convey the result? YES/NO
  ❏ Question 2: Is it natural English? YES/NO

❏ Source verification (spot-check 3 lines):
  ❏ source_line for Argument 2: Points to actual argument in 03_reasoning.md? YES
  ❏ source_line for Implication 1: Points to actual consequence in 04_consequences.md? YES
  ❏ source_line for Question 1: Points to actual question in 01_questions.md? YES

❏ JSON validity:
  ❏ python -m json.tool {file} → no syntax errors
  ❏ All required fields present (no truncation)
  ❏ No escaped characters broken

❏ Final sanity check:
  ❏ Can I paste this JSON into Claude as system prompt? YES
  ❏ Would Claude understand the reasoning? YES
  ❏ Is this 10x better than before (empty arrays)? YES
```

---

## EXAMPLE: How to Fill ONE Principle

**Source 02_ideas.md (ideal-work):**
```
## ИДЕЯ 1: Мастерство — Это Путь, Не Пункт Назначения

**Формулировка:** Мастерство — это доскональное знание того, как получить отличный результат...
```

**Source 03_reasoning.md:**
```
## АРГУМЕНТ 1: История Авиации Как Зеркало Для ПО

**Тезис:** Программирование сейчас находится на той же стадии развития...

### 1.1 Параллельная Эволюция
**Авиация (1500s-1950s = 450 лет):**
- 1500s: Леонардо да Винчи — концепция полета
...
```

**Source 04_consequences.md:**
```
## СЛЕДСТВИЕ 1: Для Разработчика Каждый День Должен Начинаться с TDD

**Практическое Действие:**
Каждое утро разработчик пишет тесты ДО кода.
...
```

**RESULT in 05_llm_instructions.json:**
```json
{
  "id": "principle_1",
  "number": "1",
  "principle": "Mastery is a Path, Not a Destination",
  "statement": "Mastery is thorough knowledge of how to obtain excellent results, emerging from good training and extensive experience. It is not a destination you reach, but a continuous path of learning and growth.",
  "tags": [...],
  "source": "02_ideas.md: ИДЕЯ 1",
  "source_line": 5,
  
  "supporting_arguments": [
    {
      "id": "arg_001",
      "name": "Aviation History As a Mirror for Software",
      "claim": "Computer programming is currently at the same stage of development that aviation was in the 1920s.",
      "evidence": "Aviation took 450 years (1500-1950) to mature: from da Vinci's concepts to the Wright brothers' controlled flight (1903) to Boeing 707 civilian aviation (1950). Programming has only 90 years of history (1930-2020), with industrial programming for just 50 years. Like aviation in the 1920s, software engineering lacks standardized practices, systemic discipline, and professional maturity.",
      "source": "03_reasoning.md: АРГУМЕНТ 1",
      "source_line": 5
    },
    {
      "id": "arg_009",
      "name": "Growth of Developers Every 5 Years",
      "claim": "The number of developers doubles every 5 years, meaning most developers are inexperienced.",
      "evidence": "2000: ~1 million developers; 2010: ~2 million; 2020: ~4 million; 2025: ~8 million. This means approximately 50% of all developers have less than 2 years of experience. Only 12.5% have 10+ years experience. The industry cannot expect professionalism when half the workforce is beginners without systematic mentoring or standards.",
      "source": "03_reasoning.md: АРГУМЕНТ 9",
      "source_line": 309
    }
  ],
  
  "related_implications": [
    {
      "id": "impl_001",
      "name": "For Developer, Every Day Should Start with TDD",
      "what_means": "Each morning, a developer writes tests BEFORE code. The cycle is: write test (RED) → write code to pass (GREEN) → refactor (REFACTOR) → repeat.",
      "when_applies": "This is the daily discipline for every developer, every day, every task.",
      "why_matters": "By day's end: 100+ cycles, 50+ new lines of code, 0 bugs in production. Tests become perfect low-level documentation. Code is structured (tests reveal design problems). Developer has pride: 'I worked well.'",
      "source": "04_consequences.md: СЛЕДСТВИЕ 1",
      "source_line": 5
    },
    {
      "id": "impl_002",
      "name": "First 1-2 Weeks of TDD Are Painful",
      "what_means": "New TDD practitioners will work slower for the first 1-2 weeks while the brain relearns to write tests first.",
      "when_applies": "When a developer or team adopts TDD for the first time.",
      "why_matters": "By week 2: becomes faster. By week 4: much faster. By month's end: cannot work without TDD. The temporary slowdown is the price of mastery. With mentorship, learning accelerates to 4 weeks instead of 3 months.",
      "source": "04_consequences.md: СЛЕДСТВИЕ 2",
      "source_line": 29
    }
  ],
  
  "related_questions": [
    {
      "id": "question_01",
      "text": "What fundamental practices does a programmer need to develop true mastery?",
      "source": "01_questions.md: Question 1"
    }
  ]
}
```

---

## NOTES FOR LLM EXECUTION

1. **Work book-by-book:** ideal-work → pragmatic-programmer → code-fits-in-head → martin-clean-code
2. **Each book is independent:** No cross-references needed
3. **Translation matters:** Use natural English, not word-for-word Russian
4. **Verification:** Spot-check translations before finalizing
5. **Commit after each book:** Don't batch all 4 at once (easier to debug)

---

**Script Version:** 1.0  
**For:** Pass 4 v2.0 Execution  
**Status:** Ready for LLM Agent
