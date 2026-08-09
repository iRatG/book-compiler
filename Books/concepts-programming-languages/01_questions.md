# Concepts of Programming Languages — Central Questions

## Question 1: How Do You Choose a Programming Language?
**Why it matters:** Language choice affects team velocity, system reliability, and maintenance costs for years.

**Sub-questions:**
- Should fit come before familiarity? (Fit: what the language is good at; Familiarity: what your team knows)
- What domain-specific advantages matter most for your problem?
- What trade-offs are you accepting (performance vs. safety vs. speed-to-code)?

**Related to:** Principles 1, 2, 12, 14

---

## Question 2: What Do Type Systems Actually Prevent?
**Why it matters:** Understanding what types catch helps you evaluate static vs. dynamic languages correctly.

**Sub-questions:**
- Can type errors be caught at compile-time or only at runtime?
- How much overhead do type checks add?
- When is dynamic typing actually safer than static typing?

**Related to:** Principles 3, 4

---

## Question 3: How Does Memory Management Affect Architecture?
**Why it matters:** Memory strategy determines latency, throughput, and what architectural patterns work.

**Sub-questions:**
- Can you afford garbage collection pauses (GC stops, latency)
- Do you need manual control over memory (systems programming)?
- Does the language give you escape hatches when defaults don't fit?

**Related to:** Principle 6

---

## Question 4: Which Paradigm Fits This Problem?
**Why it matters:** Working against a language's paradigm creates friction; working with it enables elegance.

**Sub-questions:**
- Is this problem fundamentally imperative (step-by-step logic)?
- Is this problem fundamentally declarative/functional (data transformation)?
- Is this problem fundamentally about modeling objects and their interactions?
- Can the language support multiple paradigms smoothly?

**Related to:** Principle 7

---

## Question 5: What Errors Does This Language Make Easy or Hard?
**Why it matters:** Language design makes certain bugs nearly impossible and others trivial.

**Sub-questions:**
- What category of bugs can't happen in this language by design?
- What category of bugs is this language susceptible to?
- Are the language's weak points critical for my use case?

**Related to:** Principle 2, 9

---

## Question 6: How Explicit vs. Implicit Is This Language?
**Why it matters:** Implicit behavior (magic) saves typing but costs maintainability.

**Sub-questions:**
- What happens automatically that I should know about?
- What special rules exist that aren't obvious from reading the code?
- Will a newcomer understand the code or need hidden knowledge?

**Related to:** Principle 8

---

## Question 7: Is This Language Orthogonal or Tangled?
**Why it matters:** Orthogonal languages are easier to learn and understand; tangled languages require memorizing interactions.

**Sub-questions:**
- Do language features interact in unexpected ways?
- Can I understand one feature in isolation or must I understand others first?
- How many special cases does the language have?

**Related to:** Principle 9

---

## Question 8: What Composability Patterns Does This Language Enable?
**Why it matters:** Some languages make composition natural; others make it awkward, leading to code duplication.

**Sub-questions:**
- Can I combine small, simple functions into larger behaviors?
- Are higher-order functions (functions that take/return functions) natural?
- Does the language make me repeat logic or can I abstract it?

**Related to:** Principle 10, 13

---

## Question 9: How Learnable Is This Language?
**Why it matters:** Learning time affects hiring, onboarding, and team productivity.

**Sub-questions:**
- How many core concepts must I learn before I'm productive?
- Are the concepts regular (consistent rules) or irregular (special cases)?
- How much "hidden knowledge" do I need to be effective?

**Related to:** Principle 11

---

## Question 10: Does This Language's Abstraction Level Match My Problem?
**Why it matters:** Too high and you can't control what matters; too low and you waste time on details.

**Sub-questions:**
- Am I fighting the language (wrestling with low-level details)?
- Am I blind to important details (language hiding too much)?
- Can I drop to lower levels when needed?

**Related to:** Principle 12

---

## Question 11: What Patterns Does This Language Make Possible That Others Don't?
**Why it matters:** Languages enable architectures; lack of features prevents solutions.

**Sub-questions:**
- What can I only do in this language?
- What can I do in this language but would be awkward in others?
- What architectural patterns does this language enable naturally?

**Related to:** Principle 13

---

## Question 12: What's the Performance Characteristic?
**Why it matters:** Some systems can accept GC pauses; others cannot. Some can accept dynamic dispatch; others need compiled code.

**Sub-questions:**
- What's the latency profile (worst-case, average-case)?
- What's the throughput profile (can it handle N requests/second)?
- What overhead does this language add compared to manual implementation?

**Related to:** Principle 6, 14

---

## Question 13: Why Does This Language Exist?
**Why it matters:** Every language solves a real problem someone faced. Understanding the problem explains the language's design.

**Sub-questions:**
- What was broken about older languages?
- What problem did this language solve that others couldn't?
- Who are the primary users and what are they optimizing for?

**Related to:** Principle 15

---

## Tags
#language-selection, #design-trade-offs, #paradigms, #type-systems, #memory-management, #pragmatism

