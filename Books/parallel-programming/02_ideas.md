# Core Ideas, Concepts & Principles

## PRINCIPLE 1: Concurrency Requires a Mental Model

**Claim:** You cannot write correct concurrent code without a clear, formal model of how execution works.

Sequential code: "This line executes, then that line, then that line."

Concurrent code: "These lines execute in some order, subject to synchronization constraints."

**The principle:** Different mental models lead to fundamentally different code:
- Shared memory model: Think about variables and who touches them
- Actor model: Think about messages and isolated state
- Dataflow model: Think about streams and transformations
- Functional model: Think about immutable values and pure functions

**Why it matters:** Mixing models without realizing it is a common source of bugs.

**Tags:** #mental-models, #concurrency-abstraction, #formal-reasoning

---

## PRINCIPLE 2: Thread Safety is Not Binary

**Common fallacy:** "Code is either thread-safe or it isn't."

**Reality:** Thread safety depends on:
- Which threads are allowed (same thread? any thread?)
- What operations are concurrent (reads? writes? both?)
- What consistency is required (strict? eventual? causal?)

**Example:** A list might be safe for concurrent reads but not concurrent writes. Or it might be safe if all modifications happen on one thread.

**The subtlety:** A class can be "thread-safe for reading" and "thread-safe for single-writer" simultaneously, but not thread-safe for concurrent writes.

**Tags:** #thread-safety-nuance, #consistency-models, #specification

---

## PRINCIPLE 3: Locks Provide Two Distinct Guarantees

**Guarantee 1: Mutual Exclusion**
- Only one thread in the critical section at a time
- Prevents "interleaved instructions" corrupting shared data

**Guarantee 2: Memory Synchronization**
- Changes made by a thread holding the lock are visible to other threads that acquire it later
- This is orthogonal to mutual exclusion

**The crucial insight:** You can have mutual exclusion without visibility, and this is a bug:
```
// Thread A
lock.acquire()
x = 1
lock.release()

// Thread B
lock.acquire()
print x  // Might print 0, not 1, if lock doesn't sync memory!
lock.release()
```

**Tags:** #locks-semantics, #mutual-exclusion, #memory-visibility

---

## PRINCIPLE 4: Memory Ordering is a Fundamental Property

**Execution isn't sequential.** Modern CPUs reorder instructions for performance:
- Loads can move before previous stores
- Stores can be delayed and batched
- Each core has its own cache view of memory

**Memory barriers enforce ordering:**
- **Acquire barrier:** Prevents later operations from moving before it
- **Release barrier:** Prevents earlier operations from moving after it
- **Full barrier:** Prevents all reordering

**Why it matters:** Without understanding barriers, you can't reason about what "volatile" or "synchronized" actually guarantees.

**Tags:** #memory-ordering, #memory-barriers, #CPU-architecture

---

## PRINCIPLE 5: Different Synchronization Primitives Have Different Guarantees

**Mutex/Lock:**
- Mutual exclusion: ✓
- Memory sync: ✓
- Fairness: ✗ (no guarantee who gets in next)
- Progress: Blocking (threads wait, wasting CPU)

**Atomic Operations:**
- Mutual exclusion: ✗ (no critical sections)
- Memory sync: ✓ (with barriers)
- Fairness: ✗
- Progress: Lock-free (no waiting)

**Semaphore:**
- Counting: ✓ (multiple resources)
- Mutual exclusion: ✓ (if count=1)
- Fairness: Sometimes (depends on queue)
- Memory sync: ✗ (depends on implementation)

**Monitor (Lock + Condition Variable):**
- Mutual exclusion: ✓
- Conditional waiting: ✓ (wait for signals)
- Fairness: ✗
- Progress: ✓ (coordinated wake-up)

**The principle:** Choosing the wrong primitive for your problem is a common mistake.

**Tags:** #synchronization-primitives, #formal-properties, #tool-selection

---

## PRINCIPLE 6: Shared State Scaling is Non-Linear

**Amdahl's Law:** If S% of your code must be sequential (holds a lock):
```
Speedup with N cores = 1 / (S + (1-S)/N)
```

**Example:** If 10% of work is sequential:
- 2 cores: ~1.8x speedup
- 4 cores: ~3.1x speedup
- 10 cores: ~5.3x speedup
- 100 cores: ~9.1x speedup

**The practical insight:** Contention on shared state is not linear. As you add cores, the cost of synchronization grows superlinearly because:
- More threads competing for the same lock
- Cache line bouncing between cores
- Memory bandwidth becoming saturated

**Tags:** #amdahl-law, #scalability-limits, #contention-analysis

---

## PRINCIPLE 7: Lock-Free Programming is Not "Faster Programming"

**Misconception:** "Use atomics instead of locks for better performance."

**Reality check:**
- Atomics can be faster if contention is high and critical section is tiny
- But atomics are *harder* to use correctly (retry loops, ABA problems)
- Locks have predictable latency; atomics have variable latency (retries)

**The truth:** Lock-free is for experts optimizing genuine bottlenecks, not a general recommendation.

**Common pitfalls:**
- ABA problem: Value changes A→B→A, CAS thinks it's unchanged
- Memory ordering bugs: Atomics alone don't guarantee visibility
- Retry storms: Busy-waiting on failed CAS operations wastes CPU

**Tags:** #lock-free, #performance-myths, #expert-techniques

---

## PRINCIPLE 8: The Actor Model Eliminates Shared Memory Races

**How actors avoid concurrency bugs:**
1. Each actor has private state (no sharing)
2. Communication only through asynchronous messages
3. No locks needed (no shared data to protect)

**The trade-off:**
- ✓ No data races, no memory visibility issues, simpler reasoning
- ✗ No determinism (message order is not guaranteed)
- ✗ Ordering guarantees are weaker
- ✗ Testing and debugging become harder

**Why it works:** If data isn't shared, it can't be raced on.

**Tags:** #actor-model, #isolation, #message-passing

---

## PRINCIPLE 9: Immutability is Concurrency-Free Lunch (Almost)

**Key insight:** Immutable data cannot be corrupted by concurrent access.

**Guarantee:** If data never changes:
- No thread sees inconsistent state (it's always the same)
- No cache coherency issues (no writes to invalidate)
- No synchronization needed (just read the constant)

**The catch:** Immutability helps with data safety but doesn't solve coordination:
- You still need to coordinate when to switch from version A to version B
- Atomic references solve this, but you're back to synchronization

**Practical use:** Immutable data + atomic reference to it = safe updates without locks on the data.

**Tags:** #immutability, #functional-concurrency, #state-management

---

## PRINCIPLE 10: Progress Guarantees Come in Levels

Different synchronization approaches provide different progress guarantees:

**Blocking:**
- Mutex: If a thread is slow, others must wait (worst progress)

**Obstruction-free:**
- If only one thread is running, it makes progress
- But if multiple threads contend, no guarantee (live-lock possible)

**Lock-free:**
- At least one thread makes progress in any execution
- But not every thread (starvation possible)

**Wait-free:**
- Every thread makes progress in finite steps
- Strongest guarantee, hardest to implement

**The principle:** Stronger guarantees cost more (complexity, synchronization overhead).

**Tags:** #progress-guarantees, #formal-properties, #correctness-levels

---

## PRINCIPLE 11: False Sharing Destroys Scalability

**Hidden problem:** Two threads, different variables, same cache line.

**What happens:**
```
Thread A: x = 1    (on core 0)
Thread B: y = 2    (on core 1)
```

Even though they're modifying different variables, if `x` and `y` are in the same 64-byte cache line:
- Thread A's write invalidates Thread B's cache line
- Thread B's write invalidates Thread A's cache line
- Constant cache-line bouncing (invalidation traffic)
- Severe performance degradation

**The solution:** Padding or array positioning to ensure different threads' data live in different cache lines.

**Tags:** #false-sharing, #cache-effects, #performance-optimization

---

## PRINCIPLE 12: Distributed Concurrency Changes Everything

When concurrency spans multiple machines:

**New realities:**
- Network failures are common (not rare exceptions)
- Latency goes from nanoseconds to milliseconds (6+ orders of magnitude)
- Synchronous coordination becomes impractical
- Consistency must be eventual (not immediate)

**Consequence:** Algorithms that work on a single machine (strict consensus) become impossible across unreliable networks.

**Solution:** Asynchronous, message-based protocols with weaker guarantees (Byzantine-tolerant consensus, causal ordering).

**Tags:** #distributed-systems, #network-failures, #asynchronous-protocols

---

## PRINCIPLE 13: Consistency Models Define the Rules of the Game

**Strict Consistency (Linearizability):**
- All operations appear in a total order
- Every read sees the latest write
- Hardest to achieve, most intuitive

**Causal Consistency:**
- Operations causally related must appear ordered
- Concurrent operations can be reordered
- Sweet spot for many distributed systems

**Eventual Consistency:**
- All replicas converge to the same state, eventually
- Allows maximum availability and partition tolerance
- Weak guarantee, but practical

**The principle:** Pick the consistency model that matches your constraints, not the strongest one.

**Tags:** #consistency-models, #distributed-systems, #trade-offs

---

## PRINCIPLE 14: Concurrency Testing Requires New Strategies

**Traditional testing fails:** Unit tests run sequentially; they can't trigger most race conditions.

**Why:** Race conditions depend on precise timing, hardware scheduling, and cache behavior.

**Better strategies:**
- **Stress testing:** Run the code for hours under load, count failures
- **Model checking:** Explore all possible interleavings (tools: ThreadSanitizer, Java PathFinder)
- **Formal verification:** Mathematically prove correctness (tools: TLA+, Alloy)
- **Property-based testing:** Generate random concurrent scenarios, check invariants

**The insight:** You can't test your way to concurrent correctness; you must reason about it.

**Tags:** #testing-concurrency, #verification, #reliability

---

## PRINCIPLE 15: Parallelism is Not Always Worth It

**Amdahl's Law again:** If only 5% of your work parallelizes, speedup with 10 cores is ~2x.

**Before parallelizing, ask:**
1. Is the problem actually parallel? (Different data streams, not just multiple tasks)
2. Is the speedup worth the complexity? (Concurrent code is 5-10x harder to understand and debug)
3. Have you optimized the sequential version first? (Usually the first speedup comes from sequential optimization)

**The radical idea:** Most code should be sequential. Only parallelize when:
- Profiling shows a real bottleneck
- The speedup is worth the additional complexity
- The problem has genuine data parallelism

**Tags:** #pragmatism, #premature-optimization, #complexity-cost

---

## How These Principles Connect

```
Principles 1-2    → Understanding what thread safety means
Principles 3-5    → Tools and guarantees for achieving it
Principles 6-7    → Why scalability is hard
Principles 8-9    → Alternative approaches (actors, immutability)
Principles 10-11  → Lower-level performance considerations
Principles 12-13  → How things change at scale
Principles 14-15  → Practice and pragmatism
```

**Tags:** #principle-hierarchy, #knowledge-integration, #progressive-understanding
