# Ontology: The 5-Layer Book Model

## Overview

A book is understood as a system with five interconnected layers:

```
PURPOSE (Why does this book exist?)
  ↓
QUESTIONS (What does the author ask?)
  ↓
IDEAS (What concepts, claims, principles does the author introduce?)
  ↓
REASONING (How does the author defend these ideas?)
  ↓
CONSEQUENCES (What follows? What can we do with this?)
```

Each layer contains specific types of nodes. Relationships (edges) connect nodes across layers, showing how ideas depend on each other and support the book's overall structure.

---

## Key Invariants (All Models Must Satisfy)

These five invariants are non-negotiable constraints on all models:

- **No node without source.** Every claim has provenance (chapter/section/location).
- **Status is always declared.** No ambiguity between explicit and inferred; every node is tagged.
- **Relationships are explicit.** Connections are named with typed edges, not left implicit.
- **Qualifications are preserved.** Scope, exceptions, conditions are part of the node, not discarded for brevity.
- **Examples are not ideas.** If something is purely illustrative, it's an Example node with an ILLUSTRATES relation, not a Concept or Claim.

---

## Five Layers and Their Node Types

### Layer 1: PURPOSE

**What:** The book's raison d'être — the problem it solves, the question that prompted it, the author's intent.

**Node types:**
- **Problem** — A specific difficulty, gap, or unsolved challenge the book addresses.
- **Intent** — What the author aims to accomplish. May differ from the problem (e.g., intent could be "convince readers to think differently" while the problem is "widespread misunderstanding").

### Layer 2: QUESTIONS

**What:** The central and subsidiary questions that organize the book's inquiry.

**Node types:**
- **Question** — An open inquiry the author poses. Questions range from the book's central framing question down to sub-questions that guide reasoning.

### Layer 3: IDEAS

**What:** The intellectual content — concepts, claims, principles that the author introduces to engage the questions.

**Node types:**
- **Concept** — A term, definition, or idea (e.g., "deep reading", "intellectual humility"). Concepts are building blocks; they're used in claims and arguments.
- **Claim** — A propositional assertion. The author asserts it as true (e.g., "All reading should begin with purpose").
- **Principle** — A general rule or law the author establishes (e.g., "Compression must never strengthen a claim").

### Layer 4: REASONING

**What:** The apparatus by which the author supports ideas — how ideas are defended, illustrated, and grounded.

**Node types:**
- **Argument** — A logical structure linking premises to a conclusion. An argument supports a claim.
- **Evidence** — A fact, study, observation, or quotation that grounds a claim (explicit textual support).
- **Example** — An illustration or concrete instance. Examples clarify ideas but are not themselves ideas.
- **Assumption** — An unstated or implicit premise the author relies on.

### Layer 5: CONSEQUENCES

**What:** What the reader should take away, do, apply, or question.

**Node types:**
- **Implication** — A logical result or extension of ideas. "If A, then B."
- **Application** — A practical use case or method derived from the ideas.
- **Limitation** — A scope boundary, exception, or condition where the ideas may not apply.

---

## Node Template

**CANONICAL: This template is the authoritative specification for all nodes across all documents.**

Every node in the book model uses this structure:

```yaml
id: [unique identifier]
type: [one of the 13 types above]
title: [short label]
statement: [the core claim or definition, 1-2 sentences]
status: [explicit | inferred | interpretation | evaluation]
importance: [core | important | supporting | detail]
confidence: [high | medium | low]
source: 
  chapter: [or section, or "intro", "conclusion"]
  location: [page range or passage excerpt]
relations: 
  - type: [see Relations list below]
    target: [id of related node]
    note: [optional clarification]
```

### Status Definitions

**CANONICAL: These definitions are the authoritative source for epistemic tagging. Other documents reference this section.**

- **explicit** — The author states this directly in the text.
- **inferred** — Clearly implied but not stated verbatim; a straightforward inference from what is said.
- **interpretation** — An interpretation of ambiguous or metaphorical passages; a reading that requires subjective judgment.
- **evaluation** — Your (the reader/skill's) judgment or assessment; not something the author claimed.

### Importance Definitions

- **core** — Central to the book's main thesis. Removing it would break the argument.
- **important** — Significant; supports the core ideas. Needed for deep understanding.
- **supporting** — Reinforces important ideas; often an example, detail, or sub-argument.
- **detail** — Illustrative or ancillary; included for completeness but not essential to the core structure.

### Confidence Definitions

- **high** — Clear, unambiguous, well-supported in the text.
- **medium** — Reasonable interpretation but not explicit; some ambiguity.
- **low** — Inferred or interpretive; depends on reading assumptions.

---

## Relations (Edges)

**CANONICAL: This is the authoritative specification of all relation types. Other documents reference this section.**

Relationships show how nodes connect and depend on each other:

| Relation | Meaning |
|----------|---------|
| **ANSWERS** | Idea/Claim answers a Question |
| **SUPPORTS** | Evidence/Argument supports a Claim or Idea |
| **DEPENDS_ON** | Claim depends on another Idea or Concept |
| **EXPLAINS** | Concept explains or defines another Concept; Argument explains a Claim |
| **ILLUSTRATES** | Example illustrates a Concept or Claim |
| **QUALIFIES** | Limitation qualifies a Claim (boundaries, exceptions, scope) |
| **CONTRADICTS** | One Claim contradicts another (used to flag tensions in the text) |
| **LEADS_TO** | Implication logically leads to a Consequence or Application |
| **PART_OF** | Idea/Concept is a component of a larger Idea or framework |

---

## Node Admission Rule

**CANONICAL: This is the authoritative admission rule. Other documents reference this section.**

**A node earns a place in the model if it:**
1. Is necessary for understanding the book's central ideas
2. Is a dependency of other important nodes
3. Represents a significant original contribution by the author
4. Is required for application or use of the ideas
5. Is critical enough that losing it would distort the author's position

**A node can be dropped if it:**
- Is purely illustrative (use ILLUSTRATES relation instead)
- Is a passing mention not connected to the core argument
- Is a sub-point of a supporting idea (fold into the parent)
- Is redundant with another node

**Principle:** The model should be *full enough to reconstruct* the book's thought, but *small enough to understand* at a glance.

---

## Example Node

```yaml
id: REC-001
type: Principle
title: Reconstruction Before Compression
statement: Reading should reconstruct the author's thought before compressing or summarizing. Compression that happens too early loses nuance and may strengthen claims beyond the author's intent.
status: explicit
importance: core
confidence: high
source:
  chapter: 1
  location: "Introduction, opening paragraphs"
relations:
  - type: ANSWERS
    target: Q-001
    note: Answers the question of how to approach deep reading
  - type: SUPPORTS
    target: C-002
    note: Supports the claim that summary-based reading is insufficient
```

---

## Output File Structure

The skill renders each book as 5 markdown files in `Books/<slug>/`:

1. **00_purpose.md** — Problem, Intent nodes
2. **01_questions.md** — Question nodes
3. **02_ideas.md** — Concept, Claim, Principle nodes
4. **03_reasoning.md** — Argument, Evidence, Example, Assumption nodes
5. **04_consequences.md** — Implication, Application, Limitation nodes

Each file groups its nodes hierarchically (by layer and sub-topic), preserves the node template fields as readable metadata, and includes a "Relations" section linking to other files where relevant.

