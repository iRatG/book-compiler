# APPLY Clean Code by Robert C. Martin

## When to use

Use when prioritizing readability, maintainability, and sustainable development pace over short-term speed. This applies especially during code review, refactoring, and any work touching existing code where clarity determines future change cost.

## Primary bias to correct

The misconception that working code is automatically clean code. Code can run correctly while being expensive, fragile, and slow to modify.

## Decision rules

- Preserve behavior, leave touched code cleaner within scope, and reject schedule pressure or "we'll fix it later" excuses for new mess.
- Write for local reasoning: readers should understand intent and logic without reconstructing hidden state, navigating wide jumps, or guessing vocabulary.
- Use precise names with one consistent term per concept; rename when vocabulary hides intent, overloads meaning, or forces comments to compensate.
- Keep functions small, focused, at a single abstraction level, and told top-down so intent appears before detail.
- Minimize parameters and avoid boolean flags, output parameters, and grab-bag argument lists; model the concept instead.
- Separate commands from queries; functions that answer should not mutate behind the reader's back.
- Keep the happy path readable by isolating error handling, invalid-state handling, and cleanup logic; prefer explicit optionality over null-like sentinel flow when the language supports it.
- Expose behavior rather than raw representation; avoid train-wreck access chains, utility dumping grounds, and mixed responsibilities.
- Keep construction, framework, persistence, transaction, security, and vendor details outside business behavior.
- Make public APIs small, explicit, and hard to misuse; encode boundary logic, required order, and likely changes where readers can see them.
- Use comments only for rationale, constraints, warnings, or external contracts; never as a bandage for bad names or structure.
- Treat tests as production code: readable, deterministic, aligned with the behavior they protect, and backed by proportionate validation.
- Let design emerge through tests, duplication removal, expressiveness, and minimal structure; avoid needless abstractions and infrastructure.
- When touching code, remove the code smell that most increases future change cost, but do not silently broaden the task beyond the smallest cleanup that keeps the requested change safe and readable.

## Trigger rules

- When a function mixes setup, validation, computation, and side effects, split the phases.
- When a comment explains control flow, simplify names or structure first before keeping the comment.
- When a function both mutates and answers, or hides mode switching behind a flag, separate the responsibilities.
- When duplication, repeated switches, or primitive data clusters appear, name the concept with an argument object, polymorphism, or a small abstraction.
- When a boundary leaks framework, vendor, or persistence quirks inward, add or strengthen a local adapter.
- When async, concurrency, or framework entry points enter, isolate threading policy, minimize shared mutable state, define shutdown protocol, and test timing-sensitive behavior.
- When fixing a bug or changing behavior, add or update the test that protects the intended contract.
- When cleanup starts spreading into unrelated areas, cut back to the smallest refactor that keeps the change safe and readable.

## Final checklist

- Can a reader follow the change locally without reconstructing hidden state?
- Are names and intent carrying the meaning without narration?
- Is mutation explicit and the happy path still readable?
- Did framework, persistence, vendor, and construction details stay behind boundaries?
- Did I remove at least one code smell from the touched area?
- Do tests protect the changed behavior?
- Did I actually run the relevant tests or checks?
