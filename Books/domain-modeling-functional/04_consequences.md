# Domain Modeling Made Functional — Consequences & Application

## APPLICATION 1: Event Storming Workshop
Run event storming session with domain experts and developers:
1. Identify key events (OrderPlaced, PaymentReceived)
2. Identify commands triggering events (PlaceOrder, ReceivePayment)
3. Identify entities affected (Order, Payment, Customer)
4. Identify boundaries (where does responsibility change?)

Result: Shared mental model visible on whiteboard; code later matches this.

---

## APPLICATION 2: Ubiquitous Language Audit
Review codebase:
- Are domain expert terms used in code? YES = good
- Are technical terms mixed with business terms? YES = fix it
- Would domain expert understand the code? NO = rewrite

Establish glossary: Business term = code term. Keep in sync.

---

## APPLICATION 3: Bounded Context Design
Identify contexts:
- Order-Taking (receive and price orders)
- Billing (create invoices, track payments)
- Shipping (manage deliveries)
- Pricing (product prices, discounts)

Each context has:
- Own terminology
- Own rules
- Own database (optional)
- Clear interface for communication

---

## APPLICATION 4: State Machine Modeling
For each entity with lifecycle (Order, Quote, Invoice):
1. Identify all states (UnvalidatedOrder → ValidatedOrder → PricedOrder → OrderPlaced)
2. Identify state transitions (what triggers each?)
3. Implement as separate types (each state is distinct type in code)
4. Compiler ensures no invalid transitions

Example: UnvalidatedOrder.toValidated() returns ValidatedOrder (not Order). Cannot accidentally create validated order twice.

---

## APPLICATION 5: Type-Driven Validation
Encode business rules in types:

```fsharp
type OrderQuantity = private OrderQuantity of int
module OrderQuantity =
    let create qty = 
        if qty > 0 && qty < 1000 then Ok (OrderQuantity qty)
        else Error "Invalid quantity"
```

Invalid quantities cannot be created. Rules enforced by type system, not runtime checks.

---

## APPLICATION 6: Event-Driven Architecture Design
Model workflows as event chains:
1. OrderForm received → PlaceOrder command → Order validated
2. Order validated → OrderPlaced event
3. OrderPlaced event → Billing system listens → Invoice created
4. Invoice created → InvoiceCreated event
5. InvoiceCreated event → Shipping system listens → Prepare shipment

Each event represents something that happened. Commands initiate actions.

---

## APPLICATION 7: Persistence Layer Design
Design persistence to support domain:
- Serialization: Convert domain types to storage format
- Deserialization: Convert storage format back to domain types
- Domain logic remains unchanged if storage format changes

Example: JSON storage → XML storage. Domain types don't change.

---

## APPLICATION 8: Domain Service Design
Services that span contexts or require external data:

```
Calculate Discount service:
- Input: Order, Customer, Product (domain objects)
- Output: Discount (domain value type)
- Pure function (no side effects)
- Can be tested without infrastructure
```

---

## APPLICATION 9: Workflow Testing
Test workflows without persistence:

```
test "placing order should create OrderPlaced event" =
    let order = createTestOrder()
    let event = order.place()
    assert event = OrderPlaced
```

No database needed. Pure logic, pure test.

---

## APPLICATION 10: Documentation as Code
Use domain model as documentation:

```
type Order = {
    orderId: OrderId
    items: OrderLineItem list
    status: OrderStatus // explicit states
    addresses: ShippingAddresses
}
```

Someone reading this knows:
- Orders have multiple line items
- Orders have status (state machine)
- Orders require shipping addresses
- Each order has unique ID

---

## APPLICATION 11: Refactoring for Understanding
When domain understanding improves:
1. Update ubiquitous language
2. Update domain model
3. Update code
4. Update tests

Example: Discover that "pending" orders split into "awaiting payment" and "awaiting inventory". Refactor model to reflect this distinction.

---

## APPLICATION 12: Validation Rules as Domain Types
Capture validation in types:

```
type EmailAddress = private EmailAddress of string
module EmailAddress =
    let create email =
        if Regex.IsMatch(email, emailPattern)
        then Ok (EmailAddress email)
        else Error "Invalid email"
```

Invalid emails cannot be created. Rule enforced by type.

---

## APPLICATION 13: Aggregate Design
An aggregate is a cluster of domain objects that change together:

Order aggregate:
- Order (root)
  - OrderLineItems (parts)
  - ShippingAddress (part)

Invariants maintained at aggregate level. Easier to reason about.

---

## APPLICATION 14: Anti-Corruption Layer
When integrating with external system (different language/concepts):

```
External system: "customer_record"
Your system: "customer"

Anti-corruption layer translates between them.
Your domain code never touches external concepts.
```

Keeps your domain model pure.

---

## APPLICATION 15: Continuous Model Learning
As system evolves and new insights emerge:
1. Update domain model
2. Update ubiquitous language
3. Refactor code
4. Deploy changes

Domain is living thing. Model grows with understanding.

---

## Quarterly Review
- Have new domain insights emerged?
- Does code still match domain?
- Are bounded contexts still appropriate?
- Has ubiquitous language drifted from code?

---

## Tags
#domain-driven-design, #event-driven-architecture, #type-safety, #domain-modeling
