# Central Questions: What Does Refactoring Answer?

The questions readers have *before* opening this book, organized by theme:

## **1. Why Should I Refactor? (What's the Payoff?)**

- If my code works, why spend time improving it?
- How do I convince my manager that refactoring is worth time when we have features to ship?
- What's the real economic benefit? Does it make us faster or just "cleaner"?
- Why do some teams add features 5x faster on old codebases while others wish they could start over?

## **2. When Should I Refactor? (How Do I Know It's Time?)**

- How do I recognize when code *needs* refactoring vs when it's "good enough"?
- Should I refactor *before* adding a feature, *during*, or *after*?
- What's the "Rule of Three"—when do I stop duplicating and start factoring out common code?
- Should I spend time on comprehension refactoring (making code I don't need to change more readable)?

## **3. How Do I Refactor Safely? (What Are the Mechanics?)**

- How do I change code without breaking it?
- What does "small, behavior-preserving steps" actually look like in practice?
- When am I safe to stop refactoring and verify my changes?
- What role do tests play—is testing required, or just recommended?

## **4. What Problems Signal I Should Refactor? (The Smell Test)**

- How do I recognize "bad smells" in code that indicate design problems?
- What's the difference between duplicated code, long functions, and long parameter lists?
- When does a class have too many responsibilities (divergent change vs shotgun surgery)?
- What does "global data," "mutable data," or "feature envy" actually look like?

## **5. What Are the Specific Refactorings? (The Toolkit)**

- What's Extract Function vs Inline Function—when do I use each?
- How do I decompose a long function without creating spaghetti?
- What's the difference between Replace Conditional with Polymorphism and other approaches?
- How many refactorings exist, and how do I know which one to apply?

## **6. How Do Tests Relate to Refactoring? (Can I Refactor Without Tests?)**

- Do I need comprehensive tests to refactor safely?
- What's "self-testing code" and how do I build it?
- If I inherit legacy code with no tests, can I refactor it?
- How do tests *enable* refactoring rather than slow it down?

## **7. What Gets in the Way? (Obstacles & Trade-offs)**

- If I refactor, won't I slow down feature delivery?
- How do feature branches and branching strategies affect refactoring?
- What happens when code is owned by different teams?
- When is refactoring *not* worth it (when should I rewrite instead)?

## **8. How Do I Justify Refactoring? (The Business Case)**

- How do I explain refactoring to non-technical managers?
- Should I tell management when I'm refactoring, or just do it as part of my work?
- What's the "design stamina hypothesis"—is it real or just theory?
- How do I prove refactoring made us faster?

## **9. What About Legacy Code? (Starting From a Mess)**

- How do I refactor a 20-year-old system with no tests?
- Is refactoring even possible if I can't understand the code?
- What strategies work for gradually improving bad code without breaking it?
- When do I give up and rewrite instead?

## **10. How Do I Embed Refactoring in Team Practice? (Making It Stick)**

- Should refactoring be done in separate commits from features, or mixed together?
- How does continuous integration relate to refactoring?
- How do I build a team culture that refactors regularly, not just on cleanup days?
- What's the relationship between code reviews and refactoring?

## **11. How Do Teams Avoid Over-Refactoring? (When to Stop)**

- Can a team refactor too much?
- How do I balance improving design with shipping features?
- What's the judgment call between refactoring and leaving messy code alone?

## **12. What's Different About Refactoring in Modern Languages? (2018 Perspective)**

- Are modern languages better at supporting refactoring than older ones?
- How do functional programming concepts (immutability, pipelines) change the refactoring approach?
- What role do automated refactorings in IDEs play—can I trust them?

## **13. How Do I Know I've Refactored Correctly?**

- How do I verify that I haven't changed the observable behavior?
- What's the relationship between passing tests and successful refactoring?
- Can I refactor if I don't have comprehensive tests?

## **14. What Are the Top Code Smells I Should Watch For?**

- What's more common: duplicated code, long functions, or something else?
- How do I distinguish between "long enough to worry about" and "acceptably long"?
- What's primitive obsession and why is it a smell?

---

#refactoring #questions #problem-solving #design #code-quality
