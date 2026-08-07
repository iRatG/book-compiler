# Clean Code Audit: Side-by-Side Examples

Comparing how each version approaches the same topic.

---

## EXAMPLE 1: Function Naming

### Local Version (Deep Dive)
```
### C-009: Функция должна быть маленькой (вмещаться на экран)

Тип: Правило дизайна
Статус: явный
Важность: высокая
Уверенность: высокая

### Формулировка

Мартин утверждает, что функция должна быть настолько маленькой, 
что вмещается на одном экране. Это не магическое число, 
а психологический принцип:

1. Человек может удержать в голове максимум 7±2 элемента
2. Функция больше экрана → превышает лимит когнитивной нагрузки
3. Маленькие функции легче тестировать
4. Маленькие функции легче комбинировать

### Контрпример

Функция, которая делает 3 вещи:

```java
public void processOrder(Order order) {
  validateOrder(order);        // Валидация
  applyDiscount(order);        // Скидка
  updateInventory(order);      // Инвентарь
  sendConfirmation(order);     // Email
}
```

Проблема: одна функция для четырех проблем (четыре причины для изменения).

### Хороший пример

```java
public void processOrder(Order order) {
  if (!validator.isValid(order))
    throw new InvalidOrderException();
  
  order.applyDiscount();
  inventory.update(order);
  mailer.sendConfirmation(order);
}
```

Лучше, но каждая строка - это еще одна функция:

```java
public void processOrder(Order order) {
  validate(order);
  applyDiscount(order);
  reserveInventory(order);
  notifyCustomer(order);
}
```

### Ключевое следствие

Функция должна делать "одно" на одном уровне абстракции.
Если функция требует комментария "сначала делаем X, потом Y" - она делает два.

### Исключения

- Конструкторы часто делают несколько инициализаций
- Setup методы в тестах могут быть длиннее (но должны быть скучными)
```

**Analysis Time:** 3-5 minutes to understand  
**Confidence After Reading:** High (know why AND how)  
**Can cite in PR?** Yes, but needs explanation  

---

### GitHub Version (Quick Reference)
```
**Function Design:** Functions must remain small, handle one 
responsibility, and avoid boolean parameters. The document warns 
against hidden side effects and recommends separating command 
operations from query operations.
```

**Analysis Time:** 30 seconds  
**Confidence After Reading:** Medium (know what to do)  
**Can cite in PR?** Yes, directly quotable  

---

### 🎲 Comparison

| Aspect | Local | GitHub |
|--------|-------|--------|
| Explains WHY | ✅ Yes (cognitive load) | ❌ Assumed known |
| Shows examples | ✅ Yes (bad + good) | ⚠️ Mentioned, not shown |
| How to apply | ✅ Clear (extract functions) | ✅ Clear (small functions) |
| Time to understand | ❌ 5 minutes | ✅ 30 seconds |
| Confidence to decide | ✅ High | ⚠️ Medium |
| PR citation | ⚠️ Requires context | ✅ Direct quote |

---

## EXAMPLE 2: Error Handling

### Local Version
```
## C-020: Обработка ошибок - это функция программы, не добавок

Тип: Замысел автора
Статус: явный
Важность: высокая
Уверенность: высокая

### Формулировка

Многие разработчики смотрят на обработку ошибок как на 
техническое требование ("нам нужно это сделать"), а не как на 
часть логики приложения.

Мартин говорит: это неправильно. Обработка ошибок - это ТАК ЖЕ 
важна, как бизнес-логика.

### Проблема

Когда вы вкладываете обработку ошибок в конце (после 500 строк 
бизнес-логики), получается:

```java
try {
  // 500 строк бизнес-логики
  // где каждая может выбросить исключение
  // но мы их сначала игнорируем
} catch (Exception e) {
  // потом пытаемся их всех обработать
  // = неразбериха
}
```

### Решение

Выделить обработку ошибок в отдельное место:

```java
try {
  doBusinessStuff();
} catch (FirstException e) {
  handleFirstCase();
} catch (SecondException e) {
  handleSecondCase();
}
```

Теперь "happy path" видно с первой линии.

### Ключевое следствие

Каждое исключение - это решение проекта. Если вы обрабатываете 
IOException, это значит, что вы ЗНАЛИ про эту проблему и 
РЕШИЛИ как ее решать.

Это не "добавок", это часть алгоритма.
```

**Learning Value:** 9/10 (Teaches thinking, not just rules)

---

### GitHub Version
```
**Error Handling:** Explicit error management keeps happy paths 
readable. The guide discourages returning `null` sentinels without 
safer alternatives.
```

**Actionability:** 9/10 (Clear what to do)  
**Learning Value:** 4/10 (Why is assumed)

---

### 🎲 Comparison

| Aspect | Local | GitHub |
|--------|-------|--------|
| Explains WHY | ✅ Yes (happy path clarity) | ❌ Not explained |
| Shows anti-pattern | ✅ Yes (nested try-catch) | ❌ Not shown |
| Shows pattern | ✅ Yes (structured errors) | ✅ Yes (explicit management) |
| Time to learn | ❌ 5 minutes | ✅ 1 minute |
| Can apply immediately | ⚠️ With interpretation | ✅ Yes |

---

## EXAMPLE 3: Comments

### Local Version
```
## C-012: Чистый код не нуждается в комментариях

Тип: Замысел автора
Статус: явный
Важность: высокая
Уверенность: высокая

### Формулировка

Это САМОЕ СПОРНОЕ правило Мартина. Его цитируют неправильно.

Мартин НЕ говорит: "никогда не пишите комментарии".
Мартин говорит: "код должен быть настолько понятен, что 
комментарии не нужны для объяснения ЧТО он делает".

### Контрпример (плохой комментарий)

```java
// увеличиваем счетчик
i++;

// проверяем, что счет не отрицательный
if (balance >= 0)
```

Проблема: комментарий повторяет код. Это не нужно.

### Хороший комментарий

```java
// ++i вместо i++ потому что нам не нужна временная переменная
i++;

// Закон Мёрфи: проверяем даже на то, что как будто 
// гарантируется логикой, потому что пару раз баги приходили 
// с этой стороны
if (balance >= 0)
```

### Решение

Если код требует комментария "что здесь происходит", 
переименуйте переменные/функции:

```java
// Плохо:
if (user.flags & 0x1) // ACTIVE flag?

// Хорошо (без комментария):
if (user.isActive())
```

### Ключевое следствие

Лучший комментарий - это код, который не нуждается в комментарии.

Но комментарии нужны для:
- "Почему" (решения дизайна)
- "Предупреждения" (Закон Мёрфи)
- "История" (почему код не переработан вчера)
```

**Depth:** 9/10 (Clarifies common misunderstanding)

---

### GitHub Version
```
**Code Structure:** Comments should never compensate for poor 
naming. Self-explanatory code takes precedence; comments serve 
only when they convey information code cannot express clearly 
(legal requirements, non-obvious intent, constraints).
```

**Clarity:** 9/10 (Direct and actionable)

---

### 🎲 Comparison

| Aspect | Local | GitHub |
|--------|-------|--------|
| Clarifies misconception | ✅ Yes (it's not "no comments") | ❌ Misunderstood as "no comments" |
| Shows when comments good | ✅ Yes (why, warnings, history) | ✅ Yes (constraints, non-obvious) |
| Shows when bad | ✅ Yes (code duplication) | ✅ Yes (compensating for names) |
| Time to understand | ❌ 5 minutes | ✅ 1 minute |
| Nuance captured | ✅ Yes | ⚠️ Partial |

---

## 📊 PATTERN ANALYSIS

### When Local Version Wins
1. **Topic has misconceptions** (like comments rule)
2. **Rule has exceptions** (when to break the rule)
3. **Why matters more than what** (building judgment)
4. **Teaching a philosophy** (not just enforcing)

### When GitHub Version Wins
1. **Quick decision needed** (PR review time)
2. **Rule is simple** (no exceptions)
3. **Enforcement is goal** (not learning)
4. **Team already knows why** (just needs checklist)

### Ideal Workflow
```
┌─────────────────────────────────────────┐
│ GitHub: "Minimize parameters"           │
│ Reviewer cites rule in PR comment       │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ Developer confused, asks "Why?"         │
│ Reviewer sends link to Local version    │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│ Developer reads C-010 (chapter 3)       │
│ Understands the reasoning               │
│ Applies rule correctly going forward    │
└─────────────────────────────────────────┘
```

---

## 🎯 SUMMARY

**Local Version Excellence:**
- Deep understanding
- Teaches reasoning
- Clarifies misconceptions
- Builds judgment

**GitHub Version Excellence:**
- Quick reference
- Direct applicability
- Team enforcement
- PR citations

**The Perfect System:** Use BOTH, linked together.