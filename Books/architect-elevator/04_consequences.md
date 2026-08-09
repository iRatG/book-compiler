# The Software Architect Elevator — Consequences & Application

## APPLICATION 1: Riding the Elevator
1. **Up to boardroom:** Understand strategy, budget, timelines
2. **Down to engine room:** Understand technical constraints, real obstacles  
3. **Translate:** Reframe business goals in technical terms; explain technical realities in business terms

Do this consistently to build credibility.

---

## APPLICATION 2: Engagement Audit
- How many hours/week in engine room? (If < 20%: too disconnected)
- How many hours/week in architecture discussions? (If < 50%: architecture gets deprioritized)
- How credible are you with engineers? (Ask them)

---

## APPLICATION 3: Decision Framework
For major architectural decisions:
1. Identify reversible vs. irreversible
2. For irreversible: Use structured decision-making (trade-off matrix)
3. For reversible: Decide quickly; change later if needed
4. Document decision + reasoning (architectural decision record)

---

## APPLICATION 4: Automation Strategy
Identify high-risk manual processes:
- Deployments
- Infrastructure changes
- Configuration management
- Incident response

Prioritize by: impact × frequency

Automate highest-priority first.

---

## APPLICATION 5: Infrastructure-as-Code Adoption
1. Choose target (Terraform, CloudFormation, etc.)
2. Train team on software practices (version control, CI/CD, testing)
3. Migrate configurations to code
4. Add code review for all changes
5. Add CI/CD (automatic apply on merge)

---

## APPLICATION 6: Worldview Documentation
Create Architecture Vision Document:
- What problems are we solving?
- What's our technology strategy?
- Which languages/frameworks do we use?
- Which databases?
- How do we deploy?
- What are non-negotiables vs. recommendations?

Share widely. Update as understanding evolves.

---

## APPLICATION 7: Bias Mitigation
For major decisions:
1. Create trade-off matrix (options vs. criteria)
2. Involve people with different perspectives
3. Challenge assumptions explicitly
4. Look for disconfirming evidence, not just confirming

---

## APPLICATION 8: Organizational Transformation
1. Identify desired behavior (fast deployments, autonomous teams)
2. Reverse-engineer required beliefs (errors are ok, teams trusted)
3. Create evidence (show success stories)
4. Change incentives (reward fast deployments)
5. Restructure if needed (reduce approval layers)

---

## APPLICATION 9: Meeting Reduction
Audit calendar:
- Which meetings could be async (written update + comments)?
- Which require real-time discussion?
- Which are "just in case" and never contribute?

Convert to async. Eliminate unnecessary.

Target: <10 meetings/week for architects.

---

## APPLICATION 10: Decision Communication
Don't: "We're using Kubernetes."
Do: "We evaluated Docker Swarm vs. Kubernetes. K8s won because [specific reasons]. Trade-off: [cost]. Opportunity cost: [what we gave up]. This decision is reversible by [date/cost]."

Story beats mandate.

---

## APPLICATION 11: Culture Assessment
Beliefs to evaluate:
- "Change is risky" vs. "Not changing is risky"
- "Specialists better than generalists"  
- "Technology first" vs. "Business value first"
- "Follow the plan" vs. "Adapt to reality"

Ask teams. Document. Plan culture shifts.

---

## APPLICATION 12: Credibility Building
1. Engage in code reviews (shows understanding)
2. Help debug critical issues (builds respect)
3. Make and admit small decisions (builds track record)
4. Deliver on promises (builds trust)

Don't:
- Blame people for problems
- Make decisions without understanding consequences
- Disappear during crises

---

## APPLICATION 13: Strategy Articulation
Write down:
- Where are we (current state)?
- Where do we want to go (vision)?
- What are the obstacles?
- How do we get there (roadmap)?
- What are the milestones?

Update quarterly.

---

## APPLICATION 14: Reversibility Evaluation
For each major decision:
- How reversible is this? (1-5 scale, 5 = completely reversible)
- If irreversible, when should we decide (now vs. defer)?
- What information would make us more confident?
- Can we run experiment first?

---

## APPLICATION 15: Quarterly Architect Retrospective
- Did you ride the elevator?
- Did you maintain credibility?
- Did you enable change or block it?
- What did teams learn from you?
- What did you learn from teams?

---

## Tags
#leadership, #organizational-change, #strategy, #execution
