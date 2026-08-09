# Domain Modeling Made Functional — Purpose

## Why This Book Matters

**Central Problem:** Teams build software without truly understanding the domain. Requirements get mistranslated. Code diverges from business reality. Changes become expensive because code doesn't reflect actual business processes.

**The Cost:**
- Miscommunication between domain experts and developers
- Code doesn't match how business actually works
- Changes to requirements require large refactors
- Domain knowledge lost when experts leave
- Bugs because code assumptions don't match business rules

## What This Book Teaches

"Domain Modeling Made Functional" by Scott Wlaschin teaches how to:

- Discover domain through event storming
- Build shared mental model with domain experts
- Use Ubiquitous Language (business terminology in code)
- Design domain models that encode business rules
- Use functional programming to keep domain logic pure
- Organize code around business workflows, not technical layers

## The Core Insight

**Software is a communication problem before it's a coding problem.**

The primary value of code isn't that it works—it's that it communicates the domain to developers who read it. If code doesn't match how the business actually works, it's wrong, even if it executes correctly.

**Key distinction:**
- Bad domain modeling: Code has OrderBase abstract class, Order and Quote subclasses, flags scattered everywhere
- Good domain modeling: Code has Order, Quote, ValidatedOrder, PricedOrder—each state is a distinct type encoding valid transitions

## The Process

1. **Listen** to domain experts (not assumptions)
2. **Model** the domain through events and workflows
3. **Encode** business rules in types (making invalid states impossible)
4. **Keep** domain logic pure (separate from infrastructure)
5. **Test** that model matches business reality

## Who Should Read This

- **Architects** designing systems for evolving requirements
- **Teams** building complex business software
- **Leads** struggling with requirements changes causing massive refactors
- **Developers** learning Domain-Driven Design (DDD)
- **Anyone** using F# (the book uses F# to demonstrate functional domain modeling)

## What You'll Learn

15 principles about:
- Discovering domain through deep listening
- Building shared mental models
- Using types to encode business rules
- Keeping domain logic separate from persistence
- Organizing code around business workflows, not layers
- Making invalid states impossible

---

## Tags
#domain-driven-design, #domain-modeling, #ubiquitous-language, #functional-programming, #business-logic, #event-storming, #type-systems

## Source
Wlaschin, S. (2018). Domain Modeling Made Functional. Pragmatic Bookshelf.
