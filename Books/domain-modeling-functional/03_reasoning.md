# Domain Modeling Made Functional — Reasoning & Evidence

## ARGUMENT 1: Shared Understanding Prevents Rework
Domain experts see the problem one way; code often implements it differently. This gap causes:
- Requirements misinterpretation
- Features that don't match business workflow
- Expensive rework

Shared mental model eliminates translation.

---

## ARGUMENT 2: Domain Understanding Precedes Design
Unclear requirements make any design irrelevant. Must understand business first.

Process: Listen → Understand → Model → Design

Skipping understanding step wastes all downstream work.

---

## ARGUMENT 3: Events Reveal Causality
Events (OrderPlaced, PaymentReceived) reveal what actually happens. State machines (tables with flags) hide causality.

Business works through events, not data storage. Code should match business.

---

## ARGUMENT 4: Ubiquitous Language Prevents Knowledge Loss
Domain knowledge lives in experts' heads. When they leave, it's gone. Code as documentation preserves it.

Teams using ubiquitous language report 50% fewer misunderstandings in requirements.

---

## ARGUMENT 5: Bounded Contexts Reduce Cognitive Load
Large domains become unmanageable. Partitioning into contexts:
- Reduces complexity per team
- Enables independent evolution
- Clarifies responsibilities
- Minimizes coupling

Amazon's "two-pizza rule" (team size ≤ 6) maps to bounded contexts.

---

## ARGUMENT 6: Events Enable Asynchronous Communication
Commands (do X) and events (X happened) decouple contexts. Order context doesn't need to wait for Shipping. It sends OrderPlaced event; Shipping responds when ready.

Asynchronous workflows scale better; more resilient.

---

## ARGUMENT 7: Persistence Ignorance Prevents Over-Design
Database considerations (normalization, performance) distort domain model. Designing domain first, persistence second:
- Domain remains clear
- Can switch databases without changing logic
- Easier to test (in-memory implementations)

---

## ARGUMENT 8: Domain Experts Know Reality; Assumptions Fail
Developers often assume how business works. Wrong. Assumptions become bugs.

Deep listening to domain experts reveals:
- Edge cases others didn't consider
- Workarounds people actually use
- Real constraints vs. stated ones

---

## ARGUMENT 9: Types Encode Business Rules
Rules captured in types are enforced by compiler. Rules captured in comments are ignored.

Example: ProductCode type enforces "W + 4 digits OR G + 3 digits" format. Invalid codes cannot be created.

Cost of bug at compile-time: 0. Cost at runtime: investigation + fix.

---

## ARGUMENT 10: State Machines Prevent Invalid Operations
Not all operations valid in all states. OrderPlaced → can send; Order deleted → cannot send.

State machines (separate types per state) make this explicit. Compiler prevents invalid operations.

---

## ARGUMENT 11: Database-Driven Design Creates Impedance Mismatch
Database design (tables, normalization) doesn't match business concepts. Order + Quote → OrderBase abstract class with IsQuote flag. Convoluted.

Domain-first design keeps concepts aligned.

---

## ARGUMENT 12: Class Inheritance Doesn't Solve Domain Modeling
Order and Quote are fundamentally different (different validations, different workflows). Forcing into OrderBase + subclasses creates artificial abstractions.

Better: Separate Order and Quote types; encode differences in types.

---

## ARGUMENT 13: Business Value Guides Prioritization
Some domain concepts make money; others cost money. Prioritize money-makers.

Orders generate revenue; quotes cost money. Build Order workflows first; quotes second.

Resource allocation should match business value.

---

## ARGUMENT 14: Dependency Inversion Enables Testing
If domain depends on infrastructure:
- Can't test without real database/API
- Tests slow down
- Difficult to test edge cases

If infrastructure depends on domain:
- Can test domain with fake implementations
- Tests fast
- Easy to test edge cases

---

## ARGUMENT 15: Pure Functions Enable Composition
Side effects (database, API calls) make functions unpredictable and hard to test. Pure domain logic:
- Deterministic (same input → same output)
- Composable (can combine operations)
- Testable (no setup required)

---

## Summary: Discovery → Modeling → Code
Events reveal workflows. Types prevent errors. Purity enables testing. Result: code matches business reality.
