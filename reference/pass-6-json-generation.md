# Pass 6: JSON Generation for LLM (v3.0)

**Purpose:** Transform 5-layer markdown model into actionable LLM instructions JSON

**Input:** 
- `00_purpose.md` through `04_consequences.md` (from Book directory)

**Output:** 
- `05_llm_instructions.json` (one per book, in same directory)

**Key Principle:** Each book gets its OWN unique JSON extraction, not a generic template.

---

## RULES

### Rule 1: ONE GENERATOR FOR ALL BOOKS

The generator is **universal** - same code works for any book.

```
for each_book in Books/:
    generator.process(book_dir)
    → generates book_dir/05_llm_instructions.json
```

### Rule 2: EACH BOOK IS INDEPENDENT

No cross-book data mixing.

```
❌ Don't: "This principle appears in both clean-architecture and ideal-work"
✅ Do: Generate separate JSONs. Let each stand alone.
```

### Rule 3: REAL DATA ONLY

Extract ONLY what's actually in that book's markdown.

```
Book: clean-architecture/
├─ 00_purpose.md → extract: title, author, problem, intent
├─ 01_questions.md → extract: 10 central questions
├─ 02_ideas.md → extract: 15 principles (ONLY main principles, not subsections)
├─ 03_reasoning.md → extract: 10 arguments with evidence
├─ 04_consequences.md → extract: 12 implications
└─ Result: Clean Architecture JSON (unique to this book)

Book: ideal-work/
├─ 00_purpose.md → extract: title, author, problem, intent
├─ 01_questions.md → extract: questions (whatever number is there)
├─ 02_ideas.md → extract: principles (whatever number is there)
├─ 03_reasoning.md → extract: arguments
├─ 04_consequences.md → extract: implications
└─ Result: Ideal Work JSON (unique to this book)
```

### Rule 4: LINKING IS BOOK-INTERNAL ONLY

Links between principles ↔ arguments ↔ implications are **within the same book only**.

```
✅ principle_2 links to arg_001 (both from same book)
❌ principle_2 (clean-arch) doesn't link to arg_001 (ideal-work)
```

### Rule 5: TAGS ARE BOOK-SPECIFIC

Each book has its own tag set. No unification across books.

```
clean-architecture tags: #cost-of-change, #architecture, #paradigms, ...
ideal-work tags: #professionalism, #tdd, #ethics, #craftsmanship, ...
pragmatic-programmer tags: #dry, #automation, #estimation, ...

Each JSON contains only its book's tags.
```

### Rule 6: STRUCTURE IS IDENTICAL ACROSS ALL JSONs

Every 05_llm_instructions.json has the same top-level structure:

```json
{
  "metadata": { title, author, publication, ... },
  "system_instruction": "For LLM to use this book's principles",
  "quick_reference": { core_goal, top_3_principles, ... },
  "principles": [ ... each principle complete ],
  "decision_guide": { ... },
  "faq": [ ... ],
  "usage_guide": { ... },
  "tags": [ ... ],
  "version_info": { ... }
}
```

### Rule 7: SYSTEM INSTRUCTION IS BOOK-SPECIFIC

Each book's system_instruction tells LLM what this book is about.

```
Clean Architecture:
  "You are an expert architect applying Clean Architecture principles..."

Ideal Work:
  "You are a professional software craftsperson guiding on ethics and TDD..."

Pragmatic Programmer:
  "You are a practical developer applying pragmatic principles..."
```

Each instruction references that book's principles, not others.

### Rule 8: METRICS COME FROM BOOK'S OWN DATA

No invented metrics. Extract from book's reasoning/implications.

```
clean-architecture:
  - Has "cost of change" metric in 03_reasoning.md → extract it
  - Has empirical data in ARG-001 → reference it
  
ideal-work:
  - Has TDD metrics (test coverage, defect rates) → extract
  - Has no cost-of-change metric → don't invent it

pragmatic-programmer:
  - Has estimation metrics → extract
  - Has automation ROI → extract
```

### Rule 9: LINKING STRATEGY

Links are built using:
1. **Exact tag matches** (same tags)
2. **Semantic similarity** (related words)
3. **Content references** (principle mentions in argument)
4. **Core principles** (principles 1-3 link to most content)

No manual linking. Algorithm handles it.

### Rule 10: SOURCE TRACKING

Every element references source:

```json
{
  "id": "principle_2",
  "source": "02_ideas.md: PRINCIPLE 2",
  "source_line": 12,
  "supporting_arguments": [
    {
      "id": "arg_001",
      "source": "03_reasoning.md: Argument 1",
      "source_line": 5
    }
  ]
}
```

LLM can verify everything in source.

---

## ALGORITHM

```
FOR each book in Books/:
  
  1. PARSE markdown (00-04)
     - Extract metadata (title, author, publication)
     - Extract principles (main level only)
     - Extract arguments/questions/implications
     - Extract all tags
  
  2. LINK internally
     - Link principles ↔ arguments (same book only)
     - Link principles ↔ implications (same book only)
     - Link principles ↔ questions (same book only)
  
  3. GENERATE JSON
     - metadata section
     - system_instruction (book-specific)
     - quick_reference
     - principles array (with linked data)
     - decision_guide
     - faq
     - usage_guide
     - tags
     - version_info
  
  4. VALIDATE
     - No invented data
     - All sources traceable
     - Structure consistent
  
  5. SAVE
     - Output: book/05_llm_instructions.json
     - One JSON per book, independent

END FOR
```

---

## EXAMPLE: Two Different Books

### Clean Architecture JSON

```json
{
  "metadata": {
    "title": "Clean Architecture...",
    "author": "Robert C. Martin",
  },
  "system_instruction": "You are an expert architect...",
  "principles": [
    {
      "id": "principle_1",
      "principle": "Architecture is NOT Separate from Code",
      "supporting_arguments": [ arg_001, arg_002, arg_003 ],
      "related_implications": [ impl_001, impl_002 ],
      "code_review_checklist": [ ... ]
    },
    ...
  ],
  "tags": ["#architecture", "#cost-of-change", "#paradigms", ...]
}
```

### Ideal Work JSON

```json
{
  "metadata": {
    "title": "The Clean Coder...",
    "author": "Robert C. Martin",
  },
  "system_instruction": "You are a professional software craftsperson...",
  "principles": [
    {
      "id": "principle_1",
      "principle": "Craftsmanship is a Journey, Not a Destination",
      "supporting_arguments": [ arg_001, arg_004 ],
      "related_implications": [ impl_003, impl_005 ],
      "code_review_checklist": [ ... ]
    },
    ...
  ],
  "tags": ["#professionalism", "#tdd", "#ethics", "#craftsmanship", ...]
}
```

**Notice:** 
- Different principles
- Different supporting arguments  
- Different tags
- Different system instruction
- But SAME JSON structure

---

## PROCESSING ORDER

```
1. clean-architecture/     → 05_llm_instructions.json
2. ideal-work/             → 05_llm_instructions.json
3. pragmatic-programmer/   → 05_llm_instructions.json
4. code-fits-in-head/      → 05_llm_instructions.json
5. parallel-programming/   → 05_llm_instructions.json
```

Each independent. No dependencies between them.

---

## QUALITY GATES (PER BOOK)

For each generated JSON:

- [ ] All data sourced from this book's markdown
- [ ] No invented metrics or examples
- [ ] All principles have statement from source
- [ ] Source tracking complete (line numbers, sections)
- [ ] Links are to same book's content only
- [ ] Tags are from this book only
- [ ] System instruction is book-specific
- [ ] JSON structure matches v3.0 spec
- [ ] No cross-book references

---

## FAIL CONDITIONS

Don't generate if:
- ❌ Book's markdown files don't exist (00-04 missing)
- ❌ Can't parse principles (structure unrecognizable)
- ❌ Critical data is missing (metadata, purpose)

Report: "Cannot process [book]. Reason: [why]"

---

## SUCCESS CRITERIA

After running generator on all 5 books:

```
Books/
├─ clean-architecture/
│  ├─ 00_purpose.md
│  ├─ 01_questions.md
│  ├─ 02_ideas.md
│  ├─ 03_reasoning.md
│  ├─ 04_consequences.md
│  └─ 05_llm_instructions.json ✓
├─ ideal-work/
│  ├─ 00_purpose.md
│  ├─ 01_questions.md
│  ├─ 02_ideas.md
│  ├─ 03_reasoning.md
│  ├─ 04_consequences.md
│  └─ 05_llm_instructions.json ✓
├─ pragmatic-programmer/
│  └─ 05_llm_instructions.json ✓
├─ code-fits-in-head/
│  └─ 05_llm_instructions.json ✓
└─ parallel-programming/
   └─ 05_llm_instructions.json ✓
```

Each JSON:
- ✅ Unique to its book
- ✅ No invented data
- ✅ Fully traceable
- ✅ Ready for LLM use
- ✅ Can be used independently

---

## USAGE

```bash
# Generate for ALL books at once
python scripts/universal_json_generator.py Books/

# Or for single book
python scripts/universal_json_generator.py Books/clean-architecture/

# Result: Each book has its own 05_llm_instructions.json
```

Output:
```
[OK] Generated 5 books
  ✓ clean-architecture: 15 principles, 10 arguments
  ✓ ideal-work: 6 principles, 8 arguments
  ✓ pragmatic-programmer: 7 principles, 9 arguments
  ✓ code-fits-in-head: 8 principles, 7 arguments
  ✓ parallel-programming: 7 principles, 6 arguments
```

Each JSON is standalone, independent, ready for LLM.

---

## NOTES

- Generator is **universal** (works for any 5-layer markdown structure)
- Output is **unique per book** (each book's own JSON)
- Data is **real** (only what's in markdown)
- System is **scalable** (add new books, generator works same way)
- Each book is **independent** (no cross-book dependencies)

This is Pass 6 of the book-compiler pipeline.
