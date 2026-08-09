# A Philosophy of Software Design — Core Ideas (15 Principles)

## PRINCIPLE 1: Complexity is the Enemy
#complexity #design-metric #software-quality

Complexity is anything related to the structure of a software system that makes it hard to understand and modify the system. The overall complexity of a system is determined by the complexity of each part weighted by the fraction of time developers spend working on that part.

---

## PRINCIPLE 2: Dependencies and Obscurity are Complexity's Causes
#dependencies #obscurity #change-amplification #cognitive-load

Complexity is caused by two things: dependencies and obscurity. Dependencies create change amplification (a change requires changes in many places) and cognitive load (developers must know a lot). Obscurity creates unknown unknowns (developers don't even know what they don't know).

---

## PRINCIPLE 3: Strategic Programming vs Tactical Programming
#strategic-programming #tactical-programming #technical-debt #long-term-thinking

Tactical programming (focusing on getting feature working today) leads to accumulated complexity that slows future development exponentially. Strategic programming requires 10-20% investment time upfront but pays for itself within 6-18 months through faster future development.

---

## PRINCIPLE 4: Modules Should Be Deep
#modules #deep-modules #information-hiding #interface-design

The best modules are those that provide powerful functionality yet have simple interfaces. Module depth represents the benefit-to-cost ratio (benefit=functionality, cost=interface complexity). Deep modules provide maximum leverage against complexity.

---

## PRINCIPLE 5: Information Hiding
#information-hiding #encapsulation #module-design #abstraction

Each module should encapsulate a few pieces of knowledge (design decisions). The knowledge is embedded in the module's implementation but does not appear in its interface. Information hiding simplifies interfaces (reducing cognitive load) and makes systems easier to evolve.

---

## PRINCIPLE 6: Information Leakage is a Red Flag
#information-leakage #dependencies #module-coupling #back-door-dependencies

Information leakage occurs when the same knowledge is used in multiple places. Back-door leakage (knowledge shared but not in interfaces) is worse than interface leakage because it's not obvious. Both create dependencies between modules.

---

## PRINCIPLE 7: Avoid Temporal Decomposition
#temporal-decomposition #modularity #module-organization #knowledge-encapsulation

When designing modules, focus on the knowledge that's needed to perform each task, not the order in which tasks occur. Organizing code by execution order often results in information leakage because design decisions appear at multiple stages.

---

## PRINCIPLE 8: General-Purpose Modules are Deeper
#general-purpose-modules #module-design #special-purpose #abstraction

A class with a general-purpose interface and implementation tends to be deeper than a class with a special-purpose interface. General-purpose mechanisms provide better information hiding and reduce special cases in client code. Specialization should be pushed upward (to callers).

---

## PRINCIPLE 9: Define Errors Out of Existence
#error-handling #exception-handling #api-design #complexity-reduction

The best way to eliminate exception handling complexity is to define your APIs so that there are no exceptions to handle. Define errors out of existence. Exception handling code is complex, difficult to test, and often contains bugs.

---

## PRINCIPLE 10: Code Should be Obvious
#code-clarity #readability #maintainability #cognitive-load

If code is obvious, it means that someone can read the code quickly, without much thought, and their first guesses about the behavior or meaning of the code will be correct. Nonobvious code increases development time and bug likelihood.

---

## PRINCIPLE 11: Use Strong Names and Consistency
#naming-conventions #code-consistency #patterns #cognitive-load

Precise and meaningful names clarify the behavior of code. If similar things are always done in similar ways, readers can recognize patterns they have seen before and immediately draw conclusions without analyzing code in detail.

---

## PRINCIPLE 12: Comments Are Essential for Deeper Modules
#comments #documentation #code-explanation #obscurity-reduction

Obscurity is one of the main causes of complexity. The solution to the obscurity problem is to write code that makes information obvious and use comments to provide information that cannot be inferred from the code. Comments should explain intent and non-obvious behavior.

---

## PRINCIPLE 13: Design It Twice
#design-process #multiple-designs #trade-offs #decision-making

The best way to improve your design is to consider multiple alternatives and choose the best one. Don't implement the first idea that comes to mind. Thinking about multiple designs forces you to consider trade-offs.

---

## PRINCIPLE 14: Pull Complexity Downward
#api-design #module-responsibility #complexity-distribution #module-depth

If something is complicated, the module should do the work so that clients of the module don't have to. This is the opposite of pushing complexity onto the caller. Pushing complexity to callers multiplies the complexity.

---

## PRINCIPLE 15: Invest 10-20% Time in Design, Not Features
#technical-investment #refactoring #sustainable-pace #long-term-productivity

Spend about 10-20% of your total development time on design investments. This is small enough that it won't impact schedules significantly, but large enough to produce significant benefits. This modest investment pays for itself within months.

---

## Summary Table

| ID | Principle | Master Tag |
|----|-----------|-----------|
| 1 | Complexity is enemy | #complexity |
| 2 | Dependencies & obscurity | #change-amplification |
| 3 | Strategic programming | #technical-investment |
| 4 | Modules should be deep | #module-design |
| 5 | Information hiding | #encapsulation |
| 6 | Information leakage | #module-coupling |
| 7 | Avoid temporal decomposition | #modularity |
| 8 | General-purpose modules | #abstraction |
| 9 | Define errors away | #error-handling |
| 10 | Code obvious | #clarity |
| 11 | Strong names & consistency | #patterns |
| 12 | Comments essential | #documentation |
| 13 | Design it twice | #design-process |
| 14 | Pull complexity down | #api-design |
| 15 | Invest 10-20% in design | #technical-investment |

**Cross-Book Tags:** #software-design, #complexity, #architecture, #refactoring
