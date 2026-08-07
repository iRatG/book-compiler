# Central Questions & Inquiry Structure

## The Big Question
**"What are the rules of software architecture that work for all systems?"**

Martin spent 50+ years programming and noticed that despite radical differences in system types (embedded, batch processing, real-time, web, games, accounting, telecommunications), they all obey the same architectural principles. This book explores *what those universal rules are*.

**Tags:** #universal-rules, #pattern-recognition, #architectural-principles

---

## Part I: Foundational Questions

### Question 1: What is the actual difference between Design and Architecture?

Many developers think design = low-level detail, architecture = high-level structure.

**Martin's position:** There is NO difference.

- Architecture includes all levels of decisions, from high-level structure to the placement of electrical outlets
- Both high-level and low-level decisions form one continuous fabric
- A good architect cannot avoid details; details define architecture

**Related challenge:** How do we stop thinking of architecture as separate from code?

**Tags:** #design-vs-architecture, #false-dichotomy, #implementation-detail

---

### Question 2: What is the Goal of Software Architecture?

**Answer:** Minimize human effort to create and maintain the system.

But this raises sub-questions:
- Effort for whom? (Users, developers, managers, stakeholders)
- Over what timeframe? (Initial build vs. 5-year maintenance)
- What counts as "effort"? (Time, cost, risk, cognitive load)

**The Eisenhower Matrix Question:** Is functionality more important than architecture?

**Tags:** #architectural-goal, #effort-minimization, #stakeholder-value

---

### Question 3: Why Do Development Teams Slow Down Over Time?

Empirical observation: As codebases grow and teams expand, velocity decreases despite larger team size.

**Root questions:**
- Is it inherent to software? Or a sign of architectural failure?
- Can a team maintain constant velocity while adding features indefinitely?
- What causes "the mess" that everyone blames?

**The Real Question:** Is there a path to sustainable productivity, or does every system inevitably decay?

**Tags:** #productivity-decay, #technical-debt, #system-aging, #velocity

---

### Question 4: When Should You Stop and "Rewrite From Scratch"?

Many teams believe the solution to architectural problems is to restart.

**The hard question:** Is this another form of Hare-and-Tortoise arrogance? Or sometimes legitimate?

**Tags:** #rewrite-temptation, #incremental-vs-radical, #decision-making

---

## Part II: Architectural Decision Questions

### Question 5: How Do You Decompose a Complex System?

**The function decomposition question:**
- Break the system into functions → break those into smaller functions → recursively

**The module question:**
- What is a module? How do you draw boundaries?

**The layering question:**
- Should architecture be layered? Hexagonal? Microservices? Event-driven?

**Tags:** #decomposition, #modularity, #system-organization

---

### Question 6: What Controls Should Govern Cross-Module Communication?

- Should modules be loosely or tightly coupled?
- What makes a "good" interface between components?
- When should boundaries be permeable vs. rigid?

**Tags:** #coupling, #interfaces, #component-boundaries

---

### Question 7: Which Paradigm Should Dominate: Structural, OO, or Functional?

All three are valid. But do they solve the same problems or different problems?

- **Structural:** Recursively decomposable, testable units
- **OO:** Crossing architectural boundaries, controlled dependencies
- **Functional:** Data immutability, predictable state changes

**The real question:** How do you combine all three for optimal architecture?

**Tags:** #programming-paradigms, #paradigm-choice, #architectural-patterns

---

## Part III: Questions About Value & Stakeholders

### Question 8: Who Decides Architecture Priorities?

Two competing values:
- **Behavior:** The software must work correctly *now*
- **Architecture:** The software must be changeable *forever*

**The conflict:** Urgent (behavior) vs. Important (architecture)

**Who should win?** Developers must advocate for architecture against business pressure, but how?

**Tags:** #value-conflict, #stakeholder-alignment, #advocacy

---

### Question 9: How Do You Know Your Architecture is Good?

**Metrics that don't work:**
- Code quality scores
- Test coverage percentages  
- Performance benchmarks

**Metric that does work:**
- **Cost of change over time:** Does adding a feature take the same effort in month 1 vs. month 12?

**Tags:** #architectural-quality, #measurement, #sustainability

---

### Question 10: When Does Architecture "Cry Out" its Structure?

Should looking at your codebase organization tell you what the system *does*?

**Example:** A web framework-driven structure hides the business domain under MVC folders.

**Clean architecture question:** Can you look at the directory structure and know whether you're building an e-commerce system vs. a hospital system vs. a gaming platform?

**Tags:** #screaming-architecture, #domain-driven-design, #code-organization

---

## Implicit Questions (Not Explicitly Stated)

These questions emerge from Martin's arguments:

### 11: Is Software Different From Physical Architecture?

Physical buildings have gravity, material constraints. Software is "pure thought."

**Does this mean:**
- Software architecture should be radically different?
- Or are the principles deeper than medium?

**Tags:** #metaphor-limits, #abstraction-levels, #software-nature

---

### 12: Can You Actually Prove Software Correctness?

Dijkstra dreamed of formal proofs. Does this work?

**Practical question:** How do you gain confidence that complex systems work?

**Tags:** #formal-verification, #testing, #proof-vs-science

---

### 13: What is "Craftsmanship" in Software Development?

Why should developers "care" about architecture when business only cares about features?

**Tags:** #professionalism, #craftsmanship, #identity

---

## How These Questions Organize the Book

```
Part I: Questions 1-2      → Foundation (What is arch?)
        Questions 3-4      → Problem (Why it fails)
Part II: Questions 5-7     → Paradigms (How to build)
        Questions 8-9      → Values (What to choose)
Part III: Questions 10-13  → Vision (What it means)
```

Each remaining chapter answers one of these questions through evidence, examples, and principle-building.

**Tags:** #book-structure, #curriculum-design, #inquiry-framework
