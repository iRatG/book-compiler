# A Philosophy of Software Design — Agent Rules

## WHEN TO USE THESE PRINCIPLES
- Design reviews and refactoring decisions
- Architecture assessments
- Code quality evaluations
- Module design discussions

## HOW TO APPLY

### Rule 1: Complexity Audit
Measure: (1) Change amplification, (2) Cognitive load, (3) Unknown unknowns
Action: Refactor high-complexity modules proportional to change frequency

### Rule 2: Deep vs. Shallow Module Test
Calculate: Functionality / Interface complexity
Target ratio: > 1 (deep)

### Rule 3: Information Hiding Review
Check: Are design decisions hidden? Is interface simple?

### Rule 4: Strategic Allocation
Allocate 10-20% time for design/refactoring every sprint

### Rule 5: Obvious Code Audit
Is code understandable at first reading? If not: refactor for clarity

### Rule 6: Naming Standards
Enforce: descriptive names, consistent patterns, clear intent

### Rule 7: Comment Policy
Every class: intro comment. Complex functions: intent comments

### Rule 8: Design Review Process
Multiple designs > single design

---

## WHEN UNCERTAIN

**Q: Should we refactor?**
A: If complexity is slowing development = YES

**Q: How much design investment?**
A: 10-20% time; pays for itself in 6-18 months

**Q: Deep or shallow modules?**
A: Deep modules reusable; shallow modules copied

---

## COMMON MISTAKES

❌ Tactical programming (hack now, fix later)
✅ Strategic programming (invest 10-20%)

❌ Shallow modules with complex interfaces
✅ Deep modules with simple interfaces

❌ Information leakage across modules
✅ Clear encapsulation with hidden details

---

## Tags
#complexity, #modularity, #refactoring, #design-quality
