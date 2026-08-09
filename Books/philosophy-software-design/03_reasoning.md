# A Philosophy of Software Design — Reasoning & Evidence

## ARGUMENT 1: Complexity Growth is Exponential, Not Linear
**Principle:** Complexity is the Enemy

A 100k-line system is not 2x as complex as a 50k-line system. Complexity grows exponentially because:
1. More code = more interactions between parts
2. Developers must understand more to make changes
3. Mistakes increase with cognitive load
4. Fixing mistakes introduces more complexity

**Evidence:** Empirical studies show development velocity decreases as systems grow, despite adding developers.

**Mechanism:** Each new module increases the number of potential interactions with existing modules geometrically.

---

## ARGUMENT 2: Change Amplification Signals Bad Design
**Principle:** Dependencies and Obscurity are Complexity's Causes

When changing one thing requires changing many things, the design is bad.

**Example:** Website where banner color is hardcoded in 100 pages. Changing color requires 100 changes. This is change amplification.

**Better design:** Color defined in one place; all pages reference it. Changing color = 1 change.

**Cost:** Change amplification multiplies developer time by 2-100x for simple changes.

---

## ARGUMENT 3: Tactical Programming Creates Compounding Technical Debt
**Principle:** Strategic Programming vs Tactical Programming

Ousterhout's research: TDD actually takes less time even on first task:
- Tactical: Hack out feature in 1 day; 10% slower than estimate
- Strategic: Design first, then code; takes same 1 day
- Tactical on next feature: Now takes 2 days (complexity compounds)
- Strategic on next feature: Still takes 1 day

**Long-term ROI:** 10-20% investment in design pays for itself in 6-18 months.

---

## ARGUMENT 4: Module Depth Ratio Determines Reusability
**Principle:** Modules Should Be Deep

Module depth = (functionality provided) / (interface complexity)

Deep modules (high ratio):
- Unix I/O: 5 functions (open, read, write, seek, close) = hundreds of thousands of lines of implementation hidden
- Result: Reusable; easy to use; powerful

Shallow modules (low ratio):
- Java I/O: Need FileInputStream, BufferedInputStream, ObjectInputStream = 3 objects for reading file
- Result: Verbose; hard to reuse; weak functionality per layer

**Practical consequence:** Deep modules are reused; shallow modules copied or wrapped, adding complexity.

---

## ARGUMENT 5: Hidden Knowledge Prevents Divergence
**Principle:** Information Hiding

When knowledge is hidden (encapsulated), it's maintained in one place. When knowledge is visible, it must stay synchronized across multiple places.

**Example:** JSON parsing logic hidden in one module vs. JSON parsing code in 3 different modules. If JSON format changes:
- Hidden: Update 1 place; all 3 uses automatically work
- Visible: Update 3 places; risk one is missed; bugs

**Cost:** Each duplicate of knowledge = opportunity for bugs when knowledge changes.

---

## ARGUMENT 6: Back-Door Leakage is Worse Than Interface Leakage
**Principle:** Information Leakage is a Red Flag

**Interface leakage:** Knowledge is in interface; at least it's visible
- Can see the dependency in the code
- Can trace what changes will affect what

**Back-door leakage:** Knowledge shared but not in interfaces; hidden
- Cannot see the dependency by reading code
- Changes break things mysteriously
- Much harder to diagnose and fix

**Example:** Two classes both know HTTP request format but don't have explicit dependency. Changing format breaks both non-obviously.

---

## ARGUMENT 7: Temporal Decomposition Encourages Information Leakage
**Principle:** Avoid Temporal Decomposition

When you organize code by execution order (step 1, step 2, step 3), knowledge about each step is often scattered.

**Example:** HTTP server split into: ReadRequest class and ParseRequest class. Both have knowledge of HTTP format = leakage.

**Better:** CombinedHTTPRequest class. Single place knows HTTP format.

---

## ARGUMENT 8: Generality Improves Reusability; Specialization Requires Workarounds
**Principle:** General-Purpose Modules are Deeper

General-purpose API (works with any text):
```
class TextStorage:
    def insert(position, text): ...
    def delete(position, count): ...
```

Can use for any text editing scenario. Reusable.

Special-purpose API (optimized for sequential editing):
```
class DocumentEditor:
    def append_at_end(text): ...
```

Only works for sequential editing. Cannot reuse for other scenarios. Clients must implement workarounds.

---

## ARGUMENT 9: Defining Errors Away Simplifies APIs
**Principle:** Define Errors Out of Existence

**Bad API:**
```
unset variable
# Error if variable doesn't exist
```

**Good API (redefine semantics):**
```
ensure_variable_not_set
# Success whether variable existed or not
```

Changed the API definition so error case no longer exists. Simpler.

**Cost:** Requires thinking differently about the problem; usually worth it.

---

## ARGUMENT 10: Obvious Code Reduces Cognitive Load
**Principle:** Code Should be Obvious

When code is non-obvious, developers must:
1. Read the code
2. Trace execution mentally
3. Understand intent
4. Verify understanding

Obvious code skips steps 2-4; developer gets it immediately.

**Cost:** Obvious code takes slightly longer to write; saves 10x time in reading/understanding.

---

## ARGUMENT 11: Consistency Enables Pattern Recognition
**Principle:** Use Strong Names and Consistency

When developers see consistent patterns, they recognize them instantly.

**Example:** If all managers have `team_members` attribute and all members have `reports_to` attribute, code becomes predictable. Consistent naming enables instant understanding.

Inconsistency forces developers to read carefully to understand each situation.

---

## ARGUMENT 12: Comments Explain What Code Cannot
**Principle:** Comments Are Essential for Deeper Modules

Good comments explain:
- Why this design (not what it does)
- Non-obvious consequences
- Interactions with other modules
- Intent (what problem this solves)

Code explains what; comments explain why.

**Cost:** Comments take time; but save 10x time in understanding.

---

## ARGUMENT 13: Considering Multiple Designs Reveals Trade-offs
**Principle:** Design It Twice

First design: Often good but not optimal. Can't see all consequences.
Second design: Different approach; reveals what first design sacrificed.
Third design: Can synthesize best of both.

Result: Final design much better than if you'd just built first idea.

---

## ARGUMENT 14: Pushing Complexity to Callers Multiplies It
**Principle:** Pull Complexity Downward

If module is complex but clients see it, each caller must handle the complexity.

**Example:** If JSON parsing complex and done by each caller = 10 callers = complexity × 10.

If JSON parsing complex but hidden inside module = complexity × 1.

**Cost:** Building deep module takes more upfront time; but saves time later for every caller.

---

## ARGUMENT 15: Design Investment ROI is Positive Within Months
**Principle:** Invest 10-20% Time in Design

Ousterhout's analysis:
- 10% design time investment
- Reduces defects by 20%
- Reduces development time by 20%+
- Pays for itself in 6-18 months
- Long-term productivity >> short-term velocity

**Evidence:** Teams that invest in design consistently finish faster than teams that rush.

---

## Summary: How Arguments Connect

1-3: **Why complexity matters** (costs exponential; tactical creates compounding debt)
4-8: **How to design modules** (deep, hidden, general-purpose)
9-12: **How to write clear systems** (obvious code, comments, consistency)
13-15: **How to think about design** (multiple designs, pull complexity, invest time)

**Core insight:** Complexity is not free. Design investments prevent complexity accumulation. Long-term thinking wins.
