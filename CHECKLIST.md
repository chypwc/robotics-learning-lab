# Project Intelligence Checklist

This checklist operationalises [PLAN.md](PLAN.md) under the project rules in [AGENTS.md](AGENTS.md). `PLAN.md` remains the source for rationale and detailed explanations; this file records execution and evidence.

## How to use this checklist

- Keep only one capability phase active at a time.
- Complete the reusable gates for every capability phase after Phase 0.
- Add a link or path to evidence when checking an important item.
- Mark a phase complete only when all exit evidence exists.
- Correct blocking gaps before proceeding; place non-blocking improvements in the backlog.
- Do not restart an entire learning cycle because of one failed test. Review the missed concept, retest it, and continue.

## Programme status

- [x] Create the detailed project plan.
- [x] Create the root project rules.
- [x] Phase 0 — Development environment.
- [ ] Phase 1 — Geometry, mechanics, and control.
- [ ] Phase 2 — Probability and state estimation.
- [ ] Phase 3 — Perception and semantic understanding.
- [ ] Phase 4 — Mapping, SLAM, and memory.
- [ ] Phase 5 — Planning and autonomous decision-making.
- [ ] Phase 6 — Advanced reinforcement learning.
- [ ] Phase 7 — World models and imagined futures.
- [ ] Phase 8 — Aerospace theory and UAV transfer.
- [ ] Phase 9 — Integrated research release.

## Programme controls

- [ ] Record the available study and engineering hours per week.
- [ ] Maintain one prioritised backlog.
- [ ] Identify the currently active phase.
- [ ] Define the current phase start date and target review date.
- [ ] Apply the scope-control questions before adding work.
- [ ] Review risks at the beginning and end of each phase.
- [ ] Record consequential decisions in architecture decision records.
- [ ] Preserve negative results and failed experiments.
- [ ] Review the roadmap after every phase without changing the central research question casually.

## Reusable capability gates

Complete this lifecycle for every capability phase after Phase 0:

```text
Learn and write → Engineer → Verify and release
```

Phase 0 is the environment bootstrap exception and has its own setup and verification checklist.

### A. Learning and lecture-note gate

Begin with enough orientation to direct learning, without treating it as a separate definition stage:

- [ ] State the capability and phase research question.
- [ ] State the intended robot behaviour.
- [ ] Identify prerequisite mathematics.
- [ ] Identify prerequisite physics.
- [ ] Identify prerequisite algorithms and software concepts.
- [ ] List the major concepts in dependency order.
- [ ] Define notation before using it.
- [ ] Define units, frames, assumptions, and prerequisites.
- [ ] Explain each concept in plain language.
- [ ] Show central derivations step by step without unexplained jumps.
- [ ] Include at least one worked example for each major topic.
- [ ] Explain how the mathematics or physics informs engineering choices.
- [ ] State failure conditions and limitations.
- [ ] Use `$...$` for inline mathematics.
- [ ] Use `$$...$$` for display mathematics.
- [ ] Keep the chapter self-contained.
- [ ] Ensure all algorithmic or scientific scripts trace to documented mathematics.

For every major concept:

- [ ] Learn the concept.
- [ ] Complete a 5–15 minute closed-book quick test.
- [ ] Test recall of definitions and notation.
- [ ] Test a plain-language explanation.
- [ ] Test one essential derivation step.
- [ ] Test one short application.
- [ ] Test assumptions, units, or failure conditions.
- [ ] Check answers and record misconceptions.
- [ ] Review only missed material when necessary.
- [ ] Retest failed prerequisite concepts.

Before passing the learning and writing gate:

- [ ] Start later sessions with two or three retrieval questions from earlier concepts.
- [ ] Complete the cumulative chapter test.
- [ ] Correct failed prerequisite concepts.
- [ ] Schedule non-critical weaknesses for spaced review.
- [ ] Add tests, answers, hints, or worked solutions to the lecture-note source.
- [ ] Compile the chapter successfully as part of the lecture-note book.
- [ ] Write measurable capability requirements informed by the documented theory.
- [ ] Define the simplest credible baseline.
- [ ] Define interfaces and architecture implications sufficiently for implementation.
- [ ] Define the acceptance scenario before implementation.
- [ ] State what is excluded from the phase.
- [ ] Record traceability from equations to requirements and planned tests.
- [ ] Confirm the learning record and engineering specification are ready before implementation begins.

### B. Engineering gate

- [ ] Assign unique IDs to requirements.
- [ ] Trace infrastructure work to an engineering requirement.
- [ ] Define module responsibilities.
- [ ] Define interfaces, schemas, units, frames, and timestamps.
- [ ] Define valid ranges and uncertainty representation.
- [ ] Define invalid, missing, and stale-data behaviour.
- [ ] Keep configuration separate from source code.
- [ ] Implement the simplest credible baseline first.
- [ ] Keep code modular and testable.
- [ ] Add structured logging and diagnostics.
- [ ] Add unit tests.
- [ ] Add package integration tests.
- [ ] Add ROS interface tests where applicable.
- [ ] Add a headless simulation test where applicable.
- [ ] Add failure handling and safe fallback where applicable.
- [ ] Pin material dependencies and configurations.
- [ ] Record the link between equations, requirements, implementation, and tests.

### C. Verification and release gate

- [ ] State the hypothesis and falsification condition.
- [ ] Declare independent, dependent, and controlled variables.
- [ ] Freeze baselines and ablations.
- [ ] Freeze scenarios and random seeds.
- [ ] Define metrics and aggregation.
- [ ] Define failure and excluded-run policies.
- [ ] Record software, data, model, and configuration versions.
- [ ] Run the acceptance scenarios.
- [ ] Record requirement results.
- [ ] Record performance and resource measures.
- [ ] Record safety and failure observations.
- [ ] Preserve negative results.
- [ ] Correct blocking defects.
- [ ] Add non-blocking work to the backlog.
- [ ] Update the theory chapter only when an error or important result requires it.
- [ ] Complete the design or release review.
- [ ] Create a versioned capability release.

## Phase 0 — Development environment

Phase 0 only establishes and verifies the project environment. Learning chapters, capability requirements, robot implementation, sensors, and mission engineering begin in later capability phases.

### Set up

- [x] Confirm Windows 11 remains the host operating system.
- [x] Install or verify WSL2 Ubuntu 24.04.
- [x] Configure the Codex app to access the WSL checkout and execute project commands through Ubuntu WSL2.
- [x] Create the authoritative repository checkout under the WSL Linux home filesystem.
- [x] Confirm the repository is not built from `/mnt/c` or `/mnt/d`.
- [x] Install and verify ROS 2 Jazzy.
- [x] Install and verify Gazebo Harmonic.
- [x] Install and verify the modern C++ toolchain.
- [x] Install and verify the Python environment.
- [x] Install PyTorch inside WSL2.
- [x] Install and verify Quarto and the PDF toolchain.

### Verify and record

- [x] Create and build a minimal ROS workspace from a clean shell.
- [x] Run a minimal ROS publisher/subscriber smoke test.
- [x] Launch Gazebo Harmonic through a minimal documented command.
- [x] Verify PyTorch detects the GPU.
- [x] Compile a minimal Quarto/LaTeX document.
- [x] Record environment versions.
- [x] Record installation and verification commands.
- [x] Record the environment architecture decision.
- [x] Record failures, workarounds, and known limitations.

### Phase 0 exit

- [x] The authoritative checkout is under the WSL Linux home filesystem.
- [x] A clean shell builds the minimal ROS workspace.
- [x] The ROS publisher/subscriber smoke test passes.
- [x] Gazebo launches through a documented command.
- [x] PyTorch GPU verification passes.
- [x] The document toolchain compiles a minimal document.
- [x] Environment versions and verification results are recorded.
- [x] Phase 0 review is complete.

Evidence:

- Environment setup record: [docs/environment/phase0_setup.md](docs/environment/phase0_setup.md)
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)

## Phase 1 — Geometry, mechanics, and control

### Learn and write

- [ ] Vectors and matrices.
- [ ] Coordinate frames and unit conventions.
- [ ] Rotation matrices.
- [ ] Homogeneous transformations.
- [ ] Jacobians.
- [ ] Ordinary differential equations.
- [ ] Numerical integration.
- [ ] Differential-drive kinematics.
- [ ] Newtonian mechanics.
- [ ] Force, torque, friction, and actuator limits.
- [ ] Feedback and proportional control.
- [ ] Integral and derivative control.
- [ ] Stability intuition and transient response.
- [ ] Delay, saturation, wind-up, and disturbance rejection.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 1 test.
- [ ] Compile the mechanics and control chapter before implementation.

### Engineer

- [ ] Create a minimal differential-drive simulation with odometry.
- [ ] Implement coordinate-transform utilities.
- [ ] Implement the differential-drive kinematic model.
- [ ] Implement trajectory generation.
- [ ] Implement an open-loop baseline.
- [ ] Implement proportional control.
- [ ] Implement PID control.
- [ ] Add velocity and acceleration limits.
- [ ] Add saturation handling.
- [ ] Add command validation.
- [ ] Add watchdog behaviour.
- [ ] Add emergency stop.
- [ ] Add stopped-safe fallback.
- [ ] Add control telemetry and diagnostics.
- [ ] Add unit and simulation tests.

### Verify and exit

- [ ] Freeze straight and curved trajectory scenarios.
- [ ] Test sensor noise.
- [ ] Test command latency.
- [ ] Test actuator saturation.
- [ ] Test model mismatch.
- [ ] Test external disturbances.
- [ ] Compare open-loop, proportional, and PID control.
- [ ] Measure tracking error, overshoot, settling time, and control effort.
- [ ] Verify constraint violations remain within requirements.
- [ ] Verify watchdog and emergency-stop behaviour.
- [ ] Explain the observed behaviour from the documented equations.
- [ ] Complete the Phase 1 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Release: _TBD_

## Phase 2 — Probability and state estimation

### Learn and write

- [ ] Conditional probability and Bayes' rule.
- [ ] Gaussian random variables.
- [ ] Expectation and covariance.
- [ ] Recursive Bayesian filtering.
- [ ] Kalman-filter derivation.
- [ ] Nonlinear measurement models.
- [ ] Extended Kalman filters.
- [ ] Observability.
- [ ] Sensor bias, drift, latency, and calibration.
- [ ] Innovation statistics and uncertainty consistency.
- [ ] Numerical conditioning.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 2 test.
- [ ] Compile the estimation chapter before implementation.

### Engineer

- [ ] Define wheel-odometry sensor and process models.
- [ ] Define the IMU model.
- [ ] Define landmark or simulated-position observations.
- [ ] Implement the odometry-only baseline.
- [ ] Implement a naive-fusion baseline.
- [ ] Implement the Kalman filter.
- [ ] Implement the extended Kalman filter.
- [ ] Publish covariance.
- [ ] Monitor innovations.
- [ ] Publish sensor-health flags.
- [ ] Inject noise, bias, latency, outliers, and dropout.
- [ ] Add estimator unit, integration, and simulation tests.

### Verify and exit

- [ ] Compare odometry only, naive fusion, tuned EKF, and mis-specified EKF.
- [ ] Test sensor dropout and recovery.
- [ ] Measure position and orientation error.
- [ ] Evaluate innovation statistics.
- [ ] Evaluate uncertainty consistency.
- [ ] Verify incorrect assumptions are detectable.
- [ ] Verify sensor loss triggers a degraded mode.
- [ ] Complete the Phase 2 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Release: _TBD_

## Phase 3 — Perception and semantic understanding

### Learn and write

- [ ] Camera and pinhole models.
- [ ] Projective geometry and homogeneous image coordinates.
- [ ] Rigid transforms and geometric error.
- [ ] Optics, lighting, field of view, and resolution.
- [ ] Depth and LiDAR measurement geometry.
- [ ] Neural networks and backpropagation.
- [ ] CNNs and representation learning.
- [ ] Transfer learning.
- [ ] Augmentation and class imbalance.
- [ ] Precision, recall, and calibration.
- [ ] Inference latency and resource constraints.
- [ ] Domain shift and out-of-distribution inputs.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 3 test.
- [ ] Compile the perception chapter before implementation.

### Engineer

- [ ] Calibrate camera and range-sensor models.
- [ ] Implement sensor preprocessing.
- [ ] Define and version the dataset.
- [ ] Write annotation and data-quality rules.
- [ ] Train or adapt a detector or segmenter.
- [ ] Calibrate model confidence.
- [ ] Add object tracking.
- [ ] Project detections into the shared world frame.
- [ ] Create the training and evaluation pipeline.
- [ ] Register model artefacts and configurations.
- [ ] Implement the ROS inference node.
- [ ] Add latency, resource, and failure telemetry.

### Verify and exit

- [ ] Test normal conditions.
- [ ] Test blur.
- [ ] Test low light.
- [ ] Test partial occlusion.
- [ ] Test unfamiliar backgrounds.
- [ ] Test sensor noise.
- [ ] Measure accuracy, calibration, latency, and resource use.
- [ ] Measure downstream navigation impact.
- [ ] Verify output frames and timestamps.
- [ ] Verify confidence degrades under adverse conditions.
- [ ] Reproduce evaluation from versioned data and model artefacts.
- [ ] Complete the Phase 3 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Dataset and model: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Release: _TBD_

## Phase 4 — Mapping, SLAM, and memory

### Learn and write

- [ ] Occupancy grids and Bayesian map updates.
- [ ] Localisation, mapping, and SLAM.
- [ ] Pose graphs and graph optimisation.
- [ ] Loop closure.
- [ ] Spatial indexing and nearest-neighbour retrieval.
- [ ] Working memory.
- [ ] Spatial-semantic memory.
- [ ] Episodic memory.
- [ ] Replay, retrieval, forgetting, and invalidation.
- [ ] Computational ideas from place cells, grid cells, and predictive coding.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 4 test.
- [ ] Compile the mapping and memory chapter before implementation.

### Engineer

- [ ] Implement or integrate occupancy mapping.
- [ ] Integrate SLAM.
- [ ] Attach semantic observations to the map.
- [ ] Define the current working-state representation.
- [ ] Define the episodic event schema.
- [ ] Include provenance, time, confidence, and invalidation fields.
- [ ] Implement event retrieval.
- [ ] Implement deterministic mission replay.
- [ ] Version maps and memory stores.
- [ ] Implement environmental change detection.
- [ ] Implement stale-memory invalidation.

### Verify and exit

- [ ] Compare no persistent memory, geometric memory, and geometric-plus-episodic memory.
- [ ] Run repeated missions.
- [ ] Run missions in changed environments.
- [ ] Measure mission efficiency and retrieval cost.
- [ ] Measure stale-memory failures.
- [ ] Verify memory improves at least one mission measure.
- [ ] Verify stale memories cannot silently dominate decisions.
- [ ] Complete the Phase 4 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Release: _TBD_

## Phase 5 — Planning and autonomous decision-making

### Learn and write

- [ ] Graphs, queues, heaps, and complexity.
- [ ] Dijkstra and A*.
- [ ] Admissible heuristics.
- [ ] Configuration space and collision detection.
- [ ] Sampling-based planning, RRT, and RRT*.
- [ ] Constrained optimisation.
- [ ] Splines and trajectory smoothing.
- [ ] Model-predictive control.
- [ ] Expected utility, risk, and constraints.
- [ ] Behaviour trees and hierarchical planning.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 5 test.
- [ ] Compile the planning chapter before implementation.

### Engineer

- [ ] Define a validated mission schema.
- [ ] Implement the mission executive.
- [ ] Implement A* global planning.
- [ ] Implement a local collision-avoidance baseline.
- [ ] Evaluate one sampling-based planner.
- [ ] Implement trajectory optimisation or MPC.
- [ ] Handle planner timeout.
- [ ] Handle infeasible goals.
- [ ] Implement replanning.
- [ ] Log alternatives, costs, constraints, and selection.
- [ ] Keep the safety supervisor authoritative.

### Verify and exit

- [ ] Test different obstacle densities.
- [ ] Test narrow passages.
- [ ] Test moving obstacles.
- [ ] Test localisation uncertainty.
- [ ] Test blocked goals.
- [ ] Test limited computation.
- [ ] Test energy-aware route costs.
- [ ] Measure success, path cost, clearance, latency, and energy.
- [ ] Verify planner failure triggers fallback.
- [ ] Complete the mobile-robot inspection mission.
- [ ] Complete the Phase 5 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Release: _TBD_

## Phase 6 — Advanced reinforcement learning

### Learn and write

- [ ] MDPs and partial observability.
- [ ] Policy gradients.
- [ ] Actor-critic methods.
- [ ] PPO.
- [ ] SAC.
- [ ] Replay, entropy, and critic bias.
- [ ] Recurrent and goal-conditioned RL.
- [ ] Hierarchical RL.
- [ ] Constrained MDPs and safe exploration.
- [ ] Imitation and offline RL.
- [ ] Curriculum learning and domain randomisation.
- [ ] Distribution shift and robust evaluation.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 6 test.
- [ ] Compile the advanced-RL chapter before implementation.

### Engineer

- [ ] Select exactly one bounded RL task.
- [ ] Explain why learning may add value.
- [ ] Freeze the classical baseline.
- [ ] Freeze the shared environment and evaluation API.
- [ ] Implement or reproduce PPO.
- [ ] Implement or reproduce SAC.
- [ ] Track seeds and configurations.
- [ ] Track checkpoints and training curves.
- [ ] Add curriculum or domain randomisation only with a stated hypothesis.
- [ ] Add the classical safety wrapper.
- [ ] Implement the ROS inference interface.
- [ ] Define safe behaviour when the policy is missing or invalid.

### Verify and exit

- [ ] Compare the classical baseline, PPO, and SAC.
- [ ] Evaluate multiple seeds.
- [ ] Evaluate held-out scenarios.
- [ ] Measure average and worst-case performance.
- [ ] Measure sample efficiency and failure rate.
- [ ] Measure robustness and inference latency.
- [ ] Record safety interventions.
- [ ] Retain a learned policy only if it earns a measured advantage.
- [ ] Verify safe operation without the policy.
- [ ] Complete the Phase 6 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Training artefacts: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Release: _TBD_

## Phase 7 — World models and imagined futures

### Learn and write

- [ ] System identification and analytical dynamics.
- [ ] Neural dynamics models.
- [ ] Physics-plus-residual dynamics models.
- [ ] Probabilistic prediction.
- [ ] Aleatoric and epistemic uncertainty.
- [ ] Ensembles and uncertainty calibration.
- [ ] Latent variables and variational inference.
- [ ] One-step and rollout error.
- [ ] Compounding model error and model exploitation.
- [ ] Dyna, PETS, Dreamer, and TD-MPC at the required conceptual depth.
- [ ] Random shooting and cross-entropy planning.
- [ ] Model-based reinforcement learning.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 7 test.
- [ ] Compile the world-model chapter before implementation.

### Engineer

- [ ] Define and version the trajectory-data schema.
- [ ] Implement the data-collection service.
- [ ] Implement the analytical dynamics model.
- [ ] Implement the neural dynamics model.
- [ ] Implement the physics-plus-residual model.
- [ ] Estimate predictive uncertainty.
- [ ] Build one-step and rollout evaluation.
- [ ] Implement random-shooting or cross-entropy planning.
- [ ] Integrate learned-model MPC.
- [ ] Add uncertainty penalties.
- [ ] Add planning-horizon limits.
- [ ] Add confidence-triggered fallback.

### Verify and exit

- [ ] Compare one-step prediction error.
- [ ] Compare long-horizon prediction error.
- [ ] Compare sample efficiency.
- [ ] Compare uncertainty calibration.
- [ ] Compare out-of-distribution behaviour.
- [ ] Compare analytical MPC, neural-model MPC, and hybrid-model MPC.
- [ ] Compare the selected model-free RL baseline.
- [ ] Measure mission, energy, safety, and computation outcomes.
- [ ] Verify uncertainty is useful for fallback.
- [ ] Test for model exploitation.
- [ ] State whether the main hypothesis is supported, rejected, or narrowed.
- [ ] Complete the Phase 7 research review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Dataset and models: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Research conclusion: _TBD_
- Release: _TBD_

## Phase 8 — Aerospace theory and UAV transfer

### Learn and write

- [ ] Three-dimensional coordinate frames.
- [ ] Quaternions and angular velocity.
- [ ] Six-degree-of-freedom rigid-body dynamics.
- [ ] Inertia tensors.
- [ ] Thrust, reaction torque, and rotor allocation.
- [ ] Aerodynamic drag and wind disturbance.
- [ ] Energy consumption and flight envelopes.
- [ ] Hover linearisation.
- [ ] Cascaded position and attitude control.
- [ ] LQR.
- [ ] Constrained MPC.
- [ ] Geofencing, battery reserve, and failsafe behaviour.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 8 test.
- [ ] Compile the aerospace chapter before implementation.

### Engineer

- [ ] Establish PX4 software-in-the-loop.
- [ ] Implement or verify the multirotor model.
- [ ] Establish the position and attitude control baseline.
- [ ] Add wind disturbances.
- [ ] Add payload and mass changes.
- [ ] Add the energy model.
- [ ] Add flight-envelope constraints.
- [ ] Add geofencing and reserve policy.
- [ ] Transfer the mission interface.
- [ ] Transfer perception, mapping, and memory interfaces.
- [ ] Transfer planning, telemetry, and safety interfaces.
- [ ] Document which components transfer unchanged and which require adaptation.

### Verify and exit

- [ ] Test the nominal inspection-and-return mission.
- [ ] Test wind.
- [ ] Test changed mass.
- [ ] Test estimator degradation.
- [ ] Test sensor dropout.
- [ ] Test model mismatch.
- [ ] Test communication loss.
- [ ] Test low battery.
- [ ] Test planner failure.
- [ ] Verify all declared failures enter a safe mode.
- [ ] Complete the Phase 8 safety and architecture review.
- [ ] Create the UAV capability release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: [docs/environment/phase0_verification.md](docs/environment/phase0_verification.md)
- Safety review: _TBD_
- Release: _TBD_

## Phase 9 — Integrated research release

### Freeze the research package

- [ ] Freeze benchmark scenarios.
- [ ] Freeze the evaluation protocol.
- [ ] Freeze baselines and ablations.
- [ ] Freeze metrics, seeds, and trial counts.
- [ ] Freeze software, data, model, and container versions.

### Complete evaluation

- [ ] Run the complete mobile-robot mission suite.
- [ ] Run the complete UAV mission suite.
- [ ] Run the fault-injection campaign.
- [ ] Run distribution-shift evaluation.
- [ ] Complete the baseline comparison matrix.
- [ ] Complete the ablation matrix.
- [ ] Preserve unsuccessful and negative results.
- [ ] Reproduce the principal result from a clean environment.

### Complete engineering evidence

- [ ] Finalise requirements and verification results.
- [ ] Finalise architecture and interface documentation.
- [ ] Finalise the hazard register and safety evidence.
- [ ] Finalise data and model documentation.
- [ ] Finalise environment and build instructions.
- [ ] Verify the complete automated test suite.
- [ ] Verify release containers where used.
- [ ] Produce representative mission demonstrations.
- [ ] Produce interpretable decision and uncertainty traces.

### Complete learning and research evidence

- [ ] Compile the full lecture-note book to PDF.
- [ ] Compile the full lecture-note book to HTML.
- [ ] Verify notation and terminology are consistent across chapters.
- [ ] Verify cumulative tests and solutions are included.
- [ ] Complete the technical research report.
- [ ] State whether the main hypothesis is supported, rejected, or narrowed.
- [ ] Separate demonstrated conclusions from future hypotheses.
- [ ] State limitations and boundary conditions explicitly.
- [ ] Complete the final research and engineering review.
- [ ] Publish the first complete research release.

Evidence:

- Frozen benchmark: _TBD_
- Lecture-note book: _TBD_
- Technical report: _TBD_
- Reproduction record: _TBD_
- Demonstrations: _TBD_
- Final release: _TBD_

## Lecture-note book quality checklist

- [ ] Every chapter states learning objectives.
- [ ] Every chapter identifies prerequisites.
- [ ] Notation is defined before use.
- [ ] Symbols are consistent across chapters.
- [ ] Units and coordinate frames are explicit.
- [ ] Assumptions are explicit.
- [ ] Derivations are step-by-step.
- [ ] Important equations use valid LaTeX syntax.
- [ ] Worked examples are correct and reproducible.
- [ ] Major concepts have quick retrieval tests.
- [ ] Every chapter has a cumulative test.
- [ ] Answers, hints, or worked solutions are available.
- [ ] Engineering connections are explained.
- [ ] Failure modes and limitations are discussed.
- [ ] Sources and citations are complete.
- [ ] Code-generated figures are reproducible.
- [ ] PDF compilation passes.
- [ ] HTML compilation passes.
- [ ] Document-link checks pass.

## Systems-engineering quality checklist

- [ ] Mission and system boundaries remain current.
- [ ] Requirements have unique IDs and measurable thresholds.
- [ ] Requirements include operating conditions and verification methods.
- [ ] Interfaces define schemas, units, frames, timing, and invalid states.
- [ ] Architecture reflects the implemented system.
- [ ] Hazards have controls and verification evidence.
- [ ] Requirements trace to architecture, implementation, and tests.
- [ ] Consequential decisions have decision records.
- [ ] Each subsystem defines fallback behaviour.
- [ ] Design reviews occur before phase release.
- [ ] Verification results are preserved with release evidence.

## Software-engineering quality checklist

- [ ] Algorithmic code traces to documented mathematics.
- [ ] Infrastructure code traces to requirements.
- [ ] C++ is used appropriately for timing-sensitive and performance-critical nodes.
- [ ] Python and PyTorch are used appropriately for learning, data, and evaluation.
- [ ] Package responsibilities are explicit.
- [ ] Configuration is separated from source code.
- [ ] Dependencies are pinned.
- [ ] Random seeds are explicit where relevant.
- [ ] Formatting and linting pass.
- [ ] Static analysis passes where configured.
- [ ] Unit tests pass.
- [ ] Integration tests pass.
- [ ] ROS interface tests pass.
- [ ] Headless simulation tests pass.
- [ ] Scenario acceptance tests pass.
- [ ] Fault-injection tests pass where applicable.
- [ ] Logs and diagnostics are structured.
- [ ] CPU, memory, and GPU use are observable where relevant.
- [ ] Builds are reproducible.
- [ ] Releases are versioned.

## Final completion criteria

- [ ] The mobile robot completes the defined inspection mission.
- [ ] The UAV completes the transferred inspection-and-return mission.
- [ ] Perception, belief, memory, planning, control, prediction, learning, and safety use documented interfaces.
- [ ] Every learned component has a classical baseline.
- [ ] Every learned component has a safe fallback.
- [ ] Analytical, neural, and hybrid world models have been compared reproducibly.
- [ ] The primary hypothesis has an evidence-based conclusion.
- [ ] Safety and distribution-shift limitations are explicit.
- [ ] The complete lecture-note book compiles to PDF and HTML.
- [ ] Another person can reproduce the principal experiment from the documentation.
