# HOW TO ACTUALLY USE book-compiler IN REAL WORK

**Version:** Practical Guide  
**Audience:** Programmers, architects, teams  
**Goal:** Show 5 real usage patterns (not theory)

---

## ⚠️ IMPORTANT: Three Levels of Using These Books

### Level 1: Copy-Paste (Easiest, Immediate)
```
Open Claude/GPT
Paste: Books/clean-architecture/06_agent_rules.md
Ask: "Review this code for architectural issues"
→ Claude applies the rules directly
```

### Level 2: System Prompt (Better, Persistent)
```
In your Claude Code / GPT settings:
1. Create a "system instruction" entry
2. Paste: Books/clean-architecture/05_llm_instructions.json
3. Now EVERY conversation uses Clean Architecture principles
```

### Level 3: Custom Integration (Best, Programmatic)
```
Read the JSON programmatically
Extract principles you need
Build custom prompts for YOUR domain
(E.g., extract "refactoring" principles only for legacy system work)
```

---

## 🎯 FIVE REAL-WORLD USAGE PATTERNS

### PATTERN 1: Code Review Using Rules

**Situation:** You have code to review. Want to check against best practices.

**How to do it:**

```
Step 1: Copy the agent rules
$ cat Books/clean-architecture/06_agent_rules.md

Step 2: Open Claude Code
/new

Step 3: Paste at the start
---
You are a code architect. Apply these rules when reviewing:

[paste content of 06_agent_rules.md here]

Now review this code for violations:
[your code here]
---

Step 4: Claude will say:
"Violations:
- R1: Architecture is embedded at all levels (violated: no DI)
- R2: Cost-of-change metric (violated: 1 feature = 3 file changes)
- R3: Architectural decision made collaboratively (violated: no review)

Fix recommendations:
1. Extract interfaces for dependencies
2. Consolidate change coupling
3. Discuss with team"
```

**Why this works:** Claude understands rules, sees your code, applies each rule, explains violations.

---

### PATTERN 2: Architecture Decision Making

**Situation:** You're deciding between two designs. Which is better?

**How to do it:**

```
Step 1: Load multiple books
[Paste Books/clean-architecture/05_llm_instructions.json]
[Paste Books/pragmatic-programmer/05_llm_instructions.json]
[Paste Books/code-fits-in-head/05_llm_instructions.json]

Step 2: Ask Claude
"We're choosing between:

Option A: Monolith with clear layers (easy to understand, hard to scale)
Option B: Microservices (easy to scale, harder to understand)

Which is better? Check against all three books' principles."

Step 3: Claude will say:
"Through Clean Architecture lens:
- Option A: Better (cost-of-change is lower for small-medium teams)
- Option B: Adds architecture complexity (violates: minimize change cost)

Through Pragmatic Programmer lens:
- Option A: Better (YAGNI principle: don't build for scale you don't have)
- Option B: Okay if you have operational excellence (CI/CD, monitoring)

Through Code That Fits lens:
- Option A: Better (cognitive load is lower; devs understand whole system)
- Option B: Risk (each service becomes complex; understanding fails)

Recommendation: Option A until your traffic forces Option B"
```

**Why this works:** Rules are checkpoints. Multiple books = multiple perspectives. Helps you make REASONED decisions, not rushed ones.

---

### PATTERN 3: Justifying Refactoring to Manager

**Situation:** Manager says "Why spend 2 weeks refactoring? Just ship features!"

**How to do it:**

```
Step 1: Load Refactoring book
[Paste Books/refactoring/06_agent_rules.md]

Step 2: Load Pragmatic Programmer  
[Paste Books/pragmatic-programmer/05_llm_instructions.json]

Step 3: Ask Claude
"Our code is tangled. Refactoring this module will take 2 weeks.
Manager says 'just ship features'. How do I justify refactoring?"

Step 4: Claude will quote:
"From Refactoring (R2: Design Stamina Hypothesis):
'Good design allows you to go faster for longer.
Teams that neglect design eventually ship nothing because 
they're bogged down in complexity.'

From Refactoring (R12: Justify economically):
'Refactoring now = next feature is 3x faster
This is the fastest way to work.'

Evidence: After refactoring similar module last quarter,
we added 5 features in 3 weeks (vs. 1 feature in 3 weeks before).

Ask manager: Would you rather:
- Spend 2 weeks now → 5 features/month later
- Skip refactoring → 1 feature/month forever?"
```

**Why this works:** Rules include ECONOMIC justification. Not "clean code is pretty" but "clean code is FASTER". Managers understand speed.

---

### PATTERN 4: Teaching Junior Developers

**Situation:** New developer on team. Teach them your standards.

**How to do it:**

```
Option A: Copy-paste rules
Step 1: Paste Books/clean-code/06_agent_rules.md to team Slack
Step 2: Say: "These are our code standards. Review against them."
Step 3: In code reviews, reference rules: "R3 violation: extract function"

Option B: Use as onboarding
Step 1: First day for junior: "Read these 5 docs"
- Books/clean-code/00_purpose.md (5 min)
- Books/clean-code/02_ideas.md (30 min)
- Books/clean-code/06_agent_rules.md (20 min)

Step 2: Next day: "Apply these rules in your PR"

Step 3: Code review: "R2 violation: your function is 80 lines; 
should be 3-5. See example in 04_consequences.md"

Why: Junior learns principles, not just "we do it this way"
```

**Why this works:** Rules are TEACHABLE. Not vague ("write clean code") but specific ("function <20 lines, clear name, single purpose").

---

### PATTERN 5: Architectural Review Meeting

**Situation:** Team meeting. Reviewing system design. Need common framework.

**How to do it:**

```
Before meeting:
Step 1: Export agent rules
$ cat Books/clean-architecture/06_agent_rules.md > /tmp/review-checklist.md

Step 2: Send to team: "Use this checklist for our review"

During meeting:
Step 3: Go through each rule
R1: "Does every developer own architecture at their level?"
    Team: "Yes, code reviews include structural feedback"
    ✓ PASS

R2: "Do we measure cost-of-change over time?"
    Team: "No, we only track velocity"
    ✗ FAIL → Action: Start measuring cycle time

R3: "Do we balance behavior (urgent) vs. architecture (important)?"
    Team: "Sometimes we skip refactoring under deadline"
    ⚠️ RISK → Action: Budget refactoring into sprints

Step 4: Decide next actions based on rule violations

Why: Framework is OBJECTIVE, not opinion-based
```

**Why this works:** Rules are conversation starters. Not "this code is bad" but "this code violates R2; here's what we can do."

---

## 🔄 THE WORKFLOW

### Daily Use

```
┌─────────────────────────────────────────┐
│ You have code/design question           │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│ 1. Decide which book applies            │
│    (Architecture? Clean Code? Tests?)    │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│ 2. Copy rules (06_agent_rules.md)       │
│    OR JSON (05_llm_instructions.json)   │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│ 3. Paste into Claude / LLM conversation │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│ 4. Ask question with your code/design   │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│ 5. Claude applies rules, explains        │
│    with source references               │
└────────────┬────────────────────────────┘
             │
             ↓
┌─────────────────────────────────────────┐
│ 6. You get: violations + fixes +        │
│    reasoning from expert author         │
└─────────────────────────────────────────┘
```

---

## 📚 WHICH BOOK FOR WHICH PROBLEM?

| Problem | Book | File | Why |
|---------|------|------|-----|
| **Architecture decision** | Clean Architecture | 06_agent_rules.md | Principles of structure |
| **Code is hard to read** | Clean Code | 06_agent_rules.md | Naming, function size, clarity |
| **Refactoring code** | Refactoring | 06_agent_rules.md | 22 smells, 66 patterns |
| **Testing strategy** | Ideal Work | 06_agent_rules.md | TDD, professionalism |
| **Estimation/timeline** | Pragmatic Programmer | 06_agent_rules.md | Realistic commitments |
| **Concurrent code** | Parallel Programming | 05_llm_instructions.json | Locks, threading, memory |
| **Legacy system** | Refactoring | 06_agent_rules.md | How to work safely |
| **API design** | Code That Fits | 06_agent_rules.md | User perspective, simplicity |
| **Business alignment** | Architect Elevator | 06_agent_rules.md | Technical ↔ business bridge |
| **Design patterns** | Domain-Driven Design | 05_llm_instructions.json | Modeling, aggregates, ubiquitous language |

---

## ⚠️ COMMON MISTAKES

### ❌ MISTAKE 1: Paste JSON, forget to ask

```
Wrong:
[Paste 05_llm_instructions.json]
[Wait for Claude to respond]
→ Nothing happens; JSON alone is not a question

Right:
[Paste 05_llm_instructions.json]
"My service is getting too big. How should I split it?
Reference principle_5 (decomposition)."
→ Claude now applies principle_5 to YOUR situation
```

### ❌ MISTAKE 2: Ignore the agent rules; use only JSON

```
Wrong:
[Use only 05_llm_instructions.json for everything]
→ You get raw principles, but not actionable rules

Right:
[Use 06_agent_rules.md for practical decisions]
[Use 05_llm_instructions.json for detailed reasoning]
→ Rules → Decisions, JSON → Understanding
```

### ❌ MISTAKE 3: Treat rules as gospel

```
Wrong:
"R2 says functions < 20 lines, so I must split this 25-line function"
→ Cargo cult programming (rules without judgment)

Right:
"R2 recommends functions < 20 lines because readability.
This 25-line function is clear (good names, single purpose).
Keep it OR split if we find it's reused."
→ Rules are guidelines, not laws
```

### ❌ MISTAKE 4: Use wrong book for the problem

```
Wrong:
"I need to refactor my code" → Paste Clean Architecture
→ Clean Architecture is about system-level structure,
  not individual function extraction

Right:
"I need to refactor my code" → Paste Refactoring
→ Refactoring has 22 code smells + 66 patterns
  for exactly this situation
```

---

## ✅ BEST PRACTICES

### ✅ DO THIS

1. **Keep agent rules (06_agent_rules.md) as team checklist**
   - Print it (2-3 pages per book)
   - Reference in code reviews
   - Use in architecture discussions

2. **Use JSON (05_llm_instructions.json) for reasoning**
   - When you need evidence for a decision
   - When justifying to manager
   - When teaching why a rule exists

3. **Rotate between books by problem**
   - Don't use only Clean Architecture
   - Don't use only Clean Code
   - Pick the book that solves THIS problem

4. **Quote sources in discussions**
   - "Clean Architecture R2 says..."
   - "Refactoring principle_8 about polymorphism..."
   - Gives weight to decisions; not just "I think..."

5. **Let Claude explain trade-offs**
   - "When not to use this rule" is in the rules
   - Ask: "Does this apply to our case?"
   - Don't blindly apply; apply with judgment

---

## 🎯 EXAMPLE: REAL CONVERSATION

**Setup:**
```
Claude Code conversation.
Paste: Books/refactoring/06_agent_rules.md
```

**Your question:**
```
We have a 200-line function that's hard to understand.
Team estimates 1 day to refactor. Manager says "no time".
How do I convince them?
```

**Claude will answer:**
```
From Refactoring (R12: Justify Economically):
"Refactoring must be justified by business metrics, not cleanliness.
Argument: 'This refactoring will make next feature 3x faster.'"

From Refactoring (R3: Embed in workflow):
"Refactoring is not separate; it's part of feature work.
Ask: 'How long to add feature WITHOUT refactoring first?'
If refactoring saves 2 days on next feature, 1-day refactoring pays off."

From Refactoring (R2: Design Stamina):
"Good design now = faster delivery over months.
Data: After similar refactoring last quarter, velocity +300%"

Suggested conversation with manager:
"Refactoring now (1 day) vs. adding feature slow (5 days).
Refactoring is the FASTER path for business."
```

---

## 🚀 START HERE (30 MINUTES)

1. **Pick one problem you have NOW**
   - "Code is hard to understand"
   - "Architecture decision needed"
   - "Legacy code is scary to touch"

2. **Find the book** (use table above)

3. **Copy the rules (06_agent_rules.md)**
   - ```bash
     cat Books/[book]/06_agent_rules.md
     ```

4. **Paste into Claude**
   - Open Claude Code
   - `/new` conversation
   - Paste rules at start

5. **Ask your question with your code/design**

6. **Get answer backed by expert author**

---

**That's it. That's how you use it.**

Not complicated. Practical. Immediately useful.

