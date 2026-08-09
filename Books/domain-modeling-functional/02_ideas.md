# Domain Modeling Made Functional — Core Ideas (15 Principles)

## PRINCIPLE 1: Shared Mental Model
#shared-understanding #ubiquitous-language #communication #domain-knowledge

The code, domain experts, and development team must share the same mental model. When developers translate requirements into code, distortion occurs. A shared model eliminates translation and misunderstanding.

---

## PRINCIPLE 2: Problem Space vs Solution Space Distinction
#problem-space #solution-space #domain-understanding #requirements

Understand the business domain first (problem space) before designing software (solution space). Unclear requirements make coding irrelevant. The domain must be understood correctly first.

---

## PRINCIPLE 3: Focus on Business Events, Not Data
#events #workflows #business-processes #value-flow

Model domains through events and transformations, not static data structures. Business value is created through transformations, not through storing data. Events reveal what actually happens and when.

---

## PRINCIPLE 4: Ubiquitous Language
#ubiquitous-language #domain-terminology #code-as-documentation #knowledge-capture

Use terminology from domain experts everywhere—in requirements, design, and especially in source code. Code becomes documentation; prevents loss of domain knowledge when experts leave; enables non-developers to read code.

---

## PRINCIPLE 5: Bounded Contexts with Clear Boundaries
#bounded-contexts #domain-boundaries #independence #modularity

Partition the domain into smaller, autonomous subsystems with explicit boundaries. Reduces complexity; enables independent evolution; clarifies team responsibilities; minimizes coupling.

---

## PRINCIPLE 6: Domain Events Trigger Workflows
#domain-events #commands #workflows #asynchronous-communication

Business processes are initiated by commands responding to events, producing new events. Mirrors how business actually works; creates decoupling between contexts; makes workflow dependencies explicit.

---

## PRINCIPLE 7: Persistence Ignorance
#persistence-ignorance #domain-purity #business-logic-separation #architecture

Domain model must be based only on business concepts, with no awareness of databases or persistence mechanisms. Prevents distortion of domain model by database constraints; keeps focus on business logic, not schema design.

---

## PRINCIPLE 8: Listen, Don't Assume
#discovery #requirements-gathering #domain-expertise #communication

Gather requirements through deep listening; resist imposing pre-conceived technical solutions. Domain experts understand nuances developers miss; assumptions lead to wrong designs.

---

## PRINCIPLE 9: Types Express Business Rules
#type-systems #invalid-states #compiler-enforcement #safety

Use the type system to encode constraints, validation rules, and business logic. What's captured in types is enforced by compiler; invalid states become unrepresentable.

---

## PRINCIPLE 10: State Machines Model Lifecycle
#state-machines #workflow-states #type-safety #state-transitions

Workflows with multiple stages should explicitly model each state transition. Prevents invalid operations; makes flow clear; catches errors at compile time.

---

## PRINCIPLE 11: Avoid Database-Driven Design
#architecture-priority #domain-first #database-agnostic #flexibility

Don't let database schema drive the domain model; instead, design domain first, persist second. Database constraints distort domain concepts; creates artificial hierarchies and flags; loses important business distinctions.

---

## PRINCIPLE 12: Avoid Class-Driven Design
#paradigm-mismatch #oop-limitations #domain-purity #design-patterns

Don't impose object-oriented class hierarchies onto the domain. Objects can drive design just as badly as databases; creates artificial abstractions (OrderBase) that don't exist in business.

---

## PRINCIPLE 13: Follow the Money
#business-value #prioritization #pragmatism #resource-allocation

Prioritize business value over technical purity; focus development effort where the business makes money. Orders are more important than quotes in manufacturing (money-making vs cost); resources are finite.

---

## PRINCIPLE 14: Dependencies Point Inward (Onion Architecture)
#architecture #dependency-inversion #domain-independence #layering

Core domain depends on nothing; outer layers (services, persistence) depend on domain; all dependencies point inward. Keeps domain pure, testable, and independent of infrastructure choices.

---

## PRINCIPLE 15: Push I/O to Edges, Keep Core Pure
#pure-functions #side-effects #testability #architecture

Keep side effects (database access, file I/O, external services) at workflow boundaries; core domain logic should be pure functions. Pure functions are predictable, testable, and composable.

---

## Summary Table

| ID | Principle | Master Tag |
|----|-----------|-----------|
| 1 | Shared mental model | #shared-understanding |
| 2 | Problem vs solution space | #domain-understanding |
| 3 | Events not data | #events |
| 4 | Ubiquitous language | #ubiquitous-language |
| 5 | Bounded contexts | #bounded-contexts |
| 6 | Events trigger workflows | #domain-events |
| 7 | Persistence ignorance | #domain-purity |
| 8 | Listen don't assume | #discovery |
| 9 | Types express rules | #type-systems |
| 10 | State machines | #state-machines |
| 11 | Avoid database-driven | #architecture-priority |
| 12 | Avoid class-driven | #paradigm-mismatch |
| 13 | Follow the money | #business-value |
| 14 | Dependency inversion | #architecture |
| 15 | Pure core, I/O at edges | #pure-functions |

**Cross-Book Tags:** #domain-driven-design, #architecture, #domain-modeling, #functional-programming
