# How to Use Clean Architecture JSON with LLM (v3.0)

**For Claude, GPT, or any LLM**

---

## The File: What It Contains

You have: `Books/clean-architecture/05_llm_instructions.json`

This JSON is **NOT a summary**. It's a **professional system prompt** for architectural guidance.

**It contains:**
- ✅ 15 core principles (with statements, not just names)
- ✅ 10 supporting arguments (with empirical evidence)
- ✅ 12 practical implications (real applications)
- ✅ 10 central questions (for decision-making)
- ✅ Code review checklists (actionable items)
- ✅ Practical metrics (formulas to measure)
- ✅ Anti-patterns (what looks right but is wrong)

**What's NOT in it:**
- ❌ No invented examples
- ❌ No made-up metrics or costs
- ❌ No pseudo-code
- ❌ No guessing

Everything is sourced from the book.

---

## Method 1: Use as System Prompt (Simple)

### Step 1: Copy the system_instruction

```bash
# Get the system instruction from the JSON
cat Books/clean-architecture/05_llm_instructions.json | jq '.system_instruction'
```

### Step 2: Paste into Claude

Open a new Claude conversation. Paste this into the first message:

```
[Paste the system_instruction here]

Now help me review this code through the lens of Clean Architecture principles.
```

### Step 3: Ask LLM to review

Paste your code. Ask:

```
Review this code against Clean Architecture principles. 
Cite which principles apply. 
Reference supporting arguments for evidence.
Show how to improve it.
```

**LLM will now:**
- Reference principle IDs
- Show supporting evidence
- Provide actionable recommendations
- Avoid hallucinations

---

## Method 2: Use Specific Principles (Advanced)

### If you want principle-specific guidance:

```json
{
  "system_instruction": "[full system instruction here]",
  "focus_principle": "principle_2",
  "principle_detail": {
    "id": "principle_2",
    "principle": "The Goal of Architecture is Minimizing Human Effort",
    "statement": "...",
    "supporting_arguments": [ ... ],
    "related_implications": [ ... ],
    "code_review_checklist": [ ... ],
    "practical_metrics": [ ... ]
  }
}
```

### Example prompt:

```
I'm concerned about the cost of change in my system.

Here's the principle that applies:
[Paste principle_2 object from JSON]

My code:
[Your code]

Does my code follow this principle?
```

---

## Method 3: Code Review Workflow (Professional)

### For team code reviews:

```
I'll review this PR through Clean Architecture lens.

Here are the applicable principles:
[Paste principle_2, principle_3, principle_9]

Here's the code:
[Code from PR]

For each principle:
1. Does it violate the principle?
2. What's the supporting argument?
3. What does the code_review_checklist say?
4. What would practical_implications recommend?
```

**LLM now acts as:**
- Code reviewer
- Architect
- Evidence provider
- Practical guide

---

## Method 4: Design Discussion (Architecture)

### When making design decisions:

```
I'm deciding between:
A) [Option A]
B) [Option B]

Here's the decision framework from Clean Architecture:
[Paste quick_reference section]

Which aligns better with the principles?
Why?
What does the evidence show?
```

---

## Method 5: Team Advocacy (Explaining to Managers)

### When you need to defend architecture:

```
Manager: "Skip the tests, we need this feature in 2 weeks."

Here's what Clean Architecture says:

[Paste principle_4 with supporting_arguments]

The evidence shows:
[Quote from arg_003: False Economy experiment]

So the answer is: [...]
```

---

## What to Copy-Paste for Different Scenarios

### Scenario 1: "This code is a mess. Where do I start?"

Copy:
- principle_2 (Minimize Cost of Change)
- principle_8 (Technical Debt)
- related_implications for both

### Scenario 2: "How do I convince my team to refactor?"

Copy:
- supporting_arguments (with empirical data)
- practical_metrics (show cost over time)
- faq section

### Scenario 3: "Is this architectural decision right?"

Copy:
- decision_guide
- related_questions
- supporting_arguments

### Scenario 4: "How should I test this?"

Copy:
- principle_7 (Testing Philosophy)
- code_review_checklist items
- related_implications

---

## Red Flags: When to Question LLM

Even with this JSON, you should verify when LLM:

❌ **Cites a principle that isn't in the JSON**
→ Ask it to show the exact principle_id

❌ **Invents a metric or cost**
→ Check if it's in practical_metrics section

❌ **Recommends something without evidence**
→ Ask: "Which supporting_argument justifies this?"

❌ **Forces a principle when it doesn't apply**
→ Check related_implications - does it actually apply to your situation?

✅ **Good sign**: LLM quotes principle IDs, cites source lines, references supporting_arguments

---

## Example Interaction

### You:
```
Review this TypeScript code:

class UserService {
  saveUser(user: User) {
    db.save(user);           // Direct DB call
    email.send(user.email);  // Direct email call
    analytics.log(user);     // Direct analytics call
  }
}

Does this follow Clean Architecture?
```

### Good LLM response (with this JSON):

```
This violates principle_2: Minimize Cost of Change.

Supporting evidence (principle_2.supporting_arguments):
- ARG-001: Productivity Collapse
- ARG-003: False Economy

The problem:
- UserService depends directly on DB, Email, Analytics
- Changing any of these requires changing UserService
- Cost increases: blast_radius = 3 files minimum

Practical metric (principle_2.practical_metrics):
- Formula: hours_spent / features_delivered
- This code: one change = 3x effort (change DB + email + analytics)

Code review checklist (principle_2.code_review_checklist):
- ☐ Are dependencies injected? NO - they're hardcoded
- ☐ Can we change database without touching this? NO

Related implication (principle_2.related_implications):
- IMPL-002: Use Polymorphism to Cross Boundaries
  "Instead of UserService depending on concrete classes,
   it should depend on Repository, EmailService, AnalyticsService interfaces"

Recommendation:
```typescript
class UserService {
  constructor(
    private repository: UserRepository,
    private emailService: EmailService,
    private analyticsService: AnalyticsService
  ) {}

  saveUser(user: User) {
    this.repository.save(user);
    this.emailService.send(user.email);
    this.analyticsService.log(user);
  }
}
```

This way, UserService changes only when business logic changes, not when infrastructure changes.
```

---

## Best Practices

### DO:
✅ Ask LLM to cite principle IDs  
✅ Ask LLM to show supporting_arguments  
✅ Ask LLM to use code_review_checklist items  
✅ Ask LLM to reference metrics with formulas  
✅ Ask for concrete code examples (bad → good)  
✅ Ask when and when NOT to apply  

### DON'T:
❌ Accept principles without IDs  
❌ Accept metrics without formulas  
❌ Let LLM invent examples or costs  
❌ Force a principle into every discussion  
❌ Ignore context (startup vs enterprise, etc)  
❌ Skip verifying against the JSON  

---

## Full Workflow for Architecture Review

```
1. IDENTIFY applicable principles
   → Which principles_to_use = []?

2. READ the principles
   → statement, tags, related_questions

3. GATHER evidence
   → supporting_arguments with evidence

4. CHECK practice
   → related_implications with practical_adoption

5. REVIEW code
   → code_review_checklist items

6. MEASURE impact
   → practical_metrics formulas

7. RECOMMEND changes
   → Show bad_approach → good_approach
   → Quantify improvement
   → Reference principle_id + source
```

---

## JSON File Locations

```
📁 Books/
└─ 📁 clean-architecture/
   ├─ 00_purpose.md
   ├─ 01_questions.md
   ├─ 02_ideas.md
   ├─ 03_reasoning.md
   ├─ 04_consequences.md
   └─ 05_llm_instructions.json ← USE THIS

Shortcut (one file):
Books/clean-architecture/05_llm_instructions.json
```

---

## Troubleshooting

### "LLM is hallucinating"
→ Add to your prompt: "Only cite what's in this JSON. If not in JSON, say 'not in JSON'."

### "LLM is not being specific"
→ Ask: "Cite the principle_id. Quote the supporting_argument."

### "Different LLM = different answers"
→ Paste the full system_instruction at the start. It guides behavior.

### "Principle doesn't seem to apply"
→ Check when_NOT_to_use section if it exists. Read related_questions for context.

---

## Updates

**This guide applies to:** JSON v3.0 (generated 2026-08-09)

**Format:** Clean Architecture principles with smart linking

**Quality:** No invented data. All sourced from markdown model.

**Traceability:** Every element references source (line numbers, sections)

---

## Questions?

If LLM isn't applying principles correctly:

1. Check if principle_id is in JSON
2. Verify supporting_arguments exist
3. Read related_implications for practical context
4. Ask LLM to quote from JSON verbatim

Everything is traceable. You can always verify.

---

**Remember:** This JSON is a professional tool. Use it to apply real principles, not to excuse decisions. Good architecture takes discipline, but it's worth it.
