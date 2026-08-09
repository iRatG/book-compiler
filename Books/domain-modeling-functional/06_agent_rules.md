# Domain Modeling Made Functional — Agent Rules

## WHEN TO USE THESE PRINCIPLES
- Domain discovery and requirements gathering
- Domain model design and refactoring
- Bounded context definition
- Workflow design
- Type system design

## HOW TO APPLY

### Rule 1: Event Storming
Identify: events → commands → entities → boundaries

### Rule 2: Ubiquitous Language Audit
Check: Do code and domain experts use same terminology?

### Rule 3: Bounded Context Design
Identify autonomous subsystems with clear interfaces

### Rule 4: State Machine Modeling
Model lifecycles with separate types per state

### Rule 5: Type-Driven Design
Encode business rules in types; make invalid states unrepresentable

### Rule 6: Workflow Design
Model as: Command → Event → New event chain

### Rule 7: Pure Core, I/O at Edges
Domain logic pure; side effects at boundaries

---

## WHEN UNCERTAIN

**Q: How do I understand the domain?**
A: Listen deeply; don't assume; ask domain experts

**Q: When should I refactor domain model?**
A: When new understanding emerges; update continuously

**Q: Database first or domain first?**
A: Domain first; persist second

---

## COMMON MISTAKES

❌ Forcing domain into database schema
✅ Domain first; persistence second

❌ Shared OrderBase class for Order + Quote
✅ Separate types for different business concepts

❌ Ignoring domain expert terminology
✅ Use ubiquitous language everywhere

---

## Tags
#domain-driven-design, #domain-modeling, #event-driven-architecture, #type-safety
