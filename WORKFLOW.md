# Adding New Books to book-compiler

**Version:** 2.0  
**Status:** Automated workflow (Pass 1-5)

---

## Quick Start (30 seconds)

```bash
# 1. Create source folder with metadata
mkdir -p source/my-new-book
cat > source/my-new-book/README.md <<EOF
# My New Book

**Author:** Name
**Year:** 2024
**Language:** English or Russian
**Source:** [link or path]

## Description
1-2 sentences about what this book covers

## Content Type
- [x] Technical book (software/architecture)
- [ ] Philosophy/methodology
- [ ] Other: ___

## Key Areas
#tag1 #tag2 #tag3
EOF

# 2. Run skill in Claude Code
/book-compiler my-new-book

# 3. Done! Check results
ls Books/my-new-book/
# Output: 00_purpose.md, 01_questions.md, ..., 06_agent_rules.md
```

**That's it.** System handles Pass 1-5 automatically.

---

## Detailed Workflow

### Step 1: Prepare Source Material

Create a folder in `source/`:

```
source/
└── my-new-book/
    ├── README.md              ← REQUIRED: book metadata
    ├── book.pdf               ← OPTIONAL: source PDF
    ├── book-excerpt.txt       ← OPTIONAL: relevant passages
    └── notes.md               ← OPTIONAL: your annotations
```

### Step 2: Fill README.md Template

```markdown
# Book Title

**Author:** Full Name
**Publication Year:** YYYY
**Language:** English or Russian
**Source:** [Link to book or path to PDF]

## Description

One or two sentences describing what this book is about and why it matters.

## Content Type

- [x] Technical book (software architecture, design patterns, etc.)
- [ ] Philosophy of work/methodology
- [ ] Process and practices
- [ ] Other: ___________

## Key Areas (tags)

Comma-separated or hashtag-separated areas this book covers:

#architecture, #quality, #process, #professionalism

## Notes (optional)

Any additional context that helps reconstruction:
- What makes this book unique?
- What problem does it solve?
- Who should read it?

```

**Example 1: Technical Architecture Book**

```markdown
# Systems Architecture in Practice

**Author:** John Doe
**Publication Year:** 2023
**Language:** English
**Source:** https://example.com/systems-architecture

## Description

How to design distributed systems that scale, with real-world patterns from Netflix and Uber.

## Content Type

- [x] Technical book (software architecture, design patterns, etc.)
- [ ] Philosophy of work/methodology
- [ ] Process and practices

## Key Areas

#architecture, #systems-design, #scalability, #distributed-systems, #patterns
```

**Example 2: Professional Practices Book**

```markdown
# Effective Leadership in Engineering

**Author:** Jane Smith
**Publication Year:** 2022
**Language:** Russian
**Source:** ./my-books/leadership-book.pdf

## Description

Как строить инженерные команды, принимать решения под давлением, и делегировать ответственность.

## Content Type

- [ ] Technical book (software architecture, design patterns, etc.)
- [x] Philosophy of work/methodology
- [x] Process and practices

## Key Areas

#leadership, #团队-building, #decision-making, #responsibility
```

### Step 3: Run the Skill

In **Claude Code**, run:

```
/book-compiler my-new-book
```

Or with explicit parameters:

```
/book-compiler my-new-book --language=russian --force-regenerate
```

**Parameters:**
- `--language=russian|english` — Layers 0-4 language (default: detect from README)
- `--force-regenerate` — Regenerate even if book already exists
- `--from-pass=4` — Start from Pass 4 (reuse 00-04, regenerate 05-06)
- `--validate-only` — Check JSON validity without regenerating

### Step 4: System Executes Automatically

The skill will:

**Pass 1: Purpose**
- Read source materials
- Identify central problem and author's intent
- Write `00_purpose.md` (problem, goal, audience, scope)

**Pass 2: Questions**
- Extract 12-15 central questions
- Group by topic
- Write `01_questions.md`

**Pass 3: Ideas**
- Extract 12-15 core principles
- Add tags for Library cross-referencing
- Write `02_ideas.md`

**Pass 3b: Reasoning**
- Extract 8-10 supporting arguments
- Include evidence and examples
- Write `03_reasoning.md`

**Pass 3c: Consequences**
- Extract 12-14 practical applications
- Write `04_consequences.md`

**Pass 4: LLM Instructions (JSON)**
- Read layers 00-04 completely
- Generate structured JSON with principles, arguments, implications, questions
- Full source citations (source + line number)
- **Always in English** (regardless of input language)
- Write `05_llm_instructions.json`

**Pass 5: Agent Rules**
- Synthesize principles into decision rules + trigger rules + checklist
- Build traceability: every rule → source principle → source material
- Write `06_agent_rules.md` (clean, pastable)
- Write `06_agent_rules.traceability.md` (audit trail)

### Step 5: Verify Results

```bash
# Check what was created
ls -la Books/my-new-book/

# Should see:
# 00_purpose.md
# 01_questions.md
# 02_ideas.md
# 03_reasoning.md
# 04_consequences.md
# 05_llm_instructions.json
# 06_agent_rules.md
# 06_agent_rules.traceability.md
```

**Logs are saved in `reports/` (local only, not in git):**

```bash
reports/my-new-book-PASS-1-5.log      # Real-time log
reports/my-new-book-PASS-1-5.md       # Summary report
```

### Step 6: Add to Git (Optional)

Once satisfied, commit the book:

```bash
git add Books/my-new-book/
git commit -m "Add my-new-book: [Author Name] - [Short description]"
git push
```

**Do NOT commit:**
```bash
source/              # Keep source materials locally
reports/             # Keep logs locally
SYSTEM_USAGE.local.md # Keep local instructions
```

---

## Troubleshooting

### Problem: "Book was analyzed poorly"

**Solution:**

1. Update `source/my-new-book/README.md` with more details
2. Add PDF or text excerpts to source folder
3. Re-run:
   ```
   /book-compiler my-new-book --force-regenerate
   ```
4. Check logs: `reports/my-new-book-PASS-1-5.md`

### Problem: "One layer is wrong (e.g., 02_ideas.md)"

**Solution:**

1. Edit `Books/my-new-book/02_ideas.md` directly (add/fix principles)
2. Regenerate Pass 4-5 (based on updated 00-04):
   ```
   /book-compiler my-new-book --from-pass=4
   ```
3. Layers 00-04 are kept; Pass 4-5 are regenerated

### Problem: "JSON is malformed"

**Solution:**

Validate without regenerating:
```
/book-compiler my-new-book --validate-only
```

If validation fails, check:
- All tags are in `#lowercase-with-hyphens` format
- All source references point to real lines in 00-04
- No unmatched quotes in JSON

---

## File Structure

### Directory Layout (Correct)

```
book-compiler/
├── Books/                           ← Finished books (IN GIT)
│   ├── clean-architecture/
│   ├── ideal-work/
│   ├── ... (other existing books)
│   └── my-new-book/                 ← Your new book (ready to commit)
│       ├── 00_purpose.md
│       ├── 01_questions.md
│       ├── 02_ideas.md
│       ├── 03_reasoning.md
│       ├── 04_consequences.md
│       ├── 05_llm_instructions.json
│       ├── 06_agent_rules.md
│       └── 06_agent_rules.traceability.md
│
├── source/                          ← Input materials (NOT in git)
│   └── my-new-book/
│       ├── README.md
│       └── book.pdf
│
├── reports/                         ← Processing logs (NOT in git)
│   ├── my-new-book-PASS-1-5.log
│   └── my-new-book-PASS-1-5.md
│
├── reference/                       ← Specs (IN GIT)
├── CLAUDE.md                        ← Developer guide (IN GIT)
├── SKILL.md                         ← Skill spec (IN GIT)
├── WORKFLOW.md                      ← This file (IN GIT)
├── README.md                        ← Project overview (IN GIT)
├── LLM_USAGE_GUIDE.md               ← Examples (IN GIT)
└── .gitignore                       ← Excludes source/ and reports/
```

### .gitignore Rules

```
# DO NOT COMMIT (local only)
source/                    # Input materials
reports/                   # Processing logs

# DO COMMIT (to git)
Books/*/                   # Finished books
reference/                 # Specifications
*.md                       # Documentation
```

---

## Quality Checks

Before committing, verify:

**Pass 1-3 (Markdown):**
- ✓ All tags are `#lowercase-with-hyphens` format
- ✓ No broken references to other files
- ✓ Each principle/question/argument has clear source
- ✓ Original language is preserved (Russian stays Russian, English stays English)

**Pass 4 (JSON):**
- ✓ Valid JSON (parseable)
- ✓ All principles have source citations (source + source_line)
- ✓ No fabricated arguments/implications (all from 00-04)
- ✓ Language is English

**Pass 5 (Agent Rules):**
- ✓ Every rule (R# or T#) has source traceability
- ✓ Traceability file covers 100% of principles (no gaps)
- ✓ Decision rules are actionable (testable conditions)
- ✓ Trigger rules follow "When X, then Y" format

---

## Examples: Two New Books

### Example 1: Software Architecture Book

```bash
# Setup
mkdir -p source/design-systems/
cat > source/design-systems/README.md <<EOF
# Design Systems at Scale

**Author:** Sarah Johnson
**Year:** 2023
**Language:** English
**Source:** O'Reilly

## Description
Practical guide to building and maintaining design systems in organizations with 50-1000 engineers.

## Content Type
- [x] Technical book (software architecture, design patterns, etc.)

## Key Areas
#design-systems, #architecture, #consistency, #scalability, #documentation
EOF

# Run
/book-compiler design-systems

# Result
Books/design-systems/00-06 ready ✅
```

### Example 2: Russian Book on Leadership

```bash
# Setup
mkdir -p source/лидерство-в-техе/
cat > source/лидерство-в-техе/README.md <<EOF
# Лидерство в технологических компаниях

**Автор:** Иван Петров
**Год:** 2023
**Язык:** Russian
**Источник:** ./my-books/leadership-tech.pdf

## Описание
Как управлять инженерными командами, принимать решения и создавать культуру ответственности.

## Тип контента
- [x] Философия работы и методология
- [x] Процессы и практики

## Ключевые области
#лидерство, #управление-командой, #решения, #культура, #масштабирование
EOF

# Run
/book-compiler лидерство-в-техе --language=russian

# Result
Books/лидерство-в-техе/00-06 ready ✅
# Layers 00-04: Russian
# Layers 05-06: English
```

---

## Adding Multiple Books

**Batch workflow:**

```bash
# Create multiple sources
for book in book1 book2 book3; do
  mkdir -p source/$book
  # Fill README.md for each
done

# Run skill for each (sequentially)
/book-compiler book1
# wait for completion, check logs
/book-compiler book2
# wait for completion, check logs
/book-compiler book3
# wait for completion, check logs

# Commit all at once
git add Books/book1/ Books/book2/ Books/book3/
git commit -m "Add 3 new books: book1, book2, book3"
git push
```

---

## Key Points

### ✅ DO

- Put source materials in `source/` (local only)
- Fill README.md accurately (helps reconstruction)
- Run `/book-compiler book-name` (skill handles everything)
- Check logs in `reports/` (verify quality)
- Commit only `Books/` folder (finished books)

### ❌ DON'T

- Edit 00-04 manually before Pass 4 (it regenerates them)
- Push `source/` or `reports/` to git
- Run Passes manually (skill orchestrates)
- Invent examples or metrics not in source
- Truncate principle statements

---

## Integration with LLM

Once a book is added:

```bash
# Copy the JSON into Claude
cat Books/my-new-book/05_llm_instructions.json

# Or use it in agent rules
cat Books/my-new-book/06_agent_rules.md
# Paste into CLAUDE.md or agent configuration
```

See **LLM_USAGE_GUIDE.md** for examples.

---

## Reference

- **CLAUDE.md** — Developer guide and project overview
- **SKILL.md** — Technical specification of all 5 passes
- **reference/pass-4-json-generation.md** — How JSON is generated
- **reference/pass-5-agent-rules-generation.md** — How agent rules are synthesized
- **reference/process.md** — Detailed procedures for Pass 1-3
- **LLM_USAGE_GUIDE.md** — How to use JSONs with LLMs

---

**Status:** ✅ Workflow tested and automated  
**Last updated:** 2026-08-09
