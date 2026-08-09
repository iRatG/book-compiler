# A Philosophy of Software Design — Central Questions

## Question 1: Why Do Software Teams Slow Down?
**Why it matters:** Most teams experience declining productivity as codebase grows.
- Is this inevitable?
- Or sign of architectural failure?
- Can productivity stay constant as system grows?

---

## Question 2: What Causes Complexity?
**Why it matters:** Understanding causes of complexity reveals solutions.
- Are some systems inherently complex?
- Or is complexity always a design choice?
- Can any system be redesigned to be simpler?

---

## Question 3: How Do You Measure Complexity?
**Why it matters:** Can't improve what you don't measure.
- Is complexity subjective or objective?
- How do you know when a module is "too complex"?
- When is refactoring worth the effort?

---

## Question 4: What Makes a Good Module?
**Why it matters:** Most design decisions are module design decisions.
- Is a good module small or large?
- Is a good module general-purpose or specialized?
- What's the relationship between module size and quality?

---

## Question 5: How Do You Hide Information?
**Why it matters:** Information hiding reduces cognitive load.
- What information should be hidden?
- What information should be visible?
- How do you decide module boundaries?

---

## Question 6: When Is Information Leakage Happening?
**Why it matters:** Information leakage creates change amplification.
- How do you detect when you're repeating knowledge?
- What's the difference between interface leakage and back-door leakage?
- How do you fix it?

---

## Question 7: Should You Decompose by Time or by Knowledge?
**Why it matters:** Temporal decomposition creates common design mistakes.
- Why do step-by-step workflows lead to bad code?
- How should you organize code if not by execution order?

---

## Question 8: When Should Classes Be General-Purpose vs. Special-Purpose?
**Why it matters:** Generality affects reusability and interface complexity.
- Is general-purpose better or worse?
- When is specialization the right choice?

---

## Question 9: How Do You Handle Errors?
**Why it matters:** Error handling is a major source of complexity.
- Can you design errors away?
- Is exception handling always necessary?

---

## Question 10: What Makes Code Obvious?
**Why it matters:** Obvious code is easier to modify.
- Is obvious code slow to write?
- Is obvious code slower to execute?
- How do you make complexity clear?

---

## Question 11: How Important Are Names and Consistency?
**Why it matters:** Names and conventions reduce cognitive load.
- Should you spend time on naming?
- How important are consistent patterns?

---

## Question 12: When Should You Write Comments?
**Why it matters:** Comments controversial; when are they helpful?
- Should every function have comments?
- What should comments explain?
- Is "good code needs no comments" true?

---

## Question 13: Should You Design Once or Design Many Times?
**Why it matters:** Design time affects software quality.
- Is iterating on design wasteful?
- What's the cost of multiple designs?

---

## Question 14: Should Complexity Live in Modules or Callers?
**Why it matters:** This choice affects entire system architecture.
- Is it better to make modules complex or clients complex?
- When do you push complexity to callers?

---

## Question 15: How Much Time Should You Spend on Design vs. Features?
**Why it matters:** Time allocation directly affects long-term productivity.
- Is 10% time on design enough?
- Too much?
- How do you know?

---

## Tags
#design-questions, #complexity, #modularity, #refactoring, #architecture
