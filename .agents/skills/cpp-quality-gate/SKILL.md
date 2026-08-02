---
name: cpp-quality-gate
description: Review and verify C++ source, headers, CMake, ament_cmake packages, Eigen code, public interfaces, and GTest changes in this robotics repository. Use when adding, modifying, diagnosing, or reviewing C++ implementation or tests; changing CMake targets or compiler settings; preparing a C++ capability for verification; or explicitly requesting a C++ quality gate.
---

# C++ Quality Gate

Apply a focused, evidence-backed quality gate to the C++ work in scope. Follow the repository's own contracts and tools instead of imposing a generic style rewrite.

## Establish the contract

1. Read the applicable `AGENTS.md`, then `PLAN.md` and `CHECKLIST.md` when they exist.
2. Identify the active capability, owning specification, implementation companion, public headers, source files, and deterministic tests.
3. Distinguish a review or diagnosis request from an implementation request. Do not edit code during a review unless the user asks for fixes.
4. Preserve unrelated worktree changes and inspect the existing build and lint configuration before proposing new tooling.

## Review the design

- Trace each algorithmic component to a documented equation or engineering requirement.
- Keep modules and functions single-purpose. Check names, types, dimensions, frames, units, assumptions, invariants, valid domains, and failure behaviour.
- Make ownership and lifetime explicit. Prefer RAII, value semantics, standard containers, and narrow interfaces; justify shared ownership or manual resource management.
- Check const-correctness, reference and value choices, exception or status semantics, and input non-mutation where promised.
- Keep pure mathematical cores independent of ROS, Gazebo, file I/O, and global state when the specification requires that boundary.
- For Eigen code, check fixed-versus-dynamic dimensions, compatible scalar types, aliasing, expression lifetimes, alignment only where required, and validated matrix structure.
- Reject speculative abstractions, dependencies, and framework integration that are outside the active capability.

## Review numerical and operational behaviour

- Check finite inputs, intermediate overflow, non-finite outputs, singular or ill-conditioned cases, branch conventions, tolerance policy, and deterministic handling of ambiguous cases.
- Check frame and sign conventions at every interface. Do not allow dimensionally compatible values to hide semantic frame or unit errors.
- Verify bounds, cancellation, shutdown, logging, and timing behaviour when the component owns operational state.
- Invoke `$scientific-numerics-review` as well when mathematical or floating-point correctness is material.

## Build and test

1. Discover the repository's configured commands before running tools.
2. Build the smallest affected target or package first. For ROS workspaces, prefer focused `colcon build` and `colcon test` commands over rebuilding unrelated packages.
3. Run configured formatting and static-analysis checks such as `clang-format` and `clang-tidy` only when their configuration and compilation database are available. Do not format unrelated files.
4. Run focused GTest or CTest cases, then the affected package suite.
5. Use sanitizers only when the target and environment support them and the added cost is proportionate to the risk.
6. If files changed, run `git diff --check`, inspect the affected diff and source regions, and repeat the relevant build and tests.

## Judge the tests

Prioritise tests for equations, public contracts, invariants, edge cases, invalid inputs, failure non-mutation, integration boundaries, and observed defects. Use independent analytic cases or oracles where possible. Do not add tests for trivial accessors, generated boilerplate, or unchanged library behaviour unless they protect a deliberate contract.

## Report the gate

Lead with pass or fail. List actionable findings by severity with exact file references, explain the violated contract and consequence, and distinguish implementation defects from missing evidence or optional improvements. Record commands and results. Do not claim the gate passed when a required check was skipped or failed.
