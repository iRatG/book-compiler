# Design Decisions: book-compiler v0

---

## Decision 1: Long-Book Handling — v0 Requires Excerpt/Chapter Only

**Status:** Decided (Confirmed)

**Context:** The design-log.md mentions "stateful reading" and context persistence for books longer than ~300 pages as a v1+ enhancement. The Gogol test case is a full novel (~500 pages), but the v0 validation plan focuses on the first chapter (~30 pages). The question: should v0 handle full books, or require users to provide a bounded excerpt?

**Decision:**

v0 skill operates on **bounded inputs only**: either a complete book under ~200 pages, a single chapter, an article, or an excerpt with clearly marked boundaries (e.g., "Chapter 3–5"). Full-book stateful reading—maintaining context and continuation state across multiple invocations—is deferred to v1+. This constraint keeps v0 implementation tractable, preserves model fidelity (no need for lossy state compression), and allows clean testing on the Gogol first chapter without requiring full-book session management. When users submit books longer than ~200 pages, the skill should detect this and request a chapter or section excerpt. This decision does not limit the *eventual* capability, only the v0 scope: v1 can layer stateful multi-pass reading over v0's single-pass engine, calling v0 repeatedly with chapter-sized windows and merging results.

**Rationale:**
- Aligns with philosophy of "small but deep" (Principle 10 from design-log).
- Reduces implementation complexity: no session state, no continuation protocol, no memory-aware compression.
- Supports clean testing: Gogol first chapter is ~30 pages, easily handled.
- Future-proof: v1 can call v0 in a loop, aggregating results.

**Implications:**
- Input contract must specify max length or request chapter/excerpt submission.
- Error messages for over-length input should be clear and offer guidance.
- Documentation should explain how to prepare long books (split by chapter).

---

## Decision 2: Fiction Handling — Adapt 5-Layer Model, No Ontology Extension in v0

**Status:** Decided (Confirmed)

**Context:** Gogol's *Dead Souls* is fiction (satirical novel), not non-fiction. The Five-Layer Model was designed for argument and exposition. Can it work for narrative? Specifically:
- PURPOSE layer: non-fiction "Problem/Intent" maps to fiction as the central conflict or narrative scenario and thematic intent.
- QUESTIONS layer: for fiction, questions shift from "What is X?" (concept) to "What becomes of X?" or "How does character evolve?"
- IDEAS layer: in fiction, "ideas" include not just abstract concepts but thematic claims, character insights, and symbolic meanings.
- REASONING/CONSEQUENCES: logic structures differently in narrative (causality of events vs. causality of argument).

The design-log notes that Foster's symbolic/literary layer (metaphor, archetype, symbol) is deferred to v1+. The question: does v0 need fiction-specific node types, or does it stretch the existing ontology?

**Decision:**

v0 **applies the existing Five-Layer Model to fiction without extending the node types**. Adaptation is semantic, not ontological:
- PURPOSE: "Problem" becomes the central conflict or dilemma; "Intent" is the author's thematic or narrative goal (what human condition the work explores).
- QUESTIONS: Remain valid; for fiction they express inquiry about character, outcome, or meaning (e.g., "What is the nature of human servility?" for *Dead Souls*).
- IDEAS: Includes both explicit thematic claims (e.g., "Corruption is systemic") and character/symbolic insights. Distinguish from examples: a character arc is not an example; it is a narrative instantiation of a thematic idea.
- REASONING: Narrative causality (event A leads to event B) as well as thematic reasoning (this character moment illustrates this principle).
- CONSEQUENCES: Thematic implications and reader takeaways.

Fiction-specific extensions (Foster's symbolic layer, character arcs as first-class node types, motif and metaphor analysis) remain future work. The current model is "sufficient" for deep reading of fiction, though less precise than a dedicated literary ontology would be.

**Rationale:**
- The Five-Layer Model is abstract enough to accommodate narrative structure.
- Minimizes v0 scope: no new node types, no new relations.
- Test case (Gogol) can proceed without delay.
- v1 can introduce literary-specific nodes (Symbol, Motif, Archetype, CharacterArc) as extensions.

**Implications:**
- Documentation (process.md) should include fiction examples and clarify how PURPOSE/QUESTIONS/REASONING map to narrative.
- Node status tags become important: thematic claims in fiction are often implicit; mark them as "inferred" or "interpretation" accordingly.
- SKILL.md scope section should be updated to say "narrative fiction" is in-scope for v0, but "deep literary analysis" (e.g., close reading of metaphor and symbol) is deferred.

---

## Decision 3: Pass 2 Completion Criteria — Fixed-Point Convergence Rule

**Status:** Decided (Confirmed)

**Context:** The current ontology.md specifies a Node Admission Rule (5 criteria for creating a node, 4 for dropping). However, it does not specify when Pass 2 (Reconstruct) is *complete*. The question: how does Claude know when extraction is "done"? Without clear stopping criteria, Pass 2 could theoretically loop forever, or terminate prematurely, or produce inconsistent results across runs.

**Decision:**

Pass 2 extraction is complete when **all four conditions are met**:

1. **Node Saturation:** Every node currently in the model passes the Node Admission Rule; no node exists that should be dropped, and no obvious uncovered node passes the rule and was missed.
2. **Relation Saturation:** All important relations between existing nodes have been identified and typed. No two nodes with a logical or textual connection remain unrelated.
3. **Fixed-Point Convergence:** A complete re-read of the source text (or a sampling scan) discovers no new nodes that meet the admission rule. This is the key: run one more verification pass; if no new nodes emerge, you have reached a fixed point.
4. **Status Honesty:** Every node's status tag (explicit/inferred/interpretation/evaluation) is accurate and defensible given the node's source. No implicit assumptions are hidden.

**Verification Checklist (for human review):**
- [ ] Node Admission Rule is applied consistently: 5 admission criteria checked for each node
- [ ] No node is missing that explains a key claim
- [ ] Relations are named and not implicit
- [ ] Status tags are honest: can I justify why C-047 is "inferred" and not "interpretation"?
- [ ] A re-scan of key chapters uncovers no new core nodes
- [ ] Qualifications and scope are preserved (not flattened)

**Rationale:**
- Provides a checkable, deterministic stopping rule that avoids infinite loops and premature termination.
- Fixed-point convergence is a standard technique in graph construction; it's well-understood and testable.
- Allows the skill to report completion with confidence: "All nodes and relations have been identified."

**Implications:**
- Process.md should document the convergence check explicitly.
- The skill's internal logic for Pass 2 should include a "convergence verification" step (re-scan or sampling).
- Output should include a brief statement: "Pass 2 complete: 47 nodes, 63 relations, fixed-point reached after 2 convergence checks."

---

## Decision 4: Cross-File Linking — Plain Markdown Links (Option A)

**Status:** Decided (Confirmed)

**Context:** When a node in `02_ideas.md` references a node in `03_reasoning.md`, how is the link expressed? Three options:
- **A:** Plain markdown `[E-015](reference/03_reasoning.md#E-015)` — portable, works everywhere.
- **B:** Obsidian wikilinks `[[E-015]]` — better discoverability in Obsidian, not portable.
- **C:** No explicit cross-file links; rely on relation metadata and implicit discovery.

**Decision:**

Use **plain markdown links (Option A)**. All cross-file node references use the format:

```markdown
[NODE-ID](path/to/file.md#NODE-ID)
```

Examples:
- Intra-file relation: `[E-015](#E-015)`
- Cross-file relation: `[A-003](03_reasoning.md#A-003)`
- External reference (future): `[Gogol-Ch1](../../books/dead-souls/01_questions.md#Q-047)`

**Rationale:**
- **Portability:** Works in any markdown editor, GitHub, GitLab, VS Code, Obsidian, static site generators.
- **Human-readable:** The URL is visible and understandable; no magic linking required.
- **Simplicity:** No dependency on Obsidian or any specific platform.
- **Future-proof:** If the project later needs Obsidian support, a converter can automatically rewrite markdown links to wikilinks; the reverse is not true.

**Implications:**
- Obsidian users can still use the vault and navigate the files; wikilink autocompletion won't work, but markdown links are clickable in Obsidian.
- v1+ can introduce Obsidian-specific features (custom metadata, canvas files, embeds) without breaking v0 portability.
- Documentation should note: "Files are plain markdown for maximum portability. Obsidian users: treat the Books/ directory as a regular vault; all links are clickable."

---

## Decision 5: Authorial Contradictions — Flag When Both Claims Pass Admission Rule

**Status:** Decided (Confirmed)

**Context:** The ontology.md defines a CONTRADICTS relation but provides no rule for when to use it. Scenarios:
- Author says X on page 10, says ¬X on page 150. Obvious contradiction → flag it.
- Author explores view A, then qualifies it later ("but only in cases where..."). Not a contradiction → don't flag.
- Author expresses two competing values or intuitions without fully resolving them. Ambiguous intent → sometimes flag?

The question: what is the rule? Without it, contradictions are reported inconsistently or not at all, losing important signals for critical reading.

**Decision:**

Create a CONTRADICTS relation (and dual nodes) **if and only if all three conditions are met**:

1. **Both claims are explicit or inferred (not interpretation):** The author explicitly states or strongly implies both propositions. If one is purely interpretive or evaluative, it's not a contradiction worth flagging (it's a reading disagreement).
2. **Both claims pass the Node Admission Rule independently:** Each claim is important enough to exist in the model on its own merits (not a minor detail or passing comment). This filters out trivial contradictions (e.g., "I sometimes prefer tea" vs. "usually I prefer coffee" — neither important enough to be a core node).
3. **The contradiction is important for understanding:** Flagging it aids critical thinking, reveals tension in the author's reasoning, or is necessary to understand the book's structure or argument. If two nodes contradict but neither affects the reader's understanding of the central thesis, skip the flag.

**Implementation:**
- Create both nodes independently using the admission rule.
- If contradiction detected during Pass 2, add a CONTRADICTS edge: `Node-A --CONTRADICTS--> Node-B`.
- In the markdown output, include an explicit note: `Contradiction flagged: X contradicts Y (see [Node-Y](#Node-Y)). Both are author-explicit. Reader should attend to this tension.`
- Document the reason for flagging in the relation's note field.

**Rationale:**
- Supports the principle "Preserve first, compress later" and "Attend to nuance": contradictions are part of the author's texture.
- Prevents false positives (every qualified statement is not a contradiction).
- Makes the model's perspective on contradiction transparent: the reader can see *why* this pair is flagged.
- Supports critical reading: readers can examine flagged contradictions and form their own judgment.

**Implications:**
- Documentation should provide examples: e.g., Gogol's *Dead Souls* satirizes corruption and human nature in ways that can seem contradictory (pity + ridicule). These should be flagged.
- The skill should not "resolve" contradictions on behalf of the author; the model presents both claims and the tension.
- Output should include a "Tensions & Contradictions" section listing all CONTRADICTS relations with explanatory notes.

---

## Glossary Updates

### New Terms & Definitions

**Fixed-Point Convergence (Pass 2)**
In graph construction, a state in which re-reading the source text produces no new nodes that meet the admission rule. Used as the stopping criterion for Pass 2. (See Decision 3.)

**Node Saturation**
The state in which all nodes currently in the model pass the Node Admission Rule and no obvious uncovered node should be added. Part of the Pass 2 completion criteria. (See Decision 3.)

**Relation Saturation**
The state in which all important logical or textual connections between existing nodes have been named as typed edges. Part of the Pass 2 completion criteria. (See Decision 3.)

**Fiction Adaptation**
The application of the Five-Layer Model to narrative fiction by reinterpreting PURPOSE (conflict/theme), QUESTIONS (character/outcome inquiry), and IDEAS (thematic claims and insights) without introducing new node types. (See Decision 2.)

**Bounded Input Constraint**
The v0 requirement that a source text be either a complete short work (<~200 pages) or a clearly bounded excerpt (chapter, section, article). Full-book stateful reading is deferred to v1+. (See Decision 1.)

### Refined Definitions

**Node Admission Rule** (refined in light of Decisions 3 & 5)
A node earns a place in the model if it:
1. Is necessary for understanding the book's central ideas
2. Is a dependency of other important nodes
3. Represents a significant original contribution by the author
4. Is required for application or use of the ideas
5. Is critical enough that losing it would distort the author's position

**Note:** Applied consistently across all node types. Used as the stopping criterion for Pass 2 (fixed-point convergence) and as the filter for CONTRADICTS relations.

**CONTRADICTS Relation** (newly clarified in Decision 5)
A typed edge between two Claim or Principle nodes indicating logical contradiction. Created when:
- Both claims are explicit or inferred (not interpretation/evaluation).
- Both claims pass the Node Admission Rule independently.
- The contradiction is important for understanding the book or supporting critical reading.

Contradictions are preserved and flagged; the model does not resolve them on behalf of the author.

**Epistemic Status (existing, reaffirmed)**
- **explicit** — The author states this directly in the text.
- **inferred** — Clearly implied but not stated verbatim; straightforward inference.
- **interpretation** — An interpretation of ambiguous or metaphorical passages; requires subjective judgment. Not eligible for CONTRADICTS relations.
- **evaluation** — Your (the reader/skill's) judgment or assessment; not something the author claimed. Not eligible for CONTRADICTS relations.

---

## Consistency & Cross-References

These decisions are consistent with and complement the existing philosophy and ontology:

- **Decision 1** (bounded input) is grounded in principle "Simple Surface, Deep Interior" (design-log Principle 10) and supports the Five-Layer Model's tractability.
- **Decision 2** (fiction adaptation) applies the principle "Book as a System" (design-log Principle 3) to a new domain without expanding the ontology.
- **Decision 3** (fixed-point convergence) operationalizes the Node Admission Rule and provides a deterministic stopping rule for Pass 2.
- **Decision 4** (markdown links) honors the principle of portability and simplicity, deferring platform-specific enhancements to v1+.
- **Decision 5** (contradiction flagging) supports principle "Preserve first, compress later" (design-log Principle 2) and enables critical reading.

All decisions preserve the core constraint: **minimum ontology, maximum explanatory power**.

---

## Next Steps

1. Update `SKILL.md` scope section to reflect Decisions 1 & 2 (bounded input, fiction adaptation).
2. Update `process.md` (or create it) to include:
   - Fiction examples (mapping PURPOSE/QUESTIONS/IDEAS to narrative).
   - Pass 2 convergence checklist (Decision 3).
   - Cross-file linking examples (Decision 4).
   - Contradiction flagging examples (Decision 5).
3. Smoke-test on Gogol first chapter: verify that the Five-Layer Model and node types capture fiction content without requiring extensions.
4. Document error messages for over-length input (Decision 1).
