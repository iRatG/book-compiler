# Quick Summary: book-compiler Audit vs mattpocock

**TL;DR:** Two different systems; book-compiler is stronger for education & LLM integration; mattpocock is proven in production.

---

## What is book-compiler?

6-layer system for analyzing technical books:

```
00_purpose.md       → Why read this?
   ↓
01_questions.md     → What questions does it answer?
   ↓
02_ideas.md         → What principles/ideas?
   ↓
03_reasoning.md     → Why do they work? (proofs)
   ↓
04_consequences.md  → How to apply them?
   ↓
05_llm_instructions.json  → Machine-readable (for LLMs/agents)
   ↓
06_agent_rules.md*  → Decision rules + trigger rules + checklist
```

**\* New in v4.0 (Pass 5)**

---

## What is mattpocock/agent-rules-books?

3-size markdown system:

```
clean-architecture.md        (full: 515 lines)
clean-architecture.mini.md   (recommended: 49 lines)
clean-architecture.nano.md   (compact: 36 lines)
```

Plus: COMPATIBILITY.md (14×14 matrix of which books work together)

---

## Side-by-Side

| Aspect | book-compiler | mattpocock |
|--------|---|---|
| **Books** | 11 | 14 |
| **Layers per book** | 6 (+ Pass 5 agent rules) | 3 (sizes) |
| **Format** | Markdown + JSON | Markdown only |
| **Language** | Russian (00-04) + English (05+) | English only |
| **Compatibility matrix** | ❌ Not yet | ✅ 91 pairs analyzed |
| **Production tested** | 🔶 Not yet | ✅ Cursor, Claude Code |

---

## book-compiler's Unique Strengths

1. **Reasoning layer** (03_reasoning.md)
   - mattpocock has rules; book-compiler has *why* the rules exist
   - Users understand consequences, not just commands

2. **Structured JSON** (05_llm_instructions.json)
   - mattpocock: copy-paste markdown
   - book-compiler: machine-readable data + auto-generated rules

3. **Pass 5 Agent Rules**
   - Converts principles to decision/trigger/checklist format
   - Automatically traceable to source (no fabricated data)
   - Can be tested in real agents

4. **Multilingual**
   - Russian developers read books on Russian
   - LLMs get English JSON (universal)
   - mattpocock: English-only

---

## mattpocock's Unique Strengths

1. **Scale**
   - 14 books vs 11
   - Includes: DDD, Enterprise Patterns, Legacy Code, Data-Intensive Systems

2. **Production Proven**
   - Works in Cursor, Claude Code (proven)
   - book-compiler: untested in real tools

3. **Compatibility Matrix**
   - COMPATIBILITY.md: Which books work together
   - 78 complementary pairs, 2 conflicting, 11 overlapping
   - Prevents LLM from giving contradictory advice

4. **Simple Copy-Paste**
   - Open conversation, paste nano/mini/full file
   - Done. No JSON parsing required.

---

## What Should book-compiler Do?

### Right Now (Priority 1)
- [ ] Update README (says 6 books, but it's 11)
- [ ] Document Pass 5 in README (users don't know it exists)
- [ ] Create this summary file (done ✓)

**Time:** 30 minutes

### Next Session (Priority 2)
- [ ] Complete Pass 5 for remaining 10 books
- [ ] Test one 06_agent_rules.md in actual Claude/GPT conversation
- [ ] Fix any rule clarity issues

**Time:** 2-3 hours

### Later (Priority 3)
- [ ] Only if 15+ books: add compatibility matrix like mattpocock
- [ ] Otherwise: keep using tags + Library/concepts/

**Time:** Defer (not needed with 11 books)

---

## Should book-compiler Copy mattpocock?

**No.** Different strengths.

**Mattpocock's approach:** "Give me decision rules in 3 sizes, tested in production"

**book-compiler's approach:** "Give me full understanding (6 layers) + structured data for agents + traceability"

**Why book-compiler is better for:**
- Russian developers
- Educational deep dives
- LLM integration (JSON + Pass 5)
- Understanding *why* decisions matter

**Why mattpocock is better for:**
- Quick production use
- Proven in real tools
- Compatibility matrix
- Simplicity (just copy-paste)

---

## What Makes book-compiler Special?

### 1. No Fabricated Data
- Every rule in Pass 5 traces back to exact source (03_reasoning.md, 02_ideas.md)
- 06_agent_rules.traceability.md proves it
- mattpocock: rules are good but not explicitly traced

### 2. Automation-Ready
- Layer 05 (JSON) can auto-generate Pass 5 rules
- Could auto-generate nano/mini/full variants
- mattpocock: all manual, static files

### 3. Multilingual + LLM-Friendly
- Humans read layers 00-04 in their language
- LLMs/agents always get English JSON + Pass 5
- mattpocock: all English, no structure

---

## Conclusion

**book-compiler is good, but incomplete:**
- ✅ Better architecture (6 layers > 3 sizes)
- ✅ Better for deep learning (has reasoning + consequences)
- ✅ Better for LLMs (JSON + traceability)
- ✅ Better for Russian devs (multilingual)
- ❌ Not production-tested yet
- ❌ No compatibility matrix
- ❌ Scale smaller (11 vs 14)
- ❌ Pass 5 only done for 1 book

**Next step:** Complete Priority 1 & 2 above. Then you'll know if Pass 5 works.

---

**See also:** [AUDIT_REPORT_2026-08-09.md](AUDIT_REPORT_2026-08-09.md) (full analysis)
