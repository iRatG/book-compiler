# LLM Instructions Usage Guide

## What is 05_llm_instructions.json?

The **6th layer** of every book — a machine-readable compilation of principles from layers 2-4 (Ideas, Reasoning, Consequences).

Instead of reading a 50-page book, you can load a single JSON file into a conversation and Claude/GPT will understand the book's core principles and apply them.

---

## What Each File Contains

```json
{
  "metadata": {
    "title": "Clean Architecture",
    "author": "Robert C. Martin",
    "format_version": "1.0"
  },
  "system_instruction": "You are guided by Clean Architecture principles...",
  "principles": [
    {
      "id": "principle_1",
      "principle": "Clear statement",
      "reasoning": "Why this matters",
      "tags": ["#architecture", "#cost-reduction"],
      "severity": "CRITICAL"
    }
  ],
  "faq_for_llm": [...]
}
```

---

## How to Use

### Option 1: System Prompt (Recommended)

Paste the `system_instruction` + principles into your system prompt:

```
You are an expert code reviewer guided by Clean Architecture principles.

When reviewing code:
- Minimize cost of change (principle_1)
- Separate business logic from delivery (principle_2)
- Invert dependencies toward abstractions (principle_3)

Reference: Books/clean-architecture/05_llm_instructions.json
```

### Option 2: Conversation Start

At the beginning of a conversation:

```
Here are the principles I want you to follow:
[paste content from 05_llm_instructions.json]

Now let's discuss my architecture...
```

### Option 3: Code Review with Multiple Books

Load principles from multiple books:

```
Principles from Clean Architecture: [JSON from book 1]
Principles from The Pragmatic Programmer: [JSON from book 2]
Principles from Code That Fits in Head: [JSON from book 3]

Review this code through all three lenses:
[code here]
```

---

## Books Available (11 Total)

| Book | Principles | Language | Key Tags |
|------|-----------|---|------|
| Clean Architecture | 6 | English | #architecture, #cost-of-change, #paradigms |
| Ideal Work (Clean Coder) | 6 | English | #craftsmanship, #tdd, #professionalism, #ethics |
| Pragmatic Programmer | 7 | English | #dry, #automation, #risk-management, #estimation |
| Parallel Programming | 7 | English | #concurrency, #synchronization, #performance |
| Code That Fits in Head | 8 | English | #readability, #cognitive-load, #simplicity |
| Clean Code | 15 | Russian | #craftsmanship, #readability, #naming |
| Philosophy of Software Design | 10+ | English | #design, #systems-thinking |
| Domain-Driven Design | 10+ | English | #domain-modeling, #patterns |
| Concepts in Programming Languages | 10+ | English | #language-design, #paradigms |
| Architect Elevator | 8+ | English | #architecture, #leadership, #organization |
| **Refactoring** ⭐ | **20** | English | #refactoring, #code-quality, #design, #testing, #behavior-preservation |

**Note:** All 05_llm_instructions.json files are in English, regardless of whether layers 00-04 are in Russian or English. This enables universal LLM compatibility.

---

## Example: Code Review Using LLM Instructions

### Setup

```bash
# Load Clean Architecture principles
cat Books/clean-architecture/05_llm_instructions.json
```

### In Claude

```
You are a code architect guided by these principles from Clean Architecture:
[paste JSON]

Review this code:

```python
class UserController:
    def __init__(self, db):
        self.db = db
    
    def create_user(self, name, email):
        # Business logic mixed with database
        sql = f"INSERT INTO users VALUES ({name}, {email})"
        self.db.execute(sql)
        return {"status": "ok"}
```

What principles are violated? How to fix?
```

### Claude Responds

```
Violations:
1. **principle_2** (dependency inversion): Controller depends on concrete DB, not abstraction
2. **principle_1** (minimize cost): Changing DB adapter requires changing business logic
3. **implication_2**: No separation between business logic and delivery mechanism

Fix:
- Extract business logic to UserService
- Define UserRepository interface
- Inject repository into controller
```

---

## Programmatic Usage

### Python

```python
import json

# Load principles
with open('Books/clean-architecture/05_llm_instructions.json') as f:
    instructions = json.load(f)

# Get all CRITICAL principles
critical = [p for p in instructions['principles'] if p['severity'] == 'CRITICAL']

# Get principles by tag
architecture_principles = [
    p for p in instructions['principles']
    if any('#architecture' in tag for tag in p.get('tags', []))
]
```

### LLM Prompt

```
System Principles (from Clean Architecture):
{
  "principles": [
    {% for principle in principles %}
    - {{ principle.principle }} (#{{ principle.id }})
    {% endfor %}
  ]
}

User Query: [user asks something]

Apply the principles above when responding.
```

---

## Generation

To regenerate all files:

```bash
python generate-llm-instructions.py Books/clean-architecture
python generate-llm-instructions.py Books/ideal-work
# etc...

# Or batch:
for book in Books/*/; do
  python generate-llm-instructions.py "$book"
done
```

---

## Examples: Using Refactoring (NEW)

### Example 1: Identify Code Smells

```
Paste: Books/refactoring/05_llm_instructions.json

Question: What code smells does this function have?

code:
function processPayment(user, amount, cardToken, db, logger) {
    // 200 lines mixing payment logic, logging, database access
}

Claude will reference:
- Long Parameter List smell → Introduce Parameter Object
- Long Function smell → Extract Function
- Feature Envy → Move Function
- And suggest specific refactorings from principle_8 (22 code smells)
```

### Example 2: Justify Refactoring to Management

```
Paste: Books/refactoring/05_llm_instructions.json

Question: How do I justify this refactoring to my manager?

Context: I want to refactor our payment module (1 week effort) before adding 
multi-currency support. Without refactoring, multi-currency will take 3 weeks.

Claude will use principle_6 (economic justification):
"Your refactoring will make the next change 3x faster. That's the fastest 
way to work. It's not about 'clean code'—it's about business speed."
```

### Example 3: Combine Refactoring + Architecture

```
Paste: Books/clean-architecture/05_llm_instructions.json
Paste: Books/refactoring/05_llm_instructions.json

Question: Our architecture is clear but code is tangled. How do we bridge the gap?

Claude will show how refactoring (principle_1: behavior-preserving) 
enables the architecture principles to actually manifest in code.
```

---

## Advanced: Combining Multiple Books

Load principles from multiple books in one system:

```json
{
  "clean_architecture": { /* principles from book 1 */ },
  "pragmatic_programmer": { /* principles from book 2 */ },
  "refactoring": { /* principles from book 3 */ }
}
```

Then when reviewing code or discussing design:

```
Evaluate this code/architecture against all three books' principles.
Report violations with reference to principle IDs from each book.

For example:
- Clean Architecture violation (principle_2): Layer boundary crossed
- Pragmatic Programmer violation (principle_2): Estimate not met due to poor structure
- Refactoring opportunity (principle_8): Code smell "Feature Envy" detected
```

---

## What NOT to Do

❌ Don't just read the JSON and guess what it means  
❌ Don't use principles from the wrong context (e.g., concurrency principles for web requests)  
❌ Don't treat FAQ as exhaustive — they're just examples  
✅ Do load system_instruction first  
✅ Do reference principle IDs in feedback  
✅ Do combine multiple books when appropriate  

---

## Format Stability

- `format_version: "1.0"` is stable
- Field order may change; use by name not position
- Tags are always hashtagged (#tag-name)
- IDs follow pattern: principle_N, arg_N, implication_N
