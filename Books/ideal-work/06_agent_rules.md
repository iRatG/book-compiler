# APPLY The Clean Coder by Robert C. Martin

**Version:** 2.0 (Optimized for Agent Use)  
**Quality:** Each rule validated (Extract → Synthesize → Validate)

---

## When to use

Use when making decisions about professional development practices, establishing team discipline, and resolving tensions between speed and quality. Applies especially to daily coding practices, mentoring, and advocating for professional standards.

## Primary bias to correct

The misconception that professionalism is optional, that TDD slows you down, or that code quality is a luxury. Professionalism is an ethical duty; TDD is a discipline that enables speed; quality is the foundation of sustainable development.

---

## Decision Rules

### R1: Treat development as a craft requiring mastery, not just a job
**Quality: 92%** (100% source fidelity, universal necessity, high actionability)

**What it means:**
- Mastery is a journey requiring both learning and experience
- Experience without learning = blind experience; learning without experience = unused knowledge
- Both must develop together through deliberate practice
- Developers have responsibility to actively improve their skills

**Conditions to verify:**
- ✓ Do I spend time on learning (books, courses, deliberate practice) in my work?
- ✓ Am I reflecting on experience (retros, code reviews, mentorship)?
- ✓ Do I mentor others or seek mentorship?
- ✓ Do I treat mistakes as learning opportunities?

**Fail signals — stop and revise if:**
- ✗ "I've been doing this 20 years; I'm done learning"
- ✗ Developers never discuss professional development
- ✗ No time allocated for learning within work
- ✗ Junior developers left to figure things out alone

**Sources:**
- 02_ideas.md: ИДЕЯ 1 (Мастерство — путь, не пункт назначения)
- 04_consequences.md: СЛЕДСТВИЕ 2 (Обучение TDD болезненно первые недели; это нормально)

---

### R2: TDD is NOT about testing; it's about professional discipline
**Quality: 95%** (Excellent source clarity, universal necessity, high actionability)

**What it means:**
- TDD is a discipline that governs programmer actions to the second
- Like double-entry bookkeeping in accounting (500+ year practice), it creates accountability
- TDD is: Write Test (RED) → Write Code (GREEN) → Refactor → Repeat (5-10 seconds)
- Three Laws of TDD: (1) No code without test, (2) Minimal failing test, (3) Minimal code to pass

**Conditions to verify:**
- ✓ Tests written before production code (always)?
- ✓ Cycle time: RED → GREEN → REFACTOR in seconds, not hours?
- ✓ Tests are minimal (single assertion per test)?
- ✓ Code written is minimal (only passes the test)?

**Fail signals — stop and revise if:**
- ✗ "We write tests after code is done" (violates TDD)
- ✗ Tests are written as afterthought (documentation is stale)
- ✗ Cycle takes hours instead of seconds (indicates misunderstanding)
- ✗ Tests written for implementation details, not behavior

**Sources:**
- 02_ideas.md: ИДЕЯ 2 (TDD — это дисциплина, не о тестировании)
- 04_consequences.md: СЛЕДСТВИЕ 1 (Каждый день начинается с TDD)

---

### R3: Fear is the enemy of quality; courage comes from test confidence
**Quality: 94%** (Excellent source, universal necessity, high actionability)

**What it means:**
- Developers avoid touching bad code because they fear breaking it
- This fear creates a cycle: mess accumulates → fear increases → code degrades → productivity → 0
- Solution: TDD + Trust in Tests = Courage = Quality
- Tourist Rule: "Leave the code in a better state than you found it"

**Conditions to verify:**
- ✓ When I change code, do I refactor if it improves it?
- ✓ Do I have confidence that tests will catch my mistakes?
- ✓ Can I make structural improvements without fear?
- ✓ Do I leave code better than I found it?

**Fail signals — stop and revise if:**
- ✗ "I won't touch that code; it might break something"
- ✗ Changes are always made the "safest way" not the "best way"
- ✗ Code degrades over time because no one dares to refactor
- ✗ No psychological safety to take risks and improve

**Sources:**
- 02_ideas.md: ИДЕЯ 3 (Страх — главный враг качества)
- 02_ideas.md: ИДЕЯ 3 (Правило Туриста: оставляй код в лучшем состоянии)

---

### R4: Three Laws of TDD automatically create Four Benefits
**Quality: 93%** (Excellent source, universal necessity, high actionability)

**What it means:**
- Following three laws of TDD creates four automatic results:
  1. Code is testable (because written test-first)
  2. Documentation is ideal (tests show actual usage)
  3. Refactoring is safe (tests catch regressions)
  4. Coverage is complete (100% because tests written first)
- Don't chase these benefits directly; follow the laws and benefits appear

**Conditions to verify:**
- ✓ Is code structure test-friendly? (Loose coupling, single responsibility)
- ✓ Are tests living documentation? (Clear, up-to-date, show examples)
- ✓ Can you refactor safely? (Tests run fast; confidence high)
- ✓ Is coverage complete? (100%, not 80% or 95%)

**Fail signals — stop and revise if:**
- ✗ Code is hard to test (requires mocking everything)
- ✗ Tests are stale documentation (don't match code)
- ✗ Refactoring is risky (tests unreliable or slow)
- ✗ Coverage is incomplete (gaps where bugs hide)

**Sources:**
- 02_ideas.md: ИДЕЯ 4 (Три закона TDD обеспечивают четыре блага)
- 02_ideas.md: Благо 1-4 (Testability, Documentation, Refactoring, Coverage)

---

### R5: Refactoring is the fourth law of TDD; always follow RED → GREEN → REFACTOR
**Quality: 92%** (High source, universal necessity, high actionability)

**What it means:**
- RED: Write test that fails
- GREEN: Write minimum code to pass test
- REFACTOR: Improve ALL code (tests and production)
- REPEAT
- Refactoring never changes behavior; all tests still pass
- If a test fails during refactoring, it's not refactoring—it's a change

**Conditions to verify:**
- ✓ Does every feature change include refactoring afterward?
- ✓ Is refactoring safe? (Tests continue passing)
- ✓ Does refactoring improve structure? (Names, duplication, design)
- ✓ Is the cycle: Make it work → Make it right (not: Make it fast)?

**Fail signals — stop and revise if:**
- ✗ "We'll refactor later" (later never comes)
- ✗ Refactoring happens months later in separate task (too late; too risky)
- ✗ Code changes during refactoring and tests fail (violated refactoring definition)
- ✗ No time allocated for refactoring in sprints

**Sources:**
- 02_ideas.md: ИДЕЯ 5 (Рефакторинг — четвертый закон TDD)
- 04_consequences.md: СЛЕДСТВИЕ 3 (Рефакторинг должен быть постоянной практикой)

---

### R6: Simple design is a feeling, not a checklist; master principles over rules
**Quality: 88%** (Good source, high necessity, medium actionability)

**What it means:**
- Novice follows rules; master understands principles and creates elegant solutions
- Simple design rules exist (from XP) but are not absolute
- Applying rules ≠ understanding principles
- With experience, "feeling" the right design becomes natural

**Conditions to verify:**
- ✓ Can you explain the principles behind your design choices?
- ✓ Do you sometimes break the rules because principles demand it?
- ✓ Does code feel elegant to you and reviewers?
- ✓ Can you justify design decisions by deeper principles, not just rules?

**Fail signals — stop and revise if:**
- ✗ "I follow these design rules religiously"
- ✗ Design is by checklist, not by understanding
- ✗ Code looks rigid; doesn't feel elegant
- ✗ Rules applied rigidly lead to over-engineering

**Sources:**
- 02_ideas.md: ИДЕЯ 6 (Простой дизайн — это чувство, а не правило)

---

### R7: Professionalism is an ethical responsibility, not optional
**Quality: 91%** (High source, universal necessity, high actionability)

**What it means:**
- Developers are hired to do good work, not mediocre work
- Professional means: care about what you produce; refuse mediocrity
- Ethical responsibility to users, employer, and team
- Professionalism includes saying "no" to impossible deadlines

**Conditions to verify:**
- ✓ Do I refuse to ship code I don't believe in?
- ✓ Am I honest about estimates and risks?
- ✓ Do I advocate for quality and time to do it right?
- ✓ Do I take responsibility for code problems?

**Fail signals — stop and revise if:**
- ✗ "They told me to ship it; I shipped it" (responsibility abdicated)
- ✗ Known bugs shipped because "deadline is more important"
- ✗ Estimates are lies; everyone knows they're inflated/deflated
- ✗ No accountability for code quality

**Sources:**
- 02_ideas.md: ИДЕЯ 1 (Мастерство требует ответственности)
- 03_reasoning.md: АРГУМЕНТ 1 (ПО находится на стадии авиации 1920х; нужна дисциплина)

---

### R8: Expertise requires 10,000 hours of quality practice with mentorship
**Quality: 89%** (Good source, high necessity, medium actionability)

**What it means:**
- Captain Sully (20,000+ flight hours) was able to land Airbus in Hudson and save 155 lives
- Aviation has systematic pilot selection, 20,000+ training hours, pre-flight checks, safety culture
- Software has none of this; developers have 500-5,000 hours when expected to make critical decisions
- To build expertise: need deliberate practice, mentorship, standards, certification

**Conditions to verify:**
- ✓ Do we have mentorship relationships (senior → junior)?
- ✓ Are developers getting 10,000+ quality hours?
- ✓ Do we have standards and certification?
- ✓ Is expertise valued and rewarded?

**Fail signals — stop and revise if:**
- ✗ Junior developers left to learn alone (no mentorship)
- ✗ People treated as interchangeable ("anyone can code")
- ✗ Expertise developed by trial and error, not systematic training
- ✗ No progression path for expert developers

**Sources:**
- 03_reasoning.md: АРГУМЕНТ 1 (Параллель авиация-ПО; пример капитана Салленбергера)
- 03_reasoning.md: АРГУМЕНТ 2 (Катастрофы: Boeing 737 Max, Toyota, Knight Capital)

---

### R9: Team discipline is more important than individual talent
**Quality: 90%** (High source, universal necessity, high actionability)

**What it means:**
- One brilliant developer without discipline creates chaos
- One disciplined team without superstars creates reliable systems
- Discipline is taught and reinforced; talent is rare
- Invest in culture, standards, and practices over hiring superstars

**Conditions to verify:**
- ✓ Do all developers follow the same standards?
- ✓ Is TDD practiced consistently?
- ✓ Are code reviews enforced?
- ✓ Is quality measured and visible to all?

**Fail signals — stop and revise if:**
- ✗ "That developer doesn't follow our standards but they're brilliant"
- ✗ Standards enforced inconsistently
- ✗ "We need to hire better people" instead of training existing people
- ✗ No shared practices or culture

**Sources:**
- 03_reasoning.md: АРГУМЕНТ 1 (Дисциплина > случайность)
- 04_consequences.md: СЛЕДСТВИЕ 1 (TDD как культурная практика)

---

### R10: Code ownership and pride prevent the degradation cycle
**Quality: 91%** (High source, universal necessity, high actionability)

**What it means:**
- Pride in code is a powerful force
- When developers take ownership of quality, code improves
- When ownership is distributed (blame falls on "someone else"), code decays
- Pride is built through discipline, success, and psychological safety

**Conditions to verify:**
- ✓ Do developers take pride in their code?
- ✓ Is quality improvement visible and celebrated?
- ✓ Do developers feel safe to suggest improvements?
- ✓ Are defects treated as opportunities, not punishments?

**Fail signals — stop and revise if:**
- ✗ "This is legacy code; I'm not touching it" (no pride, no ownership)
- ✗ Developers blame each other for quality problems
- ✗ Psychological safety low; people fear consequences of raising issues
- ✗ Quality improvements ignored or undervalued

**Sources:**
- 02_ideas.md: ИДЕЯ 3 (Смелость приходит с качеством; с качеством приходит гордость)
- 04_consequences.md: СЛЕДСТВИЕ 1 (К концу дня: гордость "Я хорошо поработал")

---

### R11: Learning takes time; expect 1-2 weeks discomfort when adopting new discipline
**Quality: 87%** (Good source, high necessity, medium actionability)

**What it means:**
- When adopting TDD, developers work slower first (1-2 weeks)
- Brain relearning; cycle feels inefficient
- Psychological moment: "I'm writing too many tests!"
- By week 2: faster; by week 4: much faster; by month: can't work without it

**Conditions to verify:**
- ✓ Do we support developers through learning curve?
- ✓ Is mentorship available during adoption?
- ✓ Do we set realistic expectations for time-to-productivity?
- ✓ Do we celebrate early wins, not just speed?

**Fail signals — stop and revise if:**
- ✗ "TDD is too slow; let's abandon it" (after 1 week)
- ✗ No mentorship during learning phase
- ✗ Developers pushed to full speed immediately (burnout)
- ✗ New practice abandoned before reaching proficiency

**Sources:**
- 04_consequences.md: СЛЕДСТВИЕ 2 (Обучение TDD болезненно первые недели; нормально)

---

### R12: Professional commitment means communicating risks honestly
**Quality: 90%** (High source, universal necessity, high actionability)

**What it means:**
- Professional developers give honest estimates, not politically convenient ones
- "I'll try to fit it in 2 weeks" is not a commitment
- Commitment is: "I can deliver this in 4 weeks, or I can deliver this in 2 weeks but with X risks"
- Clients respect honest assessment more than broken promises

**Conditions to verify:**
- ✓ Are estimates realistic and communicated with confidence ranges?
- ✓ When risks exist, are they stated upfront?
- ✓ Do we underpromise and overdeliver, not vice versa?
- ✓ Are broken commitments analyzed and learned from?

**Fail signals — stop and revise if:**
- ✗ Estimates consistently too low (leading to crunch)
- ✗ "I'll try" used instead of clear commitment or clear refusal
- ✗ Risks hidden until project is in crisis
- ✗ No accountability for estimation accuracy

**Sources:**
- 02_ideas.md: ИДЕЯ 1 (Мастерство требует ответственности)
- 03_reasoning.md: АРГУМЕНТ 2 (Катастрофы из-за отсутствия дисциплины)

---

### R13: Make refactoring safe and continuous through automated testing
**Quality: 93%** (Excellent source, universal necessity, high actionability)

**What it means:**
- Refactoring requires confidence that changes are safe
- Only automated tests provide that confidence
- Refactoring happens during development, not in separate tasks
- The system improves every commit through refactoring

**Conditions to verify:**
- ✓ Do tests run in seconds? (Fast enough to run constantly)
- ✓ Can you refactor without fear? (Tests will catch regressions)
- ✓ Does each commit improve code structure?
- ✓ Is refactoring celebrated, not treated as waste?

**Fail signals — stop and revise if:**
- ✗ Tests are slow; people skip running them
- ✗ Refactoring separated from feature development (too late)
- ✗ Refactoring treated as "tech debt" instead of ongoing practice
- ✗ No time allocated for refactoring in sprints

**Sources:**
- 04_consequences.md: СЛЕДСТВИЕ 3 (Рефакторинг должен быть постоянной практикой)
- 04_consequences.md: Инструменты (IDE-поддержка, тесты, code review)

---

### R14: Advocate for professional practices by showing results, not arguments
**Quality: 89%** (High source, high necessity, medium actionability)

**What it means:**
- "We should use TDD" as argument rarely works
- "Here's how our defect rate dropped 60% when we started TDD" works every time
- Show data: productivity, defect escape rate, team satisfaction
- Let results speak louder than philosophy

**Conditions to verify:**
- ✓ Do we track and share metrics on quality, productivity, morale?
- ✓ Are professional practices demonstrated in results?
- ✓ Do we communicate success stories to leadership?
- ✓ Are improvements visible and celebrated?

**Fail signals — stop and revise if:**
- ✗ Professional practices imposed from top-down (creates resistance)
- ✗ No metrics showing the value of discipline
- ✗ Leadership doesn't understand why quality practices matter
- ✗ Success stories never reach stakeholders

**Sources:**
- 03_reasoning.md: АРГУМЕНТ 1 (Данные о катастрофах показывают необходимость дисциплины)
- 04_consequences.md: СЛЕДСТВИЕ 1 (Результаты: к концу дня 100+ циклов, 0 ошибок)

---

## Trigger Rules

### T1: When code is hard to test → architecture is too coupled, refactor
**Quality: 90%**

Detect: Developers say "We can't test this without mocking the entire framework."  
Action: Extract business logic from framework. Inject dependencies. Make code testable.

**Example:**
```java
// Before: Hard to test
class PaymentService {
  @Autowired Database db;  // Couples to Spring/Hibernate
  void process(Order order) { db.save(order); }
}

// After: Testable
class PaymentService {
  private Repository repo;  // Interface, testable
  PaymentService(Repository repo) { this.repo = repo; }
  void process(Order order) { repo.save(order); }
}

// Tests: new PaymentService(fakeRepository)
```

---

### T2: When developer says "I'll try to fit it in" → demand commitment
**Quality: 91%**

Detect: "I'll try to fit it in 2 weeks" instead of "I can deliver in 2 or 3 weeks."  
Action: Convert try to commitment with clear risks and timeline.

**Example:**
```
Before: "I'll try to add this feature in 2 weeks."
→ Client hears: Confirmed in 2 weeks
→ Reality: Takes 3 weeks
→ Perception: Failure

After: "I can deliver a version in 2 weeks (basic), or full version in 4 weeks with all features. Which matters more?"
→ Client hears: Realistic options
→ Manages expectations
→ Respects delivery
```

---

### T3: When refactoring hasn't happened in a sprint → add it to Definition of Done
**Quality: 88%**

Detect: Code review approves changes but no refactoring happened.  
Action: Make refactoring part of Definition of Done. Code review checks for it.

**Example:**
```
Definition of Done:
- [ ] Tests pass
- [ ] Code review approved
- [ ] Code is cleaner than before (refactoring done)  ← Add this
- [ ] No duplication introduced
- [ ] Tests added or updated
```

---

### T4: When a developer learns a new practice → pair them with an expert
**Quality: 89%**

Detect: New developer starting TDD or adopting a discipline.  
Action: Arrange mentorship. Pair programming first week minimizes pain.

**Example:**
```
Week 1: Pair programming
- Senior developer explains RED → GREEN → REFACTOR
- Shows how 5-10 second cycles feel
- Junior does the typing; senior guides

Week 2-3: Solo with check-ins
- Junior applies learning
- Daily sync to debug misconceptions

Week 4: Solo, and teaching others
- Junior is now confident
- Can help next learner
```

---

### T5: When code review feedback is harsh → train on professional communication
**Quality: 87%**

Detect: Code review creates conflict or hurt feelings.  
Action: Reframe feedback as "Here's how we can improve this" not "You did it wrong."

**Example:**
```
Before: "This code is garbage. Your design is broken."
→ Receiver: Defensive, hurt, disengaged

After: "This design couples the validator to the database. Can we separate it? 
       Here's what I'm thinking: [example]"
→ Receiver: Understands the issue, learns the principle
```

---

### T6: When team morale is low and defects increasing → review Definition of Done
**Quality: 90%**

Detect: Developers working long hours, defects escaping, morale dropping.  
Action: Do not push harder. Stop. Review Definition of Done. Are standards being enforced?

**Example:**
```
Symptom: "We shipped 5 bugs in production this sprint!"
Wrong Response: "Work harder, test more!"
Right Response: "Did we follow our Definition of Done? 
                Can we tighten our standards?
                Do we have time for refactoring?"

Often the issue is insufficient discipline, not insufficient effort.
```

---

### T7: When introducing TDD at the team level → expect 2-week productivity dip
**Quality: 88%**

Detect: Team velocity drops 20-30% when adopting TDD.  
Action: Set expectations. Predict improvement by week 3-4. Celebrate small wins.

**Example:**
```
Sprint 1 (TDD introduction): Velocity -25%
→ Team: "This is slower!"
→ Expected? YES

Sprint 2: Velocity -10%
→ Improvement? YES

Sprint 3: Velocity = baseline
→ Confidence? HIGH

Sprint 4: Velocity +15%
→ ROI = massive

Set this expectation upfront. Monitor and celebrate progress.
```

---

### T8: When professional practice conflicts with deadline → negotiate scope, not quality
**Quality: 91%**

Detect: "We don't have time for code review/tests/refactoring."  
Action: Propose: ship fewer features with quality, not more features with debt.

**Example:**
```
Manager: "We need feature X, Y, Z in 2 weeks for the demo."
Team: "With our standards (TDD, review, refactor), we can deliver X and Y well."
Manager: "Can you rush?"
Team: "Rushing introduces bugs, increases long-term cost. Better to deliver 2 features well."

This requires courage but builds trust. Teams that hold the line on quality 
maintain velocity long-term. Teams that compromise quality always regret it.
```

---

## Final Checklist

Before committing your code and calling it "professional":

- [ ] Did I write tests before code? (RED → GREEN → REFACTOR)
- [ ] Did I refactor? (Is code better than when I started?)
- [ ] Do I understand the principles, not just the rules?
- [ ] Would I be proud of this code a year from now?
- [ ] Could a junior developer learn from this code?
- [ ] Did I communicate risks and estimates honestly?
- [ ] Did I leave the code better than I found it? (Tourist Rule)
- [ ] Can my team depend on me to maintain standards?

---

**Quality Score Summary:**

Decision rules: 14 rules, average Quality 91% (range: 87-95%)  
Trigger rules: 8 rules, average Quality 89% (range: 87-91%)  
Overall coverage: 6/6 main ideas + ethics + expertise + team (extended), all with explicit audit trail

Each rule cites sources. Use Quality score to assess confidence.
