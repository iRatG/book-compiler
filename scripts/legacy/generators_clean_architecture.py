"""
Specialized JSON Generator for Clean Architecture book.

Customizes principle generation with book-specific metrics, scenarios, and anti-patterns.
"""

from typing import Dict, List, Any
from generate_llm_instructions import JSONGenerator


class CleanArchitectureGenerator(JSONGenerator):
    """Generate JSON for Clean Architecture with domain-specific content."""

    def _generate_metrics(self, principle_id: str) -> List[Dict]:
        """Generate practical metrics specific to Clean Architecture principles."""

        metrics_by_principle = {
            'principle_1': [
                {
                    'name': 'Architectural Consistency Score',
                    'formula': 'violations_found / total_architectural_boundaries * 100',
                    'how_to_measure': 'Code review: check if architects reviewed implementation. Track violations.',
                    'good_value': '0-5% violations',
                    'bad_value': '> 20% (architecture design not matching implementation)',
                    'example': {
                        'scenario': 'Architect designed boundaries in documentation, developers implemented differently',
                        'calculation': '3 violations / 10 boundaries = 30% inconsistency',
                        'interpretation': 'BAD: Architecture and implementation diverged'
                    }
                }
            ],
            'principle_2': [
                {
                    'name': 'Cost per Feature',
                    'formula': 'total_hours_per_release / number_of_features_delivered',
                    'how_to_measure': 'Track in sprint board. Hours / features per release.',
                    'good_value': 'Should stay ±10% across releases',
                    'bad_value': 'Increases > 15% per release (exponential growth)',
                    'example': {
                        'scenario': 'Tracking velocity across releases',
                        'calculation': 'v1: 200h/10 features=20h/feature | v2: 200h/8 features=25h/feature (+25%)',
                        'interpretation': 'BAD: Architecture degrading'
                    }
                },
                {
                    'name': 'Blast Radius (files changed per logic change)',
                    'formula': 'number_of_files_modified / number_of_business_rule_changes',
                    'how_to_measure': 'Git diff: count files changed per logical change',
                    'good_value': '< 3 files per business rule change',
                    'bad_value': '> 10 files (tight coupling)',
                    'example': {
                        'scenario': 'Change discount calculation logic',
                        'calculation': 'Bad: 15 files (DB, API, UI, validators). Good: 2 files (UseCase, test)',
                        'interpretation': 'Good = low coupling, easy to change'
                    }
                },
                {
                    'name': 'Test Suite Feedback Time',
                    'formula': 'seconds_to_run_unit_tests',
                    'how_to_measure': 'CI/CD pipeline, time unit tests complete',
                    'good_value': '< 30 seconds',
                    'bad_value': '> 5 minutes (developers skip tests)',
                    'example': {
                        'scenario': 'Unit tests integration time',
                        'calculation': 'Bad: 8 minutes (coupled to DB). Good: 10 seconds (mocked)',
                        'interpretation': 'Fast tests = fast feedback = fast changes'
                    }
                }
            ],
            'principle_3': [
                {
                    'name': 'Behavior vs Architecture Trade-off Score',
                    'formula': 'days_architectural_work / total_sprint_days',
                    'how_to_measure': 'Sprint planning: track hours spent on architecture vs features',
                    'good_value': '20-30% of sprint time on architecture/refactoring',
                    'bad_value': '< 10% (technical debt growing) OR > 50% (too much architecture)',
                    'example': {
                        'scenario': '2-week sprint time allocation',
                        'calculation': '3 days architecture / 10 sprint days = 30%',
                        'interpretation': 'GOOD: Balanced investment'
                    }
                }
            ],
            'principle_4': [
                {
                    'name': 'Test Coverage by Layer',
                    'formula': 'covered_lines / total_lines * 100 (measure by layer)',
                    'how_to_measure': 'Code coverage tool (Istanbul, Coverage.py, etc)',
                    'good_value': 'Business logic: > 80% | Controllers/UI: > 60%',
                    'bad_value': '< 40% overall or > 20% critical path untested',
                    'example': {
                        'scenario': 'OrderUseCase test coverage',
                        'calculation': 'Business logic: 95% covered (good). API Controller: 50% (acceptable)',
                        'interpretation': 'Core logic covered, adaptation layer less critical'
                    }
                },
                {
                    'name': 'Defect Escape Rate',
                    'formula': 'defects_found_in_production / total_defects * 100',
                    'how_to_measure': 'Bug tracking: compare PRE-release vs POST-release defects',
                    'good_value': '< 5%',
                    'bad_value': '> 20% (tests not catching bugs)',
                    'example': {
                        'scenario': '100 total defects found in release',
                        'calculation': '90 found in QA, 10 in production = 10% escape',
                        'interpretation': 'Tests could have caught those 10'
                    }
                }
            ],
            'principle_5': [
                {
                    'name': 'Paradigm Compliance Score',
                    'formula': 'correctly_used_paradigms / total_code_sections * 100',
                    'how_to_measure': 'Code review: verify Structured/OOP/Functional at right layers',
                    'good_value': '> 80% compliance',
                    'bad_value': '< 60% (mixed paradigms at wrong levels)',
                    'example': {
                        'scenario': 'Architecture review',
                        'calculation': '8/10 modules follow paradigm rules = 80%',
                        'interpretation': 'Good'
                    }
                }
            ],
            'principle_6': [
                {
                    'name': 'Paradigm Distribution',
                    'formula': 'Count modules by primary paradigm (Structured % / OOP % / Functional %)',
                    'how_to_measure': 'Classify modules in architecture review',
                    'good_value': 'Distributed across all three (no single paradigm > 70%)',
                    'bad_value': '90% OOP (over-engineering) or 100% Functional (too abstract)',
                    'example': {
                        'scenario': 'System composition',
                        'calculation': 'Structured: 30% | OOP: 35% | Functional: 35%',
                        'interpretation': 'GOOD: Balanced'
                    }
                }
            ]
        }

        return metrics_by_principle.get(principle_id, super()._generate_metrics(principle_id))

    def _generate_code_review_checklist(self, principle_id: str) -> List[str]:
        """Generate code review checklist specific to Clean Architecture."""

        checklists = {
            'principle_1': [
                '☐ Are architects reviewing this implementation?',
                '☐ Does design match what was actually coded?',
                '☐ Can architects explain the architectural intent?',
                '☐ Will juniors understand why this boundary exists?',
            ],
            'principle_2': [
                '☐ Does this change touch only 1-3 files (low blast radius)?',
                '☐ Can I change the database without touching this code?',
                '☐ Can I change the API/UI without touching business logic?',
                '☐ Are dependencies injected or hardcoded?',
                '☐ If I need to test this, how many mocks do I need?',
            ],
            'principle_3': [
                '☐ Does this prioritize behavior over architecture OR includes minimal architectural polish?',
                '☐ Is there technical debt being tracked (not just ignored)?',
                '☐ Is refactoring time allocated in this sprint?',
            ],
            'principle_4': [
                '☐ Can this code be tested without a database?',
                '☐ Are tests isolated (one test failure = one problem)?',
                '☐ Is the test feedback time < 30 seconds?',
                '☐ Would skipping this test slow down future changes?',
            ],
            'principle_5': [
                '☐ Is business logic structured (sequences, conditionals, loops)?',
                '☐ Are polymorphic boundaries using OOP abstraction?',
                '☐ Are data transformations using functional patterns (immutable)?',
            ],
            'principle_6': [
                '☐ Does this module use ALL THREE paradigms appropriately?',
                '☐ Is Structured used within modules?',
                '☐ Is OOP used at boundaries?',
                '☐ Is Functional used for data flow?',
            ]
        }

        return checklists.get(principle_id, super()._generate_code_review_checklist(principle_id))

    def _generate_warnings(self, principle_id: str) -> List[str]:
        """Generate red flags specific to Clean Architecture violations."""

        warnings = {
            'principle_1': [
                '⚠️ Architects not participating in code reviews',
                '⚠️ Implementation deviates from documented design',
                '⚠️ Juniors confused about architectural intent',
            ],
            'principle_2': [
                '⚠️ Effort per feature increasing release-over-release',
                '⚠️ Change requires modifying > 5 files',
                '⚠️ Tests take > 5 minutes to run',
                '⚠️ New junior can\'t add a feature without help',
            ],
            'principle_3': [
                '⚠️ No refactoring time allocated this sprint',
                '⚠️ Technical debt list ignored',
                '⚠️ All time goes to features, zero to structure',
            ],
            'principle_4': [
                '⚠️ Test coverage < 40%',
                '⚠️ Tests depend on database/filesystem/API',
                '⚠️ Defects found in production, not QA',
                '⚠️ Test run time > 2 minutes for unit tests',
            ],
            'principle_5': [
                '⚠️ Goto statements or spaghetti control flow',
                '⚠️ Functions > 500 lines',
                '⚠️ Function has > 7 parameters',
            ],
            'principle_6': [
                '⚠️ 100% OOP (deep inheritance hierarchies)',
                '⚠️ 100% Functional (impossible to model domain)',
                '⚠️ No structure at all (chaotic control flow)',
            ]
        }

        return warnings.get(principle_id, super()._generate_warnings(principle_id))

    def _generate_scenarios(self, principle: Dict, reasoning: Dict, consequences: Dict) -> List[Dict]:
        """Generate real Clean Architecture scenarios with costs."""

        scenarios_by_principle = {
            'principle_1': [
                {
                    'scenario': 'Architects design, developers implement without collaboration',
                    'bad_approach': {
                        'description': 'Architects create UML diagrams, hand off to developers',
                        'code': '// Diagram says: "Use MVC pattern with dependency injection"\n// Developer interprets: tight coupling is faster',
                        'cost': '6 months: divergence discovered, major refactoring required',
                        'problem': 'Architects never saw actual code. Developers never understood intent.'
                    },
                    'good_approach': {
                        'description': 'Architect pair-programs first module with developer',
                        'code': '// Architect shows: why boundaries matter\n// Why dependencies must flow inward\n// Developer learns by doing',
                        'cost': '1 week extra on first module, saves months on rest',
                        'why_works': 'Knowledge transfer + real constraints surface early'
                    }
                }
            ],
            'principle_2': [
                {
                    'scenario': 'Change discount calculation logic',
                    'bad_approach': {
                        'description': 'Discount logic mixed into OrderProcessor with DB, email, analytics',
                        'code': 'class OrderProcessor {\n  process(order) {\n    db.save(order);\n    email.send(order);\n    analytics.log(order);\n  }\n}',
                        'cost': 'v1: 2 weeks. v2: 4 weeks (2x slower). v3: 8 weeks. v4: 16 weeks.',
                        'problem': 'Touch 1 thing = change DB, email, analytics. All must be retested.'
                    },
                    'good_approach': {
                        'description': 'Discount logic isolated, dependencies injected',
                        'code': 'function calculateDiscount(user, history) {\n  if (user.isVIP) return 0.2;\n  if (history.totalSpent > 10000) return 0.1;\n  return 0;\n}\n\nclass OrderService {\n  process(order) {\n    const discount = calculateDiscount(user, history);\n    order.applyDiscount(discount);\n  }\n}',
                        'cost': 'v1: 3 weeks. v2: 3 weeks. v3: 3 weeks (stable).',
                        'why_works': 'Discount function testable alone. No side effects. Simple to change.'
                    }
                },
                {
                    'scenario': 'Add new payment method (PayPal, Stripe, Apple Pay)',
                    'bad_approach': {
                        'description': 'Each payment method requires modifying OrderProcessor',
                        'code': 'if (paymentMethod == "paypal") { /* paypal code */ }\nif (paymentMethod == "stripe") { /* stripe code */ }\nif (paymentMethod == "applepay") { /* applepay code */ }',
                        'cost': 'Each payment method: 2 days. 3 methods = 6 days. 10th method: still 2 days (ok). But risk is high.',
                        'problem': 'Each change touches same file. Each must be fully tested.'
                    },
                    'good_approach': {
                        'description': 'Payment method implements interface. Injected at runtime.',
                        'code': 'interface PaymentGateway {\n  validate(payload);\n  charge(amount);\n}\nclass PayPalGateway implements PaymentGateway { ... }\nclass StripeGateway implements PaymentGateway { ... }\n\nclass PaymentProcessor {\n  constructor(gateway: PaymentGateway) { }\n  process() { this.gateway.charge(amount); }\n}',
                        'cost': 'v1: 2 days to add PayPal interface. v2: 1 day (Stripe implements). v3: 1 day (Apple Pay).',
                        'why_works': 'New payment = 1 new file. No existing code modified. Low risk.'
                    }
                }
            ],
            'principle_3': [
                {
                    'scenario': 'Pressure: "Ship feature by Friday"',
                    'bad_approach': {
                        'description': 'Skip architecture. Just make it work.',
                        'code': '// Quick hack: hardcode discount logic\nif (user.isVIP) total = total * 0.8;\nelse total = total * 0.95;',
                        'cost': 'Friday: shipped (1 day faster). Monday: new requirement breaks logic. By v3: unmaintainable.',
                        'problem': 'Felt fast initially. Actually slow when change comes.'
                    },
                    'good_approach': {
                        'description': 'Invest minimal architecture + Friday deadline',
                        'code': 'interface DiscountRule { applies(user); amount(user); }\nclass VIPRule implements DiscountRule { ... }\n// Add rules via interface, not if statements',
                        'cost': 'Friday: shipped (2 hours slower). New requirement: 10 minutes to add new rule.',
                        'why_works': 'Urgency + architecture possible if you do it right'
                    }
                }
            ],
            'principle_4': [
                {
                    'scenario': 'Bug found in production. How fast can you fix and verify?',
                    'bad_approach': {
                        'description': 'Business logic mixed with database. No isolated tests.',
                        'code': 'function processOrder() {\n  const user = db.query("SELECT...");\n  const discount = calculateDiscount(user);\n  db.save(order);\n}',
                        'cost': 'Find bug: 2 hours. Reproduce locally: 4 hours (need DB setup). Fix: 1 hour. Deploy: 1 hour. Total: 8 hours.',
                        'problem': 'Can\'t test logic without full database setup. Manual testing required.'
                    },
                    'good_approach': {
                        'description': 'Business logic isolated. Fast unit tests.',
                        'code': 'function calculateDiscount(user) { ... } // Pure function\ntest("discount for VIP", () => {\n  const discount = calculateDiscount({isVIP: true});\n  assert(discount == 0.2);\n});',
                        'cost': 'Find bug: 2 hours. Test locally: 30 sec. Fix + verify: 1 hour. Deploy: 1 hour. Total: 4 hours.',
                        'why_works': 'Tests run in seconds. No DB setup. Confidence high.'
                    }
                }
            ],
            'principle_5': [
                {
                    'scenario': 'Complex algorithm: calculate shipping cost',
                    'bad_approach': {
                        'description': 'Spaghetti control flow. Hard to test.',
                        'code': 'function calculateShipping() {\n  if (weight < 5) goto small;\n  if (country == "US") goto domestic;\n  // 50 lines of nested ifs\n}',
                        'cost': 'Hard to test. Hard to modify. Easy to break.',
                        'problem': 'Control flow is unclear. Edge cases hide.'
                    },
                    'good_approach': {
                        'description': 'Structured decomposition. Clear flow.',
                        'code': 'function calculateShipping(order) {\n  const baseRate = getBaseRate(order.weight);\n  const regional = getRegionalMultiplier(order.country);\n  const rush = getRushMultiplier(order.expedited);\n  return baseRate * regional * rush;\n}',
                        'cost': 'Clear logic. Easy to test. Easy to modify.',
                        'why_works': 'Each function does one thing. Composition is clear.'
                    }
                }
            ],
            'principle_6': [
                {
                    'scenario': 'Design a payment system using all three paradigms',
                    'bad_approach': {
                        'description': '100% OOP: deep inheritance hierarchies, hard to test',
                        'code': 'PaymentProcessor -> StripePaymentProcessor -> StripeUSDPaymentProcessor',
                        'cost': 'Fragile. Adding new currency = create new subclass. Changing logic = affects all subclasses.',
                        'problem': 'Over-engineered, tightly coupled'
                    },
                    'good_approach': {
                        'description': 'Structured logic + OOP boundaries + Functional data transform',
                        'code': '// Structured: clear algorithm\nfunction processPayment(order, gateway) {\n  validate(order);\n  charge(gateway, amount);\n  updateLedger(order);\n}\n\n// OOP: polymorphic gateway\ninterface PaymentGateway { charge(amount); }\nclass StripeGateway implements PaymentGateway { ... }\n\n// Functional: transform data\nconst ledgerEntry = {\n  ...order,\n  charged: true,\n  timestamp: now()\n};',
                        'cost': 'Clear, testable, modular. Adding payment method = 1 class. Changing algorithm = 1 function.',
                        'why_works': 'Right tool for each job'
                    }
                }
            ]
        }

        principle_id = principle.get('id')
        return scenarios_by_principle.get(principle_id, super()._generate_scenarios(principle, reasoning, consequences))

    def _generate_anti_patterns(self, principle_id: str) -> List[Dict]:
        """Generate Clean Architecture anti-patterns."""

        anti_patterns = {
            'principle_2': [
                {
                    'name': 'God Object Pattern',
                    'looks_right': 'OrderProcessor handles all order logic. Seems "complete" and "efficient".',
                    'actually_wrong': 'Touches 7+ dependencies. Any change affects everything. Tests are 500 LOC and fragile.',
                    'cost': 'Initial: seems fast. By v3: impossible to change without breaking something.',
                    'solution': 'Split by behavior: OrderValidator, OrderCalculator, OrderPersistence, OrderNotifier'
                },
                {
                    'name': 'Over-Engineering for Future',
                    'looks_right': 'Built plugin architecture for features we "might need someday"',
                    'actually_wrong': 'Code is 3x more complex. 50% slower to add features. Features never needed plugins anyway.',
                    'cost': 'Dead code. Cognitive load. Maintenance burden.',
                    'solution': 'YAGNI: Design for TODAY\'s change, not hypothetical future. Refactor when needed.'
                },
                {
                    'name': 'Tight Coupling (Hidden Dependencies)',
                    'looks_right': 'OrderService.getUser() directly calls UserService.getUser() which calls DatabaseService',
                    'actually_wrong': 'Can\'t test OrderService without database. Can\'t reuse UserService in different contexts.',
                    'cost': 'Tests require full infrastructure. Tests are slow. Tests are brittle.',
                    'solution': 'Inject dependencies: OrderService(userRepository). Mock in tests.'
                },
                {
                    'name': 'Premature Optimization (Performance over Changeability)',
                    'looks_right': 'We optimized queries. Code is 2% faster.',
                    'actually_wrong': 'Hardcoded SQL in 20 places. Changing schema = massive refactor. Business logic scattered.',
                    'cost': 'v1: +2% speed. v2+: -50% velocity due to change difficulty.',
                    'solution': 'Design for change first. Optimize only measured bottlenecks. Use repository pattern.'
                }
            ],
            'principle_4': [
                {
                    'name': 'High Test Cost (Brittle Tests)',
                    'looks_right': 'We have 90% test coverage!',
                    'actually_wrong': 'Tests depend on database, file system, external API. One small change breaks 100 tests.',
                    'cost': 'High maintenance. Developers avoid changing code. Tests become liability.',
                    'solution': 'Isolate business logic. Mock external dependencies. Tests should run in milliseconds.'
                },
                {
                    'name': '"We\'ll Test Later"',
                    'looks_right': 'Ship faster without tests. We\'ll add tests after.',
                    'actually_wrong': 'Later never comes. Code accumulates. Testing existing code is 5x harder than writing tests first.',
                    'cost': 'Defects in production. Refactoring impossible. Velocity keeps dropping.',
                    'solution': 'TDD: Write test first. Changes are always safe.'
                }
            ]
        }

        return anti_patterns.get(principle_id, super()._generate_anti_patterns(principle_id))

    def _generate_when_not_to_use(self, principle: Dict) -> List[str]:
        """Generate honest 'when NOT to use' for Clean Architecture principles."""

        when_not = {
            'principle_1': [
                'One-off scripts or throw-away prototypes',
                'Proof-of-concept code that will be deleted',
                'When team is 1 person (no communication issues)'
            ],
            'principle_2': [
                'One-off data migration script (run once, discard)',
                'Rapid prototypes (< 2 weeks, will be deleted)',
                'Hard real-time systems where performance MUST override changeability'
            ],
            'principle_3': [
                'Emergency bug fixes (fix now, refactor later)',
                'Startup MVP where speed-to-market is existential',
                'Experiments where you\'ll throw away the code'
            ],
            'principle_4': [
                'One-off scripts (100% test coverage is overkill)',
                'Glue code that won\'t change (low ROI on testing)',
                'Prototype code being thrown away'
            ],
            'principle_5': [
                'Performance-critical tight loops (sometimes goto-like patterns needed)',
                'Heavily optimized systems (structure may sacrifice readability for speed)',
                'Legacy code you won\'t modify'
            ],
            'principle_6': [
                'Specialized domains requiring pure Functional (compiler, data processing)',
                'Hard real-time systems requiring pure performance mindset',
                'Simple scripts where paradigm mixing adds complexity'
            ]
        }

        principle_id = principle.get('id')
        return when_not.get(principle_id, super()._generate_when_not_to_use(principle))

    def _generate_context_qualifiers(self, principle_id: str) -> Dict[str, str]:
        """Generate Clean Architecture context qualifiers."""

        contexts = {
            'principle_2': {
                'for_monolith': 'Fully applicable. Minimize cost of change within the monolith.',
                'for_microservices': 'Apply at service boundary. Each service minimizes its own change cost.',
                'for_ui_only': 'Adapt for frontend: component isolation, state management, testability.',
                'for_startup': 'Balance with speed-to-market. Good architecture enables faster pivots.',
                'for_embedded': 'Performance constraints may override change cost. Use as tiebreaker.',
            },
            'principle_4': {
                'for_monolith': 'Test everything. Monolith has no deployment boundaries to contain failures.',
                'for_microservices': 'Each service fully tested. Service boundary prevents cascading failures.',
                'for_ui_only': 'Test logic separately from rendering. Mock browser DOM.',
                'for_startup': 'Test critical path early. Less critical features can catch up.',
                'for_embedded': 'Embedded systems often can\'t be easily tested post-deployment. Test thoroughly.',
            }
        }

        return contexts.get(principle_id, super()._generate_context_qualifiers(principle_id))

    def _generate_implementation_steps(self, principle_id: str) -> List[Dict]:
        """Generate Clean Architecture implementation roadmap."""

        steps = {
            'principle_2': [
                {
                    'step': 1,
                    'name': 'Identify business core',
                    'action': 'Find code that NEVER changes vs code that changes every release. Business logic = core.',
                    'time': '1-2 days'
                },
                {
                    'step': 2,
                    'name': 'Separate business logic from delivery',
                    'action': 'Extract business logic to pure functions. Database/API/UI = delivery details.',
                    'time': '1-2 sprints'
                },
                {
                    'step': 3,
                    'name': 'Inject dependencies',
                    'action': 'Pass Database, EmailService as constructor args. Stop hardcoding.',
                    'time': '1-2 sprints'
                },
                {
                    'step': 4,
                    'name': 'Measure baseline',
                    'action': 'Start tracking cost per feature BEFORE and AFTER. Measure Blast Radius.',
                    'time': '1 sprint'
                },
                {
                    'step': 5,
                    'name': 'Iterate',
                    'action': 'Each sprint: one boundary or layer gets cleaned up.',
                    'time': 'Ongoing'
                }
            ],
            'principle_4': [
                {
                    'step': 1,
                    'name': 'Write tests for critical path',
                    'action': 'Find code that would break the business if it failed. Test that first.',
                    'time': '1-2 sprints'
                },
                {
                    'step': 2,
                    'name': 'Move to TDD for new code',
                    'action': 'All new features: write test first.',
                    'time': 'Immediate'
                },
                {
                    'step': 3,
                    'name': 'Isolate business logic',
                    'action': 'Can tests run without database? If not, refactor.',
                    'time': '1-2 sprints'
                },
                {
                    'step': 4,
                    'name': 'Track metrics',
                    'action': 'Defect escape rate. Test coverage by layer. Test feedback time.',
                    'time': 'Ongoing'
                }
            ]
        }

        return steps.get(principle_id, super()._generate_implementation_steps(principle_id))
