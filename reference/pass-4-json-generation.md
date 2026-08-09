# Pass 4: Generate LLM Instructions JSON (LLM-Driven Procedure)

**Purpose:** Transform a book's 5-layer markdown model into actionable JSON for LLM consumption.

**Input:**
- `00_purpose.md` through `04_consequences.md` for one book (in any language; any header convention)

**Output:**
- `05_llm_instructions.json` in the same directory (always in English)

**Key Principle:** Generate faithful English distillations of the book's own content. No invented data. Every field must trace to an identifiable passage in the source.

---

## PROCEDURE (for the LLM executing Pass 4)

### 1. Read the book's content fully

Load all five markdown files (`00_purpose.md` through `04_consequences.md`) and read them completely to understand:
- What problem the book addresses (from 00_purpose.md)
- What questions organize the content (from 01_questions.md)
- What principles/ideas the book proposes (from 02_ideas.md)
- What arguments and evidence support each idea (from 03_reasoning.md)
- What implications and applications follow from each idea (from 04_consequences.md)

### 2. Identify every principle

Read `02_ideas.md` completely, regardless of its structure:
- If principles are marked with top-level headers (`## PRINCIPLE N:`, `## ИДЕЯ N:`, `## ПРИНЦИП N:`, etc.), extract one principle per header.
- If principles are embedded in chapter sections as list items (like `martin-clean-code`), extract one principle per item (e.g., each `**C-NNN:**` item in a chapter is one principle).
- **Do not** regex-match a specific keyword or heading level; instead, **read and identify** each distinct principle by its role in the argument.

For each principle, extract:
- **principle**: A short, clear restatement of the principle (if the source uses multiple words like "Идея N: Принцип X is Y", extract just "Principle X is Y")
- **statement**: The full, complete explanation of the principle as it appears in `02_ideas.md` — entire paragraphs, no truncation
- **tags**: Any tags/keywords that help categorize the principle (usually marked with `#word` in the markdown)
- **source**: The exact reference (`02_ideas.md: PRINCIPLE N`, `02_ideas.md: Глава N, C-NNN`, etc.)
- **source_line**: The actual line number in the markdown file where this principle begins

### 3. Extract supporting arguments, implications, and questions

For each principle identified in step 2, locate its supporting content in the other layers by **reading and matching on meaning**, not on tag overlap:

**Supporting Arguments (from `03_reasoning.md`):**
- Read `03_reasoning.md` fully
- Identify each argument/reasoning section (may be marked as `## ARGUMENT N:`, `## ARG N:`, `## РАССУЖДЕНИЕ N:`, etc., or as paragraph prose)
- For each argument, determine: Does this argument support, explain, or provide evidence for the principle we're linking?
- If yes, extract:
  - **id**: A unique identifier (e.g., `arg_001`, `arg_002`, ...)
  - **name**: The name/title of the argument (e.g., "The False Economy of Shipping Faster")
  - **claim**: The main assertion of the argument — the full first paragraph or claim statement, **no truncation**
  - **source**: Reference (e.g., `03_reasoning.md: Argument 3`)
  - **source_line**: Line number in the markdown

**Related Implications (from `04_consequences.md`):**
- Read `04_consequences.md` fully
- Identify each implication/application section (may be marked as `## IMPLICATION N:`, `## APPLICATION N:`, `## ПРИМЕНЕНИЕ N:`, etc.)
- For each implication, determine: Does this follow from or apply the principle we're linking?
- If yes, extract:
  - **id**: A unique identifier (e.g., `impl_001`, `impl_002`, ...)
  - **name**: The name/title of the implication (e.g., "Expect Change; Design for It")
  - **what_means**: What this implication means in practice — the full explanation, **no truncation**
  - **source**: Reference (e.g., `04_consequences.md: Implication 9`)
  - **source_line**: Line number in the markdown

**Related Questions (from `01_questions.md`):**
- Read `01_questions.md` fully
- Identify each question (may be marked as `## QUESTION N:`, `## Q N:`, `### Вопрос N:`, etc., or as prose)
- For each question, determine: Does this question relate to or help explain the principle?
- If yes, extract:
  - **id**: A unique identifier (e.g., `question_01`, `question_02`, ...)
  - **text**: The full text of the question
  - **source**: Reference (e.g., `01_questions.md: Question 2`)
  - **source_line**: Line number in the markdown

### 4. Translate into English

For every piece of text extracted above (principle statement, argument claim, implication explanation, question text), **translate into faithful, complete English**:
- Preserve the original meaning and nuance
- Use complete sentences (no truncation)
- If the original is already in English, use it as-is
- If the original is in Russian (or another language), translate it idiomatically into clear, professional English suitable for pasting into an LLM conversation

**Translation is not invention**: If you encounter ambiguity, translate literally and faithfully rather than inferring additional meaning not in the source.

### 5. Extract metadata

From `00_purpose.md`, extract:
- **title**: The book's title
- **author**: The book's author (may be listed as `**Author:**` or `**Автор:**`)
- **publication**: Year or edition information (may be listed as `**Publication:**` or `**Издание:**`)
- **language_of_source**: The actual language of layers 00-04 for this book (`"English"`, `"Russian"`, etc.)

### 6. Extract global tags

From all five markdown files, extract every unique tag (usually marked as `#word` or `#word-word`). Collect them into a single alphabetized list for the JSON's `tags` array.

---

## JSON SCHEMA (lean, non-fabricated)

```json
{
  "metadata": {
    "title": "Book Title",
    "author": "Author Name",
    "publication": "Publication info (year, edition, etc.)",
    "book_name": "slug-from-directory-name",
    "format_version": "4.0",
    "generated_at": "ISO 8601 timestamp",
    "language": "English",
    "source_language": "English|Russian|...",
    "generation_pass": "Pass 4: Generate LLM Instructions (LLM-driven)"
  },

  "system_instruction": "An English-language prompt suitable for pasting into an LLM conversation. Tells the LLM: 'You are applying [Book Title]'s principles to real work. Here's how to use this JSON: 1) Identify which principle applies, 2) Review supporting_arguments for evidence, 3) Check related_implications for practical application, etc. Rules: Only cite what's in this JSON; quote supporting_arguments; use source references; if a principle doesn't apply, say so. Everything here is sourced from the book. Nothing is invented.'",

  "quick_reference": {
    "book": "slug-from-directory-name",
    "principles_count": number_of_principles,
    "top_3_principles": [ "Principle 1 statement", "Principle 2 statement", "Principle 3 statement" ],
    "questions_count": number_of_questions,
    "arguments_count": number_of_arguments,
    "implications_count": number_of_implications
  },

  "principles": [
    {
      "id": "principle_1",
      "number": 1,
      "principle": "Short, clear statement of the principle",
      "statement": "Full, untruncated explanation from the source markdown",
      "tags": [ "#tag1", "#tag2", ... ],
      "source": "02_ideas.md: PRINCIPLE 1",
      "source_line": 3,

      "supporting_arguments": [
        {
          "id": "arg_001",
          "name": "Argument Name/Title",
          "claim": "Full claim statement, no truncation",
          "source": "03_reasoning.md: Argument 1"
        },
        ...
      ],

      "related_implications": [
        {
          "id": "impl_001",
          "name": "Implication Name/Title",
          "what_means": "Full explanation, no truncation",
          "source": "04_consequences.md: Implication 1"
        },
        ...
      ],

      "related_questions": [
        {
          "id": "question_01",
          "text": "Full text of the related question",
          "source": "01_questions.md: Question 1"
        },
        ...
      ]
    },
    ...
  ],

  "decision_guide": {
    "when_uncertain_ask": [
      "Question 1 from 01_questions.md",
      "Question 2 from 01_questions.md",
      ...
    ],
    "framework": "When in doubt, reference supporting_arguments for evidence and related_implications for practical application."
  },

  "faq": [
    {
      "question": "How do I know this principle applies?",
      "answer": "Check if your situation matches the principle's scope. Review the related_questions and related_implications for context.",
      "principle_refs": [ "principle_1", "principle_2", ... ]
    }
  ],

  "tags": [ "#tag1", "#tag2", ... ],

  "version_info": {
    "json_version": "4.0",
    "pass": "Pass 4: Generate LLM Instructions (LLM-driven)",
    "generation_date": "ISO 8601 timestamp",
    "book": "slug-from-directory-name",
    "principles": number_of_principles,
    "arguments": number_of_arguments,
    "implications": number_of_implications,
    "questions": number_of_questions,
    "tags": number_of_unique_tags,
    "data_quality": "No invented data. All content sourced from markdown layers 00-04 and translated faithfully into English."
  }
}
```

**Field-by-field notes:**
- `statement`, `claim`, `what_means`: **Full text, no truncation** (unlike the legacy regex generator, which limited these to 150/100 chars).
- `source` and `source_line`: Every element must be traceable to the original markdown. Include line numbers so the LLM can verify.
- `supporting_arguments`, `related_implications`, `related_questions`: These are arrays of matching objects from the source layers. Link by **content**, not by tag-overlap algorithm. If a principle has no supporting arguments, the array is empty (but present).
- `source_language` in metadata: Records the actual language of layers 00-04 for this book, so users know whether the source was English, Russian, etc. This clarifies that layer 05 is always English even when 00-04 is not.

---

## SCOPE NOTE

This procedure produces a **lean, faithful schema**. The following are **out of scope** and should **not** be included, even if tempting:

- ❌ `practical_metrics` with formulas, quantified costs, or calculated examples
- ❌ `code_review_checklists` or similar actionable-but-invented guidance
- ❌ `scenarios` with estimated hours or fabricated cost numbers
- ❌ `anti_patterns` derived by inverting principles rather than sourced from the book
- ❌ `context_qualifiers` ("for microservices", "for startup", etc.) unless explicitly stated in the source
- ❌ `implementation_roadmaps` or step-by-step plans not present in the source
- ❌ `common_misconceptions` not explicitly addressed in the book
- ❌ `decision_criteria` or "when to use" guidance beyond what appears in the source

**Why?** These rich fields risk fabricating data not present in the source, which violates the core "no invented data" principle. If a future version of this skill wants to add these, they must be sourced explicitly from each book's content, not generated formulaically.

---

## SPECIAL HANDLING: martin-clean-code

`Books/martin-clean-code/02_ideas.md` is organized by book chapter (`## Глава N: <title>`) rather than by top-level principle headers. Within each chapter, principles are marked as bold list items: `**C-NNN:**` <principle text>.

**Extract these directly:**
- Each `**C-NNN:**` item is one principle.
- `principle`: The ID and short statement (e.g., "C-001: Code is written for people first")
- `statement`: The full explanation of that principle from the same section
- `source`: `02_ideas.md: Глава N, C-NNN`
- **No restructuring of the markdown is required.** The LLM-driven procedure extracts by reading and understanding, not by requiring a specific header convention.

---

## PROCESSING ORDER

Apply this procedure to each book independently (books are unrelated; links are only within-book):

1. `Books/clean-architecture/` → `05_llm_instructions.json`
2. `Books/parallel-programming/` → `05_llm_instructions.json`
3. `Books/pragmatic-programmer/` → `05_llm_instructions.json`
4. `Books/ideal-work/` → `05_llm_instructions.json`
5. `Books/code-fits-in-head/` → `05_llm_instructions.json`
6. `Books/martin-clean-code/` → `05_llm_instructions.json`

---

## QUALITY GATES

Each generated JSON must satisfy:

- [ ] `principles_count > 0` (the book has principles)
- [ ] Every principle has a non-empty `statement` field (full explanation, no truncation)
- [ ] Every supporting_argument has a non-empty `claim` field (full claim, not truncated)
- [ ] Every related_implication has a non-empty `what_means` field (full explanation, not truncated)
- [ ] `source` and `source_line` present for every principle, argument, implication, question
- [ ] Every `statement`, `claim`, and `what_means` traces to an identifiable passage in that book's own 00-04 markdown (spot-check 2-3 principles per book)
- [ ] `source_language` field accurately reflects the language of this book's layers 00-04
- [ ] All tags are from this book only (no cross-book tags)
- [ ] JSON is valid JSON (parseable with `json.parse()`)
- [ ] No invented data (metrics, formulas, scenarios, anti-patterns, etc.)

---

## VERSIONING

**v4.0 (current):** LLM-driven procedure, lean schema (metadata, system_instruction, quick_reference, principles[], decision_guide, faq, tags, version_info). No fabricated data. Replaces regex-based generator. Handles any header convention, any language. Always outputs English.

---

## USAGE

After executing this procedure for all 6 books:

```bash
# Each book now has a regenerated 05_llm_instructions.json

# To use in Claude or other LLM:
1. Open a new conversation
2. Paste the JSON or its system_instruction section
3. Ask the LLM to apply the book's principles to your code/design

# Example:
> Paste: Books/clean-architecture/05_llm_instructions.json
> Ask: "Review this architecture against Clean Architecture principles"
> Claude applies the principles and cites supporting_arguments for every claim
```

---

**See Also:** SKILL.md (Pass 4 overview), reference/pipeline-complete.md (full pipeline), reference/decisions.md (why this procedure replaced the regex approach)
