# Pass 5 Traceability Completion Plan — Добавить 06_agent_rules.traceability.md

**Дата начала:** 2026-08-09  
**Статус:** PLANNING (ждет одобрения перед выполнением, после Pass 4)  
**Приоритет:** Priority 2 (высокое, зависит от Pass 4 завершения)  
**Зависит от:** PASS_4_IMPROVEMENT_PLAN.md (Pass 4 должен быть готов сначала)

---

## 1. ПРОБЛЕМА (Specification)

### 1.1 ЧТО ОТСУТСТВУЕТ

**Текущее состояние:**

| Книга | 06_agent_rules.md | 06_agent_rules.traceability.md | Статус |
|-------|---|---|---|
| martin-clean-code | ✅ Есть | ✅ Есть | 🟢 Complete |
| clean-architecture | ✅ Есть | ✅ Есть | 🟢 Complete |
| ideal-work | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| pragmatic-programmer | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| code-fits-in-head | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| parallel-programming | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| architect-elevator | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| concepts-programming-languages | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| domain-modeling-functional | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |
| philosophy-software-design | ✅ Есть | ❌ **ОТСУТСТВУЕТ** | 🟠 Incomplete |

**Недостающих файлов: 8**

---

### 1.2 ЧТО ДОЛЖЕН СОДЕРЖАТЬ 06_agent_rules.traceability.md

**Пример (из martin-clean-code/06_agent_rules.traceability.md):**

```markdown
# Pass 5 v2.0: Agent Rules Traceability Audit
## [Book Name] by [Author]

**Book:** {name}
**Pass:** 5 (Agent Rules) - Version 2.0
**Quality:** Decision Rules avg {X}%, Trigger Rules avg {Y}%
**Generated:** 2026-08-10
**Status:** Complete and Validated

---

## Methodology: Extract → Synthesize → Validate → Optimize

[Описание 4 фаз]

---

## Quality Scoring Formula

[Формула с 4 факторами: Source Integrity + Necessity + Actionability + Cross-Book Consistency]
Average = (sum) / 4
Target: 85-95%

---

## Decision Rules Mapping (R1-RN)

### R1: [Title]
**Quality Score: XX%** = (A + B + C + D) / 4

**Source Integrity: X%**
- Principle N (line X-Y): "[quote from source]"
- Implication N (line X-Y): "[quote from source]"

**Necessity: X%**
- [Appears in X layers]
- [Central to theme? Yes/No]

**Actionability: X%**
- [Can agent check this? What's testable?]

**Cross-Book Consistency: X%**
- [Consistent with book X, book Y?]

**Sources:**
- 02_ideas.md: PRINCIPLE N (line X)
- 03_reasoning.md: ARG-N (line X)
- 04_consequences.md: IMPL-N (line X)

**Citation:** "[Direct quote from source]"

---

## Trigger Rules Mapping (T1-TN)

[Аналогично Decision Rules]

---

## Coverage Review

### Principles Coverage

| Section | Principles | Covered by Rules | Intentionally Dropped | Coverage % |
|---------|---|---|---|---|
| Section 1 | X | R1, R2, T1 | principle_N (reason) | X% |
| Section 2 | X | R3, T2 | principle_M (reason) | X% |
| **TOTAL** | **N** | **N-K** | **K** | **X%** |

---

## Intentionally-Lost Principles Ledger

| Principle ID | Title | Reason for Dropping |
|---|---|---|
| P-001 | [title] | Too narrow; covered by R5 |
| P-002 | [title] | Format-specific (Java syntax); out of scope for logic-level rules |
| P-003 | [title] | Duplicate of R8 |

---

## Decision Gates (Quality Checks)

- [ ] Every rule (R#, T#) has source citation with line number
- [ ] Every principle from 02_ideas accounted for (covered or dropped with reason)
- [ ] Every argument from 03_reasoning cited in at least one rule
- [ ] Every implication from 04_consequences addressed in at least one rule
- [ ] Every question from 01_questions answered by related_questions in JSON or rule text
- [ ] Quality scores are honest (not padded)
- [ ] Coverage review is complete

---

## Final Sign-Off

**Traceability complete:** [YES/NO]
**All principles accounted for:** [YES/NO]
**All rules sourced:** [YES/NO]
**Ready for production:** [YES/NO]
```

---

### 1.3 ПОЧЕМУ ЭТО НУЖНО

**Для аудита:**
- Каждый rule R# должен быть traceable в исходный текст
- Без traceability: можем ошибочно использовать rules, которых нет в книге

**Для maintainability:**
- Когда обновляется книга, видно какие rules затронуты
- Когда добавляется принцип, видно где его разместить

**Для доверия:**
- Трассируемость = доказательство что rules не придуманы
- Пользователь может spot-check любой rule

**Для проекта:**
- Асимметрия (2 книги с traceability, 8 без) = непрофессионально
- Все 10 книг должны быть на одном уровне

---

## 2. РЕШЕНИЕ (Procedure)

### 2.1 ДЛЯ КАЖДОЙ КНИГИ БЕЗ TRACEABILITY

**Входные файлы:**
```
Books/{name}/
  ├─ 00_purpose.md
  ├─ 01_questions.md
  ├─ 02_ideas.md
  ├─ 03_reasoning.md
  ├─ 04_consequences.md
  ├─ 05_llm_instructions.json        (уже готов после Pass 4)
  ├─ 06_agent_rules.md               (уже готов)
  └─ 06_agent_rules.traceability.md   ← СОЗДАТЬ
```

**Процедура:**

### STEP 1: Read all layers (15 minutes)
- Прочитать 00-04 и 06_agent_rules.md
- Понять какие rules там есть (R1-RN, T1-TN)

### STEP 2: Build Decision Rules Mapping (30 minutes)
Для каждого R#:
1. Найти в 06_agent_rules.md What it means
2. Найти в 02_ideas.md какой принцип это связано
3. Найти в 03_reasoning.md какие аргументы его поддерживают
4. Найти в 04_consequences.md какие применения
5. Вычислить Quality Score:
   - Source Integrity: 100% если все в source, 0% если придумано
   - Necessity: 100% если центральное, 50% если contextual
   - Actionability: 100% если testable, 0% если абстрактно
   - Cross-Book Consistency: 100% если matches other books, 0% если unique
6. Average = (A + B + C + D) / 4

### STEP 3: Build Trigger Rules Mapping (20 minutes)
То же самое для T#

### STEP 4: Coverage Review (20 minutes)
- Прочитать 02_ideas.md полностью
- Для каждого принципа:
  - Если covered by R# или T#: отметить какой
  - Если intentionally dropped: объяснить почему
- Посчитать % coverage

### STEP 5: Intentionally-Lost Ledger (10 minutes)
- Список принципов которые не вошли в rules
- Для каждого: объяснение почему
- Примеры:
  - "Too narrow: specific Java syntax"
  - "Duplicate of R5: already covered"
  - "Meta-level: about book structure, not content"
  - "Format-specific: file organization conventions"

### STEP 6: Write traceability.md (10 minutes)
- Заполнить template
- Вставить все данные из STEP 2-5

### STEP 7: Validate (10 minutes)
- Проверить Decision Gates
- Spot-check 3-4 rules: их quality scores fair?
- Проверить source_line: указывают правильно?

---

### 2.2 ПОРЯДОК ВЫПОЛНЕНИЯ (8 книг)

**Batch 1: Парные работы с martin-clean-code как reference**
1. ideal-work (аналогично Clean Coder структуре)
2. pragmatic-programmer (структура похожа)

**Batch 2: Уникальные структуры**
3. code-fits-in-head (другая структура, но знакомая)
4. parallel-programming (техническая, но ясная)

**Batch 3: Новые книги**
5. architect-elevator
6. concepts-programming-languages
7. domain-modeling-functional
8. philosophy-software-design

**Timeline per book:** 2-3 часа (LLM-driven)

---

## 3. КРИТЕРИИ УСПЕХА (Validation)

### 3.1 ДЛЯ КАЖДОГО FILE

**Структура:**
- [ ] Header с metadata (Book, Pass, Quality, Generated, Status)
- [ ] Methodology section
- [ ] Quality Scoring Formula
- [ ] Decision Rules Mapping (R1-RN)
- [ ] Trigger Rules Mapping (T1-TN)
- [ ] Coverage Review (таблица)
- [ ] Intentionally-Lost Ledger
- [ ] Decision Gates checklist

**Качество:**
- [ ] Каждый R# имеет Quality Score 85-95%
- [ ] Каждый T# имеет Quality Score 85-95%
- [ ] Каждый score имеет 4-factor breakdown
- [ ] Каждый rule имеет source citations с line numbers
- [ ] Каждый principle из 02_ideas учтен (covered или dropped)
- [ ] Ledger объясняет все intentionally-dropped

**Аудит:**
- [ ] Выборочно проверены 5 rules:
  - Quality score соответствует source?
  - line numbers указывают правильно?
  - coverage claims верны?
- [ ] Decision Gates все пройдены (или явно marked как No с обоснованием)

---

### 3.2 ПОЛНЫЙ AUDIT ПЕРЕД COMMIT

```
TRACEABILITY VALIDATION CHECKLIST:

For each of 8 books (ideal-work, pragmatic, code-fits, parallel, architect, concepts, domain-modeling, philosophy):

  ✓ File exists: 06_agent_rules.traceability.md
  ✓ File has all sections (header, methodology, formula, mappings, coverage, ledger, gates)
  ✓ Decision Rules count matches 06_agent_rules.md (R1-RN)
  ✓ Trigger Rules count matches 06_agent_rules.md (T1-TN)
  ✓ ALL rules have Quality Scores (85-95% range)
  ✓ Spot-check 3 rules:
    - [Rule N]: quality score fair? (check 4-factor breakdown)
    - [Rule M]: source citations correct? (verify line numbers)
    - [Rule K]: principle connected? (is it in 02_ideas?)
  ✓ Coverage Review table filled correctly
    - Total principles from 02_ideas: X
    - Covered by rules: Y (should be high %)
    - Intentionally dropped: Z (with reasons)
  ✓ Intentionally-Lost Ledger complete
    - Every dropped principle listed
    - Every drop has explicit reason
  ✓ Decision Gates: [YES/NO for each]
  ✓ markdown validates (no syntax errors)
```

---

## 4. DEPENDENCY & SEQUENCING

**Pass 4 → Pass 5 Traceability:**

```
Step 1: Pass 4 Improvement COMPLETE
        ↓
Step 2: Verify Pass 4 quality
        (ideal-work, pragmatic, code-fits, martin-clean-code JSON valid)
        ↓
Step 3: Pass 5 Traceability for 8 books
        (reference the improved Pass 4 data)
        ↓
Step 4: Validate both
        ↓
Step 5: Commit both together
```

**⚠️ ВАЖНО:** Pass 5 Traceability зависит от Pass 4 качества. Если Pass 4 плохой → трассируемость будет плохой.

---

## 5. TIMELINE

**После Pass 4 завершения:**

**Batch 1 (ideal-work + pragmatic):** ~5-6 часов
**Batch 2 (code-fits + parallel):** ~5-6 часов  
**Batch 3 (4 новые книги):** ~8-10 часов

**Итого:** ~18-22 часа LLM + 2-3 часа user validation

**Реалистичный timeline:** 2-3 сессии

---

## 6. RISK & MITIGATION

| Риск | Вероятность | Значимость | Mitigation |
|------|---|---|---|
| Quality scores завышены | Medium | High | Strict 4-factor check |
| Source citations неправильны | Low-Med | High | Verify line numbers in spot-checks |
| Coverage % неточны | Low | Medium | Recount principles manually |
| Intentionally-lost ledger неполна | Medium | High | Exhaustive review 02_ideas |
| Files не коммитятся | Low | High | Test git before commit |

---

## 7. APPROVAL

**Status: AWAITING PASS 4 COMPLETION THEN USER APPROVAL**

Последовательность:
1. ✅ Ты одобрил PASS_4_IMPROVEMENT_PLAN.md
2. ⏳ Pass 4 выполняется и завершается
3. ⏳ Ты валидируешь Pass 4
4. ⏳ Ты одобряешь PASS_5_TRACEABILITY_COMPLETION_PLAN.md
5. ⏳ Pass 5 Traceability выполняется

---

**Документ:** PASS_5_TRACEABILITY_COMPLETION_PLAN.md  
**Версия:** 1.0  
**Сделано:** 2026-08-09  
**Для:** Полнота audit trail для всех 10 книг  
**Цель:** Трассируемость каждого rule в исходный текст
