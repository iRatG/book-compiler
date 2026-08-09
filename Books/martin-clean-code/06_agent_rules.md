# APPLY Clean Code by Robert C. Martin

**Version:** 2.0 (Optimized for Agent Use)  
**Quality:** Each rule validated (Extract → Synthesize → Validate)

---

## When to use

Use when prioritizing readability, maintainability, and sustainable development pace. This applies especially during code review, refactoring, and any work touching existing code where clarity determines future change cost.

## Primary bias to correct

The misconception that working code is automatically clean code. Code can run correctly while being expensive, fragile, and slow to modify.

---

## Decision Rules

### R1: Preserve behavior, leave touched code cleaner, reject shortcuts
**Quality: 95%** (100% source fidelity, high necessity, medium actionability)

**What it means:**
- When you touch code, your goal is (1) don't break it, (2) leave it better than you found it
- Reject arguments like "we're in a hurry" or "we'll fix it later" as reasons to add mess
- This is a **professional duty**, not optional

**Conditions to verify:**
- ✓ Did I preserve the original behavior? (Run tests, check edge cases)
- ✓ Is there less code smell after my change than before? (Remove ≥1 smell)
- ✓ Did I reject "we'll refactor later"? (No // TODO refactor, no FIXME)

**Fail signals — stop and revise if:**
- ✗ You added new complexity to avoid fixing existing complexity
- ✗ You left the code worse than when you started (even if change is smaller)
- ✗ You added a comment explaining why you didn't clean something up

**Sources:**
- C-001, C-002, C-003 (core: people-first, duty, speed)
- Arg-001 (tech debt costs 10x later)
- App-001 (Boy Scout Rule: leave camp cleaner)

---

### R2: Write for readers — no hidden state, no wide jumps, intent in names
**Quality: 92%** (High source coverage, excellent necessity, medium actionability)

**What it means:**
- Code is local-readable when a reader understands each function/module without jumping elsewhere
- Hidden state (mutations outside function scope) breaks local reasoning
- Readers should grasp intent from names alone, without reconstructing context

**Conditions to verify:**
1. **No hidden state mutation:** 
   - ✓ Function doesn't modify globals, static fields, or parent state invisibly
   - ✓ Side effects are explicit in the name (`saveUser()` not `process()`)
   - ✓ State changes are obvious from reading one function, not scattered across imports

2. **No wide jumps:**
   - ✓ Related logic is close together (methods of same class near each other)
   - ✓ Intent appears before implementation detail
   - ✓ No circular references or distant dependencies to understand flow

3. **Names carry intent:**
   - ✓ Variable name answers "what" and "why" (not `x`, `data`, `result`)
   - ✓ Function name indicates what it does and its context
   - ✓ One term per concept everywhere in the codebase (customer OR client, not both)

**Fail signals — stop and revise if:**
- ✗ Reader must trace through 3+ functions to understand what one function does
- ✗ Reader sees a function call and must jump to another file to understand the effect
- ✗ Variable names like `x1`, `list1`, `data` force comments to explain intent

**Sources:**
- C-004, C-006, C-007 (naming rules)
- Ev-001 (bad: `getThem()`; good: `getFlaggedCells()`)
- Arg-002 (readability > performance for 99% of code)

---

### R3: Use precise names, one term per concept
**Quality: 90%** (Excellent source, high necessity, high actionability)

**What it means:**
- Every name must reveal intent and answer the "why", "what", "how" of its thing
- Bad names (`a`, `x1`, `data`, `temp`) signal you don't understand the problem
- Consistency: pick "Customer" — use it everywhere. Never mix "Customer" and "Client" for the same concept

**Conditions to verify:**
- ✓ Does the name tell me why this thing exists? (Why is it named that?)
- ✓ Does the name tell me what it represents? (What is it?)
- ✓ Does the name tell me how to use it? (How do I interact with it?)
- ✓ Is this term used consistently across the codebase? (Search for near-synonyms like customer/client)

**Fail signals — stop and revise if:**
- ✗ Code comment needed to explain what a variable means (comment indicates bad name)
- ✗ Same concept has multiple names in different modules
- ✗ Name is misleading (accountList that's not actually a List)

**Sources:**
- C-004, C-005 (name quality reflects understanding)
- C-006, C-007 (consistency, avoid misinformation)
- Ev-001 (example: list1 vs flaggedCells)

---

### R4: Keep functions small, focused, single abstraction level
**Quality: 88%** (High source, excellent necessity, medium actionability — "small" can be subjective)

**What it means:**
- One function = one reason to change
- Small means "fits on screen" in your editor (typically 3-20 lines)
- Tell the story top-down: intent first, details later

**Conditions to verify:**
- ✓ Can I name this function with a simple verb phrase? (If name has "and", function does too much)
- ✓ Does it fit on one screen? (Can I see start and end together)
- ✓ Does it have one level of abstraction? (Not mixing high-level business logic with low-level details)
- ✓ Can I describe it in one sentence? (If not, it does multiple things)

**Fail signals — stop and revise if:**
- ✗ Function name includes "and" or "or" (save AND send email)
- ✗ Function has multiple independent blocks separated by blank lines (each block could be separate)
- ✗ You need comments to explain control flow within the function
- ✗ The function has 2+ different reasons to change

**Sources:**
- C-008, C-009 (single responsibility, small size)
- Ev-002 (bad: save() does validation + encryption + persist + email)

---

### R5: Minimize parameters; avoid boolean flags and grab-bag lists
**Quality: 85%** (Good source, medium actionability — depends on language/context)

**What it means:**
- Parameters are "code noise" — every parameter adds complexity to understand and call the function
- 0-1 parameters is best; 2-3 is acceptable; 4+ is a smell
- Boolean parameters hide state switches (mode flags); model the concept instead

**Conditions to verify:**
- ✓ Can I understand this function's behavior from its name alone? (Or does calling site need parameter docs?)
- ✓ Are all parameters necessary? (Could they be constructor params, fields, or separate functions?)
- ✓ No boolean flag hiding mode switch? (If `saveUser(user, sendEmail: true)`, split into two functions)
- ✓ If many params, wrapped in an object that models the concept? (Argument object pattern)

**Fail signals — stop and revise if:**
- ✗ Function has 4+ parameters
- ✗ Boolean parameter that changes behavior (sendEmail, async, etc.)
- ✗ "Grab-bag" parameter list with unrelated things (pass `(user, template, mailServer, locale)` separately)

**Sources:**
- C-010, C-035 (minimize parameters)
- Argument objects reduce noise while being explicit

---

### R6: Separate commands from queries; don't mutate and return
**Quality: 92%** (Excellent source clarity, high necessity, high actionability)

**What it means:**
- A function either **does something** (command, returns void) or **returns something** (query, returns data)
- Never both: `var saved = user.save()` should not also persist to database invisibly
- This prevents hidden side effects that break local reasoning

**Conditions to verify:**
- ✓ If function returns a value, does it have side effects? (Then split: query and command)
- ✓ If function name is `get*`, `is*`, `has*` — does it modify anything? (No, queries are pure)
- ✓ If function modifies state, return void or explicit status, not data

**Fail signals — stop and revise if:**
- ✗ Function both returns a value AND modifies external state invisibly
- ✗ Function named `get*` or `fetch*` but also writes/deletes something
- ✗ Calling code checks result of a mutation to know if it succeeded

**Sources:**
- C-011 (command/query separation)
- Ev-002 (save() returns true but also mutates)

---

### R7: Keep happy path readable; isolate error/invalid/cleanup handling
**Quality: 90%** (Good source, excellent necessity, medium actionability)

**What it means:**
- The success case should be crystal clear (no error-checking logic in the flow)
- Errors, invalid inputs, and cleanup should be separate: raise exceptions, use early returns, or explicit `Optional<T>`
- Prefer explicit optionality (typed `Result<T>`, `Optional<T>`) over null-checks scattered in logic

**Conditions to verify:**
- ✓ Can I read the success path without seeing error handling?
- ✓ Are errors raised as exceptions (not error codes, not null)? 
- ✓ Invalid inputs rejected early (return/throw) rather than checked throughout?
- ✓ No null-checking scattered through business logic? (Use `Optional<T>` or explicit validation at boundary)

**Fail signals — stop and revise if:**
- ✗ Success logic is buried in nested if-else checking for errors
- ✗ Function returns null or special values (-1, empty string) instead of raising or using Optional
- ✗ Error cleanup code is mixed with business logic

**Sources:**
- C-020, C-021, C-023 (error handling as first-class, no null)
- Early return pattern keeps happy path clean

---

### R8: Expose behavior not raw representation; avoid mixed responsibilities
**Quality: 88%** (Good source, high necessity, medium actionability)

**What it means:**
- Don't expose raw data; expose intent
- Train-wreck access (`obj.field.subfield.data`) hides responsibilities and breaks encapsulation
- No "utility dumping grounds" (God classes with 50 unrelated methods)

**Conditions to verify:**
- ✓ Is internal state accessed through methods that hide implementation? (Not raw getters exposing structure)
- ✓ Does the class have a single, clear responsibility?
- ✓ No method that does things unrelated to that responsibility?
- ✓ Access patterns don't require knowing internal structure?

**Fail signals — stop and revise if:**
- ✗ Caller does `obj.getState().getData().getValue()` (train wreck)
- ✗ Class has 20+ public methods doing unrelated things
- ✗ Internal state exposed via public fields or simple getters (no behavior hiding)

**Sources:**
- C-024, C-025 (encapsulation, hide details)
- Mixed responsibilities create high cognitive load

---

### R9: Keep construction/framework/persistence/vendor details outside business logic
**Quality: 90%** (High source, excellent necessity, medium actionability)

**What it means:**
- Business logic should never know HOW to construct its dependencies, persist data, or use frameworks
- Use adapters/facades to isolate those concerns
- Business logic reads as domain logic, not plumbing

**Conditions to verify:**
- ✓ Does the business class create its own dependencies? (No — they're injected or obtained via factory)
- ✓ Is persistence logic in a separate DAO/Repository layer? (Not mixed with business rules)
- ✓ Does business logic reference framework code directly? (No — framework is in adapters)
- ✓ Is the domain logic readable without knowing the framework?

**Fail signals — stop and revise if:**
- ✗ Business class instantiates database connections or HTTP clients directly
- ✗ Domain model imports from Spring, Hibernate, etc. (framework leaks in)
- ✗ Transaction/security logic tangled with business rules
- ✗ Calling code must know how to construct complex object graphs

**Sources:**
- C-027 (wrap third-party code)
- Ev-002 (email/events separated from save logic)
- Hexagonal architecture alignment

---

### R10: Make public APIs small, explicit, hard to misuse
**Quality: 85%** (Good source, high necessity, medium actionability)

**What it means:**
- Public APIs should prevent common misuse through design
- Encode boundary logic, required order, likely changes where readers can see them
- Minimize what's exposed; make the common case easy, the wrong case hard

**Conditions to verify:**
- ✓ Is the public API minimal? (Only essential methods/fields exposed)
- ✓ Can misuse be prevented by the type system/API shape? (Not by convention or docs)
- ✓ Are preconditions explicit? (Type system or validation, not silent assumptions)
- ✓ Required order enforced by structure? (Builder pattern, immutable objects after construction)

**Fail signals — stop and revise if:**
- ✗ Public API has many methods that could be private or internal
- ✗ Easy to misuse the API and have subtle bugs (not caught at compile time)
- ✗ Order of operations must be documented because API doesn't enforce it

**Sources:**
- C-010, C-027 (API design, small exposure)
- Learning Tests (C-028) validate API understanding

---

### R11: Use comments only for rationale, constraints, warnings, contracts
**Quality: 93%** (Excellent source, high necessity, high actionability)

**What it means:**
- Comments should explain **why**, **constraints**, or **gotchas** — not narrate what code does
- Code is for "what", comments are for "why"
- If you're writing a comment to explain control flow, simplify the code instead

**Conditions to verify:**
- ✓ Does the comment explain WHY (not WHAT)?
- ✓ Is it about a constraint or surprising gotcha?
- ✓ Is it about an external contract (API requirement, RFC)?
- ✓ Does the code itself express WHAT clearly (so comment isn't needed)?

**Fail signals — stop and revise if:**
- ✗ Comment restates code (// increment counter above `count++`)
- ✗ Comment explains control flow (indicates code isn't clear enough)
- ✗ Stale/outdated comment (worse than no comment)

**Sources:**
- C-012, C-013 (comments as rationale only, not narration)
- C-014 (delete old comments)

---

### R12: Treat tests as production code
**Quality: 94%** (Excellent source, high necessity, medium actionability)

**What it means:**
- Tests are the first and primary user of your API
- Tests must be readable, deterministic, aligned with the behavior they protect
- Test failures should be clear and unambiguous

**Conditions to verify:**
- ✓ Test name clearly describes what is being tested and what's expected?
- ✓ Test is deterministic (same result every run)?
- ✓ Test is focused (one reason to fail)?
- ✓ Test is aligned with protected contract (not testing implementation)?
- ✓ Test failure message is clear (not cryptic assertions)?

**Fail signals — stop and revise if:**
- ✗ Test name is vague (testUser(), testSave())
- ✗ Test has random data or timing issues (non-deterministic)
- ✗ Test tests implementation details (private methods, internal state)
- ✗ Test failure message doesn't say what was expected vs actual

**Sources:**
- C-030, C-031, C-032 (tests as first user, TDD confidence, clean tests)
- App-002 (TDD cycle: red → green → refactor)

---

### R13: Let design emerge through tests and refactoring; avoid needless abstractions
**Quality: 87%** (Good source, high necessity, low actionability — depends on experience)

**What it means:**
- Write the simplest code that passes tests
- Refactor out duplication incrementally
- Don't add abstractions you don't need yet (YAGNI)
- Design should be a consequence of following previous rules, not a predetermined plan

**Conditions to verify:**
- ✓ Did I write the simplest implementation that passes all tests?
- ✓ Am I repeating code 3+ times before extracting? (Not 2 times)
- ✓ Is this abstraction actually used? (Not "might be useful later")
- ✓ Does this code have a high enough cost-of-change to justify the abstraction?

**Fail signals — stop and revise if:**
- ✗ You're building "infrastructure" for features that don't exist yet
- ✗ You extract a concept after seeing it twice (premature)
- ✗ You add a design pattern "because it's a best practice" without a concrete problem
- ✗ You inherit hierarchy of abstract classes that aren't really used polymorphically

**Sources:**
- C-040, C-045, C-046 (refactoring, emergent design, iterative process)
- Ass-003 (Boy Scout: improve incrementally, not all at once)

---

### R14: When touching code, remove the smell most increasing change cost
**Quality: 91%** (Excellent source, high necessity, medium actionability)

**What it means:**
- Identify which code smell (duplication, wrong boundary, unclear name) costs most to leave
- Fix that, but don't silently broaden scope
- Better to fix one smell perfectly than five smells partially

**Conditions to verify:**
- ✓ Did I identify the highest-leverage smell? (Which one slows down change most?)
- ✓ Is my fix scoped tightly? (Not expanding to unrelated areas)
- ✓ Does the fix actually reduce future change cost?
- ✓ Are all tests still passing?

**Fail signals — stop and revise if:**
- ✗ You're fixing smell X but notice smell Y and refactor both (scope creep)
- ✗ You fix a smell in one place but not in three similar places (inconsistent)
- ✗ Your change "while I'm here" is larger than the original fix
- ✗ You can't articulate which smell you were fixing

**Sources:**
- C-041, C-042, C-043 (smell catalog)
- Ass-003 (incremental Boy Scout cleanup, not all-at-once refactoring)

---

## Trigger Rules

### T1: When a function mixes setup/validation/computation/effects → split phases
**Quality: 89%**

Detect: Function has 3+ unrelated blocks (each separated by blank line or comment).  
Action: Extract each phase into separate function or sequence.

**Example:**
```java
// Before: all mixed
void save(User user) {
  validateUser(user);           // phase 1
  encryptPassword(user);        // phase 2  
  database.save(user);          // phase 3
  sendNotification(user);       // phase 4
}

// After: phases separated
void save(User user) {
  validateUser(user);
  User encrypted = encryptPassword(user);
  database.save(encrypted);
}
// Email sent by event listener (separate concern)
```

---

### T2: When a comment explains control flow → simplify code first
**Quality: 90%**

Detect: You're tempted to add a comment explaining how a loop/condition works.  
Action: Extract method, rename variable, simplify condition — THEN add comment only if still needed.

**Example:**
```java
// Before: comment explains flow
for (Employee e : employees) {
  // Check if salary increase should be applied
  if (e.getSalary() > 50000 && e.getYearsEmployed() > 2) {
    applyRaise(e);
  }
}

// After: code explains itself
for (Employee e : employees) {
  if (isEligibleForRaise(e)) {
    applyRaise(e);
  }
}
```

---

### T3: When a function mutates AND returns a value → separate them
**Quality: 93%**

Detect: Function both returns data and modifies external state.  
Action: Split into command (void, mutates) and query (returns data, pure).

**Example:**
```java
// Before: mixes command and query
boolean save(User user) {
  database.persist(user);  // side effect
  return true;             // return result
}

// After: separated
void save(User user) {
  database.persist(user);
}
// Caller: if (wasSuccessful) is replaced with try/catch
```

---

### T4: When duplication/switches/primitive clusters appear → name the concept
**Quality: 88%**

Detect: Same logic pattern appears 3+ times, or related data always grouped.  
Action: Extract to a named concept (method, class, enum, argument object).

**Example:**
```java
// Before: duplication
if (account.type == "checking") { doCheckingThing(); }
if (account.type == "savings") { doSavingsThing(); }
if (account.type == "investment") { doInvestmentThing(); }

// After: named concept
accountProcessor.processFor(account);
// Or: enum AccountType with behavior
```

---

### T5: When boundary leaks framework/vendor/persistence quirks → add adapter
**Quality: 90%**

Detect: Business code imports from Spring, Hibernate, HTTP library, etc.  
Action: Create adapter/facade that hides the plumbing.

**Example:**
```java
// Before: framework leaks in
class UserService {
  @Autowired private UserRepository repo;  // Spring
  
  void process(User u) {
    repo.save(u);  // Hibernate
  }
}

// After: adapter hides framework
class UserService {
  private final UserRepository repo;  // interface, not Spring
  
  void process(User u) {
    repo.save(u);  // business logic, adapter handles Spring
  }
}
// Adapter lives in infrastructure layer
```

---

### T6: When async/concurrency/framework entry points appear → isolate threading policy
**Quality: 82%**

Detect: Threading, async callbacks, or framework lifecycle in business logic.  
Action: Create clear boundary; business logic doesn't know it's async; threading is isolated.

**Example:**
```java
// Before: threading mixed in
class UserProcessor {
  void process(User u) {
    executor.submit(() -> {           // threading here
      validateUser(u);                // business logic here
      database.save(u);
    });
  }
}

// After: threading isolated
class UserProcessor {
  void process(User u) {
    validateUser(u);        // business logic, pure
    database.save(u);
  }
}
// Caller handles threading: executor.submit(() -> processor.process(u))
```

---

### T7: When fixing a bug or changing behavior → add/update the protecting test
**Quality: 95%**

Detect: You're about to commit a bug fix or behavior change.  
Action: Add test FIRST (if missing) or update existing test to prevent regression.

**Example:**
```java
// Before: bug exists, no test
public int calculateDiscount(int quantity) {
  return quantity * 0.1;  // Bug: returns cents, should return percent
}

// After: add test first, then fix
@Test void discountShouldBePercentage() {
  assertEquals(10, calculateDiscount(100));  // 100 units = 10% discount
}

public int calculateDiscount(int quantity) {
  return Math.min(quantity / 10, 20);  // Fixed + test protects it
}
```

---

### T8: When cleanup starts spreading into unrelated areas → cut scope back
**Quality: 89%**

Detect: Your refactoring is touching files/modules unrelated to original change.  
Action: Stash unrelated cleanup; commit only the change + minimum necessary cleanup.

**Example:**
```
Original task: Fix the login bug (in UserAuthenticator)

⚠️  Danger: While fixing, you notice UserManager is messy...
    and Repository has bad naming... and Config needs refactoring...
    
✓  Correct: Fix login bug, clean up nearby UserAuthenticator code only.
  Commit login fix. Create separate issues for UserManager, Repository, Config.
```

---

## Final Checklist

Before committing your change:

- [ ] Can a reader follow this change locally (line by line) without jumping elsewhere?
- [ ] Are names and intent carrying the meaning? (No cryptic names forcing comments)
- [ ] Is mutation explicit? (Commands clear, queries pure) Happy path readable? (Errors isolated)
- [ ] Did framework/persistence/vendor details stay behind boundaries?
- [ ] Did I remove at least one code smell from the touched area? (Boy Scout)
- [ ] Do tests protect the changed behavior (or new feature)?
- [ ] Did I actually run the tests, not just assume they pass?

---

**Quality Score Summary:**

Decision rules: 14 rules, average Quality 90% (range: 85-95%)  
Trigger rules: 8 rules, average Quality 90% (range: 82-95%)  
Overall coverage: 39/46 principles (85%), all with explicit audit trail

Each rule cites sources and fail signals. Use Quality score to assess confidence.
