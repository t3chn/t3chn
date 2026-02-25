# Manifesto

> Automate the work. Never automate the accountability.

## Vision

AI leverage compounds. Build the rails now, or pay for drift forever.

Tools, processes, and interfaces — machine-first. Every workflow must be callable, inspectable, and replayable by a machine. Retrofitting agents onto human-only workflows is drag that compounds. The source of truth is code, schemas, and CI state — not screenshots, not wikis, not chat history. Human UI is a projection, not the source.

Don't patch old workflows with agents. Rebuild from the assumption that agents act, and humans govern.

## Principles

1. **Delegate by default.** If an agent can do it, an agent does it. Manual work is a justified exception, documented as such. Every delegation leaves an artifact trail: diff, tests, commands run. No artifact — no delegation.

2. **Context is a product.** A task without inputs, constraints, acceptance criteria, and explicit non-goals is not a task — it's a prayer. Stop and ask. Bad context doesn't produce bad output; it produces confident wrong output.

3. **Tests as contracts.** Agents write code, tests verify it. No test — no trust. If it can't be tested, add runtime assertions, a rollback plan, and a comment explaining why. No silent behavior changes. Ever.

4. **Atomic changes, bounded scope.** One diff, one purpose, one revert path. Features, refactors, and dependency bumps do not share a commit. Agents must not exceed the scope of the task — a 3-file fix that becomes a 30-file refactor is scope violation, not initiative.

5. **Standards are machine gates.** Types, schemas, linters, CI — not prose in a wiki. If a machine can't enforce it, it's a suggestion. CI is the policy engine.

6. **Living project memory.** README, ADRs, structured memory, runbooks — agents don't relearn from zero every session. If only one person can explain it, it's not knowledge — it's debt. Memory is a first-class deliverable. Every behavior change updates memory in the same PR.

7. **Blast radius scales with the agent.** Mistakes propagate at machine speed. Least privilege by default, explicit permission escalation, immutable logs of every agent action. Zero secrets in prompts. Zero secrets in chat history.

8. **Deterministic environment.** One command from clean checkout to running tests. Pinned deps, reproducible builds, no ambient state. If the agent has to guess, the environment is broken.

9. **Feedback loops close the system.** Measure what agents produce: revert rate, test pass rate, scope creep frequency. Detect drift before it compounds. Every failure is a signal — capture it, fix the process, update memory. A system that doesn't improve from its mistakes is not a system — it's a script.

10. **Humans own outcomes.** Agents amplify capability; they do not transfer responsibility. The human steers, verifies, signs off. "The agent did it" is not an excuse.

## Anti-Principles

1. **No RPA development.** If an agent parses UI to extract data, scrapes diffs to understand intent, or infers requirements from unstructured tickets — the process is broken. Agents are not compensators. Fix the process.

2. **No vibe merges.** No merges without gates passing. No --no-verify. No "it looks fine." Gates define done — not confidence, not consensus, not deadlines. If a gate is skipped, it's recorded and justified in the PR.

3. **No lazy context.** "Just fix it," a screenshot of an error, a paraphrased log — these are not prompts. Prompts have full commands, full traces, and minimal reproducible cases. You get the output your context deserves.

4. **No silent autonomy.** Agents state assumptions before acting, show diffs before merging, report everything they ran. No audit trail means no work — not incomplete work, not unverifiable work: no work.

## Exceptions

Every principle above is a default, not a dogma. Exceptions require justification, not permission — document the exception, the reasoning, and the re-sync plan in the same PR. An unjustified exception is a violation; a justified one is engineering judgment.

---

v1.1 / 2026-02
