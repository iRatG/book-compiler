# LLM Instructions JSON Generator (v3.0)

**Purpose:** Transform 5-layer markdown book model into actionable LLM instructions JSON.

**Status:** Ready for testing  
**Version:** 3.0  
**Python:** 3.8+

---

## Quick Start

### Generate JSON for All Books

```bash
cd scripts/
python build_all_llm_instructions.py ../Books/
```

### Generate for Single Book

```bash
python build_all_llm_instructions.py ../Books/ --book clean-architecture
```

### Verbose Output

```bash
python build_all_llm_instructions.py ../Books/ --verbose
```

---

## What It Does

### Input
Five markdown files per book:
- `00_purpose.md` — Problem, Intent
- `01_questions.md` — Central Questions
- `02_ideas.md` — Principles, Concepts, Claims
- `03_reasoning.md` — Arguments, Evidence, Examples
- `04_consequences.md` — Applications, Implications, Limitations

### Process
1. **Parse** markdown files
2. **Extract** principles and supporting content
3. **Transform** into structured JSON (v3.0 format)
4. **Validate** against quality gates
5. **Generate** `05_llm_instructions.json`

### Output
Machine-readable JSON optimized for LLM consumption:
- Practical metrics (formulas, not guesses)
- Code review checklists
- Real scenarios with quantified costs
- Anti-patterns (what looks right but is wrong)
- Context qualifiers (when to apply, when NOT)
- Implementation roadmaps
- Decision criteria

---

## Architecture

### Core Modules

#### 1. `generate_llm_instructions.py`

**Base generator** used by all books.

**Classes:**
- `MarkdownParser` — Parse 5-layer markdown
- `JSONGenerator` — Transform to JSON v3.0
- `JSONValidator` — Validate output

**Key Methods:**
```python
# Usage
parser = MarkdownParser(Path('Books/clean-architecture/'))
generator = JSONGenerator(parser, metadata={...})
json_data = generator.generate()

errors = JSONValidator.validate(json_data)
```

**Customization Points:**
- Override `_generate_metrics(principle_id)` for custom metrics
- Override `_generate_scenarios(principle, ...)` for custom scenarios
- Override `_generate_anti_patterns(principle_id)` for domain-specific patterns

#### 2. `generators_clean_architecture.py`

**Specialized generator** for Clean Architecture book.

**Extends:** `JSONGenerator`

**Customizations:**
- 18 practical metrics specific to architecture
- 12 anti-patterns (God Object, tight coupling, etc)
- Real scenarios with quantified costs (hours, files changed)
- Context qualifiers (monolith, microservices, UI, startup, embedded)
- Implementation roadmaps for each principle

**Example:**
```python
class CleanArchitectureGenerator(JSONGenerator):
    def _generate_metrics(self, principle_id):
        # Custom metrics for each principle
    
    def _generate_anti_patterns(self, principle_id):
        # Clean Architecture-specific anti-patterns
```

#### 3. `build_all_llm_instructions.py`

**Orchestrator** that runs generators for all books.

**Features:**
- Auto-discovers books in `Books/` directory
- Selects appropriate generator per book
- Processes multiple books in sequence
- Generates summary report

**Usage:**
```python
# Find all books
books = find_book_directories(Path('Books/'))

# Process each
for book in books:
    success, message = process_book(book, verbose=True)
```

---

## Generator Selection

Generators are matched to books by directory name:

| Book Directory | Generator |
|---|---|
| `clean-architecture/` | `CleanArchitectureGenerator` |
| Others | `JSONGenerator` (generic) |

To add a specialized generator:

1. Create class: `class MyBookGenerator(JSONGenerator):`
2. Override methods as needed
3. Add to `get_generator_for_book()`:
   ```python
   if book_dir.name == 'my-book':
       return MyBookGenerator
   ```

---

## JSON v3.0 Format

### Key Differences from v2.0

| Aspect | v2.0 | v3.0 |
|--------|------|------|
| Metrics | Invented examples | Formulas + measurement methods |
| Scenarios | General | Specific with quantified costs |
| Anti-patterns | None | Grounded in reality |
| Context | Vague | Explicit boundaries |
| Code examples | Pseudo-code | Real language |
| When NOT to use | "Never" | Honest boundaries |

### Example Principle Object (v3.0)

```json
{
  "id": "principle_2",
  "principle": "Minimize Cost of Change",
  "scope": "system",
  "severity": "CRITICAL",
  
  "statement": "...",
  "reasoning": "...",
  
  "when_to_use": [
    "Design decisions",
    "Framework choices",
    "Long-term planning"
  ],
  
  "when_NOT_to_use": [
    "One-off scripts",
    "Throw-away prototypes",
    "Hard real-time systems"
  ],
  
  "practical_metrics": [
    {
      "name": "Cost per Feature",
      "formula": "total_hours / number_of_features",
      "good_value": "Should stay constant",
      "bad_value": "Increases > 15% per release",
      "example": {
        "calculation": "v1: 20h/feature, v2: 25h/feature",
        "interpretation": "BAD: degrading"
      }
    }
  ],
  
  "code_review_checklist": [
    "☐ Does this change touch only 1-3 files?",
    "☐ Can I change database without touching this?"
  ],
  
  "scenarios": [
    {
      "scenario": "Change discount logic",
      "bad_approach": {
        "description": "Mixed with DB, email, analytics",
        "cost": "4 hours",
        "problem": "Tight coupling"
      },
      "good_approach": {
        "description": "Isolated function",
        "cost": "30 minutes",
        "why_works": "No side effects"
      }
    }
  ],
  
  "anti_patterns": [
    {
      "name": "God Object",
      "looks_right": "Handles all logic, complete",
      "actually_wrong": "7+ dependencies, can't test",
      "solution": "Split by behavior"
    }
  ],
  
  "context_qualifiers": {
    "for_monolith": "Fully applicable",
    "for_microservices": "Apply per service",
    "for_startup": "Balance with speed"
  },
  
  "implementation_steps": [
    {
      "step": 1,
      "name": "Identify business core",
      "action": "Find code that never changes",
      "time": "1-2 days"
    }
  ]
}
```

---

## Quality Gates

Generated JSON must pass these checks:

```python
# Quality Gates (all must pass)
✓ Zero invented metrics (all have formulas)
✓ Every scenario quantified (cost specified)
✓ Every anti-pattern realistic (grounded in practice)
✓ when_NOT_to_use never empty (honest boundaries)
✓ All code real language, not pseudo-code
✓ All context_qualifiers filled
✓ FAQ scenarios real, not abstract
✓ Every principle has ≥1 metric
✓ Every principle has ≥1 checklist item
✓ Every principle has ≥1 scenario
```

Validation runs automatically. Warnings printed to console:

```
📖 Processing: clean-architecture
  ├─ Parsing markdown...
  ├─ Generating JSON...
  ├─ Validating...
  │  ⚠️  principle_3: Missing practical_metrics
  ├─ Saving...
  └─ ✓ Success!
```

---

## Customizing Generators

### Add Custom Metrics for a Principle

```python
class MyBookGenerator(JSONGenerator):
    def _generate_metrics(self, principle_id):
        if principle_id == 'principle_2':
            return [
                {
                    'name': 'Custom Metric',
                    'formula': 'calculation here',
                    'how_to_measure': 'step 1, step 2',
                    'good_value': 'target range',
                    'example': { ... }
                }
            ]
        return super()._generate_metrics(principle_id)
```

### Add Custom Scenarios

```python
def _generate_scenarios(self, principle, reasoning, consequences):
    if principle['id'] == 'principle_5':
        return [
            {
                'scenario': 'Your specific situation',
                'bad_approach': { ... },
                'good_approach': { ... }
            }
        ]
    return super()._generate_scenarios(principle, reasoning, consequences)
```

### Add Anti-Patterns

```python
def _generate_anti_patterns(self, principle_id):
    if principle_id == 'principle_2':
        return [
            {
                'name': 'Anti-pattern name',
                'looks_right': '...',
                'actually_wrong': '...',
                'cost': '...',
                'solution': '...'
            }
        ]
    return super()._generate_anti_patterns(principle_id)
```

---

## Markdown Parsing

### Expected Structure

Files must follow naming convention:
- `00_*.md` — Purpose
- `01_*.md` — Questions
- `02_*.md` — Ideas
- `03_*.md` — Reasoning
- `04_*.md` — Consequences

### Principle Extraction

Parser looks for principles in `02_ideas.md`:

```markdown
## Principle 1

### Statement

Clear statement here.

### Key Rules

- Rule 1
- Rule 2
```

**Parser extracts:**
- Principle ID (from ## header)
- Principle name (from ## header)
- Statement (first paragraph)

### Limitations & Future Improvements

Current parser is basic. Future improvements:

- [ ] Support more flexible markdown structures
- [ ] Extract from YAML frontmatter
- [ ] Handle metadata JSON headers
- [ ] Extract scenarios with cost annotations
- [ ] Auto-generate anti-patterns from principles
- [ ] Validate markdown before generation

**Workaround:** If markdown doesn't parse correctly, data can be provided via:
- Specialized generator override
- Metadata JSON in book directory
- YAML frontmatter in markdown

---

## Testing

### Test Single Book

```bash
python generate_llm_instructions.py ../Books/clean-architecture/
```

**Output:**
- `05_llm_instructions.json` created
- Validation report printed
- Errors logged if any

### Validate Existing JSON

```python
from generate_llm_instructions import JSONValidator
import json

with open('05_llm_instructions.json') as f:
    data = json.load(f)

errors = JSONValidator.validate(data)
for error in errors:
    print(f"✗ {error}")
```

### Debug Parsing

```python
from generate_llm_instructions import MarkdownParser

parser = MarkdownParser(Path('Books/clean-architecture/'))

# Check what was parsed
print("Purpose:", parser.extract_purpose())
print("Principles:", parser.extract_principles())
```

---

## Troubleshooting

### No principles found
- Check `02_ideas.md` exists
- Verify markdown headers match expected pattern
- Run with `--verbose` flag

### Metrics empty
- Override `_generate_metrics()` in specialized generator
- Check principle ID in custom generator

### JSON validation warnings
- Add missing sections to principle
- Ensure metrics have formulas
- Quantify all scenarios
- Fill all context_qualifiers

### Markdown not parsing correctly
- Check file structure: `00_purpose.md`, `01_questions.md`, etc
- Verify principle headers: `## Principle 1`
- Debug with: `parser.extract_principles()`

---

## Performance

| Operation | Time |
|-----------|------|
| Parse single book | < 1 second |
| Generate JSON | < 1 second |
| Validate | < 1 second |
| Generate 5 books | < 5 seconds |

---

## Files Generated

```
Books/
└── clean-architecture/
    ├── 00_purpose.md (input)
    ├── 01_questions.md (input)
    ├── 02_ideas.md (input)
    ├── 03_reasoning.md (input)
    ├── 04_consequences.md (input)
    └── 05_llm_instructions.json (OUTPUT)
```

**Size:** ~20-50 KB per JSON file

**Format:** Pretty-printed JSON (2-space indent)

---

## Integration

### With LLM (Claude/GPT)

```
1. Generate JSON: python build_all_llm_instructions.py Books/
2. Copy Books/clean-architecture/05_llm_instructions.json
3. Open new Claude conversation
4. Paste content or system_instruction section
5. Ask LLM to apply principles to your code
```

### With CI/CD

```bash
# Add to your CI pipeline
- name: Generate LLM Instructions
  run: |
    python scripts/build_all_llm_instructions.py Books/ --verbose
    
- name: Commit changes
  run: |
    git add Books/*/05_llm_instructions.json
    git commit -m "Update LLM instructions"
```

### With Code Review

```python
# Use code_review_checklist from JSON
# In code review template, include:
# "Does this change pass principle_2 checks?"
# Reference: Books/clean-architecture/05_llm_instructions.json
```

---

## References

- `reference/pipeline-complete.md` — Full pipeline documentation (Pass 1-5)
- `reference/json-generation-spec.md` — JSON v3.0 specification
- `reference/process.md` — How to create markdown (Pass 1-3)
- `SKILL.md` — Book Compiler skill
- `LLM_USAGE_GUIDE.md` — How to use JSON with LLMs

---

## Next Steps

1. ✅ Scripts created
2. ⏳ Test on Clean Architecture
3. ⏳ Adapt markdown parser if needed
4. ⏳ Generate JSON for all 5 books
5. ⏳ Validate all outputs
6. ⏳ Document usage for each book

---

## Contributing

To add a new specialized generator:

1. Create `generators_my_book.py`
2. Extend `JSONGenerator`
3. Override methods:
   - `_generate_metrics()`
   - `_generate_scenarios()`
   - `_generate_anti_patterns()`
   - etc
4. Add to `build_all_llm_instructions.py`:
   ```python
   if book_dir.name == 'my-book':
       return MyBookGenerator
   ```
5. Test: `python build_all_llm_instructions.py Books/ --book my-book`

---

**Version:** 3.0  
**Last Updated:** 2026-08-09  
**Status:** Ready for testing on all 5 books
