---
name: scientific-numerics-review
description: Audit mathematical and scientific software for equation fidelity, notation, units, frames, sign conventions, numerical domains, floating-point behaviour, deterministic validation, and independent verification. Use for robotics kinematics, dynamics, estimation, optimisation, control, simulation, machine-learning models with physical structure, numerical C++ or Python code, or any request to compare theory with implementation and tests.
---

# Scientific Numerics Review

Audit the complete mathematical contract, not only whether representative tests pass. Treat physical meaning, representation, floating-point behaviour, and evidence as separate concerns.

## Assemble the model contract

1. Read the applicable project instructions and the owning theory, specification, implementation companion, API, and tests.
2. Write a compact internal map of inputs, outputs, spaces or dimensions, frames, units, sign conventions, assumptions, valid domains, tolerances, and exclusions.
3. Map every implemented equation to its source equation and every scientific claim to an evidence owner.
4. Preserve the distinction between a physical object or motion and its coordinate representation.

## Check mathematical fidelity

- Re-derive the essential equation independently and compare factors, signs, transpose or inverse direction, multiplication order, indexing, and branch choices.
- Check dimensional consistency through intermediate expressions, not only inputs and outputs.
- Check that reduced representations retain their declared assumptions and are not silently treated as general models.
- Contrast confusable quantities such as point and free vector, body and spatial velocity, active motion and coordinate change, state and measurement, or exact and approximate integration.
- Confirm that exclusions in the specification remain excluded from the implementation and its claims.

## Check the numerical domain

- Test identity, zero, small-magnitude, nominal, boundary, near-singular, invalid, non-finite, and extreme finite cases when applicable.
- Inspect intermediate overflow and underflow, cancellation, loss of significance, angle reduction, normalisation drift, discontinuous branches, and ill-conditioning.
- Do not accept “all finite inputs” unless finite intermediates and outputs are guaranteed or the contract declares bounded magnitudes and rejection behaviour.
- Require deliberate behaviour for malformed shapes, invalid geometry, impossible states, ambiguous logarithms or inverses, and failed convergence.
- Check that invalid operations return no valid-looking scientific result and do not mutate accepted state unless the contract explicitly says otherwise.

## Build independent evidence

Prefer the strongest practical oracle:

1. analytic closed form or known case;
2. an independently derived equivalent formulation;
3. algebraic or geometric invariant;
4. finite-difference or numerical-refinement comparison;
5. comparison with a trusted library using independently prepared inputs.

For approximate results, declare absolute and relative tolerances with scale and units. Use convergence ratios only in the regime where the expected order is valid. Avoid exact floating-point equality except for deliberately unchanged values or exact representable contracts.

## Check reproducibility

- Control random seeds and record configurations, solver settings, tolerances, data splits, and environment details that affect the result.
- Separate training or tuning data from held-out evaluation.
- Require deterministic acceptance calculations and preserve negative results when they inform a claim.
- Distinguish implementation correctness from model adequacy: exact computation of an incomplete physical model does not establish physical accuracy.

## Report the audit

Lead with whether the scientific contract is coherent. Classify findings as mathematical mismatch, convention or unit mismatch, numerical-domain defect, validation defect, evidence gap, claim overreach, or non-blocking improvement. Give an exact reproducer for numerical defects and cite the conflicting artifacts. Do not edit during an audit unless the user asks for corrections.
