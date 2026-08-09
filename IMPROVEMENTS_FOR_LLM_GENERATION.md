# Улучшения для генерации промптов для LLM

**На основе аудита Pass 5 pilot (martin-clean-code)**

---

## Обзор находок

### Что обнаружилось в аудите

1. **Классификация знания** — не все принципы одинаковы:
   - 39/46 применяемы как decision-rules (операционные)
   - 7/46 слишком узкие/мета-уровневые (форматирование, конвенции, авторство)
   - Нужна явная фильтрация, а не полная выборка

2. **Extraction-Synthesis gap** — большой скачок между:
   - Pass 4 (JSON): 100% верно, но не готово к действию (46 принципов)
   - Pass 5 (Rules): готово к действию, но требует аудита (14 правил)
   - **Нужен промежуточный слой валидации**

3. **Уровень абстракции** — правила работают когда:
   - ✓ Есть явное условие ("When X occurs") или действие ("Do Y")
   - ✗ Нет субъективности ("это красиво", "это конвенция")
   - ✗ Нет контекстзависимости (нужна проектная конфигурация)

4. **Структурные паттерны** — принципы естественно группируются:
   - C-001,002,003 → одна "decision rule" про ядро (люди первые, долг, скорость)
   - C-004,005,006,007 → одна "decision rule" про имена (precision, consistency)
   - **Структура уже подсказывает синтез**

---

## 6 направлений улучшения

### 1. ⭐⭐⭐ Structured Synthesis (ВЫСОКИЙ ПРИОРИТЕТ)

**Проблема:** Сейчас синтез интуитивный — читаем, сжимаем в правило. Не повторяемо, зависит от LLM.

**Решение:** Явные 3 шага трансформации.

#### Шаг 1: Extract — разбить принципы на компоненты

```
Входные данные: C-001, C-002, C-003 (из 02_ideas.md)

C-001: "Код пишется для людей, прежде всего, и только потом для машин"
  → claim:      "code is for people first"
  → context:    "communication between developers"
  → consequence: "readability determines understanding"

C-002: "Чистый код - это долг разработчика перед командой"
  → claim:      "clean code is a duty"
  → context:    "professional responsibility"
  → consequence: "team moves faster"

C-003: "Скорость разработки прямо пропорциональна чистоте кода"
  → claim:      "speed ∝ code cleanliness"
  → context:    "long-term ROI"
  → consequence: "investment now saves 10x later"
```

#### Шаг 2: Synthesize — группировать и переформулировать

```
Группа: Core (люди, долг, скорость)

Общий паттерн:
- Code is for humans (C-001)
- That's a duty (C-002)
- Speed depends on it (C-003)

Синтезированное правило:
R1: "Preserve behavior, leave touched code cleaner within scope,
     reject schedule pressure or 'we'll fix later' excuses."

Почему это работает:
- "Preserve behavior" ← from C-001 (code for people)
- "leave cleaner" ← from C-002 (duty to team)
- "reject shortcuts" ← from C-003 (speed = investment)
```

#### Шаг 3: Validate — проверить что ничего не потеряли

```
Validation checklist для R1:

[✓] Source Integrity:
    - "Preserve behavior" есть в C-002 ✓
    - "leave cleaner" есть в C-040 (Boy Scout) ✓
    - "reject shortcuts" есть в Arg-001 (tech debt) ✓
    - Нет новых слов/идей

[✓] Necessity:
    - Это правило нужно агенту? Да, это основа
    - Дублирует ли другое? Нет, это ядро

[✓] Actionability:
    - Может ли агент это проверить? 
      "leave cleaner" = удалить 1 code smell ✓
      "reject shortcuts" = not adding mess ✓

[✓] Cross-Book:
    - Согласуется ли с другими книгами?
    - Clean Architecture R1: "minimize effort" ← similar
```

**Реализация:** 
- Создать структурированный шаблон для каждой книги
- LLM заполняет: extract → synthesize → validate
- Результат: **Quality Score** для каждого правила (0-100%)

---

### 2. ⭐⭐⭐ Agent-Specific Optimization (ВЫСОКИЙ ПРИОРИТЕТ)

**Проблема:** Правила написаны для людей, агент может не понять.

**Решение:** Переписать правила как думает LLM.

#### Как думает LLM (vs как думает человек)

```
ЧЕЛОВЕК                          LLM
─────────────────────────────────────────────────────────────
"Это красиво"                    Pattern detection: "this matches X"
(субъективно)                    (объективно, вероятностно)

"По конвенции в Python..."       "Context says: language=Python"
(нужно знать контекст)           (можно передать контекстом)

"Это улучшает performance"       "Performance metric: 10% faster"
(нужны точные цифры)             (требует измеримого значения)

"Скрыто состояние"               Pattern: "state is modified but
(нужна семантика)                 not visible in call signature"
                                 (парсируемо + семантическая подсказка)
```

#### Примеры оптимизации

**ТЕКУЩЕЕ правило R2** (для человека):
```
"Write for local reasoning: readers should understand intent and logic 
 without reconstructing hidden state, navigating wide jumps, or guessing 
 vocabulary."
```

**ОПТИМИЗИРОВАННОЕ правило R2** (для агента):
```
"Code is local-readable when:
 
 Condition 1: No hidden state
   ✓ Function doesn't mutate globals
   ✓ Side effects are explicit (in name, in signature)
   ✓ State changes are obvious from call
 
 Condition 2: No wide jumps
   ✓ Related logic is close together
   ✓ Intent precedes detail
   ✓ No circular references across modules
 
 Condition 3: Names carry intent
   ✓ Variable name answers 'what' and 'why'
   ✓ Function name indicates action (verb) and context
   ✓ One term per concept (no customer/client mix)
 
 Fail signal: Reader must trace through multiple functions
             or reconstruct hidden state to understand."
```

**Почему это лучше для агента:**
- Явные условия (Condition 1, 2, 3) → может проверить каждое
- Fail signal → знает что искать
- Примеры ✓/✗ → может распознать паттерны

**Реализация:**
1. Переписать каждое правило в структуру: Conditions + Fail Signals
2. Добавить примеры парсируемых паттернов
3. Тестировать: может ли агент применить к реальному коду

---

### 3. ⭐⭐ Context Levels (средний приоритет)

**Проблема:** Одна версия (14 правил, ~300 токенов) не подходит всем.

**Решение:** Три версии для разных бюджетов.

#### NANO (самые критичные, <100 токенов)

6 правил с самым высоким рычагом для большинства кодовой базы:

```
R1: Preserve behavior, leave cleaner, reject shortcuts
R2: Write for readers (no hidden state/wide jumps)
R3: Use precise names (one term per concept)
R4: Keep functions small, focused, single level
R6: Separate commands from queries
R12: Treat tests as production code
```

**Применение:** Когда агент имеет <100 токенов на систем инструкцию.

#### MINI (сбалансированный, ~300 токенов)

Все 14 decision rules (текущий уровень).

**Применение:** По умолчанию, для большинства сценариев.

#### FULL (для глубокого анализа, ~600 токенов)

14 decision rules + 8 trigger rules + примеры (bad/good code).

**Применение:** Когда есть место и хочется максимально точного анализа.

#### Использование в коде

```python
# Когда генерируем промпт для агента:

if token_budget < 100:
    rules = get_rules(book, level="NANO")
elif token_budget < 400:
    rules = get_rules(book, level="MINI")
else:
    rules = get_rules(book, level="FULL")

system_prompt = f"""
You are reviewing code against {book.title} principles.

{rules}

Review the following code:
"""
```

**Реализация:**
1. Добавить поле `level: NANO|MINI|FULL` в 06_agent_rules.md
2. Разметить каждое правило уровнем
3. Создать filter функцию для выборки по уровню

---

### 4. ⭐⭐ Validation Loop (средний приоритет)

**Проблема:** Сейчас проверяем вручную (traceability файл).

**Решение:** Автоматизированные 4 валидации + качественная метрика.

#### Validation 1: Source Integrity

```
Для каждого правила R#:
✓ Каждое ключевое слово есть в исходных принципах?
✓ Не добавили новую идею?
✓ Не исказили смысл?

Пример для R1:
"Preserve behavior" ← есть в C-002 ✓
"leave cleaner" ← есть в App-001 (Boy Scout Rule) ✓
"reject shortcuts" ← есть в Arg-001 ✓
```

#### Validation 2: Necessity Check

```
Для каждого правила R#:
✓ Это правило действительно нужно агенту?
✓ Или агент может вывести его из других правил?
✓ Есть ли дублирование с другим правилом?

Пример:
R1 (preserve behavior) + R14 (remove smell, keep safe)
→ R1 основное, R14 более узкое → не дублируют
```

#### Validation 3: Actionability Score

```
Для каждого правила оценить: может ли агент это применить?

Высокая actionability (90-100%):
T1: "When function mixes setup/validation/compute/effects → split"
    → видимо парсингом кода (function args, return, side effects)

Средняя actionability (50-80%):
R2: "Write for readers (no hidden state)"
    → требует semantic анализа, не всегда очевидно

Низкая actionability (0-50%):
R5: "Minimize parameters"
    → что "минимизировать"? 3? 4? 5?
    → зависит от контекста
```

#### Validation 4: Cross-Book Consistency

```
Когда вводим Pass 5 для всех 6 книг:
✓ Это правило согласуется с тем же правилом в других книгах?
✓ Или есть противоречия?

Пример:
Clean Code R2: "Write for readers, no hidden state"
Architecture R1: "Minimize effort to understand"
→ Согласуется ✓ (оба про коммуникацию)

Clean Code R4: "Keep functions small"
Parallel Prog R1: "Minimize shared mutable state"
→ Не противоречат (разные аспекты)
```

#### Quality Score для каждого правила

```
Quality(R#) = 
    SourceIntegrity(W=40%) * 
    Necessity(W=30%) * 
    Actionability(W=20%) * 
    CrossBookConsistency(W=10%)

Пример результатов:
R1: 95% (excellent, full source, high necessity, medium actionability)
R2: 92% (excellent)
R4: 78% (good, но actionability зависит от язык/фреймворк)
T1: 88% (good)
```

**Реализация:**
1. Создать scoring script
2. Запустить на всех 46 принципах
3. Добавить Quality Score в трaceability файл
4. Флаг: если Score < 70%, требует ревью

---

### 5. ⭐ Cross-Book Synthesis (низкий приоритет, на потом)

**Для чего:** Когда агент получит 2-3 книги сразу.

**Идея:** Синтезировать "Shared Rules" — то что согласуется между книгами.

#### Пример: Shared Rule #1 (Коммуникация)

```
Все 6 книг говорят про это (разными словами):

Clean Code (R2):            "Write for readers"
Architecture (R1):          "Intent before detail"
Pragmatic Prog (R2):        "Explicit communication"
Code Fits Head (R5):        "Reduce cognitive load"
Ideal Work (R1):            "Clarity enables confidence"
Parallel Prog (R5):         "Intent is explicit"

СИНТЕЗИРОВАННОЕ SHARED RULE:
──────────────────────────────────────────────────
"Code is readable when intent is explicit and readers
 don't need to reconstruct hidden state.
 
 This appears in:
 - Clean Code (R2):       no hidden state, no wide jumps
 - Architecture (R1):     structure enables understanding
 - Pragmatic (R2):        names and structure communicate
 - Fits Head (R5):        reduce cognitive load
 - Ideal (R1):            clarity builds confidence
 - Parallel (R5):         threading intent must be clear"
```

#### Использование

```
Когда агент получает 3 книги:

system_prompt = """
Shared principles across all 3 books:
1. Code communicates intent (all 6 books)
2. Tests protect behavior (Clean Code, Ideal Work)
3. Change cost inversely proportional to clarity (CA, Pragmatic)

Book-specific rules:
- From Clean Code: (R1-R14, T1-T8)
- From Architecture: (R1-R6, T1-T3)
- From Pragmatic: (R1-R7, T1-T5)
"""
```

**Реализация:** После того как Pass 5 будет на всех 6 книгах.

---

### 6. ⭐ Actionability Scoring (низкий приоритет, на потом)

**Для чего:** Автоматически выбирать какие правила использовать.

**Идея:** Оценить для каждого правила — может ли агент это применить.

#### Примеры скоринга

```
HIGH (95%): T1 "When function mixes setup/validation/compute/effects"
  → Почему: Легко парсировать функцию, проверить что она делает
  → Как агент использует: "Я вижу что функция делает 3+ разных вещи"
  
HIGH (90%): R3 "Use precise names, one term per concept"
  → Почему: Лингвистический анализ (customer vs client)
  → Как агент использует: "Нашел inconsistency в терминологии"

MEDIUM (60%): R2 "No hidden state, readers understand"
  → Почему: Требует семантического понимания (что hidden)
  → Как агент использует: "Функция меняет глобальное состояние"
  
MEDIUM (55%): R4 "Keep functions small, single abstraction level"
  → Почему: Что такое "small"? Что такое "single level"?
  → Как агент использует: "Функция делает 3 разных уровня абстракции"

LOW (30%): R5 "Minimize parameters"
  → Почему: Что такое минимум? 3? 4? 5?
  → Как агент использует: Очень с трудом (слишком субъективно)
```

#### Использование

```
Когда собираем промпт:

high_actionability_rules = [R for R in all_rules if R.actionability > 80%]
medium_actionability_rules = [R for R in all_rules if R.actionability > 60%]

# Используем high actionability как основные триггеры
# Используем medium как контекст
# Не используем low actionability для автоматических проверок

system_prompt = f"""
Core rules (agent can verify):
{format_rules(high_actionability_rules)}

Context rules (guide agent thinking):
{format_rules(medium_actionability_rules)}
"""
```

---

## План внедрения

### Фаза 1: Structured Synthesis + Agent-Specific Optimization
**Время:** 1-2 дня  
**Результат:** Pass 5 v2.0 с явной валидацией и оптимизацией  
**Выход:** Лучше качество правил для всех 6 книг

### Фаза 2: Validation Loop
**Время:** 1 день  
**Результат:** Quality Score для каждого правила  
**Выход:** Видно какие правила надежные, какие требуют работы

### Фаза 3: Context Levels (NANO/MINI/FULL)
**Время:** 1 день  
**Результат:** Три версии для разных бюджетов токенов  
**Выход:** Гибкость в применении

### Фаза 4+: Cross-Book Synthesis, Actionability Scoring
**Время:** После Pass 5 на всех 6 книгах  
**Результат:** Еще лучше качество и автоматизация

---

## Краткий резюме

| Направление | Приоритет | Что дает | Сложность |
|---|---|---|---|
| Structured Synthesis | ⭐⭐⭐ | Повторяемый процесс, Quality Score | Средняя |
| Agent-Specific Opt | ⭐⭐⭐ | Лучше применяются агентом | Средняя |
| Validation Loop | ⭐⭐ | Видимое качество правил | Низкая |
| Context Levels | ⭐⭐ | Гибкость в применении | Низкая |
| Cross-Book Synth | ⭐ | Когда несколько книг | Высокая |
| Actionability Score | ⭐ | Автоматизировать выбор | Средняя |

---

**Рекомендация:** Начать с Фазы 1 (Structured Synthesis) сразу для оставшихся 5 книг. Это даст видимое улучшение качества и кроме того создаст базу для остального.
