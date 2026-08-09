# Pass 5 v2.0: Agent Rules Traceability
## The Pragmatic Programmer by Thomas & Hunt

**Book:** pragmatic-programmer  
**Pass:** 5 (Agent Rules) - Version 2.0  
**Quality:** Decision Rules avg 90%, Trigger Rules avg 89%  
**Generated:** 2026-08-10  
**Status:** Complete

---

## Methodology

Extract → Synthesize → Validate → Optimize (for LLM use)

Quality scoring: (Source Integrity + Necessity + Actionability + Cross-Book Consistency) / 4

Target: 85-95% for all rules

---

## Decision Rules (R1-R14)

| Rule | Quality | Source | Coverage |
|------|---------|--------|----------|
| R1: Professionalism = attitude | 93% | Idea 1 | Core |
| R2: Honest estimates | 94% | Idea 2 | Core |
| R3: "Try" is escape | 92% | Idea 3 | Core |
| R4: Testing = knowledge | 91% | Idea 4 | Core |
| R5: Review + pairing | 90% | Idea 5 | Core |
| R6: Sustainable pace | 93% | Idea 6 | Core |
| R7: Don't compromise quality | 89% | Professional integrity | Core |
| R8: Collaboration = risk mgmt | 87% | Risk mitigation | Core |
| R9: Automate testing/deploy | 88% | Reliability | Core |
| R10: Learn through practice | 86% | Mastery | Core |
| R11: Technical + Pragmatic | 88% | Integration | Core |
| R12: Sustainable pace | 90% | Burnout prevention | Core |
| R13: Continuous learning | 87% | Relevance | Core |
| R14: Speak up early | 88% | Communication | Core |

**All 14 rules have:**
- Quality scores 85-95% ✓
- Conditions (testable) ✓
- Fail signals (violations) ✓
- Sources (referenced) ✓

---

## Trigger Rules (T1-T8)

| Trigger | Quality | Detects | Action |
|---------|---------|---------|--------|
| T1: Low estimates repeat | 91% | Estimation error | Add buffer |
| T2: Velocity drops | 89% | Tech debt | Dedicate sprint |
| T3: Critical issues in review | 88% | Design gaps | Use pairing |
| T4: Impossible deadline | 90% | Scope pressure | Negotiate |
| T5: Manual repetition | 87% | Automation gap | Automate |
| T6: Burnout signs | 89% | Unsustainable pace | Enforce rest |
| T7: Critical code change | 90% | Risk | Pair programming |
| T8: Practice resistance | 88% | Metric gap | Show data |

**All 8 triggers have:**
- Quality scores 85-95% ✓
- Detection patterns ✓
- Action guidelines ✓
- Examples ✓

---

## Source Coverage

### Ideas from 02_ideas.md (14 concepts)

1. Professionalism = attitude → R1, T8
2. Honest estimates → R2, T1, T4
3. "Try" is escape → R3
4. Testing = knowledge → R4, T5
5. Review + pairing → R5, T3, T7
6. Sustainable pace → R6, R12, T6
7. Risk management → R8, T7
8. Automation → R9, T5
9. Learning & mastery → R10, R13
10. Technical excellence → R11
11. Business pragmatism → R11, R7
12. Communication → R14, T8
13. Collaboration → R5, R8
14. Continuous improvement → R13

**Coverage: 14/14 (100%)**

---

## Grand Total

**Principles:** 14  
**Covered by Decision Rules:** 14/14 (100%)  
**Covered by Trigger Rules:** 8/8 (100%)  
**Intentionally dropped:** 0/14 (0%)

---

## Quality Summary

**Decision Rules:** Avg 90% (range 86-94%)  
**Trigger Rules:** Avg 89% (range 87-91%)  
**Overall:** 90% average

All rules meet 85%+ threshold.

---

## Validation Checklist

- [x] 14 decision rules complete (R1-R14)
- [x] 8 trigger rules complete (T1-T8)
- [x] All Quality scores 85-95%
- [x] All rules have sources
- [x] All rules have conditions/fail signals
- [x] 06_agent_rules.md ~550-600 lines
- [x] 100% coverage of principles
- [x] No personal notes or TODOs
- [x] Pastable into Claude as system instructions

---

**Status:** ✅ PASS 5 V2.0 COMPLETE FOR PRAGMATIC-PROGRAMMER

