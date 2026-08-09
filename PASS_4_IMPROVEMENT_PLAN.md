# Pass 4 Improvement Plan — Раскрыть reasoning для русских источников

**Дата начала:** 2026-08-09  
**Статус:** PLANNING (ждет одобрения перед выполнением)  
**Приоритет:** Priority 1 (критическое)

---

## 1. ПРОБЛЕМА (Specification)

### 1.1 ЧТО ИМЕННО НАРУШЕНО

**Pass 4 JSON (05_llm_instructions.json) для 4 русских источников содержит:**

```json
{
  "principle": "Code is written for people first",
  "statement": "Code is written for people first",
  "supporting_arguments": [],           ← ❌ ПУСТО
  "related_implications": [],           ← ❌ ПУСТО
  "related_questions": []               ← ❌ ПУСТО (иногда есть)
}
```

**Чего не хватает:**

| Поле | Должно содержать | Текущее состояние | Причина |
|------|---|---|---|
| `supporting_arguments` | 2-3 аргумента ИЗ `03_reasoning.md` | `[]` | Pass 4 не извлек reasoning для русских |
| `related_implications` | 2-3 применения ИЗ `04_consequences.md` | `[]` | Pass 4 не связал consequences |
| `related_questions` | 1-2 вопроса ИЗ `01_questions.md` | Иногда есть | Частично заполнено |

**Пример хорошего (clean-architecture):**
```json
{
  "principle": "Architecture is NOT Separate from Code",
  "statement": "...",
  "supporting_arguments": [
    {
      "claim": "Architects cannot avoid implementation details...",
      "evidence": "...",
      "source": "02_ideas.md"
    }
  ],
  "related_implications": [
    {
      "what_means": "You cannot hand off architecture to seniors...",
      "source": "04_consequences.md"
    }
  ]
}
```

**Пример плохого (martin-clean-code):**
```json
{
  "principle": "Code is written for people first",
  "statement": "Code is written for people first",
  "supporting_arguments": [],           ← ❌
  "related_implications": [],           ← ❌
}
```

---

### 1.2 КАКИЕ КНИГИ ЗАТРОНУТЫ

**4 книги с русскими источниками (00-04 в русском):**
1. `Books/ideal-work/` (Clean Coder)
2. `Books/pragmatic-programmer/`
3. `Books/code-fits-in-head/`
4. `Books/martin-clean-code/`

**Не затронуты (уже хорошо):**
- `Books/clean-architecture/` ✅ (English source)
- `Books/parallel-programming/` ✅ (English source)

---

### 1.3 ПОЧЕМУ ЭТО ПРОБЛЕМА

**Для LLM:**
- JSON используется как system prompt для code review
- Без supporting_arguments: LLM может не понять почему принцип важен
- Без related_implications: LLM не знает где применять
- **Результат:** Неполное руководство → плохие советы

**Для пользователя:**
- Нельзя быстро найти доказательства принципа
- Нельзя пасте JSON в Claude для полноценной консультации
- Два уровня качества JSON (clean-architecture vs остальные) = непредсказуемость

**Для проекта:**
- Нарушает TECHNICAL_REQUIREMENTS.md пункт 4: "All 6 books follow this pattern"
- Асимметричное качество ведет к техническому долгу

---

## 2. РЕШЕНИЕ (Procedure)

### 2.1 ЧТО ДЕЛАТЬ

Для каждого принципа в каждой русской книге:

**ШАГ 1: Найти supporting_arguments в 03_reasoning.md**
- Прочитать `03_reasoning.md` полностью
- Для каждого принципа найти аргументы, которые его поддерживают
- Вытащить 2-3 самых сильных аргумента

**ШАГ 2: Найти related_implications в 04_consequences.md**
- Прочитать `04_consequences.md` полностью
- Для каждого принципа найти где его применяют
- Вытащить 2-3 самых важных применения

**ШАГ 3: Связать с related_questions из 01_questions.md**
- Проверить есть ли вопросы которые этот принцип отвечает
- Добавить если есть

**ШАГ 4: Заполнить JSON поля**
- Перевести все на английский (как Pass 4 требует)
- Добавить source citations (какая строка из какого файла)

**ШАГ 5: Валидировать**
- Проверить что ничего не придумано
- Все traces back к оригинальному markdown

---

### 2.2 ПРОЦЕДУРА ДЛЯ КАЖДОЙ КНИГИ

**Для каждой из 4 русских книг:**

```
1. Открыть:
   - Books/{name}/02_ideas.md (список принципов)
   - Books/{name}/03_reasoning.md (аргументы)
   - Books/{name}/04_consequences.md (применения)
   - Books/{name}/01_questions.md (вопросы)
   - Books/{name}/05_llm_instructions.json (что нужно заполнить)

2. Для каждого принципа в 02_ideas.md:
   - Найти 2-3 аргумента в 03_reasoning.md
   - Найти 2-3 применения в 04_consequences.md
   - Найти связанные вопросы в 01_questions.md

3. Перевести на английский

4. Обновить 05_llm_instructions.json:
   - supporting_arguments: добавить объекты с claim, evidence, source
   - related_implications: добавить объекты с what_means, source
   - related_questions: добавить объекты с text, source (если не было)

5. Проверить:
   - Каждый argument имеет source_line
   - Каждая implication имеет source_line
   - Переводы верны (не придуманы)
   - Количество fields соответствует clean-architecture примеру
```

---

### 2.3 ОЖИДАЕМЫЙ РЕЗУЛЬТАТ

**ДО (текущее):**
```json
{
  "principle": "Code is written for people",
  "statement": "Code is written for people",
  "supporting_arguments": [],
  "related_implications": []
}
// 4 fields, 2 из них пусто, не информативно
```

**ПОСЛЕ (ожидаемое):**
```json
{
  "principle": "Code is written for people",
  "statement": "Code is written for people first and only then for machines.",
  "supporting_arguments": [
    {
      "claim": "Code is read 10x more than written; reader comfort is paramount",
      "evidence": "Studies show developers spend 90% of time reading vs 10% writing",
      "source": "03_reasoning.md: ARG-42, line 123-145"
    },
    {
      "claim": "Names should tell story; poor names force comments",
      "evidence": "When variable names are vague (data, x1), reader must infer intent",
      "source": "03_reasoning.md: ARG-43, line 150-165"
    }
  ],
  "related_implications": [
    {
      "what_means": "Every name is an opportunity to communicate",
      "when_applies": "When naming variables, functions, classes",
      "source": "04_consequences.md: IMPL-5, line 78-95"
    },
    {
      "what_means": "Refactoring for clarity is not optional; it's as important as making code work",
      "when_applies": "During code review and daily development",
      "source": "04_consequences.md: IMPL-7, line 102-118"
    }
  ],
  "related_questions": [
    {
      "id": "question_3",
      "text": "How do I write code that reads as prose?",
      "source": "01_questions.md: Question 3"
    }
  ]
}
// 5 fields, все заполнены, информативно, полезно LLM
```

---

## 3. КРИТЕРИИ УСПЕХА (Validation)

### 3.1 ДЛЯ КАЖДОЙ КНИГИ

**Quantitative:**
- [ ] `supporting_arguments` не пусто (≥2 на принцип в среднем)
- [ ] `related_implications` не пусто (≥2 на принцип в среднем)
- [ ] `related_questions` заполнено (если применимо)
- [ ] Каждый argument имеет source_line
- [ ] Каждая implication имеет source_line

**Qualitative:**
- [ ] Все supporting_arguments извлечены из 03_reasoning.md, не придуманы
- [ ] Все related_implications извлечены из 04_consequences.md, не придуманы
- [ ] Переводы на английский верны (сохраняют смысл)
- [ ] JSON валидируется по schema

**Coverage:**
- [ ] 100% принципов из 02_ideas.md имеют supporting_arguments
- [ ] 100% принципов из 02_ideas.md имеют related_implications
- [ ] ≥80% принципов имеют related_questions

---

### 3.2 ПОЛНЫЙ АУДИТ ПЕРЕД COMMIT

Перед тем как закоммитить, проверить:

```
VALIDATION CHECKLIST:

For Books/ideal-work/05_llm_instructions.json:
  ✓ Принципов в JSON: X (должно совпадать с 02_ideas.md)
  ✓ Принципов с supporting_arguments: X/Y (Y = всего принципов)
  ✓ Принципов с related_implications: X/Y
  ✓ JSON валидируется (можно pasте в Python json.loads)
  ✓ Выборочно проверены 3 принципа:
    - supporting_arguments точны? (текст совпадает с 03_reasoning.md)
    - related_implications точны? (текст совпадает с 04_consequences.md)
    - source_line указывает на правильную строку?

For Books/pragmatic-programmer/05_llm_instructions.json:
  [Те же чеки]

For Books/code-fits-in-head/05_llm_instructions.json:
  [Те же чеки]

For Books/martin-clean-code/05_llm_instructions.json:
  [Те же чеки]
  + ДОПОЛНИТЕЛЬНО:
    ✓ Metadata.title, author, publication заполнены
    ✓ Metadata.source_language = "Russian"
```

---

### 3.3 КОГДА ГОТОВО

**Готово** = 4 JSON файла которые:
1. Полностью заполнены (supporting_arguments + related_implications)
2. Валидны (JSON parse OK, schema OK)
3. Прошли выборочную аудит проверку (3+ принципа на каждую книгу)
4. Можно пасте в Claude как system prompt

---

## 4. КОМАНДА И ОТВЕТСТВЕННОСТЬ

| Кто | Что | Когда |
|-----|-----|-------|
| Claude (LLM) | Извлечение arguing, implications, переводы | Session 1 (текущая) |
| User (ты) | Одобрение plan, spot-checks, валидация | Session 1 (текущая) |
| Git | Commit с полным audit trail | После одобрения user |

---

## 5. TIMELINE

**Estimated работы:**
- ideal-work: 30-45 минут (45 принципов)
- pragmatic-programmer: 20-30 минут (35 принципов, меньше)
- code-fits-in-head: 25-35 минут (40 принципов)
- martin-clean-code: 35-50 минут (46 принципов)

**Итого:** ~2-3 часа LLM + 30 минут user validation

---

## 6. RISK & MITIGATION

| Риск | Вероятность | Значимость | Mitigation |
|------|---|---|---|
| Неправильный перевод | Medium | High | Spot-check 5-10 переводов |
| Неправильное извлечение arguments | Medium | High | Проверить source_line автоматически |
| Придуманные details | Low | High | Strict rule: only from source |
| JSON syntax error | Low | Medium | Validate с Python json.loads |

---

## 7. APPROVAL

**Status: AWAITING USER APPROVAL**

Перед началом выполнения:
- [ ] Ты согласен с этим планом?
- [ ] Ты согласен с процедурой (Step 1-5)?
- [ ] Ты согласен с критериями успеха?
- [ ] Начинаем работу?

---

**Документ:** PASS_4_IMPROVEMENT_PLAN.md  
**Версия:** 1.0  
**Сделано:** 2026-08-09  
**Для:** Полнота Pass 4 для русских источников  
**Цель:** Раскрыть reasoning и implications в JSON для LLM
