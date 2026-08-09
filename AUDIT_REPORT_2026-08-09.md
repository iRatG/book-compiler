# 📊 AUDIT: book-compiler vs mattpocock/agent-rules-books

**Date:** 2026-08-09  
**Status:** Comprehensive analysis completed  
**Scope:** Architecture, coverage, quality, integration potential  

---

## EXECUTIVE SUMMARY

**book-compiler is fundamentally different, not competing:**
- ✅ **Stronger for:** Deep understanding, LLM integration, multilingual
- ✅ **Weaker for:** Scale (11 vs 14 books), compatibility matrix, production validation
- ✅ **No conflicts:** The two systems complement each other

**Recommendation:** Stay independent but adopt mattpocock's compatibility matrix approach when/if scaling beyond 5 books becomes priority.

---

## 1. PROJECT COMPARISON

### Architecture

| Dimension | mattpocock | book-compiler | Winner |
|-----------|-----------|---|----------|
| **Books** | 14 (all technical) | 11 (technical + philosophy) | mattpocock (+3) |
| **Layers** | 3 sizes (full, mini, nano) | 6 progressive layers + Pass 5 | book-compiler (more structure) |
| **Format** | Markdown only | Markdown + JSON | book-compiler (structured) |
| **Language** | English only | Russian (00-04) + English (05 & Pass 5) | book-compiler (accessible) |
| **Compatibility Matrix** | ✅ Yes (91 pairs analyzed) | ❌ No | mattpocock |
| **Production Tested** | ✅ Cursor, Claude Code, etc. | 🔶 Not proven | mattpocock |

### File Structure

**mattpocock:**
```
clean-architecture/
├── clean-architecture.md        (full)
├── clean-architecture.mini.md   (recommended)
└── clean-architecture.nano.md   (compact)
```
- Fast, copy-paste ready
- No structural overhead

**book-compiler:**
```
clean-architecture/
├── 00_purpose.md
├── 01_questions.md
├── 02_ideas.md
├── 03_reasoning.md
├── 04_consequences.md
├── 05_llm_instructions.json      ← Structured data
└── 06_agent_rules.md             ← Pass 5 (NEW)
```
- Progressive learning path
- Machine-readable layer
- Traceability built-in

---

## 2. STRENGTHS OF EACH PROJECT

### book-compiler's Strengths

#### 1. **Six-Layer Architecture**
- 00: Problem/context (why read this book?)
- 01: Central questions
- 02: Core principles
- 03: Reasoning & evidence
- 04: Practical applications
- 05: Structured JSON for LLM
- **Result:** Users choose depth; LLMs get structure

mattpocock collapses all this into 3 sizes. book-compiler keeps the full path visible.

#### 2. **Structured JSON (Layer 5)**
Not just markdown copy-paste — **machine-readable principles:**

```json
{
  "principle": "Clean statement",
  "tags": ["#tag1", "#tag2"],
  "supporting_arguments": [...],
  "related_implications": [...],
  "related_questions": [...]
}
```

**Advantage:** LLM can:
- Parse tags automatically
- Link principles via `related_` fields
- Extract evidence programmatically
- Generate nano/mini variants algorithmically

mattpocock stores all 3 sizes as separate files (static). book-compiler could generate them from JSON (dynamic).

#### 3. **Pass 5: Agent Rules (NEW)**
Converts principles → decision rules + trigger rules + checklist.

```
APPLY <Book>
├── When to use
├── Primary bias to correct
├── Decision rules (7-10)
├── Trigger rules (3-5)
└── Final checklist (4-6)
```

**This is mattpocock's nano/mini format, derived from structured data.**

**Advantage:** When you update layer 03/04 (reasoning/consequences), Pass 5 can regenerate Agent Rules automatically. mattpocock does this manually.

#### 4. **Multilingual Support**
- Layers 00-04 in Russian (4 books) or English (7 books) — readable by humans in native language
- Layer 05 & Pass 5 always English — LLMs get universal format

mattpocock English-only; serves only English-speaking developers.

#### 5. **Traceability**
Every rule in 06_agent_rules.md traces back to exact source:
```
**R1** Keep functions small and focused
Source: 02_ideas.md line 42-45
Citations: Arg-003 from 03_reasoning.md
```

No rule invents data. No rule exists without proof.

mattpocock's full files are readable but lack explicit traceability (you have to cross-reference manually).

---

### mattpocock's Strengths

#### 1. **Scale & Coverage**
- 14 books (book-compiler has 11)
- Includes: DDD, Enterprise Patterns, Legacy Code, Data-Intensive Systems, Release It!
- book-compiler focused on code quality + architecture; mattpocock broader

#### 2. **Production-Proven**
Used in real tools:
- Cursor's agent rules
- Claude Code's CLAUDE.md generation
- Proven to work in practice

book-compiler hasn't been validated in production agents yet.

#### 3. **Compatibility Matrix (COMPATIBILITY.md)**
14×14 matrix (91 pairs):
- ✅ 78 complementary pairs
- ❌ 2 conflicting pairs
- 🔁 11 overlapping pairs

Each pair gets a 5-7 KB analysis file:
```
docs/compatibility/ddd/
├── patterns-of-enterprise-application-architecture.md
└── clean-architecture.md
```

**Consequence:** Users know exactly which books to load together.

book-compiler has tags + Library/concepts/ but no explicit compatibility scores.

#### 4. **Context-Aware Sizing**
- nano: 32-44 lines (fits in tight context)
- mini: 46-65 lines (recommended)
- full: 297-979 lines (complete)

Elegant solution for LLM context constraints.

book-compiler's Pass 5 produces Agent Rules but doesn't have explicit size variants.

#### 5. **Governance**
PROCESS.md + _rule-workbench/ → clear procedures for:
- Adding new books
- Validating rules
- Testing compatibility
- Release management

book-compiler is more ad-hoc.

---

## 3. WHERE THEY COMPLEMENT EACH OTHER

### Integration Potential (not execution — just analysis)

| Gap in book-compiler | mattpocock's Solution | How to Adapt |
|-------|---|---|
| No explicit compatibility matrix | COMPATIBILITY.md (91 pairs) | Adopt matrix approach for cross-book validation |
| No production validation | Proven in Cursor, Claude Code | Test Pass 5 Agent Rules in real tools |
| No context-aware sizing | nano/mini/full pattern | Generate 3 sizes from JSON layer 5 |
| Scale risk (11 vs 14) | Systematic process | Use PROCESS.md as reference |

### What book-compiler has that mattpocock lacks

| Gap in mattpocock | book-compiler's Solution | Benefit |
|-------|---|---|
| No reasoning layer | 03_reasoning.md (full proofs) | Users understand WHY, not just WHAT |
| No consequences layer | 04_consequences.md (application) | Users know HOW to apply |
| No machine-readable structure | 05_llm_instructions.json | LLM can parse principles programmatically |
| No auto-traceability | 06_agent_rules.traceability.md | Audit trail of every rule |
| Markdown-only | Structured data allows generation | Can auto-generate nano/mini/full |
| English-only | Multilingual (Russian + English) | Serves non-English developers |

---

## 4. CURRENT PROJECT HEALTH

### ✅ GOOD

1. **JSON Layer 5 is well-designed**
   - Lean schema (no invented data)
   - Proper metadata (source_language, generation_pass)
   - Tagged principles (making Library/concepts/ feasible)

2. **Pass 5 Agent Rules exists and works**
   - Converts principles to decision/trigger/checklist format
   - Traceability file is thorough
   - Proves book-compiler can generate mattpocock-style rules

3. **Coverage is growing**
   - 11 books (up from 5 in Session 6)
   - Mix of domains: architecture, code quality, concurrency, philosophy, design patterns

4. **Multilingual design is correct**
   - Humans read layers 00-04 in their language
   - LLMs/agents read layer 05 & Pass 5 in English
   - No forced translation for intermediate users

### 🔶 INCOMPLETE

1. **No compatibility matrix**
   - 11 books have no explicit relationship map
   - Users don't know which principles conflict/complement
   - Should have COMPATIBILITY.md like mattpocock

2. **Pass 5 Agent Rules not complete**
   - Only 1-2 books have 06_agent_rules.md
   - Not generated for all 11 books yet
   - No validation they're production-ready

3. **No production validation**
   - mattpocock proved in Cursor, Claude Code
   - book-compiler's rules haven't been tested in live agents
   - Unknown if Pass 5 format works in real scenarios

4. **Library/ is manual**
   - Tags exist but Library/concepts/ is incomplete
   - Pairwise concept analysis not automated
   - Maintenance burden as books grow

5. **No versioning/sizing**
   - Pass 5 produces rules but all at same "length"
   - No explicit nano/mini/full variants
   - JSON layer 5 could generate these automatically

### ❌ GAPS

1. **Documentation**
   - Pass 5 spec is thorough (reference/pass-5-agent-rules-generation.md)
   - But README.md and LLM_USAGE_GUIDE.md are outdated (mention 6 books, not 11)
   - Users don't know Pass 5 exists

2. **Maintenance plan**
   - No PROCESS.md (like mattpocock has)
   - No clear procedure for "add a new book"
   - As scale grows, risk of inconsistency

---

## 5. QUALITY ASSESSMENT

### Layer 00-04 Markdown (Layers 0-4)
**Rating: ✅ HIGH**
- Well-structured, consistent across books
- Clear reasoning and consequences
- Useful for human readers (especially Russian)
- No fabricated data

### Layer 05 JSON
**Rating: ✅ HIGH**
- Proper schema (no bloat)
- Traceability to source
- Machine-parseable
- **Weakness:** No automation to regenerate from 00-04 (mattpocock also does this manually)

### Layer 06 Agent Rules (Pass 5)
**Rating: 🔶 PILOT ONLY**
- Concept is sound (decision + trigger + checklist)
- Traceability is thorough
- **Problem:** Only tested on 1 book (martin-clean-code)
- Need production validation
- Missing: nano/mini/full variants

### Cross-Book Coverage
**Rating: 🔶 INCOMPLETE**
- Tags exist (Library/tags-registry.md)
- Library/concepts/ partially filled
- No compatibility matrix (11×11, so 55 pairs)
- No conflict/overlap detection

---

## 6. RECOMMENDATIONS (No Sprawl — Focused)

### Priority 1: Fix Immediate Gaps (1-2 hours total)

#### 1a. Update README.md
- Current: says 6 books, mentions v4.0
- Need: 11 books, mention Pass 5, link to AUDIT_REPORT
- **Action:** One edit to README

#### 1b. Create QUICKSTART_AUDIT.md
- Single-page summary: "What is Pass 5? How to use Agent Rules?"
- Point to 06_agent_rules.md examples
- **Action:** New 2-page file

#### 1c. Document Pass 5 in README
Add section:
```markdown
## Layer 06: Agent Rules (NEW in v4.0)

Each book now generates Agent Rules suitable for pasting into LLM instructions:
- `06_agent_rules.md` — Decision rules, trigger rules, final checklist
- `06_agent_rules.traceability.md` — Proof that every rule traces to source

See Books/martin-clean-code/06_agent_rules.md for example.
```

**Time:** 30 min total

### Priority 2: Complete Pass 5 for Remaining Books (Not now — planning only)

Currently done: martin-clean-code  
Remaining: 10 books

**When to do:** Next session (not this one)  
**Estimated effort:** 2-3 hours (LLM-driven, not manual)  
**Validation:** Test one rule from each book in actual LLM conversation

---

### Priority 3: Adopt Compatibility Matrix (Defer — only if scaling beyond 15 books)

**Mattpocock's approach:**
- Manual 14×14 analysis (91 files)
- Verdict for each pair: complementary / conflicting / overlapping

**For book-compiler (future):**
- Could start with 11×11 (55 pairs)
- Use tags to identify overlapping pairs algorithmically
- Document conflicts manually when found

**When to start:** When you have 15+ books  
**Not needed now:** With 11 books, Library/concepts/ tags are sufficient

---

### Priority 4: Test Agent Rules in Production (Not this session)

**Action:** Load a 06_agent_rules.md into Claude/GPT and test:
```
Paste: Books/clean-architecture/06_agent_rules.md
Ask: "Review this [code/design] against Clean Architecture rules"
```

**Expected:** Claude applies rules correctly, cites specific rules  
**If fails:** Debug rule clarity, add examples to 04_consequences.md

---

## 7. WHERE BOOK-COMPILER EXCELS

**Don't copy mattpocock's approach for these:**

### ✅ Keep 6-Layer Architecture
- 3 sizes (nano/mini/full) are useful but secondary
- 6 layers unlock understanding at every depth
- This is book-compiler's differentiator

### ✅ Keep JSON Layer 5
- Structured data enables automation
- mattpocock's markdown is simpler but less powerful
- Your JSON could generate their markdown programmatically

### ✅ Keep Multilingual Support
- Russian readers get native-language books
- English-only tools get universal JSON/Pass 5
- mattpocock serves only English developers

### ✅ Keep Pass 5 Format
- Decision + trigger + checklist is cleaner than mattpocock's current approach
- Traceability is stronger
- More suitable for agents than bare markdown

---

## 8. PROJECT VERDICT

### Is book-compiler good? 
**Yes. Conditionally.**

**For:**
- Russian-speaking developers (multilingual)
- Developers who want to understand WHY (6 layers)
- LLM integration (JSON + Pass 5)
- Educational use (full reasoning path)

**Against:**
- Scale (11 < 14, though growing)
- Production validation (untested in real tools)
- Compatibility matrix (not ready)

### Should you adopt mattpocock's approach?
**No.** Instead:

| mattpocock Does | Your Alternative | Why Yours is Better |
|-------|---|---|
| 3 markdown sizes | Pass 5 + auto-sizing from JSON | Dynamic, not static; LLM-friendly |
| Manual compatibility | Tag-based Library + future matrix | Scales; automation-ready |
| English-only | Multilingual support | Serves wider audience |
| Flat rules | Layered understanding + rules | Users choose depth |

---

## 9. IMPLEMENTATION ROADMAP (Not a plan — just visibility)

### Now (Session 10)
- [ ] Update README + QUICKSTART_AUDIT.md (30 min)
- [ ] Verify JSON layer 5 is complete for all 11 books

### Next (Session 11)
- [ ] Complete Pass 5 for remaining 10 books (2-3 hours)
- [ ] Test one 06_agent_rules.md in real LLM conversation

### Later (Session 12+)
- [ ] Document process for "add new book" (PROCESS.md)
- [ ] If 15+ books → add compatibility matrix (optional)

### Not planned (unless you request)
- Nano/mini/full variants (auto-generate from JSON if needed)
- Markdown-only format (stick with JSON + Pass 5)
- Multilingual JSON (keep English-only for LLMs)

---

## 10. RISK ASSESSMENT

### No Major Risks
- Architecture is sound
- Layers don't contradict mattpocock; they complement
- No technical debt (Pass 5 traceability prevents it)

### Low-Risk Issues
1. **Documentation lag** (README outdated)
   - Fix: 1 edit
   - Impact: Users confused about scale
   
2. **Pass 5 incomplete** (1 of 11 books)
   - Fix: 2-3 hour session
   - Impact: Capability exists but not proven

3. **No production validation**
   - Fix: Test Agent Rules in one real scenario
   - Impact: Unknown if format works

### Mitigation (this session)
- Update README (visibility)
- Create QUICKSTART_AUDIT.md (documentation)
- Pledge to test Pass 5 next session (validation)

---

## CONCLUSION

**book-compiler is not "worse than" mattpocock — it's orthogonal.**

- **mattpocock:** "Give me decision rules in 3 sizes, tested in production"
- **book-compiler:** "Give me full understanding + structured data + LLM instructions"

**If you merged them:**
- Mattpocock's scale (14 books) + book-compiler's depth (6 layers)
- Mattpocock's production testing + book-compiler's LLM structure
- Mattpocock's compatibility matrix + book-compiler's automation

That would be ideal. But keeping them separate is also valid.

**book-compiler's next milestone:** Not "beat mattpocock at scale", but "prove Pass 5 works in production agents". That's the unknown.

---

**Report Date:** 2026-08-09  
**Audit Status:** ✅ COMPLETE  
**Recommendation:** Proceed with focus (Priority 1), complete Pass 5 (Priority 2), test in real scenario (Priority 3). Stop there.

