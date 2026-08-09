# 📖 Как использовать book-compiler для новых книг

**Версия:** 4.0  
**Дата:** 2026-08-09  
**Статус:** Полная инструкция + автоматизация

---

## ⚡ Быстрый старт (30 секунд)

Добавить новую книгу:

```bash
# 1. Положи исходный материал
mkdir source/my-new-book/
# Скопируй:
#   - PDF
#   - Ссылку на книгу
#   - Любые заметки

# 2. Запусти навык
# В Claude: /book-compiler my-new-book

# 3. Смотри результат
ls Books/my-new-book/
# 00_purpose.md, 01_questions.md, ..., 06_agent_rules.md готовы
```

**Это всё.** Система сама:
- Разберёт книгу (Pass 1-3)
- Сгенерирует JSON (Pass 4)
- Создаст Agent Rules (Pass 5)
- Логирует всё в `/reports/`

---

## 📋 Полная инструкция

### Шаг 1: Подготовить исходный материал

```
source/
├── my-first-book/
│   ├── README.md          ← Что это за книга?
│   ├── book.pdf           ← Исходный материал (опционально)
│   └── notes.txt          ← Твои заметки (опционально)
└── my-second-book/
    ├── README.md
    └── book.pdf
```

**Что писать в README.md:**
```markdown
# Название Книги

**Автор:** Имя Автора  
**Год:** 2024  
**Язык:** Русский / English  
**Источник:** [ссылка]

## Краткое описание

1-2 предложения о чём эта книга

## Тип контента

- [ ] Техническая книга по программированию
- [ ] Книга о проектировании архитектуры
- [ ] Книга о процессах разработки
- [ ] Другое: ___________

## Ключевые области

Например: #архитектура, #качество-кода, #тестирование
```

**Пример:** см. `source/example-books/` (будет создано)

---

### Шаг 2: Запустить book-compiler навык

#### Вариант A: Через Claude Code (рекомендуется)

```
Claude Code: /book-compiler дизайн-системы

Система:
1. Прочитает source/дизайн-системы/README.md
2. Спросит уточнения (если нужны)
3. Создаст Books/дизайн-системы/ со всеми 6 слоями
4. Логирует в reports/дизайн-системы-PASS-1-5.md
```

#### Вариант B: Параметры запуска

```
/book-compiler книга-название --language=russian --domain=architecture
```

**Параметры:**
- `--language=russian|english` — язык слоёв 00-04 (по умолчанию: English)
- `--domain=architecture|quality|process|patterns` — помогает классифицировать

#### Вариант C: С явным путём

```
/book-compiler path:source/my-book/
```

---

### Шаг 3: Навык делает всё автоматически

**Pass 1: Purpose Layer (00_purpose.md)**
- Навык читает исходный материал
- Определяет проблему, цель, аудиторию
- Пишет `00_purpose.md` (500-800 слов)
- Логирует: `Книга X → Pass 1 ✅ 12 вопросов выявлено`

**Pass 2: Questions Layer (01_questions.md)**
- Извлекает 12-15 центральных вопросов
- Группирует по темам
- Пишет `01_questions.md`
- Логирует: `Pass 2 ✅ 15 вопросов, 3 темы`

**Pass 3: Ideas Layer (02_ideas.md)**
- Определяет 12-15 ключевых принципов
- Теги для Library/
- Пишет `02_ideas.md`
- Логирует: `Pass 3 ✅ 15 принципов, 8 тегов`

**Pass 3b: Reasoning (03_reasoning.md)**
- 8-10 аргументов с доказательствами
- Эмпирические данные, примеры
- Пишет `03_reasoning.md`
- Логирует: `Pass 3b ✅ 10 аргументов`

**Pass 3c: Consequences (04_consequences.md)**
- 12-14 практических применений
- Как использовать на практике
- Пишет `04_consequences.md`
- Логирует: `Pass 3c ✅ 14 следствий`

**Pass 4: JSON Layer (05_llm_instructions.json)**
- Читает слои 00-04
- Генерирует структурированный JSON
- Таблица: принцип, теги, аргументы, примеры
- Пишет `05_llm_instructions.json` (1000-1500 строк)
- Логирует: `Pass 4 ✅ JSON 1247 строк, 15 принципов, 42 тега`

**Pass 5: Agent Rules (06_agent_rules.md + трассировка)**
- Преобразует принципы → Decision Rules
- Извлекает Trigger Rules ("When X, then Y")
- Создаёт Checklist
- Пишет `06_agent_rules.md` (650+ строк)
- Пишет `06_agent_rules.traceability.md` (400+ строк)
- Логирует: `Pass 5 ✅ 14 Decision rules, 8 Trigger rules, 100% traceability`

**Итог: Полная книга готова за один запуск**

```
Books/моя-новая-книга/
├── 00_purpose.md
├── 01_questions.md
├── 02_ideas.md
├── 03_reasoning.md
├── 04_consequences.md
├── 05_llm_instructions.json
└── 06_agent_rules.md
└── 06_agent_rules.traceability.md
```

---

## 📁 Структура папок

### Правильно

```
book-compiler/
├── Books/                      ← Готовые книги (в git)
│   ├── clean-architecture/
│   ├── ideal-work/
│   ├── my-first-book/          ← Новая (в git после готовности)
│   └── my-second-book/         ← Новая (в git после готовности)
│
├── source/                     ← Исходные материалы (НЕ в git)
│   ├── my-first-book/
│   │   ├── README.md
│   │   └── book.pdf
│   └── my-second-book/
│       ├── README.md
│       └── book.pdf
│
├── reports/                    ← Логи и отчёты (НЕ в git)
│   ├── my-first-book-PASS-1-5.log
│   ├── my-first-book-PASS-1-5.md
│   ├── my-second-book-PASS-1-5.log
│   └── [другие отчёты]
│
├── reference/                  ← Спецификации (в git)
│   ├── pass-4-json-generation.md
│   ├── pass-5-agent-rules-generation.md
│   └── [другие docs]
│
├── .gitignore                  ← source/ и reports/ исключены
├── README.md                   ← Основная документация
└── SYSTEM_USAGE.md             ← Эта инструкция
```

### .gitignore (уже создан)

```
source/       ← Исходные материалы остаются только локально
reports/      ← Логи и отчёты не коммитятся
```

---

## 🔍 Мониторинг: Логи и отчёты

### Как читать логи

После запуска `/book-compiler книга-название`:

**Лог в реальном времени:**
```
reports/дизайн-системы-PASS-1-5.log

[2026-08-10 14:23:45] Pass 1: Reading source/дизайн-системы/README.md
[2026-08-10 14:23:50] Pass 1: Extracted problem, goal, audience
[2026-08-10 14:24:15] Pass 1 ✅ 00_purpose.md written (642 words)
[2026-08-10 14:24:16] Pass 2: Extracting central questions...
[2026-08-10 14:24:45] Pass 2 ✅ 01_questions.md written (15 questions)
[2026-08-10 14:25:10] Pass 3: Extracting core principles...
[2026-08-10 14:26:30] Pass 3 ✅ 02_ideas.md written (15 principles, 9 tags)
[2026-08-10 14:26:31] Pass 3b: Extracting reasoning...
[2026-08-10 14:27:45] Pass 3b ✅ 03_reasoning.md written (10 arguments)
[2026-08-10 14:27:46] Pass 3c: Extracting consequences...
[2026-08-10 14:28:50] Pass 3c ✅ 04_consequences.md written (14 implications)
[2026-08-10 14:28:51] Pass 4: Generating JSON...
[2026-08-10 14:30:20] Pass 4 ✅ 05_llm_instructions.json written (1247 lines)
[2026-08-10 14:30:21] Pass 5: Generating Agent Rules...
[2026-08-10 14:32:15] Pass 5 ✅ 06_agent_rules.md written (652 lines, 14 Decision rules)
[2026-08-10 14:32:16] Pass 5 ✅ 06_agent_rules.traceability.md written (418 lines)
[2026-08-10 14:32:17] ✅ COMPLETE: книга готова
```

**Итоговый отчёт:**
```
reports/дизайн-системы-PASS-1-5.md

# Pass 1-5 Report: Дизайн систем

## Summary
- Book: Дизайн систем
- Source language: Русский
- Processing time: 9 минут 32 секунды
- Status: ✅ COMPLETE

## Pass 1: Purpose
✅ 00_purpose.md (642 words)
- Problem identified: Стихийное развитие систем без принципов
- Goal: Методология проектирования
- Audience: Архитекторы, lead разработчики

## Pass 2: Questions
✅ 01_questions.md (15 questions)
- Topic 1: Основы проектирования (5 questions)
- Topic 2: Масштабируемость (4 questions)
- Topic 3: Надёжность (6 questions)

## Pass 3: Ideas
✅ 02_ideas.md (15 principles)
- Принцип 1: Разделение ответственности (#responsibility-division)
- Принцип 2: Масштабируемость как архитектурное решение (#scalability)
- ...

## Pass 3b: Reasoning
✅ 03_reasoning.md (10 arguments)
- Arg 1: Эмпирические данные Google (3 case studies)
- Arg 2: Математическое доказательство
- ...

## Pass 3c: Consequences
✅ 04_consequences.md (14 implications)
- Impl 1: Как применить в своем проекте
- Impl 2: Типичные ошибки
- ...

## Pass 4: JSON
✅ 05_llm_instructions.json (1247 lines)
- Structured: 15 principles × 8 fields each
- Tags: 42 unique tags
- Quality: 91% (average across principles)

## Pass 5: Agent Rules
✅ 06_agent_rules.md (652 lines)
- Decision rules: 14
- Trigger rules: 8
- Final checklist: 7 items
- Average Quality Score: 90%

✅ 06_agent_rules.traceability.md (418 lines)
- Every rule (R1-R14, T1-T8) traced to source
- Coverage: 15/15 principles (100%)
- Intentionally lost: 0

## Quality Metrics
| Pass | Component | Status | Quality |
|------|-----------|--------|---------|
| 1 | 00_purpose | ✅ | 95% |
| 2 | 01_questions | ✅ | 92% |
| 3 | 02_ideas | ✅ | 93% |
| 3b | 03_reasoning | ✅ | 91% |
| 3c | 04_consequences | ✅ | 90% |
| 4 | 05_llm_instructions.json | ✅ | 91% |
| 5 | 06_agent_rules | ✅ | 90% |

## Ready to Use
```bash
# Use in Claude
@paste Books/дизайн-системы/06_agent_rules.md
"Review this architecture against design system principles"

# Or programmatically
curl https://raw.githubusercontent.com/.../Books/дизайн-системы/06_agent_rules.json
```
```

---

## 📝 Примеры: Две новые книги

Я создам папку `source/example-books/` с двумя примерами:

### Пример 1: Software Design Philosophy Book

```
source/example-books/design-philosophy/README.md:

# Software Design Philosophy

**Автор:** John Ousterhout  
**Год:** 2018  
**Язык:** English  
**Источник:** https://example.com/design-philosophy

## Краткое описание

Практическая философия проектирования систем, основанная на концепции "простоты, скрытости сложности".

## Тип контента
- [x] Техническая книга по программированию
- [ ] Книга о проектировании архитектуры
- [ ] Книга о процессах разработки

## Ключевые области

#design, #simplicity, #abstraction, #philosophy, #systems
```

### Пример 2: Микросервисная архитектура

```
source/example-books/microservices-architecture/README.md:

# Microservices Architecture Patterns

**Автор:** Chris Richardson  
**Год:** 2022  
**Язык:** English  
**Источник:** https://example.com/microservices

## Краткое описание

Паттерны и практики для проектирования, тестирования и развёртывания микросервисных систем.

## Тип контента
- [x] Техническая книга по программированию
- [x] Книга о проектировании архитектуры

## Ключевые области

#microservices, #distribution, #resilience, #patterns, #deployment
```

---

## 🚀 Полный workflow для ваших 2 книг

### Шаг 1: Подготовка (5 минут)

```bash
cd source/

# Книга 1
mkdir example-books/design-philosophy/
echo "# Design Philosophy" > example-books/design-philosophy/README.md
# ... [заполнить README как выше]

# Книга 2
mkdir example-books/microservices-architecture/
echo "# Microservices Architecture" > example-books/microservices-architecture/README.md
# ... [заполнить README как выше]
```

### Шаг 2: Запуск (в Claude)

```
/book-compiler design-philosophy
```

**Система делает:**
1. Читает `source/example-books/design-philosophy/README.md`
2. Создаёт `Books/design-philosophy/` со всеми 6 слоями
3. Логирует в `reports/design-philosophy-PASS-1-5.md`

**Результат:** 15-20 минут, книга готова

### Шаг 3: Второй запуск

```
/book-compiler microservices-architecture
```

**Результат:** Вторая книга готова, логи в `reports/`

### Шаг 4: Добавить в git (опционально)

```bash
git add Books/design-philosophy/
git add Books/microservices-architecture/
git commit -m "Add 2 new books: Design Philosophy + Microservices Architecture"
git push
```

**НЕ добавляем:**
```bash
# Эти остаются локально:
# - source/
# - reports/
```

---

## ⚙️ Автоматизация: Что делает навык

### Навык читает ONE файл:

```
source/моя-книга/README.md
```

### Навык ИСКЛЮЧАЕТ вопросы:

```python
# Нет вопросов типа:
# "Какой язык?"
# "Какая тематика?"
# "Сколько принципов?"

# Всё явное из README.md или параметры команды
```

### Навык ЛОГИРУЕТ ВСЁ:

- Real-time: `/reports/книга-PASS-1-5.log`
- Итоговый: `/reports/книга-PASS-1-5.md`
- Время каждого Pass
- Количество строк каждого файла
- Quality score каждого компонента
- Ошибки и предупреждения

### Навык ПРОВЕРЯЕТ качество:

```
Перед сохранением каждого файла:
✓ Все теги корректны (#tag)
✓ Все ссылки указывают на реальные места
✓ Нет дублей принципов
✓ JSON валидный
✓ Traceability полная (каждое правило доказано)
```

---

## 🛠️ Если что-то не так

### Проблема: "Книга разобрана плохо"

**Решение:**

1. Обновить `source/книга/README.md` (добавить подробности)
2. Запустить заново:
```
/book-compiler книга --force-regenerate
```
3. Проверить логи в `reports/книга-PASS-1-5.md`

### Проблема: "Один слой неправильный (например, 02_ideas.md)"

**Решение:**

1. Открыть `Books/книга/02_ideas.md`
2. Отредактировать (добавить/удалить принципы)
3. Перезапустить Pass 4-5:
```
/book-compiler книга --from-pass=4
```
(Слои 00-03 остаются, Pass 4-5 регенерируются)

### Проблема: "JSON слой повреждён"

**Решение:**

```
/book-compiler книга --from-pass=4 --validate-only
```

Система:
- Проверит JSON валидность
- Сообщит ошибки
- Не перезаписывает

---

## 📌 Ключевые моменты

### ✅ Делай

- Положи исходный материал в `source/`
- Заполни README.md точно
- Запусти `/book-compiler`
- Проверь логи в `reports/`
- Коммитай только `Books/` в git

### ❌ Не делай

- Не редактируй слои вручную (они перегенерируются)
- Не пускай `source/` в git (только локально)
- Не пускай `reports/` в git (только логирование)
- Не запускай Pass'ы вручную (навык управляет всем)

---

## 📚 Результат

После 2 запусков:

```
Books/
├── clean-architecture/          ← Старая (11 слоёв уже)
├── ideal-work/                  ← Старая
├── ... (9 остальных старых)
├── design-philosophy/           ← НОВАЯ (готова за 15 мин)
└── microservices-architecture/  ← НОВАЯ (готова за 15 мин)

reports/
├── design-philosophy-PASS-1-5.log
├── design-philosophy-PASS-1-5.md
├── microservices-architecture-PASS-1-5.log
└── microservices-architecture-PASS-1-5.md

source/ (локально, не в git)
├── example-books/
│   ├── design-philosophy/
│   └── microservices-architecture/
```

**Готово. Две новые книги, полностью разобраны, логированы, готовы к использованию.**

---

**Вопросы?** Запусти `/book-compiler --help`
