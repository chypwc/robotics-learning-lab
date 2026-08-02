---
name: robotics-capability-audit
description: Audit an implementation-sized robotics capability across learning theory, specification, implementation companion, public API, package architecture, deterministic tests, exclusions, and progress evidence. Use when reviewing capability readiness or closure, checking cross-artifact consistency and traceability, finding duplicated responsibility or scope creep, or deciding whether a robotics milestone has sufficient owned evidence.
---

# Robotics Capability Audit

Trace one bounded capability from intended learning outcome to executable evidence. Keep live status, durable knowledge, requirements, implementation, and interpreted claims in their owning artifacts.

## Select the capability

1. Read the applicable `AGENTS.md`, then `PLAN.md` and the live `CHECKLIST.md`.
2. Ignore files marked as legacy when deciding current work.
3. Identify the active or user-selected capability, its outcome, ordered gates, explicit exclusions, and linked evidence.
4. Do not silently expand the audit to adjacent capabilities or treat broader theory as implementation scope.

## Gather the evidence chain

Locate and inspect, when applicable:

- the theory and retrieval evidence;
- the project-specific specification and acceptance cases;
- the implementation companion;
- public interfaces and package boundaries;
- deterministic unit, integration, and acceptance tests;
- scenario or result manifests;
- verification reports for interpreted claims.

Report a missing artifact only when the capability workflow says it should already exist. Do not demand an implementation companion before implementation starts or a phase report for a component-level deterministic result.

## Compare the contracts

Build a compact comparison across artifacts for:

- equations and algorithm choice;
- frame, axis, sign, ordering, naming, and representation conventions;
- types, dimensions, units, timestamps, identity, and ownership;
- assumptions, valid domains, tolerances, validation, failure, and state-mutation behaviour;
- determinism, reproducibility, concurrency, and operational boundaries;
- exclusions, deferred work, and safety or performance claim limits.

Invoke `$cpp-quality-gate` or `$python-quality-gate` for language-specific implementation review. Invoke `$scientific-numerics-review` when mathematical or numerical behaviour is material.

## Check responsibility and evidence ownership

- Ensure theory teaches reusable concepts without project status or implementation commentary.
- Ensure the specification owns requirements, interfaces, acceptance criteria, and exclusions.
- Ensure the companion owns durable equation-to-software mapping and engineering cautions without duplicating theory.
- Ensure production code owns behaviour and automated tests own deterministic evidence.
- Require a verification report only for milestones, experiments, benchmarks, safety or performance claims, negative results, or evidence requiring interpretation.
- Ensure `CHECKLIST.md` links evidence and records status without copying results.
- Detect duplicated algorithms, validation, limits, metrics, scenario definitions, or safety responsibility across packages.

## Verify proportionately

Run read-only checks and the smallest relevant tests needed to validate the audit. Re-run acceptance cases when source changed or when the existing evidence cannot support the current claim. Inspect configured builds, renders, and local links when their artifacts are in scope. Do not edit during an audit unless the user requests fixes.

## Decide readiness

Separate:

- closure blockers that violate a required contract or leave required evidence absent;
- non-blocking defects explicitly accepted by the user;
- missing coverage that weakens evidence without contradicting behaviour;
- optional improvements and later-phase work.

Lead with the readiness decision, then findings ordered by severity with exact artifact references. State tests and checks run, skipped checks, residual warnings, accepted limitations, and whether live checklist status should change. Never mark a capability complete merely because representative tests pass.
