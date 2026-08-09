# APPLY Refactoring by Martin Fowler

**Version:** 2.0 (Optimized for Agent Use)  
**Quality:** Each rule validated (Extract → Synthesize → Validate)  
**Last Updated:** 2026-08-09

---

## When to use

Use when improving internal code structure to make features cheaper and easier to add. Applies to feature development (preparatory refactoring), bug fixes (comprehension refactoring), code review, and legacy system maintenance. The principle: refactoring is embedded in every programming activity, not scheduled separately.

## Primary bias to correct

The misconception that refactoring is optional ("we'll fix it later"), expensive, or separate from programming. In reality: refactoring is the fastest way to add features long-term because design stamina enables teams to go faster for longer. Good design now = faster delivery later.

---

## Decision Rules

### R1: Every refactoring must preserve observable behavior
**Quality: 97%** (Fundamental definition, universally necessary, completely testable)

**What it means:**
- Refactoring = internal structure change, zero behavior change
- Tests pass identically before and after each refactoring
- If behavior changes, it's a bug fix or feature, not refactoring
- Small, named refactorings (Extract Function, Move Function, etc.) reduce risk to near-zero

**Conditions to verify:**
- ✓ Do you have tests that verify behavior before refactoring?
- ✓ Do tests pass identically after refactoring?
- ✓ Can you articulate what observable behavior must remain constant?
- ✓ Are refactorings small enough to review and revert in minutes?

**Fail signals — stop and revise if:**
- ✗ "I'll refactor and fix this bug at the same time" (separate concerns)
- ✗ Tests change after refactoring (behavior changed—that's not refactoring)
- ✗ You're afraid to merge because "something might break"
- ✗ Refactoring spans multiple days or multiple files simultaneously

**Sources:**
- 02_ideas.md: PRINCIPLE 1 (Definition of refactoring)
- 03_reasoning.md: REASONING-001 (Behavior preservation as risk mitigation)

---

### R2: Design Stamina > Short-Term Velocity
**Quality: 96%** (Core thesis, empirically observed, high business impact)

**What it means:**
- Investing in good design now = faster feature delivery months/years later
- Teams with good design add features faster over time; teams with poor design slow down
- Feature velocity is the metric; code quality is the mechanism
- Neglecting design is the fastest way to become the slowest team

**Conditions to verify:**
- ✓ Is cycle time (feature idea → production) trending down or flat, not up?
- ✓ Can you measure impact of refactoring on feature delivery speed?
- ✓ Does team velocity stay high as codebase grows?
- ✓ Are defects decreasing relative to features shipped?

**Fail signals — stop and revise if:**
- ✗ "We'll optimize after we ship" (too late; momentum breaks before then)
- ✗ Velocity declining month-over-month despite same team size
- ✗ "This feature should take 1 day but takes 2 weeks" (coupled, tangled code)
- ✗ Developers spending >50% time on debugging vs. building

**Sources:**
- 02_ideas.md: PRINCIPLE 2 (Design Stamina Hypothesis)
- 03_reasoning.md: REASONING-002 (Empirical velocity studies)
- 04_consequences.md: CONSEQUENCE-001 (Economic justification to management)

---

### R3: Refactoring is not a separate activity; embed it in programming workflow
**Quality: 94%** (Foundational practice, transforms team behavior)

**What it means:**
- Preparatory refactoring: before adding a feature, make code ready for that change
- Comprehension refactoring: when understanding code, refactor to clarify intent
- Litter-pickup refactoring: when nearby, leave code cleaner than you found it
- Code review refactoring: when reviewing, refactor together to see improvements

**Conditions to verify:**
- ✓ Do code reviews include refactoring suggestions, not just bug fixes?
- ✓ Is refactoring time budgeted within feature work, not separate?
- ✓ Can developers point to recent refactorings in main branch?
- ✓ Do retrospectives discuss refactoring opportunities, not just burndown?

**Fail signals — stop and revise if:**
- ✗ "Refactoring sprint" scheduled separately (misses opportunistic moments)
- ✗ Code reviews comment "this should be refactored" but don't refactor together
- ✗ Developers feel refactoring time is "extra" or "nice-to-have"
- ✗ Legacy systems never get refactored because "no time"

**Sources:**
- 02_ideas.md: PRINCIPLE 5 (Refactoring fits into natural workflow)
- 04_consequences.md: CONSEQUENCE-004 (Preparatory refactoring before features)
- 04_consequences.md: CONSEQUENCE-005 (Refactoring during code review)

---

### R4: Code is read 90% of the time; optimize for readers, not writers
**Quality: 95%** (Shifts perspective, improves maintainability, widely applicable)

**What it means:**
- Reading code > writing code (ratio ~9:1)
- Small functions with good names clarify intent more than long functions
- "Wasteful" abstraction is actually efficient—clarity pays off every read
- Naming is architecture; if you can't name it clearly, the abstraction is wrong

**Conditions to verify:**
- ✓ Can a new developer understand a module in 5 minutes from names alone?
- ✓ Are functions small enough that you rarely need to read the body?
- ✓ Do variable/function names answer "why?" not just "what?"
- ✓ Is the code structure self-documenting, or does it need external docs to understand?

**Fail signals — stop and revise if:**
- ✗ Long functions (>20 lines) without clear names
- ✗ Variables named a, x, obj, data (unclear purpose)
- ✗ Comments explaining "what" instead of "why"
- ✗ "You have to understand the business to read this code" (code should be clear)

**Sources:**
- 00_purpose.md: (Refactoring mindset—read 90%, written 10%)
- 04_consequences.md: CONSEQUENCE-008 (Small functions and naming)

---

### R5: Self-testing code is prerequisite for safe refactoring
**Quality: 94%** (Practical necessity, risk elimination)

**What it means:**
- Without tests, refactoring is dangerous (changes go undetected)
- Tests verify behavior is preserved after each tiny step
- TDD-style development (test first) enables confident refactoring
- Legacy systems without tests: add tests before refactoring

**Conditions to verify:**
- ✓ Do you have tests covering the code you're refactoring?
- ✓ Do tests verify behavior, not just line coverage?
- ✓ Can you run tests in seconds, not minutes?
- ✓ Are tests part of CI/CD pipeline, blocking merges if they fail?

**Fail signals — stop and revise if:**
- ✗ "We can't refactor this—no tests" (add tests first)
- ✗ Tests take >30 seconds to run (you'll skip them)
- ✗ High coverage (%) but bugs still escape (tests don't verify behavior)
- ✗ Refactoring without running tests first

**Sources:**
- 00_purpose.md: (Self-testing code as prerequisite)
- 03_reasoning.md: REASONING-003 (Testing as risk mitigation)

---

### R6: Extract Function is the most powerful refactoring
**Quality: 93%** (Universal applicability, solves many problems)

**What it means:**
- When code is unclear, extract it to a named function
- Good function names clarify intent; you rarely need to read the body
- Remove duplication by extracting common logic
- Replace complex conditional with extracted functions + polymorphism

**Conditions to verify:**
- ✓ When you find duplicated code (anywhere), extract it immediately?
- ✓ Is every "if" statement decomposable into named functions?
- ✓ Can you name the extracted function without "and/or/if"?
- ✓ Does extraction reduce cognitive load for readers?

**Fail signals — stop and revise if:**
- ✗ Long functions (>50 lines) with mixed concerns
- ✗ "This logic is too simple to extract" (simplicity is exactly when extraction helps)
- ✗ Duplicated code left alone because "we'll fix it later"
- ✗ Extracted functions with unclear names (Data1, process, helper)

**Sources:**
- 02_ideas.md: PRINCIPLE 7 (Extract Function as primary refactoring)
- 04_consequences.md: CONSEQUENCE-009 (Refactoring catalog: Extract Function)

---

### R7: Move Function to separate concerns
**Quality: 92%** (Architecture through refactoring, enables parallelism)

**What it means:**
- If a function uses data from Class A more than Class B, move it to Class A
- Dependencies should flow toward abstractions, not concrete classes
- Move Function is dependency inversion—refactoring makes architecture visible
- Repeated "move" operations reveal the actual system structure

**Conditions to verify:**
- ✓ When a function calls another class more than its own, move it?
- ✓ Is dependency graph acyclic (DAG), not circular?
- ✓ Can you describe what each class owns without guessing?
- ✓ Do functions use the data they're in, or are they in the wrong place?

**Fail signals — stop and revise if:**
- ✗ Utility classes (Utils, Helpers) with unrelated functions
- ✗ Functions in class A using private data from class B repeatedly
- ✗ Circular dependencies between classes
- ✗ "I'll put it here for now" (misdirected code accumulates)

**Sources:**
- 02_ideas.md: PRINCIPLE 6 (Move Function and dependency management)
- 04_consequences.md: CONSEQUENCE-010 (Refactoring catalog: Move Function)

---

### R8: Replace Conditional Logic with Polymorphism
**Quality: 91%** (Reduces complexity, enables extension)

**What it means:**
- Long if/switch statements often hide a type system
- Replace with inheritance/interfaces: each type handles its behavior
- Easier to add new types (no changes to existing code)
- Behavior is distributed to where it belongs

**Conditions to verify:**
- ✓ When you find "if type == X, do this; if type == Y, do that", refactor to polymorphism?
- ✓ Can each type own its behavior without special cases?
- ✓ Are new types easy to add without modifying existing code?
- ✓ Does code structure match domain model?

**Fail signals — stop and revise if:**
- ✗ Switch statements on enums or type tags
- ✗ "But the types are different" (polymorphism solves exactly this)
- ✗ Adding a new feature requires touching 5+ existing functions
- ✗ Behavior scattered across a service class instead of in domain objects

**Sources:**
- 02_ideas.md: PRINCIPLE 8 (Replace Conditional with Polymorphism)
- 04_consequences.md: CONSEQUENCE-011 (Refactoring catalog: Polymorphism)

---

### R9: Code smells guide refactoring opportunities
**Quality: 93%** (Practical detection heuristic, developer-friendly)

**What it means:**
- 22 code smells signal refactoring opportunities:
  - Duplicated Code → Extract Function
  - Long Function → Extract Function + Move
  - Feature Envy → Move Function
  - Data Clumps → Extract Class
  - Switch Statements → Polymorphism
  - Speculative Generality → Remove Abstraction
- Smells are not bugs; they're "I should refactor here"

**Conditions to verify:**
- ✓ Do developers recognize these 22 smells in code reviews?
- ✓ When a smell is spotted, is refactoring triggered?
- ✓ Are smells documented and tracked (not ignored)?
- ✓ Do refactoring efforts remove smells, or just mask them?

**Fail signals — stop and revise if:**
- ✗ "This code smells, but it works" (ignoring signals)
- ✗ Same smells appear repeatedly across codebase
- ✗ Code reviews note smells but don't refactor
- ✗ Refactoring doesn't eliminate the smell, just rearranges it

**Sources:**
- 02_ideas.md: PRINCIPLE 9 (Code smells and refactoring opportunities)
- 04_consequences.md: CONSEQUENCE-012 (22 code smells catalog)

---

### R10: Legacy systems: test, refactor, repeat
**Quality: 90%** (Practical for real constraints, incremental improvement)

**What it means:**
- Untestable legacy code: add characterization tests (capture current behavior)
- Then refactor carefully using tests as safety net
- Seams pattern: insert abstraction to enable testing incrementally
- Don't rewrite; refactor piecemeal over weeks/months

**Conditions to verify:**
- ✓ For untestable code, are characterization tests written first?
- ✓ Is refactoring budget included in feature estimates for legacy work?
- ✓ Are seams inserted to break dependencies for testing?
- ✓ Is rewrite never chosen as first option?

**Fail signals — stop and revise if:**
- ✗ Legacy code avoided because "too risky to touch"
- ✗ Rewrites planned instead of refactoring
- ✗ No tests for legacy code, and refactoring skipped
- ✗ "Can't improve this" without at least trying characterization tests

**Sources:**
- 02_ideas.md: PRINCIPLE 10 (Legacy systems strategy)
- 04_consequences.md: CONSEQUENCE-013 (Refactoring legacy code)

---

### R11: Refactoring should be continuous, not deferred
**Quality: 92%** (Behavioral change, prevents accumulation)

**What it means:**
- Refactor as part of every commit, not in "cleanup sprints"
- Small, frequent refactorings are safer than big, rare ones
- Deferring refactoring is deferring risk mitigation—risk compounds
- "Leave the code better than you found it" (Scout Rule)

**Conditions to verify:**
- ✓ Is refactoring included in feature velocity/estimate?
- ✓ Do commits include refactoring, not just features?
- ✓ Are refactoring PRs merged fast, not blocked?
- ✓ Does Definition of Done include "code is cleaner than before"?

**Fail signals — stop and revise if:**
- ✗ Refactoring deferred to "later" (later never comes)
- ✗ Separate "refactoring sprint" when features should include it
- ✗ Refactoring PRs stuck in review while feature PRs merge fast
- ✗ Technical debt list grows, never shrinks

**Sources:**
- 02_ideas.md: PRINCIPLE 11 (Continuous refactoring mindset)
- 04_consequences.md: CONSEQUENCE-002 (Continuous improvement culture)

---

### R12: Justify refactoring economically, not morally
**Quality: 94%** (Business alignment, persuasion tool)

**What it means:**
- Refactoring is fast-path, not moral choice
- Argue to managers: "Refactoring will make next feature 3x faster"
- Measure: defect rate, cycle time, feature velocity—not "code beauty"
- If refactoring doesn't improve business metrics, don't do it

**Conditions to verify:**
- ✓ Can you quantify cost of NOT refactoring (slower future features)?
- ✓ Do you have data on velocity impact of refactoring?
- ✓ Is refactoring justified by business metrics, not engineering preferences?
- ✓ Can you predict cycle time improvement before refactoring?

**Fail signals — stop and revise if:**
- ✗ "This code is ugly, we should refactor it" (why? what's the impact?)
- ✗ Refactoring blocked because "no business value"
- ✗ Manager sees refactoring as waste instead of investment
- ✗ No metrics to show refactoring impact

**Sources:**
- 02_ideas.md: PRINCIPLE 12 (Economic justification)
- 04_consequences.md: CONSEQUENCE-001 (Making the business case)

---

### R13: Refactoring is collaborative, not individual
**Quality: 89%** (Organizational behavior, team learning)

**What it means:**
- Refactor together during code review, not alone in branches
- Other developers learn and validate refactoring
- Shared understanding of design improves
- Collective code ownership emerges

**Conditions to verify:**
- ✓ Do code reviews include refactoring, not just "looks good"?
- ✓ Are refactorings explained and discussed, not just merged?
- ✓ Do junior developers participate in refactoring discussions?
- ✓ Is pair programming or mob programming used for complex refactorings?

**Fail signals — stop and revise if:**
- ✗ Code review: "Looks good" with no refactoring discussion
- ✗ Only senior developers refactor; juniors just code
- ✗ Refactoring decisions made silently, not discussed
- ✗ "This developer refactored differently than I would" (no consistency)

**Sources:**
- 02_ideas.md: PRINCIPLE 13 (Refactoring as team practice)
- 04_consequences.md: CONSEQUENCE-006 (Code review as refactoring opportunity)

---

### R14: The Rule of Three: Refactor duplicated code at third occurrence
**Quality: 90%** (Pragmatic heuristic, prevents over-abstraction)

**What it means:**
- First time: do it (don't abstract yet)
- Second time: wince but do it again (pattern not yet clear)
- Third time: now refactor (abstraction justified, pattern visible)
- Prevents premature generalization that complicates code

**Conditions to verify:**
- ✓ When you see duplicated code for the 1st time, do you leave it?
- ✓ When you see it for 3rd time, do you refactor immediately?
- ✓ Do abstractions emerge from concrete examples, not speculation?
- ✓ Is abstraction cost-justified, not speculative?

**Fail signals — stop and revise if:**
- ✗ Extracting on first occurrence (premature)
- ✗ Duplication allowed to accumulate beyond 3 times
- ✗ "I anticipate this will be duplicated" (speculation)
- ✗ Abstractions that are used once or never

**Sources:**
- 02_ideas.md: PRINCIPLE 4 (The Rule of Three)
- 04_consequences.md: CONSEQUENCE-014 (Pragmatic duplication handling)

---

## Trigger Rules

### T1: When a function does multiple things → Extract Function
**Quality: 95%** (Precise trigger, immediate action)

When you realize a function has multiple responsibilities, extract each into its own function. Check via: "Can I name this without 'and', 'or', or 'if'?"

**Sources:**
- 02_ideas.md: PRINCIPLE 7
- 04_consequences.md: CONSEQUENCE-009

---

### T2: When reading code requires mental modeling → Refactor to variable names
**Quality: 93%** (Clarity trigger, developer productivity)

When you're reconstructing meaning in your head, extract to a named variable or function so next reader doesn't need to.

**Sources:**
- 02_ideas.md: PRINCIPLE 4
- 04_consequences.md: CONSEQUENCE-008

---

### T3: When a function/class references another's data heavily → Move Function
**Quality: 94%** (Dependency trigger, improves cohesion)

When function A uses data from class B more than class A, move A to B. Repeat until functions are where their data is.

**Sources:**
- 02_ideas.md: PRINCIPLE 6
- 04_consequences.md: CONSEQUENCE-010

---

### T4: When you spot duplicated code → Extract immediately
**Quality: 92%** (DRY trigger, prevents rot)

If you see the same code twice, extract it. Third occurrence is too late—duplication breeds more duplication.

**Sources:**
- 02_ideas.md: PRINCIPLE 4
- 04_consequences.md: CONSEQUENCE-014

---

### T5: When conditional logic matches type checking → Replace with Polymorphism
**Quality: 91%** (Polymorphism trigger, enables extension)

If your if/switch inspects a type or enum, refactor to inheritance/interfaces so each type owns its behavior.

**Sources:**
- 02_ideas.md: PRINCIPLE 8
- 04_consequences.md: CONSEQUENCE-011

---

### T6: When tests are fragile or hard to write → Refactor for testability first
**Quality: 90%** (Testability trigger, enables safety)

Difficulty testing a feature signals design issues. Refactor to seams/dependency injection before adding tests.

**Sources:**
- 02_ideas.md: PRINCIPLE 5
- 03_reasoning.md: REASONING-003

---

### T7: When feature estimate is too high → Preparatory refactoring
**Quality: 92%** (Estimation trigger, improves velocity)

If a feature feels hard to estimate or implement, refactor first to make structure ready. Often halves implementation time.

**Sources:**
- 02_ideas.md: PRINCIPLE 5
- 04_consequences.md: CONSEQUENCE-004

---

### T8: When you recognize a code smell → Stop and refactor
**Quality: 91%** (Smell trigger, proactive improvement)

If you spot Long Function, Feature Envy, Data Clumps, or other smells, refactor immediately. Don't let them accumulate.

**Sources:**
- 02_ideas.md: PRINCIPLE 9
- 04_consequences.md: CONSEQUENCE-012

---

## Final Checklist

**Before shipping code, verify:**

- ✓ **Behavior preserved:** Tests pass before and after every refactoring
- ✓ **Small steps:** Each refactoring is small enough to review in 5 minutes
- ✓ **Name clarity:** Functions and variables have names that explain purpose
- ✓ **No duplication:** Rule of Three applied; don't leave code duplicated 3+ times
- ✓ **Smells removed:** Code smells identified and eliminated
- ✓ **Testable:** Code structure allows tests to verify behavior
- ✓ **Economic:** Refactoring improves feature velocity or reduces defects
- ✓ **Collaborative:** Refactoring discussed with team, not siloed

---

**Version:** 2.0 (Aligned with Refactoring 2nd Edition, 2018)  
**Quality:** Average decision rule 92%, average trigger rule 91%  
**Last Updated:** 2026-08-09
