# Clean Architecture — A Craftsman's Guide to Software Structure and Design

## Book Information

**Author:** Robert C. Martin ("Uncle Bob")  
**Original Title:** Clean Architecture: A Craftsman's Guide to Software Structure and Design  
**Russian Translation:** 2018 (Translated by A. Makarova, Technical Editor N. Suslova)  
**ISBN:** 978-5-4461-0772-8  
**Publisher:** Издательство "Питер" (Piter Publishing)  
**Pages:** ~600 (Russian edition)

## About This Reconstruction

This directory contains a **five-layer reconstruction** of *Clean Architecture* using the **book-compiler methodology** — a systematic approach to understanding deep, non-summarized meaning of complex technical books.

### The Five-Layer Model

This book has been decomposed into five semantic layers:

1. **[00_purpose.md](00_purpose.md)** — Purpose & Problem Statement  
   *What gap does this book fill? What problem is it solving?*
   - Core problem: Productivity decline in enterprise software
   - Why architecture matters
   - Five eras of software truth
   - Intended audience & book's central claim

2. **[01_questions.md](01_questions.md)** — Central Questions & Inquiry  
   *What questions does the author ask? What inquiries organize the book?*
   - 13 central questions from foundational ("What is architecture?") to strategic ("What is craftsmanship?")
   - How these questions structure the book's curriculum

3. **[02_ideas.md](02_ideas.md)** — Core Ideas, Concepts & Principles  
   *What ideas does the author propose? What intellectual content is central?*
   - 15 core principles (e.g., "Architecture is NOT separate from code," "Cost-of-change is the metric that matters")
   - Three programming paradigms and their architectural role
   - Relationship between behavior value and architecture value
   - Why rules transcend technology

4. **[03_reasoning.md](03_reasoning.md)** — Reasoning, Arguments & Evidence  
   *How does the author support these ideas? What is the evidence?*
   - 10 major arguments with empirical/logical support
   - Real company data showing productivity collapse
   - Jason Gorman's TDD experiment
   - Fable application (Hare and Tortoise)
   - Eisenhower matrix for prioritization
   - Scientific vs. mathematical thinking

5. **[04_consequences.md](04_consequences.md)** — Practical Applications & Implications  
   *What should readers DO with these ideas?*
   - 12 practical implications for teams
   - Code examples (good vs. bad architecture)
   - How to advocate for quality to management
   - Organizing code to reveal intent
   - Building culture of discipline
   - Metrics that matter

---

## How to Use This Reconstruction

### For Learning
- **Quick overview:** Read 00_purpose + 01_questions (30 min)
- **Deep understanding:** Read all 5 layers in order (3-4 hours)
- **Reference:** Use tags to find specific concepts (#architecture-definition, #cost-of-change, #polymorphism)

### For Teaching
- Use questions (01_) to structure team discussions
- Use ideas (02_) as talking points in architecture review
- Use consequences (04_) to guide refactoring work
- Show evidence (03_) when advocating for quality time

### For Application
- Extract tags from 02_ideas for team glossary
- Use 04_consequences as checklist for new projects
- Reference specific ARG-### arguments when defending architecture decisions
- Apply implications 1-12 in team practices

---

## Tag System

Tags are cross-book concept labels. Some key tags in this book:

### Architectural Concepts
- `#architecture-definition` — What is architecture?
- `#cost-of-change` — The metric that matters
- `#modularity` — Breaking systems into parts
- `#dependency-inversion` — How to structure dependencies
- `#screaming-architecture` — Code organization reveals intent

### Programming Paradigms
- `#structured-programming` — Decomposition and testability
- `#oop` / `#polymorphism` — OOP and boundaries
- `#functional-programming` — Immutability and state
- `#multi-paradigm` — Using all three together

### Professional Practice
- `#professional-responsibility` — Developer duties
- `#advocacy` — Pushing back on shortcuts
- `#craftsmanship` — Pride in code quality
- `#team-culture` — Building culture of discipline
- `#data-driven-decisions` — Using metrics

### Evidence & Reasoning
- `#empirical-evidence` — Real data
- `#false-economy` — Shortcuts cost more long-term
- `#scientific-method` — Testing and falsifiability
- `#arrogance` — Hare and Tortoise lesson

---

## Key Takeaways (Quick Reference)

### The Problem
Developers are taught to prioritize working software (behavior) over maintainable software (architecture). This creates a productivity collapse: as codebases grow, cost per feature increases exponentially until the system becomes unmaintainable.

### The Core Insight
**All software obeys the same architectural rules**, regardless of technology. These rules come from three programming paradigms (Structured, OOP, Functional) that have existed since 1958–1968. No new paradigms exist.

### The Solution
Maintain **clean architecture** by:
1. Writing small, testable, decomposable code
2. Using polymorphism to separate high-level policy from low-level details
3. Managing state immutably where possible
4. Organizing code to reveal intent
5. Advocating for architecture against business pressure
6. Measuring cost-of-change, not just velocity

### The Outcome
- Constant velocity over time (not exponential decay)
- Easy to add features for years, not months
- Lower defect rates
- Team satisfaction (people enjoy clean code)
- Sustainable business model (cost remains manageable)

---

## Related Concepts Across Books

When reading other books in the library, watch for these same principles:

- **Single Responsibility Principle** ↔ Modular decomposition
- **Dependency Inversion Principle** ↔ Polymorphism as boundary
- **Clean Code** ↔ Small, testable functions
- **Test-Driven Development** ↔ Architecture enabling testing
- **Domain-Driven Design** ↔ "Screaming" architecture revealing intent

---

## Reading Path Recommendations

### Path 1: Philosophical (Why)
1. 00_purpose — Understand the problem
2. 01_questions — See the inquiry structure
3. 03_reasoning — Evidence for key claims
4. 02_ideas — How they're connected

**Time:** 2 hours | **Output:** Deep understanding of *why* architecture matters

### Path 2: Practical (How)
1. 00_purpose — Context
2. 02_ideas — Principles 1-15 (especially 1, 2, 9-14)
3. 04_consequences — Applications 1-12
4. 01_questions — Reread to understand structure

**Time:** 2.5 hours | **Output:** Ready to apply to your team/project

### Path 3: Reference
Search for:
- Specific tags (#cost-of-change, #polymorphism, etc.)
- Argument numbers (ARG-001, ARG-002, etc.)
- Implication numbers (IMPLICATION 1-12)
- Question numbers (Question 1-13)

**Time:** Varies | **Output:** Quick lookup during debates/decisions

---

## Notes on Translation & Adaptation

This reconstruction is based on the **Russian translation** by A. Makarova (Piter Publishing, 2018). Some terminology may differ slightly from English editions. Core ideas remain identical across all language editions.

### Translation Notes:
- "Чистая архитектура" = "Clean Architecture" (clean here means well-structured, maintainable)
- "Искусство разработки" = "The Art of Development" (emphasizes craftsmanship)
- "Программное обеспечение" = "Software" (literally "soft provision," emphasizing malleability)

---

## How to Contribute

If you find:
- Missing concepts from the book
- Tags that should be added
- Implications we haven't covered
- Better examples of principles

Add them to the appropriate file and update this README.

---

## Master Tag Cloud

#architecture-definition, #cost-of-change, #software-architecture, #design-principles, #professional-practice, #technical-leadership, #programming-paradigms, #structured-programming, #oop, #functional-programming, #testability, #dependency-inversion, #screaming-architecture, #professional-responsibility, #advocacy, #team-culture, #empirical-evidence, #falsifiability, #data-driven-decisions, #sustainable-development

---

**Status:** ✅ Complete reconstruction (5 layers, 15 principles, 12 implications, 13 questions, 10 arguments)

**Last Updated:** 2026-08-07

**Reconstruction Methodology:** book-compiler v1.0 (Five-Layer Model based on Povarnin–Adler–Foster method)

---

*This reconstruction is for deep learning and reference. For complete understanding, refer to the original book:*

**Robert C. Martin. Clean Architecture: A Craftsman's Guide to Software Structure and Design. Prentice Hall, 2017.**
