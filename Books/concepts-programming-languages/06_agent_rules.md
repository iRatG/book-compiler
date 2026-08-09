# Concepts of Programming Languages — Agent Rules for Code Review & Architecture

## WHEN TO USE THESE PRINCIPLES
- Language selection for projects
- Evaluating adoption of new programming languages
- Architecture reviews where language choice impacts design
- Performance optimization decisions
- Team discussions about technology choices
- Teaching language design concepts to teams

## DO NOT USE
- For optimizing algorithms (use algorithm complexity theory instead)
- For network design decisions (wrong domain)
- For database selection (language choice doesn't determine DB)
- For philosophical debates about "best language" (none exists)

## HOW TO APPLY

### Rule 1: Domain Matching Framework
**When:** Before selecting language for project
```
1. Identify primary constraint (performance, time, safety, learning, deployment)
2. Research ecosystems in target domain
3. Factor team expertise
4. Document decision in ADR (Architecture Decision Record)
```

### Rule 2: Type System Audit
**When:** Choosing between static and dynamic languages
```
1. Calculate cost of error reaching production
2. If cost > 1000x development time lost to typing: static types required
3. If cost < 100x: dynamic types acceptable with high test coverage
```

### Rule 3: Performance Trade-off Decision
**When:** Performance is critical (latency < 100ms or throughput > 100k ops/sec)
```
1. Profile current implementation
2. Identify bottleneck
3. Can current language solve it? (Use lower-level abstractions first)
4. Must change languages? (Measure overhead first)
```

### Rule 4: Paradigm Alignment
**When:** Designing system or evaluating language choice
```
1. Classify problem type: data transformation vs. object modeling vs. procedural
2. Choose language whose paradigm matches
3. Use language's strongest paradigm; avoid fighting language design
```

### Rule 5: Safety vs. Complexity Trade-off
**When:** Evaluating production-critical systems
```
1. Identify what bugs would cost most (type errors? null pointers? memory?)
2. Choose language that prevents those bugs by design
3. Accept learning curve as necessary cost
```

### Rule 6: Scope Design
**When:** Reviewing module boundaries
```
1. Check: Is state global when it should be encapsulated?
2. Check: Are dependencies explicit (parameters) or hidden?
3. Refactor: Move global state into classes/modules
```

### Rule 7: Binding Time Decision
**When:** Designing APIs for performance-critical code
```
1. Does binding happen at compile-time? YES → good
2. Can binding happen at compile-time? NO → must use runtime dispatch
3. Measure: Is overhead acceptable for use case?
```

## WHEN UNCERTAIN

**Q: Should we rewrite in a different language?**
A: Only if: (1) current language prevents solving critical problem, (2) problem unsolvable with current language, (3) rewrite cost < cost of not solving problem.

**Q: Is X language "better" than Y?**
A: No such thing. Each language makes trade-offs. X is better IF its trade-offs align with your problem's constraints.

**Q: How do we convince team to adopt new language?**
A: Show that: (1) current language prevents something important, (2) new language solves it, (3) benefits outweigh learning cost.

**Q: Should we use what team knows or what's best-suited?**
A: Expertise reduces time by 2-4x. Expertise wins unless new language removes fundamental problem.

**Q: What if we use multiple languages?**
A: Acceptable for large systems. Use best language per subsystem. Cost: integration complexity. Benefit: optimization. ROI positive when subsystems are large.

## COMMON MISTAKES

### Mistake 1: Choosing language based on trend
❌ "Node.js is trendy, let's use it for backend"
✅ "Identify constraint first (startup time?), then choose language solving it"

### Mistake 2: Confusing language with problem
❌ "We should use Rust because it's safer"
✅ "We need safety guarantees; Rust provides them; measure if learning curve is acceptable"

### Mistake 3: Optimizing for worst-case language
❌ "Python is slow, rewrite in C"
✅ "Profile first; 90% code doesn't matter; optimize bottleneck, not language"

### Mistake 4: Fighting language paradigm
❌ "Using Haskell (functional) for OOP-style domain models"
✅ "Use Scala or Python (multi-paradigm) or use OOP language"

### Mistake 5: Ignoring ecosystem
❌ "Rust has no ML libraries, but let's use it for ML"
✅ "If library ecosystem missing, tool isn't ready for domain"

## DECISION CHECKLIST

Before committing to language for project:

- [ ] Primary constraint identified? (perf/time/safety/learning/deploy)
- [ ] Domain ecosystem researched? (do libraries exist?)
- [ ] Team expertise considered? (hire cost, training time)
- [ ] Type system adequate for error costs?
- [ ] Memory strategy fits constraints? (GC latency, memory overhead)
- [ ] Paradigm matches problem type?
- [ ] Syntax safety sufficient for critical operations?
- [ ] Learning curve acceptable for team?
- [ ] Community healthy? (libraries, documentation, jobs)
- [ ] Evolution pragmatic? (solves real problems, not feature bloat)
- [ ] Decision documented in ADR?

**If you can't confidently answer yes to most: Choose different language**

## TAGS FOR CROSS-BOOK LINKING

| Principle | Tag | Related Books |
|-----------|-----|---------------|
| 1: Domain matching | #domain-matching | Clean Architecture, Ideal Work |
| 2: Syntax safety | #error-prevention | Ideal Work (TDD), Clean Architecture |
| 3: Type systems | #type-systems | Clean Code, Ideal Work |
| 4: Binding time | #performance | Parallel Programming, Architecture Elevator |
| 5: Scope rules | #coupling | Clean Architecture |
| 6: Memory strategy | #memory-management | Parallel Programming |
| 7: Paradigm fit | #paradigm-fit | Clean Architecture, Domain Modeling |
| 8: Explicit semantics | #explicitness | Code That Fits, Ideal Work |
| 9: Orthogonality | #simplicity | Code That Fits, Domain Modeling |
| 10: Composition | #modularity | Clean Architecture, Code That Fits |
| 11: Regularity | #consistency | Code That Fits, Clean Code |
| 12: Abstraction level | #abstraction | Clean Architecture, Code That Fits |
| 13: Feature enablement | #expressiveness | Parallel Programming, Domain Modeling |
| 14: Safety-performance | #performance-safety | Parallel Programming, Clean Architecture |
| 15: Evolution | #pragmatism | Ideal Work, Pragmatic Programmer |

---

**Last Updated:** 2026-08-09  
**Format Version:** 4.0  
**Status:** Ready for Code Review & Architecture Decisions
