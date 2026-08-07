# Deep Reading Skill — Design Conversation Log

> Рабочая история обсуждения концепции LLM-skill для глубокого чтения книг.
>
> Цель файла — сохранить не только выводы, но и сам процесс проектирования:
> как возникала идея, какие варианты рассматривались, какие формулировки стали фундаментальными.

---

## 1. Исходная постановка задачи

### Пользователь

У меня есть книга «Как читать книги». В ней есть методика чтения разных типов книг, записи, запоминание. Хочу подумать о skill для LLM, который можно положить на GitHub и использовать с VS Code, Codex и другими продуктами. На вход подаётся книга, конспект или статья, а LLM разбирает материал не как обычный summary, а по методологии чтения: строит карту, объясняет, о чём книга, что она делает, как делает, что нужно запомнить.

### ChatGPT

Идея была понята не как «промпт для summary», а как **исполняемый LLM-skill систематического чтения**.

Первичная архитектура:

```text
BOOK / ARTICLE / PAPER
        │
        ▼
Identify text type
        │
        ▼
Structural reading
        │
        ▼
Analytical reading
        │
        ▼
Critical reading
        │
        ▼
Knowledge extraction
        │
        ▼
Knowledge map
```

Ключевое отличие:

**Summary отвечает:** что написано в книге?

**Skill должен отвечать:**  
- что это за книга;
- какую проблему она решает;
- как устроена мысль;
- какие утверждения делает автор;
- как он их обосновывает;
- какие понятия нужно освоить;
- как части связаны;
- что главное, а что иллюстрация;
- с чем можно спорить;
- что нужно уметь объяснить после чтения;
- что стоит перенести в память и практику.

Появилась первая важная мысль:

> **The goal is not to compress a book. The goal is to reconstruct it well enough that the reader can think with and against it.**

Также возникла идея трёх уровней skill:
1. reading methodology;
2. reading workflows по типам текстов;
3. артефакты понимания.

Появились возможные выходы:

```text
00_book_profile.md
01_structural_map.md
02_key_questions.md
03_concepts.md
04_arguments.md
05_knowledge_map.md
06_critical_analysis.md
07_memory_notes.md
08_questions_for_self_test.md
09_final_synthesis.md
```

Отдельно выделились:
- structural map;
- concepts;
- arguments;
- what should remain after reading;
- разделение author position / LLM interpretation / critique / takeaway;
- вопросы как центральный механизм чтения;
- stateful reading для больших книг;
- syntopical mode для нескольких книг.

---

## 2. Добавление Сергея Поварнина и Томаса Фостера

### Пользователь

Предложено взять за основу также Сергея Поварнина «Как читать книги» и Томаса Фостера «Искусство чтения», обобщить методологии и взять основные детали.

### ChatGPT

Появилось решение не копировать одну методику, а собрать **синтетический протокол чтения**.

Распределение ролей:

**Поварнин** — цель, дисциплина, глубина и режим чтения.

**Адлер** — структурная и аналитическая реконструкция.

**Фостер** — художественное чтение: паттерны, символы, архетипы, интертекстуальность, ирония, второй слой смысла.

Ключевая идея:

```text
Stage 0 — Reading Intent
Stage 1 — Inspection
Stage 2 — Structural reconstruction
Stage 3 — Semantic reconstruction
Stage 4 — Argument reconstruction
Stage 5 — Deep meaning
Stage 6 — Critical reading
Stage 7 — Human presentation
```

Очень важное правило:

> **Never critique before reconstruction.**

Также возникла идея `Evidence traceability`:
каждый важный вывод знает, откуда он взялся.

Пример:

```yaml
claim_id: C17
claim: "..."
source:
  chapter: 7
  section: "..."
  pages: 154-157
confidence: high
author_explicit: true
```

---

## 3. Формализация трёх методологических столпов

### Пользователь

Добавлена книга Мортимера Адлера «Как читать книги». Решено строить skill именно для LLM, чтобы он понимал, как читать и как правильно представлять книгу человеку.

### ChatGPT

Сформулирована новая цель:

> Skill должен быть **методологией чтения для LLM**, а не инструкцией для человека.

Три автора стали тремя слоями:

- **Поварнин** — как выбрать режим чтения;
- **Адлер** — как восстановить интеллектуальную конструкцию книги;
- **Фостер** — как не потерять нелiteral meaning в художественном тексте.

Появился ключевой принцип:

```text
DO NOT SUMMARIZE YET.
First reconstruct the book.
```

Возникла внутренняя сущность `BookModel`:

```text
BookModel
│
├── identity
├── reading_goal
├── central_question
├── author_intent
├── central_thesis
├── structure
├── concepts
├── propositions
├── arguments
├── evidence
├── examples
├── assumptions
├── themes
├── patterns
├── unresolved_questions
├── contradictions
└── implications
```

И важное разделение:

```text
book
 ↓
reconstruction
 ↓
reasoning model
 ↓
evaluation
 ↓
pedagogical transformation
 ↓
human understanding
```

Вместо обычного:

```text
book
 ↓
compression
 ↓
summary
```

Появилось разделение ролей LLM:

```text
LLM AS READER
LLM AS ANALYST
LLM AS CRITIC
LLM AS TEACHER
LLM AS ARCHIVIST
```

---

## 4. Book Understanding Compiler

### Пользователь

Запрос: глубже «прожарить» идею. На входе книга, на выходе HTML, Markdown или другой результат. Важно найти самое интересное и ценное.

### ChatGPT

Появился главный архитектурный поворот:

> **На входе книга как линейный текст. На выходе — интерактивная модель знания, содержащегося в книге.**

HTML и Markdown стали рассматриваться не как ядро, а как **renderers**.

Вопрос: что такое «прочитанная LLM книга»?

LLM после обработки должна знать:

```text
WHY
QUESTION
THESIS
STRUCTURE
CONCEPTS
CLAIMS
ARGUMENTS
EVIDENCE
EXAMPLES
CONNECTIONS
ASSUMPTIONS
LIMITATIONS
CONTRADICTIONS
INTERPRETATION
IMPORTANCE
MEMORY
APPLICATION
```

Появилась формула:

```text
BOOK
 ↓
READING ENGINE
 ↓
BOOK MODEL
 ↓
HTML / Markdown / JSON
```

Появились идеи human-facing интерфейсов:
- первый экран ориентации;
- визуальная карта книги;
- Question Graph;
- Argument Map;
- Book X-Ray;
- dependency graph;
- learning order;
- non-obvious ideas;
- common misreadings;
- depth modes.

Главная метафора:

> **Book Understanding Compiler**

```text
SOURCE BOOK
     ↓
PARSING
     ↓
SEMANTIC ANALYSIS
     ↓
INTERMEDIATE REPRESENTATION
     ↓
OPTIMIZATION / EDITING
     ↓
RENDERING
     ↓
HUMAN UNDERSTANDING
```

Три книги стали методологией parser'а, а сверху появился LLM-native слой:
- context management;
- hierarchical processing;
- knowledge graphs;
- confidence;
- traceability;
- multi-pass reading;
- machine-readable state;
- interactive HTML;
- adaptive presentation.

Также появился multi-pass подход:

```text
PASS 1 — SURVEY
PASS 2 — STRUCTURE
PASS 3 — EXTRACTION
PASS 4 — CONNECTION
PASS 5 — INTERPRETATION
PASS 6 — CRITIQUE
PASS 7 — EDITORIAL
PASS 8 — VERIFICATION
PASS 9 — RENDER
```

---

## 5. Obsidian и knowledge graph

### Пользователь

Предложено подключить Obsidian, чтобы книга существовала как модель: цепи, логические связи, цели и идеи книги. Внизу — полная модель книги.

### ChatGPT

Obsidian был определён не как ещё один отчёт, а как **живой интерфейс к Full Book Model**.

```text
BOOK
  ↓
FULL BOOK MODEL
  ↓
HTML / Markdown / Obsidian / JSON
```

Появилась идея Obsidian Vault:

```text
Books/
└── How to Read a Book/
    ├── 00 Book.md
    ├── 01 Map.md
    ├── 02 Questions.md
    ├── 03 Arguments.md
    ├── 04 Learning Path.md
    ├── Concepts/
    ├── Ideas/
    ├── Arguments/
    ├── Questions/
    ├── Examples/
    ├── Critiques/
    └── Chapters/
```

Возникла идея typed relations:

```text
SUPPORTS
CONTRADICTS
DEPENDS_ON
EXPLAINS
EXAMPLE_OF
PART_OF
ANSWER_TO
ASSUMES
LEADS_TO
REFINES
APPLIES
COMPARES_WITH
```

Ключевой шаг: **цели книги тоже являются узлами графа**.

Например:

```text
AUTHOR GOAL
        │
        ├── achieved_by → idea A
        ├── achieved_by → method B
        └── culminates_in → concept C
```

Появилось различие:

```text
LLM → BookModel → KnowledgeGraph → HTML / Obsidian / Markdown
```

а не:

```text
LLM → Obsidian notes
```

Также возникла долгосрочная идея:
не граф одной книги, а граф всей библиотеки.

Это естественно привело к:
- canonical concepts across books;
- entity resolution;
- syntopical reading;
- question-centric library.

---

## 6. Full Book Model как центральный объект

### Пользователь

Запрос отдельно подумать только о Full Book Model.

### ChatGPT

Был поставлен один вопрос:

> **Что должна представлять собой полная внутренняя модель книги после того, как LLM действительно её прочитала?**

Появилась формулировка:

> **Book Model — это реконструированная интеллектуальная система произведения.**

Не summary, не mind map, не список заметок и не набор flashcards.

Были рассмотрены сущности:

- Intent
- Problem
- Question
- Goal
- Thesis
- Claim
- Function
- Term
- Concept
- Definition
- Distinction
- Principle
- Method
- Procedure
- Argument
- Evidence
- Example
- Assumption
- Tension
- Contradiction
- Tradeoff
- Paradox
- Scope
- Qualification
- Implication
- Provenance
- Transformation
- Misconception
- Contribution
- Theme
- Character/Event для fiction
- technical/scientific extensions.

Важная идея:

> **Relations are more important than entities.**

Формула:

```text
BookModel = Nodes + TypedEdges + Provenance
```

или:

```text
BM = (V, E, P)
```

Особенно важные отношения:

```text
PART_OF
DEFINES
ANSWERS
SUPPORTS
CONTRADICTS
QUALIFIES
DEPENDS_ON
EXPLAINS
ILLUSTRATES
CAUSES
LEADS_TO
APPLIES_TO
RESOLVES
SERVES
CONTRASTS_WITH
```

Также появилась идея developmental structure:

```text
Concept X
├── introduced
├── clarified
├── qualified
└── applied
```

И `BookArchitecture` как описание хода мысли:

```text
Problem
   ↓
Distinction
   ↓
Framework
   ↓
Argument
   ↓
Method
   ↓
Application
```

Очень важная итоговая формула:

> Автор столкнулся с проблемой P.  
> Сформулировал вопрос Q.  
> Предложил ответ T.  
> Для ответа ввёл понятия C.  
> Провёл различия D.  
> Защитил утверждения A аргументами R.  
> Использовал доказательства E.  
> Из этого вывел I.  
> Предложил методы M.  
> Они применимы при условиях S.  
> Всё это служит исходной цели G.

---

## 7. Переход к техническому заданию

### Пользователь

Предложено подробно обдумывать части для проектирования и постепенно писать ТЗ.

### ChatGPT

Сформирован каркас будущего ТЗ:

1. Purpose & Philosophy
2. Input Contract
3. Reading Strategy
4. Multi-pass Reading Engine
5. Full Book Model
6. Verification & Epistemics
7. Editorial / Human Representation
8. Outputs
9. State & Large Books
10. Quality Gates

Ключевой принцип:

> Не переходить к следующему разделу, пока предыдущий не стал концептуально устойчивым.

---

## 8. Purpose & Philosophy

Была сформулирована цель:

> **Skill должен преобразовывать линейный текст книги в структурированную, проверяемую и пригодную для дальнейшего использования модель интеллектуального содержания книги, а затем представлять её человеку в форме, оптимальной для понимания, запоминания, критической оценки и применения.**

Появилось определение успешного чтения:

> **Reading is successful when the model can reconstruct not merely what the book says, but why its parts exist and how they form a coherent intellectual structure.**

Уровни понимания:

```text
L0 — Extraction
L1 — Description
L2 — Structure
L3 — Reconstruction
L4 — Evaluation
L5 — Transfer
```

Появились важные `MUST NOT`:

```text
MUST NOT optimize primarily for text compression.
MUST NOT treat chapter summaries as the canonical representation.
MUST NOT equate frequency of mention with importance.
MUST NOT present inferred interpretation as an explicit author statement.
```

Разделены две карты:

```text
Source Map
Meaning Map
```

И три модели:

```text
AUTHOR MODEL
ANALYST MODEL
READER MODEL
```

Сформулированы принципы:

> **Preserve first. Compress later.**

> **Author fidelity before evaluation.**

> **Compression must never strengthen a claim.**

> **Examples are not ideas.**

> **Quotes are source evidence, not knowledge nodes.**

Появилась epistemic градация:

```text
E0 — explicit
E1 — strongly implied
E2 — inferred
E3 — interpretive hypothesis
E4 — external evaluation
```

И определение:

> **Full Book Model = typed, hierarchical, provenance-aware and uncertainty-aware graph representing the reconstructed intellectual architecture of a book.**

---

## 9. Поиск минимального, но глубокого ядра

### Пользователь

Уточнено: сейчас важно не программирование, а концепт. Он не должен быть слишком сложным или тяжёлым, но должен содержать глубину и основу, из которой сможет вырасти мощная система.

### ChatGPT

Появился design principle:

> **Minimum ontology, maximum explanatory power.**

Full Book Model был упрощён до пяти смысловых слоёв:

```text
1. PURPOSE
2. QUESTIONS
3. IDEAS
4. REASONING
5. CONSEQUENCES
```

Минимальная ontology:

```text
PURPOSE
├── Problem
└── Intent

QUESTIONS
└── Question

IDEAS
├── Concept
├── Claim
└── Principle

REASONING
├── Argument
├── Evidence
├── Example
└── Assumption

CONSEQUENCES
├── Implication
├── Application
└── Limitation
```

Всего 13 базовых типов.

Минимальные отношения:

```text
ANSWERS
SUPPORTS
DEPENDS_ON
EXPLAINS
ILLUSTRATES
QUALIFIES
CONTRADICTS
LEADS_TO
PART_OF
```

Общий контракт node:

```yaml
id:
type:
title:
statement:
importance:
confidence:
source:
status:
function:
```

Статусы:

```text
explicit
inferred
interpretation
evaluation
```

Importance:

```text
core
important
supporting
detail
```

Confidence:

```text
high
medium
low
```

Появился `Node Admission Rule`:
node создаётся только если он:
- нужен для понимания центральной идеи;
- является зависимостью других важных идей;
- представляет существенный вклад автора;
- нужен для применения;
- при потере искажает позицию автора.

Появился принцип:

> **FULL enough to reconstruct. SMALL enough to understand.**

И ещё один:

> **Simplicity above. Depth below.**

Также было решено:
- v1 не обязана идеально покрывать fiction;
- fiction и scientific-specific ontology можно делать extensions;
- syntopical reading оставить future-compatible;
- не перегружать foundation будущими функциями.

---

## 10. Философское ядро v0

### Пользователь

Фокус возвращён на основные столпы трёх авторов. Нужна версия 0 — то, без чего skill вообще не может существовать. Важно не пропустить ничего фундаментального.

### ChatGPT

Было зафиксировано философское ядро.

Три методологических опоры:

**Поварнин**

> читать нужно в соответствии с целью, типом текста и необходимой глубиной.

**Адлер**

> чтение — активная реконструкция структуры мысли автора.

**Фостер**

> буквальный слой текста не всегда равен полному смыслу.

Общая формула:

> **LLM должна не сокращать книгу, а реконструировать её как интеллектуальный объект, понять её на собственных условиях автора и только после этого преобразовать для человека.**

Двенадцать фундаментальных столпов:

### 1. Purpose before Processing

Сначала понять:
- что это за текст;
- зачем он существует;
- какой режим чтения нужен;
- какая глубина нужна.

### 2. Reconstruction before Compression

```text
BOOK
 ↓
UNDERSTAND
 ↓
RECONSTRUCT
 ↓
VERIFY
 ↓
COMPRESS / EXPLAIN
```

### 3. Book as a System

```text
WHY
 ↓
QUESTION
 ↓
ANSWER
 ↓
IDEAS
 ↓
REASONING
 ↓
CONSEQUENCES
```

### 4. Relationships over Lists

Смысл находится в связях, а не в списке идей.

### 5. Author Fidelity

```text
What does the author say?
What does the author mean?
Why does the author believe it?
What follows?
Only then: Is the author right?
```

### 6. Epistemic Separation

```text
AUTHOR EXPLICIT
INFERRED
INTERPRETATION
EVALUATION
```

### 7. Source Traceability

```text
Idea
 ↓
Source
 ↓
Chapter / Section / Passage
```

> **No important claim without provenance.**

### 8. Preserve Nuance

Сохранять:
- conditions;
- exceptions;
- scope;
- uncertainty;
- qualifications.

> **Compression must never strengthen a claim.**

### 9. Importance is Functional

Понимать не только, что сказано, но зачем элемент существует внутри конструкции книги.

### 10. Simple Surface, Deep Interior

> **Simplicity above. Depth below.**

### 11. Human Understanding is the Output Goal

LLM работает как:

```text
READER
↓
understand faithfully

TEACHER
↓
explain intelligently
```

### 12. Full Model is Canonical

```text
                 FULL BOOK MODEL
                        │
           ┌────────────┼────────────┐
           ▼            ▼            ▼
         HTML        Markdown     Obsidian
```

Все выходы — представления одной канонической модели.

---

## 11. Рабочий манифест

> **This skill does not summarize books. It reads them. It determines why a book exists, identifies the questions it addresses, reconstructs its concepts, claims, principles and reasoning, preserves the distinction between the author's statements and the model's interpretations, traces important conclusions back to the source, and builds a compact but deep model of how the book works as an intellectual system. Only after this reconstruction is complete does the skill transform the model into a human-readable representation optimized for understanding, retention and application.**

---

## 12. Решение сохранить процесс

### Пользователь

Попросил не делать очередную выжимку, а сохранить весь процесс обсуждения: от исходной идеи до хороших решений, возникших по пути, потому что последовательность разговора сама по себе ценна и её не хочется потерять.

---

## Примечание

Этот файл сохранён как **design log**, а не как финальное ТЗ.

Он намеренно содержит:
- исходные формулировки;
- промежуточные архитектурные идеи;
- повороты мысли;
- варианты, которые позже были упрощены;
- сильные фразы и принципы;
- переход от summary к Full Book Model;
- переход от богатой ontology к минимальному ядру v0.

Именно этот процесс можно использовать позднее как исходный материал для:
- Philosophy.md;
- methodology.md;
- технического задания;
- ontology spec;
- SKILL.md;
- README проекта;
- ADR / design decisions.
