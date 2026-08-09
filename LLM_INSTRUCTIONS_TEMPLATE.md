# LLM Instructions JSON Template (v2.0)

This template shows how to structure `05_llm_instructions.json` for **maximum LLM effectiveness**.

Use Clean Architecture's JSON as the reference implementation:
- [Books/clean-architecture/05_llm_instructions.json](Books/clean-architecture/05_llm_instructions.json)

---

## Structure Overview

```json
{
  "metadata": {
    "title": "Book Title",
    "author": "Author Name",
    "format_version": "2.0",
    "language": "English",
    "purpose": "What this book teaches"
  },

  "system_instruction": "Direct prompt for LLM. Paste at conversation start.",

  "quick_reference": {
    "core_goal": "Main idea",
    "top_3_principles": ["Principle 1", "Principle 2", "Principle 3"]
  },

  "principles": [
    {
      "id": "principle_1",
      "principle": "Short, actionable statement",
      "scope": "system/module/function",
      "severity": "CRITICAL/HIGH/MEDIUM",
      
      "statement": "Expanded statement",
      "reasoning": "Why this matters in practice (1-2 sentences)",
      
      "when_to_use": [
        "Situation 1",
        "Situation 2"
      ],
      "when_not_to_use": "Exception or tradeoff",
      
      "key_rules": [
        "Rule 1 - actionable",
        "Rule 2 - actionable"
      ],
      
      "bad_example": {
        "situation": "Context",
        "code": "❌ Don't do this",
        "why_bad": "Explicit consequence",
        "cost": "What breaks in real projects"
      },
      
      "good_example": {
        "situation": "Same context",
        "code": "✓ Do this instead",
        "why_works": "Concrete benefit",
        "benefit": "Real improvement"
      },
      
      "trade_offs": "What you give up by following this",
      
      "decision_criteria": {
        "pressure_1": "Factor A",
        "pressure_2": "Factor B",
        "resolution": "How to decide"
      },
      
      "common_misconceptions": [
        {
          "myth": "People often think...",
          "truth": "Actually..."
        }
      ],
      
      "how_to_measure": "How to verify this principle is applied correctly",
      
      "related_principles": ["principle_2", "principle_5"],
      
      "tags": ["#tag1", "#tag2"],
      
      "real_world_story": "Actual scenario from real project that illustrates this principle"
    }
  ],

  "decision_guide": {
    "when_uncertain_ask": [
      "Question 1 to ask yourself",
      "Question 2 to ask yourself"
    ]
  },

  "faq": [
    {
      "question": "Common question?",
      "answer": "Concise answer with principle reference",
      "principle_ref": "principle_1"
    }
  ],

  "tags": ["#tag1", "#tag2"],

  "version_info": {
    "book_edition": "Which edition?",
    "json_version": "2.0",
    "english_translated": true
  }
}
```

---

## Key Design Principles for LLM Effectiveness

### 1. **Concrete Examples Over Philosophy**
- ❌ "Separation of concerns is important"
- ✅ "When database logic mixes with business logic, changing the database requires rewriting business rules. Separate them."

### 2. **Bad AND Good Examples**
- Always show what NOT to do
- Always show what TO do instead
- Always explain WHY

### 3. **Real-World Stories**
- Not textbook examples
- Actual scenarios from real projects
- Show the cost of ignoring the principle

### 4. **Common Misconceptions**
- Address what developers often get wrong
- Correct the misunderstanding
- Explain why the truth matters

### 5. **Measurement Criteria**
- How do you know this principle is working?
- What metrics to track?
- How to verify implementation?

### 6. **Related Principles**
- Link to other principles in the same book
- Show how they work together
- Prevent treating principles in isolation

### 7. **Decision Criteria**
- When should you apply this? 
- What are the trade-offs?
- How to decide if it's worth the cost?

---

## Writing Guide for Each Section

### Statement
- One clear sentence
- Actionable, not philosophical
- What the principle IS, not why

### Reasoning
- 1-2 sentences max
- WHY this matters in practice
- Impact on real projects

### When to Use
- List 3-5 specific situations
- Not abstract, but concrete scenarios

### Key Rules
- 3-5 rules max
- Each is actionable (you can implement it)
- Starts with a verb

### Bad Example
- Show a realistic mistake
- Include code snippet
- Explain the consequence
- Quantify the cost (if possible)

### Good Example
- Same scenario, proper solution
- Include code snippet
- Explain why it works
- Show the benefit

### Trade-Offs
- What do you give up by following this?
- When might you intentionally violate it?
- When is the cost worth it?

### Common Misconceptions
- What do experienced developers get wrong?
- What's the truth?
- Why does the myth exist?

### Real-World Story
- 2-3 paragraphs max
- Actual project scenario
- What happened when principle was ignored
- What would have happened if followed

### How to Measure
- Specific, not vague
- Can someone actually track this?
- Examples: "Lines of code changed per feature", "Time to add new functionality"

---

## Checklist for Each Principle

- [ ] Statement is clear and actionable
- [ ] Reasoning explains WHY (not WHAT)
- [ ] When to use lists 3-5 specific scenarios
- [ ] Key rules are actionable (not philosophical)
- [ ] Bad example includes code and consequence
- [ ] Good example shows the fix
- [ ] Trade-offs are explicit
- [ ] Common misconceptions address real confusion
- [ ] How to measure is specific and trackable
- [ ] Real-world story is realistic
- [ ] Related principles are linked
- [ ] Tags are consistent with other principles
- [ ] Everything is in English
- [ ] No jargon without explanation
- [ ] A junior developer could understand it

---

## Priority for Other Books

### High Priority (Do Next)
1. **Ideal Work (The Clean Coder)** - About professionalism, ethics, TDD
2. **The Pragmatic Programmer** - Practical wisdom

### Medium Priority  
3. **Code That Fits in Your Head** - About cognitive load and simplicity

### Lower Priority (But Important)
4. **Parallel Programming** - More specialized, fewer people implement it

---

## Tips

- **English Only** — LLMs understand English better than translations
- **Code Examples** — Always show in code, not pseudo-code
- **Specificity** — "2 hours to add feature" > "faster"
- **Ruthless** — Cut anything not actionable
- **Link Principles** — Show how they work together
- **Test with LLM** — Paste the JSON into Claude and ask it to apply the principles to sample code

---

## Validation

Before submitting:
1. Is JSON valid? `python -m json.tool file.json`
2. Can you copy/paste the system_instruction into Claude?
3. Does Claude understand and apply the principles?
4. Would a junior developer understand each principle?
5. Is everything in English?
