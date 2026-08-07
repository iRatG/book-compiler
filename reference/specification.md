# book-compiler Specification (v0)

**Status:** Final (v0)  
**Version:** 1.0  
**Last Updated:** 2026-08-07  
**Single Source of Truth:** If SKILL.md and this specification disagree, this specification supersedes SKILL.md.

---

## 1. Problem Statement

### The Problem

Most tools designed to help readers engage with books operate through summarization: compressing text, extracting key points, and discarding nuance to achieve brevity. This approach fails for deep reading. Summarization:

- Loses qualifications, scope, and exceptions (compression strengthens claims)
- Treats frequency of mention as importance (structural function matters instead)
- Flattens the author's intellectual architecture into a list of takeaways
- Prevents readers from thinking *with* and *against* the author's actual argument
- Makes critical evaluation impossible (the model is already simplified)

The status quo leaves a reader with:
- A list of bullet points, not a structure
- Confidence without understanding
- No way to verify claims against source
- No reconstruction of how the author's ideas fit together

### Who Uses It and Why

Three primary user personas:

1. **Academic researchers** reading primary and secondary sources need to reconstruct arguments for literature reviews, synthesis, and critical assessment. They need to preserve nuance, trace evidence, and identify unstated assumptions.

2. **Software developers and technical leaders** reading methodology books, design pattern books, and systems thinking texts need to extract actionable principles while understanding their context, tradeoffs, and limitations. Oversimplification leads to cargo-cult implementations.

3. **Curious readers** engaging with complex non-fiction and narrative works want to understand how the author's ideas fit together, challenge them thoughtfully, and retain what matters long-term.

All three personas require:
- Faithful reconstruction (not compression)
- Source traceability (where does each claim originate?)
- Nuance preservation (conditions, exceptions, qualifications)
- Relationship mapping (how ideas depend on and support each other)
- Epistemological honesty (what is explicit vs. inferred vs. interpretation?)

### What Was Wrong

Existing approaches fall into three categories:

1. **Summary generators** (ChatGPT with generic prompt, claude-summarize): Optimize for brevity, lose context, flatten argument structure.

2. **Note-taking templates** (Obsidian, Roam): Shift the cognitive burden to the user; no systematic methodology; inconsistent across books.

3. **Bibliography tools** (Zotero, Mendeley): Track metadata, not meaning; require manual annotation.

None treat reading as a reconstruction process. None operationalize the three-author methodology (Povarnin on purpose, Adler on structure, Foster on layers of meaning). None output a machine-readable, verifiable model of a book's intellectual content.

---

## 2. Solution Overview

### The Core Approach

book-compiler treats reading as **compilation**: transforming linear text into an intermediate representation (a knowledge graph) that faithfully captures the book's intellectual architecture.

```
BOOK (linear text)
  ↓
PARSING (Pass 1: Survey)
  ↓
SEMANTIC ANALYSIS (Pass 2: Reconstruct)
  ↓
INTERMEDIATE REPRESENTATION (Five-Layer Model)
  ↓
VERIFICATION (Fixed-point convergence, consistency checks)
  ↓
CODE GENERATION (Pass 3: Write)
  ↓
HUMAN UNDERSTANDING (Five markdown files)
```

### The Five-Layer Model

The book is modeled as a **directed graph with five semantic layers**:

| Layer | Nodes | Meaning | Driving Question |
|-------|-------|---------|------------------|
| **PURPOSE** | Problem, Intent | Why does this book exist? | What gap does the author address? |
| **QUESTIONS** | Question | What does the author ask? | What inquiry organizes this text? |
| **IDEAS** | Concept, Claim, Principle | What intellectual content is introduced? | What ideas does the author propose? |
| **REASONING** | Argument, Evidence, Example, Assumption | How are ideas supported? | Why should we accept these ideas? |
| **CONSEQUENCES** | Implication, Application, Limitation | What follows? | What can we do with this? |

Each layer contains specific types of nodes. Nodes are connected by **typed edges** (relations) that express dependency, support, explanation, contradiction, and other semantic relationships.

### How the Model Addresses the Problem

**Faithfulness**: The model reconstructs the author's structure without compression. Nothing is lost to brevity; scope qualifications are preserved as nodes.

**Traceability**: Every node knows its source (chapter/section/page). Claims can be verified against the original text.

**Epistemological Clarity**: Every claim is tagged with status (explicit/inferred/interpretation/evaluation). The reader can distinguish what the author said from what the skill inferred or judged.

**Relational Thinking**: The model captures *how ideas fit together*, not just what they are. A reader can navigate dependencies, see what supports what, and understand the logical structure.

**Critiquability**: Because the model is explicit, readers can examine it and agree or disagree with the reconstruction. The model is transparent, not a black box.

**Scalability**: The model is machine-readable (YAML/markdown), versioned (git), and can be traversed, queried, and extended.

---

## 3. User Stories & Use Cases

### User Story 1: Researcher Synthesizing Literature

**As a** graduate student writing a literature review  
**I want to** reconstruct three foundational papers so I can extract their core claims and identify agreements and contradictions  
**So that** I can write an accurate, nuanced synthesis that respects each author's original position and shows how they relate

**Example**: A researcher reading Kuhn, Popper, and Lakatos on scientific methodology. Each offers different frameworks. A summary-based approach loses the structure. The specification allows the researcher to:
- Extract the central question each author addresses (PURPOSE/QUESTIONS layers)
- Map each author's key concepts and claims (IDEAS layer)
- Trace the evidence and arguments each offers (REASONING layer)
- Identify where they contradict (CONTRADICTS relations)
- Use that model to write a genuine synthesis

### User Story 2: Developer Learning Methodology

**As a** backend architect  
**I want to** read a systems design book (e.g., *Designing Data-Intensive Applications*) and extract actionable principles with their context and tradeoffs  
**So that** I can apply the lessons correctly without cargo-cult implementations that ignore boundary conditions

**Example**: A developer reads Chapter 5 on replication. The book presents tradeoffs (consistency vs. latency, complexity vs. correctness). A summary flattens this. The specification allows:
- Extract the problem the chapter solves (PURPOSE: "Replication introduces consistency challenges")
- Identify questions it addresses (QUESTIONS: "How do replicas stay consistent?")
- Map concepts and claims (Eventual consistency, strong consistency, read-your-write, etc.)
- Trace the reasoning for each approach (REASONING: arguments for and against each strategy)
- Preserve limitations (CONSEQUENCES: "Strong consistency has higher latency")
- Use relations to show tradeoffs (Claim A CONTRADICTS Claim B, with full context)

### User Story 3: Critical Reader Understanding Fiction

**As a** reader of Gogol's *Dead Souls*  
**I want to** understand how the author builds a satirical critique of Russian society through character and plot  
**So that** I can appreciate the work's artistic intent and engage in critical discussion about its meaning

**Example**: *Dead Souls* is a satirical novel with a central "problem" (corruption, servility, absence of human dignity in Russian life), central questions ("What is the nature of servility?" "How does society devalue the individual?"), thematic ideas (Gogol's claims about human nature through character), and narrative reasoning (character interactions, irony, satire). The specification:
- Captures PURPOSE (Gogol's thematic and narrative intent)
- Organizes QUESTIONS (thematic and character inquiries)
- Models IDEAS (thematic claims, character insights, symbolic meanings)
- Traces REASONING (narrative causality, irony, satire as argument)
- Records CONSEQUENCES (implications for the reader, what Gogol reveals about society)

All without requiring fiction-specific node types; the Five-Layer Model adapts semantically.

### Underlying Principle

All three users need the same capability: **to reconstruct how a text is built, not to be told what matters**. The specification enables them to build their own understanding by making the author's structure visible, traceable, and verifiable.

---

## 4. Implementation Decisions

This section integrates the five finalized design decisions from `reference/decisions.md` as implementation requirements and constraints.

### 4.1 Five-Layer Model: Detailed Specification

#### Layer 1: PURPOSE

**Semantic role**: The book's foundational reason for existing.

**Node types**:
- **Problem** — A specific gap, challenge, or unsolved difficulty the book addresses. Often implicit; must be inferred from context if not stated explicitly. Example: "Most readers approach all texts with the same strategy, preventing deep understanding of complex works."
- **Intent** — What the author aims to accomplish. May differ from the problem statement. Intent is teleological; it answers "What does the author want to change?" or "What does the author want the reader to understand?" Example: "Teach readers a systematic methodology for deep reading that preserves the author's thought while enabling critical evaluation."

**Constraints**:
- A book must have exactly one Problem node (or none if purely exploratory, but this is rare).
- A book must have exactly one Intent node.
- Problem and Intent are distinct: Problem is what's wrong; Intent is what the author does about it.

#### Layer 2: QUESTIONS

**Semantic role**: The organizing inquiries that structure the book.

**Node types**:
- **Question** — An open inquiry the author poses. Questions range from the book's central framing question down to sub-questions that guide reasoning. Example: "What is the proper method of reading a difficult philosophical text?" or "Why do readers often misunderstand the author's intent?"

**Constraints**:
- At least one Question node must exist (the central question).
- Questions are the spine of the book's structure; they drive all other layers.
- Questions should be distinct from their answers (answers are Claims in the IDEAS layer).

#### Layer 3: IDEAS

**Semantic role**: The intellectual content—concepts, claims, principles introduced by the author.

**Node types**:
- **Concept** — A term, definition, or foundational idea used as a building block. Concepts are *used* in claims and arguments; they are not themselves propositions. Example: "Deep reading," "intellectual structure," "epistemic status."
- **Claim** — A propositional assertion. The author asserts it as true or important. Claims can be controversial or debated. Example: "All reading should begin with establishing purpose," or "Most chapter summaries lose the author's nuance."
- **Principle** — A general rule or law the author establishes as foundational. Principles often apply across contexts and carry prescriptive or normative force. Example: "Compression must never strengthen a claim," or "Reconstruction precedes understanding."

**Constraints**:
- Concepts are *not* claims. If a concept is stated as universally true, tag it as a Principle.
- Claims are propositions that the author asserts or defends.
- Principles are claims with broader applicability or prescriptive intent.
- Do not confuse examples with concepts (examples are in the REASONING layer).

#### Layer 4: REASONING

**Semantic role**: The apparatus by which the author supports, illustrates, and grounds ideas.

**Node types**:
- **Argument** — A logical structure linking premises to a conclusion. An argument is a reasoning structure that defends or justifies a claim. Example: "If readers lack purpose, they cannot evaluate information as important or trivial. Therefore, purpose-setting is necessary for reading comprehension."
- **Evidence** — A fact, study, observation, quotation, or data point that grounds a claim in reality. Evidence is authoritative and traceable. Example: "A 1985 study showed that readers who set purpose first retain material 40% better than those who don't," or "In Chapter 3, the author describes a case of reader misinterpretation."
- **Example** — An illustration or concrete instance of a general idea. Examples clarify and make ideas tangible but are *not themselves ideas*. Example: "When reading a mystery novel, readers must attend linearly to plot. When reading a reference book, readers can skip chapters selectively."
- **Assumption** — An unstated or implicit premise the author relies on. Assumptions are often hidden; unearthing them is part of reconstruction. Example: "The author assumes readers can identify a book's main problem from its introduction," or "The author assumes that structure and meaning are related."

**Constraints**:
- Every Claim node should have at least one supporting Argument or Evidence node (SUPPORTS relation).
- Examples must be separate nodes with ILLUSTRATES relations, never merged into Concept or Claim nodes.
- Quotations are Evidence nodes, not knowledge nodes.
- Assumptions should be tagged as `inferred` (they are not explicit).

#### Layer 5: CONSEQUENCES

**Semantic role**: The results, applications, and boundaries of ideas.

**Node types**:
- **Implication** — A logical result or extension of ideas. "If the author's ideas are true, then X follows." Example: "If readers must reconstruct before compressing, then summary-based tools are insufficient for deep learning."
- **Application** — A practical use case or method derived from ideas. How can the reader *use* the author's ideas? Example: "To apply purpose-driven reading to technical books, first identify what you need to learn, then skim the table of contents to find relevant chapters."
- **Limitation** — A scope boundary, exception, or condition where ideas may not apply. Limitations preserve nuance and prevent false universalization. Example: "Deep reading is necessary for complex philosophical texts but not for light fiction," or "The Five-Layer Model applies to non-fiction and narrative but may require extension for poetry."

**Constraints**:
- Limitations are *not* criticisms. They are scope clarifications.
- Implications should be distinct from applications (implications are theoretical; applications are practical).
- Every important Claim should have at least one Limitation node (QUALIFIES relation).

### 4.2 Node Types Summary

| Node Type | Layer | Definition | Question |
|-----------|-------|------------|----------|
| **Problem** | PURPOSE | A gap or challenge the book addresses | What problem does the author address? |
| **Intent** | PURPOSE | What the author aims to accomplish | What does the author want to change? |
| **Question** | QUESTIONS | An open inquiry organizing the text | What does the author ask? |
| **Concept** | IDEAS | A term, definition, or building-block idea | What concepts are foundational? |
| **Claim** | IDEAS | A propositional assertion by the author | What does the author assert? |
| **Principle** | IDEAS | A general rule or law established by the author | What general rules apply? |
| **Argument** | REASONING | A logical structure linking premises to conclusion | How does the author defend claims? |
| **Evidence** | REASONING | A fact, study, or data point grounding claims | What supports the author's claims? |
| **Example** | REASONING | An illustration of a general idea | What instances clarify the ideas? |
| **Assumption** | REASONING | An unstated premise the author relies on | What does the author take for granted? |
| **Implication** | CONSEQUENCES | A logical result of ideas | What follows from these ideas? |
| **Application** | CONSEQUENCES | A practical use of ideas | How can ideas be applied? |
| **Limitation** | CONSEQUENCES | A scope boundary or exception | Where do ideas not apply? |

**Total**: 13 node types, organized by layer.

### 4.3 Relations (Edges) Specification

A relation is a **directed, typed edge** connecting two nodes, expressing semantic dependency, support, explanation, or contrast.

| Relation | Domain → Codomain | Meaning | Example |
|----------|-------------------|---------|---------|
| **ANSWERS** | Any → Question | A node answers or addresses a Question | Claim "Reading requires purpose" ANSWERS Question "What determines reading strategy?" |
| **SUPPORTS** | Evidence/Argument → Claim/Principle | Support establishes truth or importance | Evidence "Study shows..." SUPPORTS Claim "Purpose improves retention" |
| **DEPENDS_ON** | Claim/Implication → Concept/Principle | Logical dependency; one idea rests on another | Claim "Reconstruction precedes compression" DEPENDS_ON Principle "Preserve before simplify" |
| **EXPLAINS** | Concept/Argument → Concept/Claim | Concept defines or Argument clarifies a Claim | Concept "Deep reading" EXPLAINS Claim "Active engagement improves understanding" |
| **ILLUSTRATES** | Example → Concept/Claim | Example concretely instantiates an idea | Example "Reading mystery linearly" ILLUSTRATES Principle "Purpose determines method" |
| **QUALIFIES** | Limitation → Claim/Principle | Limitation sets scope or exception | Limitation "Deep reading only for complex texts" QUALIFIES Claim "All reading requires reconstruction" |
| **CONTRADICTS** | Claim ⇄ Claim | Logical contradiction; both claims cannot be true (see Decision 5) | Claim A: "Summarization is useful" CONTRADICTS Claim B: "Summarization loses nuance" (both author-explicit, both important, tension matters) |
| **LEADS_TO** | Implication/Consequence → Application/Implication | Logical or causal progression | Implication "Deep reading requires purpose" LEADS_TO Application "Set reading goal before opening book" |
| **PART_OF** | Concept/Idea → Concept/Framework | Composition; one idea is a component of a larger structure | Concept "Status tag" PART_OF Concept "Node metadata" |

**Total**: 9 relation types.

**Constraint on CONTRADICTS**: A CONTRADICTS relation is created if and only if:
1. Both claims are explicit or inferred (not interpretation/evaluation)
2. Both claims pass the Node Admission Rule independently (both are important enough to be nodes)
3. The contradiction is important for understanding (flagging it aids critical thinking)

When a CONTRADICTS relation is present, the output must include an explicit note: *"Contradiction flagged: X contradicts Y. Both are author-explicit/inferred. Reader should attend to this tension."*

### 4.4 Decision 1: Bounded Input Constraint (<~200 pages or Chapter)

**Decision (from reference/decisions.md)**: v0 skill operates on **bounded inputs only**.

**Input types**:
- Complete books under ~200 pages
- Single chapter from longer books
- Article or essay (typically 5-50 pages)
- Bounded excerpt with clearly marked start/end (e.g., "Chapter 3–5", "Pages 150–200")

**Input contract**: User provides plain text, Markdown, or plain prose in UTF-8. Format should preserve paragraphing and structure. No need for markup; plain text is sufficient.

**Maximum length guideline**: ~200 pages (typical: 40,000–80,000 words for a chapter or article; 50,000–200,000 words for a complete short book). This ensures:
- Model fidelity (no lossy state compression)
- Tractable computation (no need for session persistence)
- Clean testing (Gogol first chapter ~30 pages fits easily)

**Out-of-scope for v0**: Full-book stateful reading, multi-session continuation, state management across invocations.

**Future path (v1+)**: Stateful multi-pass reading can be implemented by calling v0 repeatedly on chapter-sized windows and merging results. v1 will layer session management and state persistence over v0's single-pass engine.

**Error handling**: If user submits text >200 pages without clear excerpt boundaries, the skill should:
1. Detect the length
2. Respond with a friendly error: "This text is ~X pages. I work best on chapters or articles. Please provide a single chapter or excerpt."
3. Offer guidance: "To prepare a long book, extract one chapter or pages Y–Z and submit that."

### 4.5 Decision 2: Fiction Adaptation (No Ontology Extension)

**Decision (from reference/decisions.md)**: Apply the existing Five-Layer Model to fiction without extending node types.

**Semantic mapping for fiction**:

| Layer | Non-Fiction | Fiction | Adaptation |
|-------|-------------|---------|-----------|
| **PURPOSE** | Problem (gap in knowledge), Intent (educate/convince) | Central conflict or dilemma, Thematic/narrative intent (what human condition does the author explore?) | Reinterpret: Problem → central conflict; Intent → thematic aim |
| **QUESTIONS** | Conceptual questions ("What is X?") | Character/narrative inquiries ("What becomes of X?" "How does X change?") | Remain valid for fiction; may be more about outcome and meaning |
| **IDEAS** | Concepts, Claims, Principles (abstract intellectual content) | Thematic claims, character insights, symbolic meanings | Include both abstract themes and character/narrative insights; distinguish narrative instantiation from example |
| **REASONING** | Arguments, Evidence, Examples | Narrative causality (event A leads to event B), thematic reasoning (character moment illustrates principle), dialogue as evidence | Adapt: narrative structure as reasoning; character arcs as development of thematic ideas; dialogue and scenes as evidence |
| **CONSEQUENCES** | Implications, Applications, Limitations | Reader implications (what the work reveals about humanity), thematic takeaways | Reinterpret: Implication → thematic insight; Application → existential or cultural takeaway; Limitation → scope of applicability |

**Specific guidance for fiction**:

1. **Character arcs are not examples**. A character's transformation is a narrative instantiation of a thematic idea, not an illustration. Example: Chichikov in *Dead Souls* is not an "example of a corrupt person" but a narrative embodiment of Gogol's thematic claim about servility and emptiness.

2. **Dialogue and scenes are evidence**. When Gogol describes Chichikov's behavior, that description is evidence supporting a thematic claim. Scenes function as reasoning.

3. **Status honesty matters for fiction**. Most thematic claims in fiction are inferred or interpretive. A character's internal state is often inferred from behavior. Tag these accurately.

4. **Literary-specific analysis is v1+**. Foster's symbolic layer (metaphor, archetype, motif, symbol as first-class nodes) is deferred. v0 captures thematic and narrative content using existing types.

**Scope clarification**: 
- **In-scope (v0)**: Narrative fiction, thematic reconstruction, character development, plot structure, implied themes
- **Out-of-scope (v1+)**: Deep literary/symbolic analysis, metaphor decoding, archetypal patterns, close reading of imagery

### 4.6 Decision 3: Pass 2 Completion (Fixed-Point Convergence)

**Decision (from reference/decisions.md)**: Pass 2 (Reconstruct) is complete when **fixed-point convergence** is reached.

**Definition**: A state in which re-reading the source text (or a verification scan) produces no new nodes that meet the Node Admission Rule.

**Completion criteria (all four must be met)**:

1. **Node Saturation**: Every node currently in the model passes the Node Admission Rule. No obvious uncovered node meets the rule and was missed.

2. **Relation Saturation**: All important logical or textual connections between existing nodes have been identified and typed. No two nodes with a meaningful relationship remain unrelated.

3. **Fixed-Point Convergence (verification check)**: Run one more verification pass (re-read key sections, sample chapters, or critical passages). If no new nodes that meet the admission rule are discovered, a fixed point has been reached.

4. **Status Honesty**: Every node's status tag (explicit/inferred/interpretation/evaluation) is accurate and defensible. No implicit assumptions are hidden or mislabeled.

**Verification checklist (human review)**:
- [ ] Node Admission Rule is applied consistently (5 admission criteria checked for each node)
- [ ] No node is missing that would explain a key claim or dependency
- [ ] Relations are named, not implicit
- [ ] Status tags are defensible (can you justify why Node-047 is "inferred" and not "explicit"?)
- [ ] A re-scan of key chapters/sections uncovers no new core nodes
- [ ] Qualifications, scope, and conditions are preserved in node statements

**Stopping rule**: When the checklist passes, Pass 2 is complete. Output a brief summary: "Pass 2 complete: [N] nodes, [M] relations, fixed-point reached after [K] convergence checks."

### 4.7 Decision 4: Cross-File Linking (Plain Markdown)

**Decision (from reference/decisions.md)**: Use **plain markdown links** for all cross-file references.

**Format**:
```markdown
[NODE-ID](relative/path/to/file.md#NODE-ID)
```

**Examples**:
- Intra-file (same file): `See [C-015](#C-015) for the foundational concept.`
- Cross-file (same book): `Supported by evidence [E-042](03_reasoning.md#E-042) in the reasoning layer.`
- External (future multi-book): `Contrasts with [Kuhn-P-003](../../books/kuhn-ssr/02_ideas.md#P-003).`

**Rationale**: Markdown links are portable across all editors (VS Code, GitHub, GitLab, Obsidian, static generators). No vendor lock-in. Obsidian users can navigate with regular markdown links; wikilink conversion can be added in v1+ without breaking v0.

**Constraint**: All cross-file links must be valid markdown paths and properly formatted with anchors (node IDs).

### 4.8 Decision 5: Authorial Contradictions (Flagged, Not Resolved)

**Decision (from reference/decisions.md)**: Create CONTRADICTS relations when both claims pass admission rule and the contradiction aids critical reading.

**Implementation**:

1. During Pass 2, identify claims that logically contradict (both true would be impossible).

2. Check criteria:
   - [ ] Both claims are explicit or inferred (not interpretation/evaluation)
   - [ ] Both claims pass the Node Admission Rule independently
   - [ ] The contradiction is important for understanding the text or supporting critical reading

3. If all three criteria are met:
   - Create both nodes independently
   - Add `CONTRADICTS` edge: `Node-A --CONTRADICTS--> Node-B`
   - In markdown output, include explicit note:
     ```
     **Contradiction flagged**: [Claim-A](#Claim-A) contradicts [Claim-B](#Claim-B).
     Both are author-explicit. This tension is central to understanding how 
     the author navigates competing values.
     ```

4. The model preserves both claims; it does not resolve the contradiction on behalf of the author.

**Example from fiction**: In Gogol's *Dead Souls*, the author simultaneously satirizes characters (ridicule) and pities them (compassion). These are both present and both important. Rather than choosing one, the model flags the tension and lets the reader experience it.

### 4.9 Node Admission Rule (Refined)

A node earns a place in the model if it satisfies **any one** of these five criteria:

1. **Necessary for central ideas** — Without this node, the book's central thesis or primary argument breaks.
2. **Dependency of important nodes** — Other important nodes depend on it for logical support.
3. **Significant original contribution** — The node represents a distinct idea or insight the author uniquely introduces.
4. **Required for application** — Removing it would prevent readers from applying the author's ideas.
5. **Critical to author fidelity** — Losing it would distort or misrepresent the author's position.

**Dropping criteria**: A node can be dropped if:
- It is purely illustrative (use ILLUSTRATES relation instead)
- It is a passing mention, not connected to core argument
- It is a sub-point of a supporting idea (fold into parent)
- It is redundant with another node

**Principle**: The model should be **"full enough to reconstruct, small enough to understand"** (design-log Principle 10).

### 4.10 Input and Output Contracts

#### Input Contract

**Format**: Plain text, Markdown, or prose (UTF-8, UTF-16, or ASCII)

**Structure**: Preserve:
- Paragraph breaks
- Section/chapter headings (if present)
- Line breaks that convey structure
- Quotation marks and emphasis (if available)

**Length**: 
- Minimum: ~5 pages (too short → no meaningful model)
- Optimal: 20–100 pages (chapter or article)
- Maximum (v0): ~200 pages (longer texts require stateful reading, v1+)

**Content types**:
- Non-fiction (methodology, argument, exposition, philosophy, social science)
- Narrative non-fiction (memoir, biography, history)
- Narrative fiction (novels, short stories, satirical fiction)

**Not supported (v0)**:
- Poetry (too much layering required; defer to v1+)
- Technical proofs or purely mathematical text (require specialized reasoning)
- Very long books without chapter boundaries (use chapter submission instead)

#### Output Contract

**Form**: Five markdown files in `Books/<slug>/`

**Files**:
1. `00_purpose.md` — Problem and Intent nodes, intro prose
2. `01_questions.md` — Question nodes, hierarchy, intro prose
3. `02_ideas.md` — Concept, Claim, Principle nodes, hierarchy, intro prose
4. `03_reasoning.md` — Argument, Evidence, Example, Assumption nodes, hierarchy, intro prose
5. `04_consequences.md` — Implication, Application, Limitation nodes, hierarchy, intro prose

**Per-file structure**:
- Brief introductory prose (1 paragraph) explaining the layer's role in the book
- Hierarchical organization by theme or sub-topic (using markdown `##`, `###` headings)
- Nodes in logical order (typically top-down: purpose → questions → ideas → reasoning → consequences)
- Relations section showing cross-file and intra-file links
- Closing reflection on how this layer functions in the book's architecture

**Per-node format**:
```markdown
#### [Type]: [Title]

**Statement:** [1-2 sentences]

- **Type:** [Concept | Claim | Principle | ...]
- **Status:** [explicit | inferred | interpretation | evaluation]
- **Importance:** [core | important | supporting | detail]
- **Confidence:** [high | medium | low]
- **Source:** [Chapter X, "Section Name" | pp. Y–Z | passage excerpt]

**Relations:**
- [RELATION] → [Node-ID](file.md#Node-ID) — [explanation]

**[Optional] Elaboration:**
[Additional context if needed]
```

**Quantity**: 
- Typical output: 30–100 nodes depending on source length and depth
- Short article (~30 pages): 10–30 nodes
- Chapter (~50 pages): 25–50 nodes
- Book (~200 pages): 50–100 nodes
- Estimate: ~0.25–0.5 nodes per page

**Quality criteria**:
- All nodes have required metadata (id, type, title, statement, status, importance, confidence, source)
- No critique mixed into reconstruction (author fidelity maintained)
- Relations are meaningful and explained (not just listed)
- No examples treated as ideas
- No inferred statements tagged as explicit
- File structure matches template
- Cross-file links are valid markdown

### 4.11 The Six Hard Rules (Non-Negotiable)

These rules are enforced during reconstruction and verification:

1. **Do NOT optimize for compression.** Preserve the book's texture and nuance. A reconstruction that is shorter is not automatically better. Qualifications matter.

2. **Do NOT treat chapter summaries as canonical.** Reconstruct from the actual text, not from chapter summaries or the author's own abstracts. (That would be compression of compression.)

3. **Do NOT equate frequency of mention with importance.** Function in the argument matters. An idea mentioned once but central to the thesis is core; an idea mentioned often but peripheral is supporting.

4. **Do NOT present inferred statements as explicit author claims.** Use status tags correctly. If the author doesn't state it directly, mark it as inferred/interpretation/evaluation.

5. **Do NOT treat examples as ideas.** Examples illustrate ideas; they are not ideas themselves. Create Example nodes with ILLUSTRATES relations, never fold examples into Concept or Claim nodes.

6. **Do NOT use quotations as knowledge nodes.** Quotations are evidence supporting claims, not concepts. If a quotation states an important claim, extract the claim as a node and link the quotation as Evidence.

---

## 5. The Three Passes (Detailed)

The skill operates in three sequential passes: Survey, Reconstruct, Write.

### Pass 1: Survey — Establishing Orientation

**Goal**: Establish orientation. Understand the book's shape, intent, and structure before committing to full reading.

**Duration**: 10–30 minutes depending on source length.

**Steps**:

1. **Identify text type** (2 minutes)
   - Is this primarily non-fiction (exposition, argument, methodology) or narrative (story, memoir, fiction)?
   - Is it structured as a single argument, collection of essays, reference material, or exploratory writing?
   - What is the author's primary mode: convincing, explaining, teaching, exploring, provoking?

2. **Skim the structure** (5–15 minutes)
   - Read title, subtitle, front matter (dedication, preface)
   - Read table of contents or chapter titles (if present)
   - Read introduction or opening (where author often states problem and intent)
   - Read conclusion or closing sections (where implications are stated)
   - Sample 2–3 chapter openings (first 1–2 paragraphs each)
   - Glance at back matter (index, bibliography, notes)

3. **Identify the problem** (3 minutes)
   - Ask: What difficulty, gap, or challenge prompted the author to write?
   - May need to infer from title, introduction, or opening argument
   - Write 1–2 sentences. Example: "Readers typically approach all books the same way, leading to shallow understanding of complex texts."

4. **Identify the intent** (3 minutes)
   - Ask: What does the author aim to accomplish?
   - To convince? To teach method? To challenge? To provide reference? To explore?
   - Intent ≠ Problem. Problem: what's wrong. Intent: what author does about it.
   - Write 1–2 sentences. Example: "Teach readers a systematic methodology for deep reading."

5. **Identify central questions** (3 minutes)
   - Ask: What question(s) does the author set out to answer?
   - Often stated in introduction or implied by structure
   - Write 1–3 central questions. These become Question nodes later.

6. **Determine reading goal** (2 minutes)
   - Depth: Full reconstruction or strategic overview?
   - Scope: Entire text or specific sections?
   - Time budget: How much time available?

**Output**:
- 1-paragraph orientation (what this book is, who wrote it, what it addresses)
- 1–2 sentences on problem and intent
- 1–3 central questions listed
- Sense of book structure and scope

**Example (Gogol's *Dead Souls*, Chapter 1)**:
- Text type: Satirical narrative fiction
- Problem: Corruption, servility, and the absence of human dignity in Russian society
- Intent: Expose and satirize Russian provincial life through the misadventures of Chichikov
- Questions: "What is the nature of human servility?" "How does society devalue the individual?" "What is the difference between appearance and reality?"
- Reading goal: Full reconstruction of first chapter to smoke-test fiction handling

### Pass 2: Reconstruct — Extracting the Model

**Goal**: Read the text and extract the Five-Layer Model.

**Critical rule**: Never critique before reconstruction is complete. You are understanding the author's position on its own terms, not evaluating whether it's correct.

**Duration**: 30 minutes – 2 hours depending on source length and complexity.

**Steps**:

1. **Read actively** (primary activity)
   - Read the text linearly or by sections, depending on structure
   - Mark passages that introduce major concepts, make important claims, defend claims with evidence/example, or transition between ideas
   - You are not taking detailed notes yet; you are marking the structure

2. **Extract nodes as you read** (concurrent with step 1)
   - For each major intellectual move, ask the clarifying questions below and create the appropriate node
   
   **Concepts**: "Is this a term or definition the author introduces as a building block? Is it used throughout? Is it necessary for understanding other ideas? → Create Concept node."
   
   **Claims**: "Is the author asserting this as true? Is it central or sub-point? Does it connect to central questions? → Create Claim node."
   
   **Principles**: "Is this a law or principle the author establishes? Does it apply across contexts? Is it a major takeaway? → Create Principle node."
   
   **Evidence**: "Does this data, study, observation, or quotation support a specific claim? Is it traceable? → Create Evidence node and link with SUPPORTS."
   
   **Examples**: "Is this a concrete instance of a general idea? Is it illustrative or constitutive? → Create Example node with ILLUSTRATES (not a Concept node)."
   
   **Arguments**: "Does the author link premises to conclusion? Does it defend a claim? → Create Argument node and link with SUPPORTS."
   
   **Questions**: "Does the author pose an open inquiry that organizes reasoning? → Create Question node."
   
   **Assumptions**: "Does the author rely on an unstated premise? → Create Assumption node (tag as inferred)."
   
   **Implications**: "Does this follow logically from the author's ideas? → Create Implication node."
   
   **Applications**: "Can readers *use* these ideas? How? → Create Application node."
   
   **Limitations**: "Where do these ideas not apply? What are scope boundaries or exceptions? → Create Limitation node (QUALIFIES relations)."

3. **Tag every node with metadata**
   - **Status** (epistemic): explicit | inferred | interpretation | evaluation
   - **Importance** (functional): core | important | supporting | detail
   - **Confidence** (epistemic certainty): high | medium | low
   - **Source** (traceability): Chapter X, section "...", pp. Y–Z, or passage excerpt

4. **Apply Node Admission Rule**
   - Ask for each node: Does it meet one of the 5 admission criteria?
   - Drop nodes that fail all criteria (purely illustrative, passing mention, redundant, sub-point of parent)

5. **Identify relations**
   - As you build the model, trace how nodes connect
   - Use the 9 relation types (ANSWERS, SUPPORTS, DEPENDS_ON, EXPLAINS, ILLUSTRATES, QUALIFIES, CONTRADICTS, LEADS_TO, PART_OF)
   - Only draw relations that are explicit or clearly implied; do not assume

6. **Preserve qualifications**
   - Critical: Do not lose nuance in compression
   - If author says "In most cases, X leads to Y, except when Z is present," preserve both the main claim and the limitation
   - Use Limitation nodes or preserve conditions in the statement itself
   - Tag uncertainty (e.g., "perhaps" → confidence: medium)

7. **Convergence check (fixed-point verification)**
   - After completing the linear read, run one more verification pass
   - Re-read key sections or sample chapters
   - Ask: "Are there any new nodes that meet the admission rule that I missed?"
   - If no new nodes emerge, fixed-point convergence is reached

**Output**: 
- Collection of 30–100 nodes organized by layer
- Each node has full metadata and relations
- All nodes pass admission rule
- Fixed-point convergence achieved

**Example node (from hypothetical Gogol extraction)**:
```yaml
id: Q-047
type: Question
title: What is the nature of human servility?

statement: |
  Gogol poses this as an implicit central question throughout the first chapter.
  Chichikov's social maneuvering and the characters' obsequiousness suggest
  the author is investigating what drives humans to abase themselves.

status: inferred
importance: core
confidence: medium
source:
  chapter: 1
  location: "Throughout chapter; especially Chichikov's interactions with officials"

relations:
  - type: ANSWERS
    target: P-201
    note: "Answered by the principle that servility is both pathetic and inevitable"
```

### Pass 3: Write — Rendering the Model

**Goal**: Organize the reconstructed model into five markdown files optimized for human reading.

**Duration**: 30 minutes – 1 hour depending on node count.

**Steps**:

1. **Organize nodes by layer**
   - Group all nodes into their semantic layer:
     - PURPOSE → 00_purpose.md
     - QUESTIONS → 01_questions.md
     - IDEAS → 02_ideas.md
     - REASONING → 03_reasoning.md
     - CONSEQUENCES → 04_consequences.md

2. **Structure each file hierarchically**
   - Start with a brief introductory paragraph (1–2 sentences) explaining the layer's role
   - Group nodes by theme or sub-topic using markdown headings (`##`, `###`)
   - Present nodes in logical order (usually top-down: purpose → questions → ideas → reasoning → consequences)
   - End with a brief reflection on how this layer functions in the book

3. **Format each node**
   ```markdown
   #### [Type]: [Title]
   
   **Statement:** [1-2 sentence core claim]
   
   - **Type:** [Concept | Claim | Principle | Argument | Evidence | Example | Assumption | Implication | Application | Limitation]
   - **Status:** [explicit | inferred | interpretation | evaluation]
   - **Importance:** [core | important | supporting | detail]
   - **Confidence:** [high | medium | low]
   - **Source:** [Chapter X, "Section Name" | pp. Y–Z]
   
   **Relations:**
   - [RELATION] → [Node-ID](file.md#Node-ID) — [brief explanation]
   
   **[Optional] Elaboration:**
   [1 paragraph of context if statement alone is insufficient]
   ```

4. **Write relations with explanation**
   - Relations are not decoration; they show how the book fits together
   - Always include a note explaining the connection
   - **Good**: "SUPPORTS Claim C-042: The evidence from the 1985 study demonstrates that readers who establish purpose first retain material 40% better, directly supporting this claim."
   - **Bad**: "SUPPORTS C-042"

5. **Handle cross-file links**
   - If a node relates to a node in another file, add a cross-reference
   - Format: `[Node-ID](path/to/file.md#Node-ID)`
   - Example: "Supported by Evidence [E-015](03_reasoning.md#E-015)"

6. **File structure example** (02_ideas.md)
   ```markdown
   ## IDEAS: Concepts, Claims, and Principles
   
   The book introduces key concepts that form the foundation of systematic reading...
   
   ### Foundational Concepts
   
   #### Concept: Deep Reading
   [node details]
   
   ### Core Claims
   
   #### Claim: Reading Is Purposeful
   [node details]
   
   ### Principles
   
   #### Principle: Reconstruction Before Compression
   [node details]
   ```

7. **Final verification**
   - Check file structure matches template
   - Verify all cross-file links are valid markdown
   - Confirm all nodes have required metadata
   - Ensure relations have explanatory notes

**Output**: Five markdown files in `Books/<slug>/` directory, fully formatted and linked, ready for human reading and further analysis.

---

## 6. Testing & Verification Decisions

### What Makes a Correct Run

A correct run of the skill produces a model that:

1. **Faithfully reconstructs the source** without compression or loss of qualifications
2. **Preserves author fidelity** — every claim is tagged with status; inferred statements are never presented as explicit
3. **Is traceable** — every important node has a source (chapter/section/page)
4. **Is structurally sound** — nodes fit into the Five-Layer Model; relations are valid and explained
5. **Reaches fixed-point convergence** — a verification pass uncovers no new nodes meeting the admission rule

### Verification Checklist

Use this checklist to validate a completed model:

**Metadata Integrity**
- [ ] Every node has a unique id
- [ ] Every node has a type (one of 13)
- [ ] Every node has a title (short label)
- [ ] Every node has a statement (1–2 sentences)
- [ ] Every node has status (explicit | inferred | interpretation | evaluation)
- [ ] Every node has importance (core | important | supporting | detail)
- [ ] Every node has confidence (high | medium | low)
- [ ] Every node has source (chapter/section/page)

**Epistemological Honesty**
- [ ] Status tags are accurate and defensible
- [ ] Inferred statements are tagged as "inferred," never "explicit"
- [ ] Interpretation nodes are clearly labeled and not confused with explicit claims
- [ ] Evaluation nodes (author's assessments) are not confused with author-explicit claims

**Structural Soundness**
- [ ] All nodes fit into Five-Layer Model (PURPOSE, QUESTIONS, IDEAS, REASONING, CONSEQUENCES)
- [ ] Problem and Intent nodes exist (PURPOSE layer)
- [ ] At least one Question node exists (QUESTIONS layer)
- [ ] Ideas are separated into Concepts, Claims, Principles (not mixed)
- [ ] Examples are separate nodes with ILLUSTRATES relations, not merged into ideas
- [ ] Every Claim/Principle has at least one supporting Argument or Evidence node
- [ ] Every Claim/Principle with scope boundaries has a Limitation node

**Relational Integrity**
- [ ] Relations use only the 9 valid types (ANSWERS, SUPPORTS, DEPENDS_ON, EXPLAINS, ILLUSTRATES, QUALIFIES, CONTRADICTS, LEADS_TO, PART_OF)
- [ ] Relations are meaningful and not assumed
- [ ] Every relation has an explanatory note
- [ ] Cross-file links are valid markdown paths
- [ ] If CONTRADICTS relations exist, they meet the three criteria (both explicit/inferred, both pass admission rule, contradiction matters)

**Author Fidelity**
- [ ] No critique mixed into reconstruction
- [ ] No examples presented as ideas
- [ ] Quotations are used as Evidence, not concepts
- [ ] Qualifications and scope are preserved in statements
- [ ] Nuance is not lost to compression

**Completeness**
- [ ] Fixed-point convergence has been checked (re-scan uncovers no new nodes)
- [ ] All nodes pass the Node Admission Rule
- [ ] No node is purely redundant with another
- [ ] The five files tell a coherent story

**Output Format**
- [ ] Five markdown files exist in expected locations (00_purpose.md through 04_consequences.md)
- [ ] Each file has introductory prose and node hierarchy
- [ ] Node formatting follows template (all required fields present)
- [ ] All markdown links are valid and clickable

### Reference Case: Gogol Smoke Test

The v0 validation plan uses Gogol's *Dead Souls*, Chapter 1 (~30 pages) as a reference case.

**Expected characteristics**:
- ~30–50 total nodes (fiction produces denser thematic content)
- PURPOSE: 1 Problem, 1 Intent
- QUESTIONS: 3–5 central thematic questions
- IDEAS: 8–12 concepts, 8–12 claims/principles
- REASONING: 5–8 arguments, 4–6 evidence nodes, 3–5 examples, 2–3 assumptions
- CONSEQUENCES: 3–5 implications, 2–3 applications, 1–2 limitations
- Multiple CONTRADICTS relations (satirical tone creates intentional tensions)
- Status distribution: ~70% explicit, ~25% inferred, ~5% interpretation

**Verification output includes**:
- Confirmation of fixed-point convergence
- Summary: "[N] nodes, [M] relations, fiction handled without ontology extension"
- Sample nodes from each layer showing correct metadata and relations

### Quality Gates

Before considering a model complete:

1. **Admission Rule**: Every node passes one of 5 admission criteria (checkable)
2. **Convergence**: Fixed-point verification confirms no missed nodes (checkable)
3. **Metadata**: All nodes have all required fields (automated, checkable)
4. **Honesty**: Status tags are defensible and accurate (human review, spot-checkable)
5. **Relations**: All relations are named and explained (human review, spot-checkable)
6. **Structure**: Five files follow template and link correctly (automated, checkable)

---

## 7. Out of Scope (v0, Explicitly Deferred to v1+)

### Explicitly Deferred Features

**Long-book stateful reading** (v1+)
- Multi-session continuation across chapters
- Session state management and memory
- Aggregation of per-chapter models into full-book model
- Checkpoint and recovery

**Deep literary/symbolic analysis** (v1+)
- Foster's second layer: metaphor, archetype, motif, symbol analysis
- Fiction-specific node types (Symbol, Motif, CharacterArc, Theme as first-class)
- Close reading of poetic devices or imagery
- Symbolic systems and their interpretation

**Syntopical reading** (v1+)
- Comparing concepts across multiple books
- Cross-book entity resolution (when does "justice" in Book A mean the same as "justice" in Book B?)
- Building a canonical concept library across a user's library
- Multi-book synthesis and synthesis models

**Alternative output formats** (v1+)
- HTML interactive visualization
- JSON machine-readable output
- Obsidian-native canvas or custom views
- Interactive graph visualization (SVG, Three.js)
- PDF export

**Collaborative and version control features** (v1+)
- Multi-user annotation and disagreement
- Version history and branching of interpretations
- Collaborative markup and discussion
- Merging of multiple readings

**Integration with external systems** (v1+)
- API integration with knowledge graph databases (Neo4j, etc.)
- Connection to Zotero, Mendeley, or other bibliography tools
- Sync with Obsidian or Roam Research
- LLM embedding and vector search

**Technical/specialized domains** (v1+)
- Mathematical proofs or formal logic texts
- Programming language specifications
- Highly technical scientific papers
- Extended ontologies for science, fiction, poetry

---

## 8. Principles & Philosophy (Integrated)

### Three Methodological Foundations

This skill is grounded in three classic texts on reading methodology:

**Sergey Povarnin** (*How to Read Books*, 1925)
- Reading is purposeful. Know *why* and *how deep* before you start.
- Reading mode, depth, and speed must match intent and text type.
- Philosophy: Intention → Strategy → Execution

**Mortimer Adler** (*How to Read a Book*, 1940)
- Reading is active intellectual work. The reader reconstructs the author's thought.
- Four levels: elementary, inspectional, analytical, syntopical.
- Reading answers five questions: What is the book about? How is it structured? What does the author say? Is the author right? What does it mean for me?
- Philosophy: Reconstruction before evaluation.

**Thomas Foster** (*The Art of Reading*, 2003)
- Literal meaning is not the whole truth. Literary texts contain patterns, symbols, themes, and second layers.
- Careful reading attends to what is *shown*, not only what is *said*.
- Philosophy: Surface and depth coexist; read on multiple layers.

### Six Foundational Rules (v0)

#### 1. Purpose Before Processing

Before reading, identify:
- What is this text? (type, domain, scope)
- Who wrote it? (author, context, credentials)
- What problem does it address? (the gap it fills)
- What reading depth is needed? (orientation, comprehension, critical, application)
- How should you approach it? (reading mode)

*Principle*: Purpose determines strategy. Strategy determines execution.

#### 2. Reconstruction Before Compression

```
BOOK → UNDERSTAND → RECONSTRUCT → VERIFY → COMPRESS/EXPLAIN
```

Do not optimize for brevity. Preserve the book's intellectual architecture faithfully. Compression comes later, and must never strengthen a claim or lose a qualification.

*Principle*: Fidelity before brevity.

#### 3. Author Fidelity

Understand the book on its own terms first.

Ask in order:
1. What does the author say?
2. What does the author mean?
3. Why does the author believe it?
4. What follows logically?
5. Only then: Is the author right? Do I agree?

*Principle*: Suspend judgment during reconstruction. Critique comes after understanding.

#### 4. Epistemic Separation

Tag every claim with its epistemic status:
- **explicit** — the author states it directly
- **inferred** — clearly implied but not stated
- **interpretation** — a reading of ambiguous passages
- **evaluation** — your (the reader's) assessment or external judgment

Never present inference as explicit. Never pass interpretation off as fact.

*Principle*: Transparency about sources of knowledge.

#### 5. Source Traceability

Every important claim knows where it came from.

Quote chapter, section, page, or passage. No important node without provenance.

*Principle*: No claim without a source. Traceability enables verification.

#### 6. Preserve Nuance

Save conditions, exceptions, scope, qualifications, and uncertainty. A claim loses its truth when stripped of its boundaries.

Examples:
- If author says "In most cases, X leads to Y, except when Z is present," preserve both the main claim and the limitation.
- If author says "Perhaps the most important factor is...," preserve the uncertainty; don't present it as unqualified.

*Principle*: Compression must never strengthen a claim.

### What This Skill Does NOT Do

- Does NOT summarize (compress information for speed)
- Does NOT prioritize frequency of mention over structural importance
- Does NOT treat chapter summaries as the canonical form
- Does NOT present examples as ideas
- Does NOT use quotations as knowledge nodes
- Does NOT critique before reconstruction is complete
- Does NOT optimize for brevity at the cost of nuance
- Does NOT resolve contradictions on behalf of the author
- Does NOT extend the ontology unnecessarily (v0 maintains minimal, maximum-explanatory-power types)

### What This Skill DOES Do

- Identifies the book's purpose (problem and intent)
- Reconstructs the author's central questions
- Maps key ideas (concepts, claims, principles)
- Traces reasoning (arguments, evidence, examples, assumptions)
- Outlines consequences (implications, applications, limitations)
- Tags every node with epistemic status, functional importance, confidence, and source
- Identifies relations (how ideas depend on, support, explain, contradict each other)
- Renders the model as a knowledge structure (five markdown files) that readers can use to think *with* and *against* the book
- Enables critical reading by making assumptions, contradictions, and scope boundaries explicit

### Philosophical Summary

**This skill does not summarize books. It reads them.**

It reconstructs their intellectual structure faithful to the author's intent and argument. It makes the author's thought transparent—visible in its parts and in their connections. Only after understanding is complete does it transform the reconstruction into forms optimized for human retention, critique, and application.

The goal is not to compress a book. The goal is to reconstruct it well enough that the reader can think with and against it.

---

## Appendix: Related Documents

- **reference/design-log.md** — Full design conversation, 12 principles, evolution from summary to Full Book Model
- **reference/decisions.md** — Five resolved design decisions (ADRs) with rationale and implications
- **reference/ontology.md** — Detailed specification of node types, relations, templates, and admission rules
- **reference/philosophy.md** — Three authors, six foundational rules, principles summary
- **reference/process.md** — Detailed step-by-step instructions, examples, verification checklist, FAQs
- **SKILL.md** — Manifesto and quick reference (less authoritative than this spec)

---

**End of Specification (v0)**
