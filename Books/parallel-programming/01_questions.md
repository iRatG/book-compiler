# Central Questions & Inquiry Structure

## The Big Question

**"What are the fundamental models and patterns for writing correct, scalable concurrent code?"**

Parallel programming is not about threads—it's about coordination. This book explores the mental models, abstractions, and guarantees that allow developers to reason about systems where multiple execution flows interact.

**Tags:** #core-inquiry, #concurrent-systems, #mental-models

---

## Part I: Foundational Questions on Concurrency

### Question 1: What Makes Code "Thread-Safe"?

Many developers think thread safety means "I added a lock." This is dangerously incomplete.

**The deeper layers:**
- Mutual exclusion (only one thread in critical section)
- Memory visibility (changes made by one thread are seen by others)
- Ordering guarantees (operations happen in expected sequence)
- Progress guarantees (threads don't starve or deadlock)

**Sub-question:** Can you have mutual exclusion without visibility guarantees? (Yes—and this is a common bug.)

**Tags:** #thread-safety, #mutual-exclusion, #memory-visibility

---

### Question 2: What is the Relationship Between Locks and Memory?

Developers think locks are just about preventing concurrent access. But locks also establish synchronization barriers.

**Critical distinction:**
- A lock protects a *variable* (prevents races)
- A lock also synchronizes *memory* (ensures visibility)

**The question:** Why must Java's volatile keyword exist if synchronization exists?

**Tags:** #locks-memory-relationship, #synchronization-barriers, #volatile-semantics

---

### Question 3: Why Are Some Concurrency Bugs Nearly Impossible to Reproduce?

Race conditions, visibility issues, and ordering bugs depend on precise timing and hardware behavior.

**The hard questions:**
- Why does "it works on my machine" happen so often in concurrent code?
- How do you test code that fails 1 in 10,000 times?
- Can single-threaded tests catch concurrency bugs? (Almost never.)

**Tags:** #race-conditions, #nondeterminism, #testing-challenges

---

### Question 4: What is the Difference Between Concurrency and Parallelism?

These terms are often confused. But they're fundamentally different:

- **Concurrency:** Multiple tasks *appear* to run simultaneously (switching between them)
- **Parallelism:** Multiple tasks *actually* run simultaneously (on different cores)

**Question:** Can you have concurrency without parallelism? Yes. Parallelism without concurrency? No.

**Tags:** #concurrency-vs-parallelism, #definitions, #execution-models

---

## Part II: Questions About Synchronization Mechanisms

### Question 5: When Should You Use Locks vs. Lock-Free Structures vs. Message Passing?

Three fundamentally different approaches:
1. **Locks (Pessimistic):** Assume conflicts, block preemptively
2. **Lock-Free (Optimistic):** Assume no conflict, retry on failure
3. **Message Passing:** Avoid shared state entirely

**The selection question:** How do you choose?

**Tags:** #synchronization-mechanisms, #performance-tradeoff, #design-choice

---

### Question 6: What Guarantees Does Each Synchronization Primitive Actually Provide?

- **Mutex/Lock:** Mutual exclusion + memory synchronization
- **Semaphore:** Counting resource availability
- **Monitor:** Lock + built-in condition variable
- **Atomic:** Lock-free visibility without locks
- **Barrier:** Synchronization point for all threads

**Sub-question:** Why is a semaphore not a lock? (Different progress guarantees.)

**Tags:** #synchronization-primitives, #formal-guarantees, #correctness-properties

---

### Question 7: How Do Memory Barriers and Happens-Before Relations Work?

On modern multi-core systems, operations can execute out of order unless prevented.

**The fundamental question:**
- How does a CPU ensure that store operations are actually visible to other cores?
- Why can't reads move past writes?
- What does "volatile" actually guarantee vs. what does it not?

**Tags:** #memory-barriers, #happens-before, #memory-ordering

---

## Part III: Questions About Parallelism Patterns

### Question 8: What Are the Main Parallelism Patterns, and When Does Each Apply?

- **Fork-Join:** Divide-and-conquer tasks (tree-like execution)
- **Map-Reduce:** Stateless parallel transformation
- **Pipeline:** Sequential stages, each processing in parallel
- **Task Pool:** Unbounded queue, worker threads grab tasks
- **Producer-Consumer:** One thread generates, another processes

**Question:** Why doesn't one pattern fit all problems?

**Tags:** #parallelism-patterns, #architectural-choices, #scalability

---

### Question 9: How Do You Recognize When Shared State is the Problem?

Many performance issues aren't about "not enough parallelism" but about "too much contention."

**The diagnosis question:**
- False sharing (threads on different cores invalidating each other's cache lines)
- Lock contention (many threads waiting for the same lock)
- Atomic contention (CAS operations serializing on one memory location)

**Tags:** #contention, #false-sharing, #performance-diagnosis

---

### Question 10: What is an Actor Model, and Why is It Fundamentally Different?

Actors eliminate shared memory entirely:
- Each actor has private state
- Communication via asynchronous message passing
- No locks needed, because there is nothing to lock

**Question:** Does this actually solve concurrency, or just move the problem? (It solves *coordination*.)

**Tags:** #actor-model, #message-passing, #isolation

---

## Part IV: Questions About Distributed and Large-Scale Concurrency

### Question 11: What Changes When Concurrency Spans Multiple Machines?

- Network failures are not rare edge cases—they are normal
- Latency increases by 7+ orders of magnitude
- Synchronous communication becomes impractical

**The cascade:**
- Consensus becomes genuinely hard (Byzantine Generals)
- Consistency models must be relaxed (eventual consistency)
- Causality becomes more important than atomic ordering

**Tags:** #distributed-systems, #network-failures, #consistency-models

---

### Question 12: What is the CAP Theorem, and Why Can't You Have All Three?

- **Consistency:** All nodes see the same data
- **Availability:** System responds to requests
- **Partition tolerance:** System survives network splits

**The hard question:** Which two do you choose, and how does that change your design?

**Tags:** #CAP-theorem, #distributed-tradeoffs, #architecture-choice

---

### Question 13: How Do Immutability and Functional Programming Eliminate Concurrency Bugs?

If data never changes:
- No race conditions (nothing to race on)
- No memory visibility issues (reading old data is still correct)
- No need for locks

**Question:** Is immutability the answer to all concurrency problems? (No—coordination still matters.)

**Tags:** #immutability, #functional-concurrency, #state-management

---

## Part V: Meta-Questions (How You Think About Concurrency)

### Question 14: How Do You Test Concurrent Code?

Traditional unit tests can't catch most concurrency bugs because:
- Race conditions depend on timing
- Hardware behavior varies
- Bugs may occur 1 in millions of runs

**Practical questions:**
- Stress testing (run for hours, count failures)
- Model checking (exhaustive state exploration)
- Formal verification (mathematical proofs)

**Tags:** #testing-concurrency, #verification, #reliability

---

### Question 15: When Should You Avoid Concurrency Entirely?

Not every problem requires parallel code:
- Sequential code is much simpler
- Overhead of coordination has real costs
- Amdahl's Law limits speedup (serial sections dominate)

**The decision:**
- Is the problem actually parallel? (Different data flow, not just multiple threads)
- Is the speedup worth the complexity? (Usually no, until performance demands it)

**Tags:** #complexity-cost, #premature-parallelization, #pragmatism

---

## How These Questions Organize the Book

```
Part I: Questions 1-4     → Foundation (What is thread safety?)
        Questions 5-7     → Mechanisms (How to synchronize)
Part II: Questions 8-10   → Patterns (How to structure parallelism)
Part III: Questions 11-13 → Scale (How concurrency changes at scale)
Part IV: Questions 14-15  → Practice (How to verify and decide)
```

Each section builds from basic definitions toward increasingly sophisticated patterns and guarantees.

**Tags:** #book-structure, #inquiry-framework, #progression
