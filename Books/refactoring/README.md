# Refactoring: Improving the Design of Existing Code

**Author:** Martin Fowler  
**Edition:** 2nd Edition (2018)  
**Purpose:** Comprehensive guide to systematic code improvement through behavior-preserving transformations  

---

## Quick Summary

Refactoring answers the question every programmer faces: **How do I improve code design while keeping it working?**

Martin Fowler's book teaches:
- **The Design Stamina Hypothesis**: Good design enables faster feature delivery over time
- **Why refactoring is economic, not aesthetic**: Refactor so you can ship features faster
- **How to refactor safely**: Small steps + tests = near-zero risk
- **66+ named refactorings**: Extract Function, Move Function, Replace Conditional with Polymorphism, etc.
- **22 code smells**: Patterns that signal refactoring opportunities
- **Team practices**: CI, code review, pair programming, legacy code strategies

---

## Five-Layer Structure

### Layer 0: Purpose
**File:** `00_purpose.md`  
Why this book matters, central thesis, what you'll learn

### Layer 1: Questions
**File:** `01_questions.md`  
14 central questions the book answers (organized by theme)

### Layer 2: Ideas
**File:** `02_ideas.md`  
20 core principles and their statement, reasoning, and implications

### Layer 3: Reasoning
**File:** `03_reasoning.md`  
12 main arguments with evidence for why these principles matter

### Layer 4: Consequences
**File:** `04_consequences.md`  
12+ practical applications: how to apply refactoring in real projects

### Layer 5: LLM Instructions (JSON)
**File:** `05_llm_instructions.json`  
Machine-readable, actionable format ready to paste into Claude/GPT

---

## How to Use This Book Analysis

### For Personal Learning
1. Start with `00_purpose.md` to understand the problem the book solves
2. Read `01_questions.md` to see what you'll learn
3. Study `02_ideas.md` to learn the core principles
4. Deep-dive into `03_reasoning.md` for arguments
5. Use `04_consequences.md` for practical application

### To Review Your Code with Refactoring Principles
```
Open a new Claude conversation
Paste content from 05_llm_instructions.json
Ask: "Review this code for refactoring opportunities"

Claude will reference:
- Code smells that suggest refactoring
- Specific refactorings that would help
- Trade-offs and when not to refactor
- Practical examples from the book
```

### To Discuss Refactoring Decisions with Team
Copy `05_llm_instructions.json` → paste into LLM → ask about:
- "Should we refactor this module or rewrite it?"
- "How do we justify refactoring to management?"
- "What's the best order for these refactorings?"
- "This code smell appears in our codebase—how do we address it?"

---

## Key Principles at a Glance

| # | Principle | TL;DR |
|---|-----------|--------|
| 1 | Behavior-Preserving | Refactoring ≠ any code change. It preserves behavior. |
| 2 | Design Stamina | Good design now = faster features later (weeks/months/years) |
| 3 | Self-Testing Code | Tests are prerequisite for safe refactoring |
| 4 | Read 90% | Optimize code for readers, not writers |
| 5 | Workflow Integration | Refactoring is part of daily work, not separate sprints |
| 6 | Economic Logic | Refactor because it's faster, not because code is "clean" |
| 7 | Rule of Three | 1st: do it. 2nd: wince, do it again. 3rd: refactor. |
| 8 | Code Smells | Patterns that signal refactoring opportunities (22 total) |
| 9 | Extract vs. Inline | Every extract has an inverse. You can move both directions. |
| 10 | Naming | If you can't name it, design is unclear. Rename aggressively. |
| 11 | Long-Term Gradual | Major refactoring (weeks) done incrementally, not at once |
| 12 | CI Synergy | Continuous Integration + refactoring work together beautifully |
| 13 | Code Ownership | Team ownership > individual ownership (enables refactoring) |
| 14 | Legacy Seams | No tests? Use seams to add tests gradually, then refactor. |
| 15 | vs. Rewriting | Different strategies. Refactor if effort < rewrite. |
| 16 | Review Refactor | Don't suggest refactorings—do them together concretely |
| 17 | Trade-offs | All refactorings have costs. Evaluate benefit > cost. |
| 18 | Ongoing | Refactoring is continuous practice, not one-time activity |
| 19 | Two Hats | Refactor hat vs. Feature hat. Wear one at a time. |
| 20 | Named Catalog | 66+ refactorings with proven patterns and mechanics |

---

## Common Refactorings

**Top 10 you'll use constantly:**
1. **Extract Function** — Break large function into smaller, named pieces
2. **Rename Variable/Function** — Move understanding from your head into code via names
3. **Inline Function** — Remove indirection when it's no longer adding value
4. **Replace Temp with Query** — Eliminate mutable temporary variables
5. **Extract Class** — Separate concerns when class does too much
6. **Move Function** — Relocate function to where data lives (Feature Envy)
7. **Replace Conditional with Polymorphism** — Replace if/switch with inheritance
8. **Split Phase** — Separate concerns that naturally sequence (read → process → write)
9. **Introduce Parameter Object** — Group related parameters into an object
10. **Branch By Abstraction** — Migrate to new abstraction gradually (for major refactorings)

---

## Code Smells (22 Total)

When you see these patterns, consider refactoring:
- **Mysterious Name** → Rename
- **Duplicated Code** → Extract Function
- **Long Function** → Extract Function
- **Long Parameter List** → Introduce Parameter Object
- **Global Data** → Encapsulate Variable
- **Mutable Data** → Replace Temp with Query
- **Divergent Change** → Extract Class (different concerns)
- **Shotgun Surgery** → Move Function (opposite of divergent)
- **Feature Envy** → Move Function (code wants to be with data)
- **Data Clumps** → Extract Class (data always together)
- **Primitive Obsession** → Replace Primitive with Object
- **Repeated Switches** → Replace Conditional with Polymorphism
- **Loops** → Replace Loop with Pipeline (modern languages)
- **Lazy Class** → Inline Class (no longer earning its weight)
- **Speculative Generality** → Remove abstract classes/parameters (designed but unused)
- **Temporary Field** → Extract Class (some fields used only sometimes)
- **Message Chains** → Hide Delegate (chained calls are fragile)
- **Middle Man** → Remove Middle Man (too much delegation)
- **Insider Trading** → Move Function / Change Function Declaration (data access across boundaries)
- **Alternative Classes with Different Interfaces** → Rename (make interfaces match)
- **Data Classes** → Move Function (dumb objects; behavior belongs with data)
- **Comments** → Extract Function / Rename (if you need comments, name better)

---

## Decision Tree: Refactor or Not?

```
Does this refactoring enable faster feature delivery?
├─ YES → Will refactoring effort < 1 day?
│  ├─ YES → Refactor immediately
│  └─ NO → Use Branch By Abstraction for gradual migration
└─ NO → Leave code alone (don't refactor for its own sake)
```

---

## Real-World Example: The Statement Function

Fowler's book opens with a 200-line statement function mixing calculation, formatting, and rendering. Over ~40 pages, he applies a dozen refactorings, transforming it into a clean, testable, extensible program. Each refactoring is shown concretely (before/after code). This is how you learn: see the pattern applied.

---

## Connection to Other Books

- **Clean Architecture (Robert C. Martin)**: Fowler + Martin complement each other. CA gives architecture principles; Refactoring gives mechanical techniques to improve design.
- **The Clean Coder (Robert C. Martin)**: Both emphasize professional discipline. TDD enables refactoring; refactoring enables professional code quality.
- **The Pragmatic Programmer**: Both embrace pragmatic tradeoffs. Refactoring enables sustainable pace (avoiding code decay).
- **Code That Fits in Your Head (Mark Seemann)**: Both optimize for readability and cognitive load. Small functions (refactoring goal) fit in head.

---

## How to Know This Book Worked

After reading and applying this book, you should:
- ✅ Refactor confidently, in small steps, with tests
- ✅ Recognize code smells and know which refactorings address them
- ✅ Justify refactoring to management economically ("This makes the next change 3x faster")
- ✅ Integrate refactoring into daily workflow (preparatory, comprehension, litter-pickup)
- ✅ Teach others: "Extract this function," not just "this code is messy"
- ✅ Notice: Over months, code quality improves and team velocity increases
- ✅ Build team culture around continuous refactoring, not scheduled "refactoring weeks"

---

**Status:** ✅ Complete analysis (5 layers + LLM JSON)  
**Best for:** Code review, architecture decisions, team discussions about design quality  
**Quick Start:** Paste `05_llm_instructions.json` into Claude and ask your refactoring question
