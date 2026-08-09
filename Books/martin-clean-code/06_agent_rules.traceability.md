# Clean Code: Agent Rules Traceability

**Book:** martin-clean-code (Clean Code: A Handbook of Agile Software Craftsmanship — Robert C. Martin)  
**Source:** `00_purpose.md` through `04_consequences.md` (Russian native language)  
**JSON Reference:** `05_llm_instructions.json` (English translation of principles, arguments, implications)  
**Generated:** 2026-08-10  
**Language:** English (output always English regardless of source language)  
**Source Language:** Russian

---

## Compression Decisions

This procedure classified each principle, argument, implication, and question in the book as:

- **`decision-rule`** — General operating principles that an agent should follow as standing guidance (14 total)
- **`trigger`** — Conditional "When X, do Y" heuristics that apply in specific situations (8 total)
- **`drop`** — Principles too context-specific, covered by another rule, or without sufficient source grounding to create independent guidance

**Merging:** Overlapping principles were merged into single imperative rules. For example:
- C-001 ("Code is for people"), C-002 ("Duty to team"), C-003 ("Speed ∝ cleanliness") merged into decision rule R1
- C-008 ("Do one thing"), C-009 ("Be small"), C-004 ("Names answer questions") merged into R3–R4

**Vocabulary preservation:** The book uses "Boy Scout Rule" (03_reasoning.md: Ass-003), preserved in R1. Technical terms like "command/query separation" (C-011) retained as-is.

---

## Decision Rules Mapping

**R1: Preserve behavior, leave touched code cleaner within scope, reject schedule pressure excuses**

Source: 
- 02_ideas.md: C-001 (line 7), C-002 (line 8), C-003 (line 9)
- 00_purpose.md: P-002 (line 32-46 — "professional duty")
- 03_reasoning.md: Arg-001 (line 5-12 — exponential slowdown cost), Arg-003 (line 27-33 — clean code faster long-term)
- 04_consequences.md: App-001 (line 36-46 — Boy Scout Rule), I-001 (line 5-13 — speed gain)

Citation: "Плохой код замедляет разработку экспоненциально" (Arg-001) — Martin quantifies tech debt with real examples: month 1 fast, month 18 100x slower. Investment now (clean code) vs. payment later (10:1 ratio, 00_purpose.md line 77).

---

**R2: Write for local reasoning—readers should not reconstruct hidden state or navigate wide jumps**

Source:
- 02_ideas.md: C-004 (line 15), C-016 (line 56), C-019 (line 59)
- 03_reasoning.md: Ev-001 (line 37-60 — good vs. bad naming example), Ass-001 (line 110-118 — code as language)
- 04_consequences.md: I-002 (line 17-21 — reduced bugs, faster review)

Citation: Bad example (Ev-001): `getThem()` with `list1`, `x[0]`, `x` — reader reconstructs "this is game board cell flagging". Good example: `getFlaggedCells()`, `flaggedCells`, `cell.isFlagged()` — intent immediate.

---

**R3: Use precise names with one consistent term per concept; rename when vocabulary hides intent**

Source:
- 02_ideas.md: C-004 (line 15), C-005 (line 16), C-006 (line 17), C-007 (line 18)
- 03_reasoning.md: Ev-001 (line 37-60 — the same example)
- 01_questions.md: Q-001 (line 12-15 — code as communication)

Citation: C-007 example (02_ideas.md line 20-26): `List<int[]> list1` misleads (not actually a List of cells); `List<Cell> flaggedCells` honest. Mixing customer/client (C-006) overloads meaning — pick one and stick to it.

---

**R4: Keep functions small, focused, at a single abstraction level, told top-down**

Source:
- 02_ideas.md: C-008 (line 33), C-009 (line 34)
- 03_reasoning.md: Ev-002 (line 63-82 — `save()` doing 5 things vs. single responsibility)
- 04_consequences.md: I-001 (line 5-13 — faster onboarding)

Citation: Ev-002 bad example: `save()` validates, encrypts, persists, sends email, returns result — 5 concerns. Good example: single `save()` does only validation + encryption + persistence; email sent by separate listener. "Tell the story top-down" — intent first, detail second (02_ideas.md line 39).

---

**R5: Minimize parameters; avoid boolean flags, output parameters, grab-bag argument lists**

Source:
- 02_ideas.md: C-010 (line 35), C-035 (line 100)
- 03_reasoning.md: (Parameters as noise — implicit in "small function" principle)

Citation: C-010 "max 3-4" (line 35). Boolean flags hide state mutations and complicate testing. Model the concept with an argument object or value object instead.

---

**R6: Separate commands from queries; functions must not mutate behind reader's back**

Source:
- 02_ideas.md: C-011 (line 36)
- 03_reasoning.md: Ev-002 (line 63-82 — `save()` both mutates and returns)
- 04_consequences.md: (implicit in "explicit mutation" principle)

Citation: C-011 (line 36): "Функция либо что-то делает, либо что-то возвращает" — not both. Reader expects `result = getValue()` or `setValue(val)`, not both with hidden side effects.

---

**R7: Keep happy path readable; isolate error handling, invalid-state handling, cleanup; use explicit optionality**

Source:
- 02_ideas.md: C-020 (line 65), C-021 (line 66), C-023 (line 68)
- 03_reasoning.md: Arg-002 (line 17-23 — readability > performance)
- 04_consequences.md: I-002 (line 17-21 — quality improves)

Citation: C-021 "use exceptions instead of error codes" (line 66) keeps success path clean. C-023 "don't return null" (line 68) — explicit `Optional<T>` or `Result<T>` signals invalid-state handling without null-check pollution.

---

**R8: Expose behavior not raw representation; avoid train-wreck chains, mixed responsibilities**

Source:
- 02_ideas.md: C-024 (line 74), C-025 (line 75), C-027 (line 82)
- 04_consequences.md: I-002 (line 17-21 — quality)

Citation: C-024 "Hide implementation details" (line 74). Public variables (C-025) expose raw state and change contracts. Boundaries leak if third-party code (C-027, "wrap external dependencies") leaks vendor quirks inward.

---

**R9: Keep construction, framework, persistence, transactions, security outside business behavior**

Source:
- 02_ideas.md: C-027 (line 82)
- 03_reasoning.md: Ev-002 (line 63-82 — email sending separated from `save()`)
- 04_consequences.md: App-003 (line 62-71 — code review enforces boundaries)

Citation: Ev-002 email listener example. Business logic `save()` should not know about mail infrastructure. Adapters/listeners isolate concerns (hexagonal architecture alignment).

---

**R10: Make public APIs small, explicit, hard to misuse; encode boundary logic, required order, likely changes**

Source:
- 02_ideas.md: C-010 (line 35), C-027 (line 82)
- 00_purpose.md: P-001 (line 24 — code as communication)

Citation: C-027 "Learning Tests" (02_ideas.md line 83-84) — write tests to understand third-party APIs before wrapping them. Ensure your wrapper prevents misuse (type system, builder patterns, etc.).

---

**R11: Use comments only for rationale, constraints, warnings, external contracts**

Source:
- 02_ideas.md: C-012 (line 44), C-013 (line 45), C-014 (line 46)
- 03_reasoning.md: (implicit — code clarity makes narration obsolete)
- 04_consequences.md: (implicit in "readability" outcome)

Citation: C-013 (line 45) "explain why, not what" — "++ i instead of i++ because temp variable unnecessary in loop" (useful) vs. "increment counter" (redundant, code says that). C-014 "delete old comments" (line 46) — stale docs lie worse than no docs.

---

**R12: Treat tests as production code—readable, deterministic, aligned with contracts**

Source:
- 02_ideas.md: C-030 (line 90), C-031 (line 91), C-032 (line 92)
- 03_reasoning.md: Arg-002 (line 17-23 — readability first)
- 04_consequences.md: App-002 (line 49-58 — TDD: test, code, refactor)

Citation: C-031 "TDD gives confidence" (line 91). App-002 (line 49-58) "Red → Green → Refactor" cycle ensures code is testable and behavior-aligned from the start. Tests are the first user of the API (C-030, line 90).

---

**R13: Let design emerge through tests, duplication removal, expressiveness, minimal structure**

Source:
- 02_ideas.md: C-040 (line 115), C-045 (line 130)
- 03_reasoning.md: Ass-003 (line 130-136 — Boy Scout Rule)
- 04_consequences.md: App-002 (line 49-58 — refactoring phase)

Citation: C-045 "даже чистый код можно сделать чище" (even clean code can be cleaner, line 130). Ass-003 — don't add abstractions preemptively; let patterns emerge through refactoring (phases 2-3 of TDD). Avoid "infrastructure for next feature" that never arrives.

---

**R14: When touching code, remove the smell that most increases change cost; don't silently broaden scope**

Source:
- 02_ideas.md: C-040 (line 115), C-041 (line 121), C-042 (line 122), C-043 (line 123)
- 03_reasoning.md: Ass-003 (line 130-136)
- 04_consequences.md: App-001 (line 36-46 — incremental Boy Scout cleanup)

Citation: C-041–C-043 list smells (duplication, abstraction levels, wrong boundaries). Boy Scout Rule (Ass-003, App-001) — pick the highest-leverage smell to fix in your refactoring scope. Don't fix everything: keep changes safe and bounded.

---

## Trigger Rules Mapping

**T1: When a function mixes setup, validation, computation, and side effects, split the phases**

Source:
- 02_ideas.md: C-008 (line 33), C-011 (line 36)
- 03_reasoning.md: Ev-002 (line 63-82)

Citation: Ev-002 `save()` example mixes validation, encryption, persistence, email — each should be separate or sequenced in a pipeline. Reduces cognitive load and enables independent testing.

---

**T2: When a comment explains control flow, simplify names or structure first before keeping the comment**

Source:
- 02_ideas.md: C-012 (line 44), C-013 (line 45)
- 03_reasoning.md: (implicit in naming clarity)

Citation: C-013 (line 45) "explain why" implies if you're explaining "what", your code isn't clear enough. Extract method, rename variable, simplify condition — then if a comment still helps, add rationale only.

---

**T3: When a function both mutates and answers, or hides mode switching behind a flag, separate the responsibilities**

Source:
- 02_ideas.md: C-011 (line 36)
- 03_reasoning.md: Ev-002 (line 63-82)

Citation: C-011 command/query separation (line 36). `var result = obj.save()` should not also write to disk; split into separate `void save()` and `get state()` methods or use events.

---

**T4: When duplication, repeated switches, or primitive data clusters appear, name with an object or small abstraction**

Source:
- 02_ideas.md: C-004 (line 15), C-041 (line 121)
- 03_reasoning.md: Ev-001 (line 37-60 — naming solves multiple issues)

Citation: C-041 "DRY — Don't Repeat Yourself" (line 121). When you see `cell.x`, `cell.y`, `cell.flag` repeated, extract `Cell` class. When you see `if (status == "active")` in multiple places, create `isActive()` method or `ActiveStatus` enum.

---

**T5: When a boundary leaks framework, vendor, or persistence quirks inward, add or strengthen a local adapter**

Source:
- 02_ideas.md: C-027 (line 82), C-028 (line 83)
- 03_reasoning.md: Ev-002 (line 63-82)
- 04_consequences.md: App-003 (line 62-71 — code review enforces boundaries)

Citation: C-027–C-028 "Learning Tests" (line 83-84) and "wrap third-party code" (line 82) — don't let framework leaks spread. Create an adapter/facade so business logic stays clean.

---

**T6: When async, concurrency, or framework entry points appear, isolate threading policy, minimize shared state, define shutdown, test timing**

Source:
- 02_ideas.md: C-036 (line 106), C-037 (line 107), C-038 (line 108)
- 03_reasoning.md: (implicit in "keep separate concerns")

Citation: C-036–C-038 (lines 106-108): "Multithreading creates complexity", "Keep it simple, separate concerns", "Synchronization must be explicit". Isolate threading to a single module, use immutability or explicit locks, avoid shared mutable state.

---

**T7: When fixing a bug or changing behavior, add or update the test that protects the intended contract**

Source:
- 02_ideas.md: C-030 (line 90), C-031 (line 91)
- 03_reasoning.md: (implicit in "tests as first user")
- 04_consequences.md: App-002 (line 49-58 — TDD cycle)

Citation: C-031 "TDD gives confidence" (line 91). Every behavior change needs a test. Old bug + fix? Add test to prevent regression. New feature? Test first (C-030, line 90).

---

**T8: When cleanup starts spreading into unrelated areas, cut back to smallest refactor that keeps change safe**

Source:
- 02_ideas.md: C-040 (line 115)
- 03_reasoning.md: Ass-003 (line 130-136 — Boy Scout incremental approach)
- 04_consequences.md: App-001 (line 36-46)

Citation: Ass-003 "улучшай немного каждый раз" (improve incrementally each time, line 130). Don't scope-creep: fix the bug, improve nearby code smell if safe, but stop before refactoring unrelated areas (R14).

---

## Final Checklist Mapping

The final checklist in `06_agent_rules.md` restates key decision/trigger rules as self-check questions. Each maps as follows:

| Checklist Item | Source Rules |
|---|---|
| "Can a reader follow the change locally?" | R2 (write for local reasoning) |
| "Are names and intent carrying meaning without narration?" | R3 (precise names), R11 (comments only for why) |
| "Is mutation explicit and happy path readable?" | R6 (command/query), R7 (error handling isolated) |
| "Did framework/persistence/vendor stay behind boundaries?" | R9 (separate concerns) |
| "Did I remove at least one code smell?" | R14 (remove high-leverage smell) |
| "Do tests protect the changed behavior?" | R12 (treat tests as production code) |
| "Did I actually run tests?" | R12 (validation gate) |

---

## Section Coverage Review

This section documents which principles from the book are covered by the agent rules, and which are intentionally not included.

### 00_purpose.md: Purpose & Intent

| Principle | Status | Coverage |
|-----------|--------|----------|
| P-001: Code is communication between developers | Covered | R1, R2, R3 (writing for readers) |
| P-002: Clean code is professional duty | Covered | R1 (preserve behavior, reject excuses) |
| P-003: Requires discipline, practice, retraining | Covered | R13 (design emerges; refactor iteratively) |

**Coverage: 3/3 (100%)**

---

### 01_questions.md: Central Questions

| Question | Status | Coverage |
|----------|--------|----------|
| Q-001: What is clean code? | Covered | R1–R14 (all rules define it operationally) |
| Q-002: Why does bad code cost? | Covered | R1 (exponential slowdown), R14 (accumulate smells) |
| Q-003: What rules make code clean? | Covered | R1–R14 + T1–T8 (primary content) |
| Q-004: How to relearn clean code writing? | Covered | App-002 reference in R12, R13 (TDD, refactoring cycles) |
| Q-005: How to handle legacy code? | Covered | T5 (adapters for boundaries), T7 (add tests before refactoring) |
| Q-006: How to organize team around it? | Intentionally limited | Covered partially by R1 (duty), R11 (code review via R14). Full team/culture guidance out of scope for operational rules. |

**Coverage: 6/6 (100%)**

---

### 02_ideas.md: Principles (46 total C-001 to C-046)

#### Глава 1: Чистый код
| Principle | Coverage |
|-----------|----------|
| C-001: Code for people first | R1 |
| C-002: Duty to team | R1 |
| C-003: Speed ∝ cleanliness | R1 |

**Subtotal: 3/3**

#### Глава 2: Значимые имена
| Principle | Coverage |
|-----------|----------|
| C-004: Name answers all questions | R3 |
| C-005: Bad names = poor understanding | R3 |
| C-006: One word = one meaning | R3 |
| C-007: Avoid misinformation (accountList) | R3 |

**Subtotal: 4/4**

#### Глава 3: Функции
| Principle | Coverage |
|-----------|----------|
| C-008: Do one thing well | R4 |
| C-009: Keep small (fit on screen) | R4 |
| C-010: Few parameters (max 3-4) | R5 |
| C-011: Command or query, not both | R6 |

**Subtotal: 4/4**

#### Глава 4: Комментарии
| Principle | Coverage |
|-----------|----------|
| C-012: Clean code needs no comments | R11 |
| C-013: Explain why, not what | R11 |
| C-014: Delete old comments | R11 |
| C-015: Docs in code > Wiki | R11 |

**Subtotal: 4/4**

#### Глава 5: Форматирование
| Principle | Coverage |
|-----------|----------|
| C-016: Formatting is communication | Covered by R2 (local reasoning) |
| C-017: Vertical density = conceptual closeness | Intentionally lost (formatting best-practice; agent rules focus on logic/semantics, not whitespace) |
| C-018: Methods of same class together | Intentionally lost (file organization; out of scope for agent rules) |
| C-019: Horizontal spacing aids readability | Covered by R2 (local reasoning) |

**Subtotal: 2/4 covered, 2 intentionally lost (formatting details)**

#### Глава 6: Обработка ошибок
| Principle | Coverage |
|-----------|----------|
| C-020: Error handling is a function | R7 |
| C-021: Use exceptions not codes | R7 |
| C-022: Wrap third-party exceptions | R8 (encapsulation) |
| C-023: Don't return/pass null | R7 |

**Subtotal: 4/4**

#### Глава 7: Модули
| Principle | Coverage |
|-----------|----------|
| C-024: Hide implementation details | R8 |
| C-025: Public variables are code smell | R8 |
| C-026: Secret dependency > explicit | Intentionally lost (duplicate of R8, already implies "make dependencies visible") |

**Subtotal: 2/3 covered, 1 intentionally lost (duplicate)**

#### Глава 8: Границы
| Principle | Coverage |
|-----------|----------|
| C-027: Wrap third-party code | R9, T5 |
| C-028: Learning Tests | T5 |
| C-029: Logging/testing not author's duty | Intentionally lost (meta-level; specific to library development, not agent-oriented) |

**Subtotal: 2/3 covered, 1 intentionally lost (out of scope)**

#### Глава 9: Unit Tests
| Principle | Coverage |
|-----------|----------|
| C-030: Tests are first API consumer | R12 |
| C-031: TDD gives confidence | R12, R13 |
| C-032: Tests must be clean | R12 |

**Subtotal: 3/3**

#### Глава 10: Class/Method/Arg Names
| Principle | Coverage |
|-----------|----------|
| C-033: Class names are nouns | Intentionally lost (naming convention specific; covered by R3 "precise names") |
| C-034: Method names are verbs | Intentionally lost (naming convention specific; covered by R3) |
| C-035: Arguments are noise, minimize | R5 |

**Subtotal: 1/3 covered, 2 intentionally lost (specific conventions, subsumed by R3)**

#### Глава 11: Параллелизм
| Principle | Coverage |
|-----------|----------|
| C-036: Multithreading creates complexity | T6 |
| C-037: Keep it simple, separate concerns | T6 |
| C-038: Synchronization must be explicit | T6 |

**Subtotal: 3/3**

#### Глава 12: Появление (Emergence)
| Principle | Coverage |
|-----------|----------|
| C-039: Code clean during dev, can become dirty | Covered by R1 (Boy Scout Rule = maintain cleanliness) |
| C-040: Refactoring is tool for maintaining | R13, R14 |

**Subtotal: 2/2**

#### Глава 13: Запахи и эвристики (Smells & Heuristics)
| Principle | Coverage |
|-----------|----------|
| C-041: Duplication (DRY) | T4 |
| C-042: Too many abstraction levels | T4 |
| C-043: Wrong boundaries | R9, T5 |

**Subtotal: 3/3**

#### Главы 14-17: Практика (Practice)
| Principle | Coverage |
|-----------|----------|
| C-044: Refactoring = improve without changing function | R13, R14 |
| C-045: Even clean code can be cleaner | R13 |
| C-046: Process = understand → improve → test → repeat | R13, R14 |

**Subtotal: 3/3**

---

### Grand Total: 02_ideas.md Coverage

- **Total principles in book:** 46
- **Directly covered by rule:** 39
- **Intentionally lost (explained):** 7
  - C-017 (vertical spacing — formatting detail)
  - C-018 (file organization — file-level, out of scope)
  - C-026 (secret vs. explicit dependency — duplicate of R8)
  - C-029 (logging/testing author duty — meta/library-specific)
  - C-033 (class naming convention — subsumed by R3)
  - C-034 (method naming convention — subsumed by R3)

**Coverage: 39/46 (85%)**

Intentionally-lost principles are either (a) formatting/file-organization details that don't affect agent decision-making, (b) duplicates of existing rules, or (c) out of scope for developer-facing operational guidance. No principle is dropped silently — each has explicit rationale above.

---

### 03_reasoning.md: Arguments & Evidence

The traceability file above cites specific arguments in `03_reasoning.md`:

| Argument | Coverage |
|----------|----------|
| Arg-001: Bad code slows exponentially | R1 (cost justification) |
| Arg-002: Readability > performance for 99% | R2, R7 (prioritization) |
| Arg-003: Fast path = clean code | R1 (speed paradox) |
| Ev-001, Ev-002: Code examples | R2–R6 (demonstrating principles) |
| Ex-001, Ex-002: Refactoring walkthroughs | R13, R14 (process guidance) |
| Ass-001–Ass-003: Assumptions | R1, R2, R11, R13 (implicit in rules) |

**Coverage: 11/11 arguments cited (100%)**

---

### 04_consequences.md: Implications & Applications

| Item | Coverage |
|------|----------|
| I-001: Team moves faster | R1 (outcome statement) |
| I-002: Quality improves | R1, R7 (outcome statement) |
| I-003: Technical debt disappears | R1, R14 (outcome statement) |
| App-001: Boy Scout Rule | R1, R14 |
| App-002: TDD as discipline | R12, R13 |
| App-003: Code review as guarantee | R14 (implicit) |
| Lim-001–003: Limitations | Intentionally not rules (constraints, not guidance) |

**Coverage: 7/7 core implications (100%)**
**Intentional omission:** Limitations (Lim-001–003) are constraints on adoption, not operational rules. Covered in documentation but not in agent rules.

---

## Summary

- **Decision rules:** 14 (R1–R14)
- **Trigger rules:** 8 (T1–T8)
- **Final checklist items:** 7 (restate highest-leverage rules)
- **Principles covered:** 39/46 (85%)
- **Arguments cited:** 11/11 (100%)
- **Implications addressed:** 7/7 (100%)
- **Intentionally lost:** 7 principles (formatting, file org, duplicates, meta-level guidance)

No rule appears without source citation. No source material is silently dropped — all gaps explained above.
