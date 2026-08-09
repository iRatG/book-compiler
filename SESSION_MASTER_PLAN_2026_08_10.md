# Session Master Plan: Pass 4 & Pass 5 Quality Completion

**Дата:** 2026-08-09 (планирование), 2026-08-10+ (выполнение)  
**Сессия:** Session 10  
**Статус:** 📋 PLANNING (ждет одобрения от user)

---

## ЗАЧЕМ МЫ ЭТО ДЕЛАЕМ

### Проблема (обнаружена на аудит-проверке)

Вы правильно заметили: **методология из martin-clean-code была переиспользована** для 10 книг через Pass 5 (06_agent_rules.md). Это хорошо!

**НО открыта асимметричность в Pass 4 (JSON layer 05):**

**Для англоязычных источников (clean-architecture, parallel-programming):**
- ✅ JSON полный: supporting_arguments + related_implications + related_questions
- ✅ LLM может использовать как system prompt
- ✅ Reasoning понятен

**Для русскоязычных источников (ideal-work, pragmatic, code-fits, martin-clean-code):**
- ❌ JSON минимален: только названия принципов
- ❌ supporting_arguments пусто
- ❌ related_implications пусто
- ❌ Reasoning не понятен LLM
- ❌ Нельзя пасте в Claude для полноценной консультации

**Плюс: только 2 из 10 книг имеют 06_agent_rules.traceability.md** (остальные 8 без аудит-следа).

### Последствия если НЕ ИСПРАВИТЬ

1. **Техдолг растет:** Асимметричное качество → трудная поддержка
2. **LLM неполное:** JSON для русских источников неполный → плохие советы
3. **Следующая сессия:** Кто-то спросит "почему русские JSON не заполнены?" и нужно будет переделывать
4. **Масштабируемость:** Когда добавите новые русские книги, повторится та же проблема

### Цель этой сессии

✅ **Завершить Pass 4:** Раскрыть reasoning (supporting_arguments + related_implications) для 4 русских книг  
✅ **Завершить Pass 5 Traceability:** Добавить аудит-след для 8 книг (не имеющих traceability.md)

**Результат:** Все 10 книг на одном уровне качества. Symmetric system.

---

## ПЛАН ДЕЙСТВИЙ (TWO-STEP)

### STEP 1: Pass 4 Improvement (Priority 1)

**Зачем:** Раскрыть reasoning в JSON для LLM  
**Сколько:** 4 русских книги (ideal-work, pragmatic, code-fits, martin-clean-code)  
**Результат:** JSON будут содержать supporting_arguments + related_implications (как clean-architecture)

**Документ:** `PASS_4_IMPROVEMENT_PLAN.md` ← Подробная спецификация

**Что улучшится:**

БЫЛО:
```json
{
  "principle": "Code is written for people",
  "statement": "Code is written for people",
  "supporting_arguments": [],  ← ПУСТО
  "related_implications": []   ← ПУСТО
}
```

СТАНЕТ:
```json
{
  "principle": "Code is written for people",
  "statement": "Code is written for people first and only then for machines",
  "supporting_arguments": [
    {"claim": "Code is read 10x more than written", "source": "03_reasoning.md: line 123"},
    {"claim": "Names should tell story", "source": "03_reasoning.md: line 150"}
  ],
  "related_implications": [
    {"what_means": "Every name is opportunity to communicate", "source": "04_consequences.md: line 78"},
    {"what_means": "Refactoring for clarity is mandatory", "source": "04_consequences.md: line 102"}
  ]
}
```

**Timeline:** 2-3 часа

---

### STEP 2: Pass 5 Traceability Completion (Priority 2)

**Зачем:** Добавить аудит-след для всех 10 книг  
**Сколько:** 8 книг (все кроме martin-clean-code и clean-architecture)  
**Результат:** Каждая книга имеет 06_agent_rules.traceability.md с полным audit trail

**Документ:** `PASS_5_TRACEABILITY_COMPLETION_PLAN.md` ← Подробная спецификация

**Что добавится:**

Каждая книга получит файл который объясняет:
- Какой rule (R1-RN) откуда взялся
- Какой principle он покрывает
- Какие аргументы его поддерживают
- Quality score для каждого rule (85-95%)
- Какие принципы intentionally не вошли в rules (и почему)
- Coverage review: сколько % принципов покрыто

**Timeline:** ~18-22 часа (после завершения Pass 4)

---

## CRITICAL: DEPENDENCY ORDER

```
                    ┌─────────────────────┐
                    │   USER APPROVES     │
                    │   THIS MASTER PLAN  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ PASS 4 IMPROVEMENT  │
                    │ (4 books, 2-3 hrs)  │
                    │ - Extract arguments │
                    │ - Extract implies   │
                    │ - Translate to EN   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ PASS 4 VALIDATION   │
                    │ (user spot-check)   │
                    │ - JSON valid?       │
                    │ - Coverage %?       │
                    │ - Translations OK?  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ PASS 5 TRACEABILITY │
                    │ (8 books, 18-22 hrs)│
                    │ - Map rules → source│
                    │ - Quality scores    │
                    │ - Coverage review   │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ FULL VALIDATION     │
                    │ (user spot-check)   │
                    │ - All 10 books OK?  │
                    │ - JSON + Trace OK?  │
                    └──────────┬──────────┘
                               │
                    ┌──────────▼──────────┐
                    │ COMMIT & PUSH       │
                    │ - 4 Pass 4 commits  │
                    │ - 8 Pass 5 commits  │
                    │ (or 1 big commit)   │
                    └─────────────────────┘
```

**⚠️ ВАЖНО:** Pass 4 MUST завершиться перед Pass 5, потому что трассируемость опирается на качество Pass 4.

---

## КАКИЕ ФАЙЛЫ ИЗМЕНЯТСЯ

### Pass 4 Improvement

**FILES MODIFIED:**

1. `Books/ideal-work/05_llm_instructions.json`
   - Добавить supporting_arguments для всех принципов
   - Добавить related_implications для всех принципов
   
2. `Books/pragmatic-programmer/05_llm_instructions.json`
   - Добавить supporting_arguments
   - Добавить related_implications

3. `Books/code-fits-in-head/05_llm_instructions.json`
   - Добавить supporting_arguments
   - Добавить related_implications

4. `Books/martin-clean-code/05_llm_instructions.json`
   - Добавить supporting_arguments
   - Добавить related_implications
   - Заполнить metadata.title, author, publication

---

### Pass 5 Traceability Completion

**FILES CREATED (8 new):**

1. `Books/ideal-work/06_agent_rules.traceability.md` ✨ NEW
2. `Books/pragmatic-programmer/06_agent_rules.traceability.md` ✨ NEW
3. `Books/code-fits-in-head/06_agent_rules.traceability.md` ✨ NEW
4. `Books/parallel-programming/06_agent_rules.traceability.md` ✨ NEW
5. `Books/architect-elevator/06_agent_rules.traceability.md` ✨ NEW
6. `Books/concepts-programming-languages/06_agent_rules.traceability.md` ✨ NEW
7. `Books/domain-modeling-functional/06_agent_rules.traceability.md` ✨ NEW
8. `Books/philosophy-software-design/06_agent_rules.traceability.md` ✨ NEW

---

## ДОКУМЕНТЫ КОТОРЫЕ УЖЕ ГОТОВЫ

**Используй эти как reference:**

1. **PASS_4_IMPROVEMENT_PLAN.md** — Полная спецификация что, как, почему для Step 1
2. **PASS_5_TRACEABILITY_COMPLETION_PLAN.md** — Полная спецификация что, как, почему для Step 2
3. **Books/martin-clean-code/06_agent_rules.traceability.md** — Пример хорошего трассируемости
4. **Books/clean-architecture/06_agent_rules.traceability.md** — Второй пример
5. **Books/ideal-work/06_agent_rules.md** — Пример хорошего rules file (структура правильная)

---

## APPROVAL CHECKPOINTS

### Checkpoint 1: Master Plan Approval

**ТЫ должен одобрить:**
- [ ] Я согласен что есть асимметричность в Pass 4 (русские JSON неполные)
- [ ] Я согласен что нужно раскрыть supporting_arguments и related_implications
- [ ] Я согласен с priority: сначала Pass 4, потом Pass 5 Traceability
- [ ] Я согласен с документами PASS_4_IMPROVEMENT_PLAN.md и PASS_5_TRACEABILITY_COMPLETION_PLAN.md

**Если одобрил → продолжаем.**

---

### Checkpoint 2: Pass 4 Execution & Validation

**После выполнения:**
- [ ] 4 JSON файла (ideal-work, pragmatic, code-fits, martin-clean-code) заполнены
- [ ] supporting_arguments не пусты (≥2 на принцип в среднем)
- [ ] related_implications не пусты (≥2 на принцип в среднем)
- [ ] Переводы на английский верны (spot-checked 5-10 примеров)
- [ ] Metadata заполнены полностью
- [ ] JSON валидируются (python json.loads OK)

**Если все OK → продолжаем на Pass 5.**

---

### Checkpoint 3: Pass 5 Validation & Commit

**После выполнения:**
- [ ] 8 traceability файлов созданы (для книг без них)
- [ ] Каждый file имеет правильную структуру (sections, tables, ledger)
- [ ] Quality scores честные (85-95%, не завышены)
- [ ] Coverage review заполнена
- [ ] Intentionally-lost ledger объясняет все dropped principles
- [ ] Spot-checked 3+ rules на каждом file

**Если все OK → готово коммитить.**

---

## WHAT YOU NEED TO DO NOW

### ✅ ACTION 1: Read & Approve (5 minutes)

1. Прочитай PASS_4_IMPROVEMENT_PLAN.md (sections 1-3)
2. Прочитай PASS_5_TRACEABILITY_COMPLETION_PLAN.md (sections 1-3)
3. Спроси вопросы если что неясно
4. Одобри или предложи изменения

### ✅ ACTION 2: Spot-check References (10 minutes)

Посмотри примеры:
- `Books/martin-clean-code/06_agent_rules.traceability.md` (как должно быть)
- `Books/ideal-work/06_agent_rules.md` (структура правильная)

### ✅ ACTION 3: Approve Master Plan (1 minute)

Скажи "ОК, начинаем" или "Нужны изменения в планах"

---

## EXPECTED OUTCOMES

### After Pass 4 Complete

**Quality metrics:**
- ✅ All 4 JSON files have supporting_arguments (0% → 100%)
- ✅ All 4 JSON files have related_implications (0% → 100%)
- ✅ Coverage: 95%+ of principles have arguments + implications
- ✅ Language: 100% English (translated from Russian source)

**For LLM:**
- ✅ Can paste JSON into Claude
- ✅ Claude understands reasoning behind principles
- ✅ Claude can apply principles to code review

---

### After Pass 5 Complete

**Quality metrics:**
- ✅ All 10 books have 06_agent_rules.traceability.md
- ✅ All 10 books have Quality scores (85-95%)
- ✅ All 10 books have coverage review
- ✅ All 10 books have intentionally-lost ledger

**For audit:**
- ✅ Can verify any rule by checking source citations
- ✅ Can see which principles covered, which intentionally skipped
- ✅ Professional-grade documentation

---

### System Becomes Symmetric

**Before (current):**
```
Books structure asymmetric:
- 2 books with full Pass 4 + Pass 5 traceability ✅
- 8 books with partial Pass 4 or missing traceability ❌
```

**After (after this session):**
```
Books structure symmetric:
- 10 books with complete Pass 4 ✅
- 10 books with complete Pass 5 traceability ✅
- Consistent quality across all
- Professional audit trail
```

---

## TIMELINE ESTIMATE

| Phase | Duration | Notes |
|-------|----------|-------|
| Plan Approval | 15 min | Current |
| Pass 4 Execution | 2-3 hrs | LLM-driven |
| Pass 4 Validation | 30 min | User spot-check |
| Pass 5 Execution | 18-22 hrs | Multiple sessions |
| Pass 5 Validation | 1-2 hrs | User spot-check |
| Git Commit & Push | 15 min | Final |
| **TOTAL** | **~24-26 hours** | **Realistic 3-4 sessions** |

---

## NEXT STEP: WAIT FOR YOUR APPROVAL

**Status: ⏸️ AWAITING USER APPROVAL**

Я готов выполнять, но сначала нужно твое:
- ✅ Одобрение этого Master Plan
- ✅ Одобрение деталей в PASS_4_IMPROVEMENT_PLAN.md
- ✅ Одобрение деталей в PASS_5_TRACEABILITY_COMPLETION_PLAN.md

Если все OK → начинаем Step 1 (Pass 4 Improvement) сразу.

---

**Master Plan:** SESSION_MASTER_PLAN_2026_08_10.md  
**Version:** 1.0  
**Created:** 2026-08-09  
**Status:** 📋 PLANNING  
**Author:** Claude Haiku 4.5 (planning), User (approval)

---

## QUESTIONS FOR USER

Перед тем как одобрить, обсудим:

1. **Согласен ли ты что Pass 4 неполная для русских источников?**
2. **Согласен ли ты что это нужно исправить перед добавлением новых книг?**
3. **Хочешь ли ты что-то изменить в процедурах (PASS_4_* или PASS_5_*)?**
4. **Есть ли другие приоритеты которые нужно учесть перед началом?**
