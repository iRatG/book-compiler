# A Philosophy of Software Design — Consequences & Application

## APPLICATION 1: Complexity Audit
**From Principle 1: Complexity is the Enemy**

Assess current system for complexity:

1. **Change Amplification:** Pick recent feature. How many files changed? If > 5: sign of bad design.
2. **Cognitive Load:** Estimate lines of code developer must understand to make change. If > 1000: too complex.
3. **Unknown Unknowns:** Is there code developers don't know exists? If yes: opacity problem.

**Action:** If any are red flags, refactor. Prioritize by frequency of changes to that module.

---

## APPLICATION 2: Dependency Mapping
**From Principle 2: Dependencies and Obscurity are Complexity's Causes**

List all dependencies in a module:
- Explicit (in interfaces)
- Implicit (code uses without calling)
- Temporal (order of execution matters)

**Action:** Minimize implicit and temporal dependencies. Make everything explicit.

---

## APPLICATION 3: Strategic Allocation
**From Principle 3: Strategic Programming vs Tactical Programming**

Allocate time: 80-90% features, 10-20% design/refactoring.

**Quarterly allocation example:**
- 10 weeks features (80%)
- 2 weeks design/refactoring (20%)

Don't negotiate this. Treat refactoring time as non-negotiable as code review.

---

## APPLICATION 4: Module Design Review
**From Principle 4: Modules Should Be Deep**

For each module, measure:
- **Functionality:** What does it do? (estimate: impact on system)
- **Interface:** How many methods/functions? (count)
- **Depth ratio:** Functionality / Interface complexity

**Target:** Ratio > 1 (deep)
**Red flag:** Ratio < 0.3 (shallow)

**Action:** If shallow, merge with adjacent modules or add functionality.

---

## APPLICATION 5: Information Hiding Checklist
**From Principle 5: Information Hiding**

For each module, ask:
- What design decisions are hidden?
- What information must be hidden for the interface to work?
- Is this information hidden or visible to callers?

**Rule:** Design decisions should be hidden; interfaces should be simple.

---

## APPLICATION 6: Information Leakage Detector
**From Principle 6: Information Leakage is a Red Flag**

Search code for repeated knowledge:
- Same parsing logic in 2+ places?
- Same validation rule in 2+ places?
- Same algorithm in 2+ places?

**Action:** Extract to shared module. Update all references.

---

## APPLICATION 7: Decomposition Audit
**From Principle 7: Avoid Temporal Decomposition**

If modules organized by execution order (ReadRequest, ParseRequest, ValidateRequest):
- Is knowledge of request format shared across modules?
- If yes: Reorganize by knowledge, not order.

**Pattern:** Combine to RequestHandler module with all knowledge of requests.

---

## APPLICATION 8: Generality Test
**From Principle 8: General-Purpose Modules are Deeper**

Ask for each module:
- Could this work for similar but different scenarios?
- If not, why? (What assumptions are baked in?)
- Can I make it general without losing clarity?

**Action:** If specialization is deep (>50 LOC), consider general version.

---

## APPLICATION 9: Error Elimination
**From Principle 9: Define Errors Out of Existence**

For each exception in API:
- Is this an error condition or normal operation?
- Can I redefine the operation so this isn't an error?

**Example:** Instead of "file not found" exception, define operation as "read file if it exists, return empty if not".

---

## APPLICATION 10: Obviousness Audit
**From Principle 10: Code Should be Obvious**

Read code you wrote 6 months ago. Is it obvious?
- Do variable names match what they do?
- Does flow match what you'd expect?
- Are there surprising behaviors?

**Action:** If not obvious, refactor for clarity.

---

## APPLICATION 11: Naming Standards
**From Principle 11: Use Strong Names and Consistency**

Establish naming conventions:
- Variables: descriptor + type (user_count, not uc)
- Functions: verb + noun (get_user, not get_u)
- Classes: noun (User, not UserGetter)
- Consistency: Same pattern everywhere

**Rule:** Code review should enforce naming consistency.

---

## APPLICATION 12: Comment Policy
**From Principle 12: Comments Are Essential for Deeper Modules**

Comments should explain:
- Why this design (not what the code does)
- Non-obvious consequences
- How this module interacts with others
- Intent (what problem this solves)

**Policy:** Every class should have intro comment. Every complex function should explain intent.

---

## APPLICATION 13: Design Review Process
**From Principle 13: Design It Twice**

Before implementing big feature/module:
1. Design approach A
2. Design approach B (different)
3. Discuss trade-offs
4. Choose best or synthesize hybrid

**Time:** 1-2 hours for architecture; saves weeks of rework.

---

## APPLICATION 14: API Design Rule
**From Principle 14: Pull Complexity Downward**

When designing API, ask:
- Can module do this work instead of callers?
- Is complexity hidden in module or exposed to callers?

**Rule:** Complexity belongs in module, not callers.

**Example:** Good API does sorting internally. Bad API requires callers to sort before calling.

---

## APPLICATION 15: Refactoring Budget
**From Principle 15: Invest 10-20% Time in Design**

Each sprint, allocate 10-20% time for:
- Small refactors (improving clarity)
- Reducing complexity hotspots
- Extracting duplicated knowledge
- Improving naming/consistency

**Track:** Measure how much time actually spent. Goal: stay at 10-20%.

---

## Quarterly Retrospective

Every quarter, assess:
1. Did we allocate 10-20% time to design?
2. Did code become simpler or more complex?
3. Did velocity improve or decline?
4. Did defect rate improve or decline?

**Trend:** If improving → design strategy working. If declining → need more investment.

---

## Tags
#refactoring, #modularity, #code-quality, #design-decisions, #technical-leadership
