# Project Intelligence Capability Checklist

This file is the finite execution path for [PLAN.md](PLAN.md). The archived detailed checklist is [CHECKLIST.md.old](CHECKLIST.md.old). `PLAN.md` defines the research programme and architecture; this file says what capability to finish next and what evidence closes it.

## Finish line

The required project is complete when capability `P9.10` publishes the reproducible Core Intelligence Release and the core completion gate passes. Phases 10–12 are optional and cannot block that finish line. A sound negative research result counts as completion.

## Working rules

1. Work through the required capability path in order.
2. Keep exactly one capability active.
3. Expand only the active capability into five working steps: learn and review, specify, implement, verify, and close.
4. Mark a capability complete only when its exit result passes and its evidence is linked.
5. Put useful work with no named consumer in the project backlog; do not add it to the critical path.
6. Add a required capability only by replacing, merging, or removing another capability, unless `PLAN.md` is formally rebaselined.
7. Introduce a library, framework, simulator, or infrastructure service only when the active capability names it.
8. Record a failed hypothesis or non-improving learned method, preserve the evidence, and continue; do not create an endless retry branch.
9. Keep the skill coverage ledger complete, but do not turn its concepts into progress checkboxes.
10. After closing the active capability, copy the five-step template to the next capability and make that capability active.
11. Before drafting a learning block, confirm its primary route in `textbooks/INDEX.md` and resolve any declared source gap without modifying the read-only textbook files.

## Capability definition of done

Every capability uses the same five steps:

- **Learn and review:** approve only the prerequisite theory and pass its relevant retrieval or cumulative test.
- **Specify:** define the outcome, inputs, outputs, units, frames, assumptions, exclusions, failure behaviour, and acceptance cases.
- **Implement:** build the simplest credible baseline and keep mathematical or learning logic separate from adapters where practical.
- **Verify:** run analytical, unit, integration, simulation, safety, and performance checks required by the specification.
- **Close:** link the evidence, record negative results and remaining non-blocking work, and mark the capability complete.

## Current progress

- **Required finish:** Phase 9 Core Intelligence Release.
- **Current milestone:** `M1` — Classical intelligence foundation.
- **Current phase:** Phase 1 — Geometry, mechanics, and control.
- **Active capability:** `P1.1` — Pure differential-drive motion model.
- **Current state:** Implementation and deterministic tests exist; review closure remains open.
- **Next action:** Pass the applicable retrieval and cumulative test, complete the capability review, and close `P1.1`.
- **Blockers:** None recorded.
- **Current tools:** Python, ROS 2 package tooling, `colcon`, and `pytest`.
- **Next gated tool:** Eigen in `P1.2`.

## Milestone tracker

| Milestone | Phases | Outcome | Status |
|---|---:|---|---|
| `M0` Environment bootstrap | 0 | Reproducible WSL2, ROS 2, Gazebo, C++, Python, PyTorch, and document environment | Done |
| `M1` Classical intelligence foundation | 1–5 | Mobile robot completes the bounded classical inspection mission and exposes reusable observation, belief, world-state, planning, control, telemetry, and safety contracts | Active |
| `M2` Reusable learning foundation | 6 | One bounded task supports reproducible classical, RL, replay, cost, intervention, and held-out evaluation workflows | Queued |
| `M3` Classical manipulation platform | 7 | Frozen classical grasp, reorientation, inspection, placement, retreat, and safety baseline | Queued |
| `M4` Manipulation learning | 8 | Frozen demonstration data and selected model-free learned manipulation baseline | Queued |
| `M5` World-model research and core release | 9 | Analytical, neural, and hybrid world models are compared and the Core Intelligence Release is published | Queued |
| `M6` Classical UAV extension | 10 | Frozen classical UAV inspection-and-return baseline | Optional and locked |
| `M7` UAV intelligence transfer | 11 | Selected Phase 6–9 intelligence is evaluated on the UAV without adding a new general-purpose RL family | Optional and locked |
| `M8` Integrated extension release | 12 | Reproducible multi-embodiment release | Optional and locked |

## Active capability

### P1.1 — Pure differential-drive motion model

**Supports:** `M1`, later wheel odometry, control, simulation, and RL environment dynamics.

**Exit result:** The pure model maps wheel motion to planar body motion with declared frames, units, assumptions, invalid-input behaviour, and deterministic acceptance evidence.

**Included skills:** linear algebra, coordinate frames, rotation matrices, ordinary differential equations, numerical integration, differential-drive kinematics, planar rigid-body motion, $SE(2)$, and twists.

**Excluded:** ROS node behaviour, covariance, encoder noise, slip estimation, filtering, trajectory control, and Gazebo integration.

- [ ] **Learn and review:** Pass the applicable retrieval and cumulative test and close the review of the approved prerequisite notes.
- [x] **Specify:** Define the minimum requirements, interface, units, frames, acceptance cases, and exclusions.
- [x] **Implement:** Implement wheel-to-body mapping and the differential-drive kinematic update in the ROS 2 Python package.
- [x] **Verify:** Pass the deterministic motion-model suite: 50 tests, 0 errors, 0 failures, and 0 skipped through `colcon test`.
- [ ] **Close:** Record the review result, link final evidence, and mark `P1.1` complete in the critical path.

Evidence:

- Requirements: [docs/01_motion_models/differential_drive_motion_model.md](docs/01_motion_models/differential_drive_motion_model.md)
- Linear algebra: [notes/01_linear_algebra_foundations.qmd](notes/01_linear_algebra_foundations.qmd)
- Geometry and frames: [notes/02_geometry_and_coordinate_frames.qmd](notes/02_geometry_and_coordinate_frames.qmd)
- Kinematics and integration: [notes/03_kinematics_and_numerical_integration.qmd](notes/03_kinematics_and_numerical_integration.qmd)
- Implementation companion: [notes/04_kinematics_and_numerical_integration_implementation.qmd](notes/04_kinematics_and_numerical_integration_implementation.qmd)
- ROS 2 workflow: [notes/05_ros2_packages_and_development_workflow.qmd](notes/05_ros2_packages_and_development_workflow.qmd)
- Planar motion: [notes/06_planar_rigid_body_motion_se2_and_twists.qmd](notes/06_planar_rigid_body_motion_se2_and_twists.qmd)
- Package: [ros_ws/src/differential_drive_motion_model](ros_ws/src/differential_drive_motion_model)
- Tests: [ros_ws/src/differential_drive_motion_model/test](ros_ws/src/differential_drive_motion_model/test)
- Review and release: _TBD_

## Required critical path

Complete the capabilities below from top to bottom. A capability line is a deliverable, not a list of every concept studied inside it.

### M0 — Environment bootstrap

#### Phase 0 — Development environment

- [x] **P0.1 Reproducible development environment** — verify the authoritative WSL2 checkout, ROS 2 Jazzy, Gazebo Harmonic, modern C++, Python, PyTorch with GPU, Quarto/LaTeX, a clean ROS workspace build, ROS communication, and recorded versions.

Evidence:

- [Environment setup](docs/environment/environment_setup.md)
- [Environment verification](docs/environment/environment_verification.md)

### M1 — Classical intelligence foundation

#### Phase 1 — Geometry, mechanics, and control

- [ ] **P1.1 Pure differential-drive motion model** — learn, specify, implement, test, and close the active planar motion capability.
- [ ] **P1.2 Spatial rigid-body geometry** — use modern C++ and Eigen to implement bounded $SO(3)$ and $SE(3)$ validation, composition, inversion, point transformation, and planar embedding against library-independent cases.
- [ ] **P1.3 Wheel-odometry core** — implement a pure timestamped odometry update with explicit frames, units, invalid-input behaviour, and straight, curved, and rotation-in-place cases.
- [ ] **P1.4 ROS 2 odometry adapter** — connect joint states to `nav_msgs/Odometry` and `tf2` without moving mathematical logic into the node.
- [ ] **P1.5 Gazebo odometry acceptance** — run a deterministic straight, rotation, and curved sequence and compare odometry with simulator ground truth.
- [ ] **P1.6 Bounded trajectory and control baseline** — implement constrained trajectory generation, open-loop, proportional, and PID control, saturation, anti-windup, watchdog, emergency stop, telemetry, and stopped-safe behaviour.

Phase 1 exit: the simulated robot estimates its planar motion, follows bounded trajectories under declared disturbances, and stops safely after declared failures.

#### Phase 2 — Probability and state estimation

- [ ] **P2.1 Probabilistic sensor and process models** — define wheel-odometry, IMU, and landmark or simulated-position models and establish odometry-only and naive-fusion baselines.
- [ ] **P2.2 Linear Kalman filter** — derive, implement, and verify prediction, correction, covariance, innovations, and numerical checks.
- [ ] **P2.3 Extended Kalman filter** — implement nonlinear models and Jacobians and compare a tuned and deliberately mis-specified EKF.
- [ ] **P2.4 Bounded UKF comparison** — implement the unscented transform and compare EKF and UKF on one declared nonlinear case after the EKF passes.
- [ ] **P2.5 Measurement gating and tracking primitives** — implement Mahalanobis gating, bounded nearest-neighbour association, position-and-velocity tracking, and explicit track lifecycle.
- [ ] **P2.6 Estimator integrity and fusion release** — detect bias, drift, latency, outliers, dropout, stale data, and redundant-sensor disagreement; publish covariance and health and enter a degraded mode safely.

Phase 2 exit: the project has a tested belief-state contract with uncertainty, consistency monitoring, health, provenance, and degraded behaviour.

#### Phase 3 — Perception and semantic understanding

- [ ] **P3.1 Calibrated sensor front end** — use OpenCV to calibrate and preprocess camera and range data, synchronise timestamps, and express observations in declared frames.
- [ ] **P3.2 Reproducible supervised-perception baseline** — version data and annotations and train or adapt the simplest credible detector or segmenter with PyTorch.
- [ ] **P3.3 Confidence and distribution-shift evaluation** — calibrate confidence and test blur, lighting, occlusion, unfamiliar backgrounds, class imbalance, and out-of-distribution inputs.
- [ ] **P3.4 Bounded 3D perception** — use the minimum PCL subset for point filtering, voxelisation, dominant-plane removal, clustering, and camera–range association.
- [ ] **P3.5 Multi-object tracking and shared observation contract** — publish identity, geometry, pose where observable, estimated velocity, covariance, confidence, timestamp, frame, validity, and provenance.
- [ ] **P3.6 Perception integration release** — add the ROS inference adapter, telemetry, versioned artefacts, adverse-condition acceptance, and downstream navigation checks.

Phase 3 exit: the system produces calibrated, timestamped, uncertainty-aware 3D observations and tracks through a stable interface.

#### Phase 4 — Mapping, SLAM, and memory

- [ ] **P4.1 Occupancy mapping** — implement Bayesian occupancy updates with explicit frames, time, confidence, and sensor assumptions.
- [ ] **P4.2 Pose graph and SLAM integration** — reuse the project filters, then introduce GTSAM for bounded factor-graph, smoothing, or SLAM work with explicit factors and failure behaviour.
- [ ] **P4.3 Scan matching** — implement ICP with residual, correspondence, convergence, degeneracy, and initialisation checks and study NDT as the bounded comparison.
- [ ] **P4.4 Static and dynamic world-state separation** — prevent moving agents from corrupting the persistent map and maintain time-indexed dynamic occupancy.
- [ ] **P4.5 Semantic and episodic memory** — implement working, spatial-semantic, and episodic representations with indexing, replay, retrieval, forgetting, provenance, change detection, and invalidation.
- [ ] **P4.6 World-state and memory release** — compare no memory, geometric memory, and geometric-plus-episodic memory on repeated and changed missions.

Phase 4 exit: planning receives a versioned world state that separates persistent geometry, dynamic agents, semantics, uncertainty, and valid memory.

#### Phase 5 — Planning and autonomous decision-making

- [ ] **P5.1 Mission executive** — implement a deterministic behaviour tree or hierarchical executive with cancellation, recovery, blocked-goal handling, and stopped-safe states.
- [ ] **P5.2 Global planning** — implement and compare Dijkstra and A* with admissible heuristics, explicit graph costs, and unreachable-goal behaviour.
- [ ] **P5.3 Local avoidance and Nav2 baseline** — implement the project-owned static local baseline, then integrate Nav2 as the bounded production comparison.
- [ ] **P5.4 Sampling-based planning** — implement one bounded RRT/RRT* comparison with collision checking, failure limits, and reproducible scenarios.
- [ ] **P5.5 Trajectory optimisation or MPC** — specify one constrained problem, select one solver, and expose a solver-independent interface with tolerances and failure behaviour.
- [ ] **P5.6 Dynamic-agent prediction and risk decisions** — implement constant-motion predictions, multi-hypothesis occupancy, time-to-collision, collision probability, proceed/slow/stop/yield/replan decisions, chance constraints, and conservative fallback.
- [ ] **P5.7 Classical mobile-robot release** — complete the inspection mission with frozen scenarios, perception, belief, map, memory, planning, control, telemetry, and safe fallback.

Milestone `M1` exit: the classical mobile robot completes the bounded inspection mission and supplies the baseline and interfaces consumed by learning.

### M2 — Reusable learning foundation

#### Phase 6 — Reusable reinforcement-learning foundations

- [ ] **P6.1 Learning, data, and evaluation contracts** — freeze simulator-neutral observations, actions, task context, reward, safety cost, termination, truncation, replay, trajectory, intervention, model, and held-out evaluation schemas.
- [ ] **P6.2 Frozen classical task baseline** — select one bounded mobile-robot task and freeze scenarios, metrics, budgets, seeds, safety wrapper, and classical performance.
- [ ] **P6.3 PPO baseline** — reproduce PPO through the shared contract with documented policy-gradient and actor-critic mathematics.
- [ ] **P6.4 SAC baseline** — reproduce SAC with replay, entropy, target networks, critic checks, and matched evaluation.
- [ ] **P6.5 TD3 baseline** — reproduce TD3 with deterministic policy gradients, twin critics, target-policy smoothing, delayed updates, and matched evaluation; learn DDPG without requiring a separate benchmark.
- [ ] **P6.6 Logged imitation and offline evaluation** — preserve failures and interventions, implement one bounded behavioural-cloning baseline, and separate fixed-log claims from interactive evidence.
- [ ] **P6.7 Constrained RL experiment** — implement one PID-Lagrangian extension of PPO or SAC with distinct reward and cost, an explicit budget, and an independent classical safety wrapper.
- [ ] **P6.8 Reusable RL release** — compare classical, PPO, SAC, TD3, imitation, and constrained results under declared data and interaction budgets and release reusable PyTorch, NumPy/SciPy, logging, inference, and ROS-adapter components.

Milestone `M2` exit: one task supports reproducible model-free RL, offline evidence, explicit safety costs, classical fallback, and reuse by manipulation.

### M3 — Classical manipulation platform

#### Phase 7 — Classical simulated manipulation

- [ ] **P7.1 Manipulator model and production integration** — add one simulated six- or seven-degree-of-freedom arm with URDF, SRDF, frames, limits, collision geometry, `ros2_control`, MoveIt 2, and Gazebo.
- [ ] **P7.2 Kinematics with Pinocchio** — derive and verify forward, inverse, and differential kinematics, Jacobians, singularities, redundancy, null-space motion, and manipulability against independent cases.
- [ ] **P7.3 Dynamics and control** — verify mass matrix, gravity, Coriolis, centrifugal, friction, external contact, inverse dynamics, and required joint-, task-, impedance-, or admittance-control behaviour.
- [ ] **P7.4 Collision-aware planning and execution** — establish the planning scene, self- and environment-collision checks, swept safety envelopes, time-indexed obstacle checks, and bounded joint and Cartesian trajectories.
- [ ] **P7.5 Grasp and inspection executive** — implement gripper state, grasp frames, friction and stability checks, reach, grasp, lift, reorient, inspect, place, retreat, and stopped-safe states.
- [ ] **P7.6 Frozen classical manipulation release** — test unreachable, singular, collision, timeout, pose-error, grasp, mass, friction, contact-force, and retreat cases and freeze the benchmark and safety fallback.

Milestone `M3` exit: the manipulation mission works safely without any learned policy.

### M4 — Manipulation learning

#### Phase 8 — Imitation and reinforcement learning for manipulation

- [ ] **P8.1 Demonstration and intervention dataset** — extend the Phase 6 schema for manipulator, object, contact, recovery, intervention, failure, and task context with episode-level train, validation, and held-out splits.
- [ ] **P8.2 Behavioural cloning and recovery** — implement pointwise cloning, measure covariate shift and compounding error, and evaluate recovery demonstrations, interventions, and DAgger.
- [ ] **P8.3 IQL fixed-data baseline** — audit support and quality, then implement expectile value regression and advantage-weighted policy extraction on the frozen dataset; study CQL as the conceptual pessimistic comparison.
- [ ] **P8.4 Temporal and multimodal policy gate** — add observation history, action chunking, or one ACT-, diffusion-, flow-, or other conditional generative policy only when simpler cloning exposes a stated temporal or multimodality failure.
- [ ] **P8.5 Goal-conditioned SAC with HER** — reuse Phase 6 SAC for sparse-reward goals and Hindsight Experience Replay.
- [ ] **P8.6 RLPD offline-to-online baseline** — use demonstration-seeded replay, balanced offline/online sampling, critic ensembles, and a declared simulator-interaction budget after simpler baselines freeze.
- [ ] **P8.7 Residual policy** — learn one bounded correction over the frozen classical controller.
- [ ] **P8.8 Manipulation-learning release** — compare admitted methods under matched data or interaction budgets, test safety shielding and invalid actions, preserve negative results, and freeze the selected model-free baseline.

Milestone `M4` exit: demonstration data and the justified model-free manipulation comparison are frozen for the world-model experiment.

### M5 — World-model research and Core Intelligence Release

#### Phase 9 — World models, road-agent prediction, and core release

- [ ] **P9.1 Transition-data and model contract** — reuse trajectory schemas and define simulator- and ROS-independent state, action, context, predictive distribution, uncertainty, validity, and provenance.
- [ ] **P9.2 Analytical manipulator model** — implement the approved system-identification and Pinocchio-based dynamics model using only inputs available to every comparison.
- [ ] **P9.3 Neural transition model** — implement the purely neural next-state model and one-step, contact-transition, and rollout evaluation.
- [ ] **P9.4 Physics-plus-residual model** — learn declared friction, payload, delay, compliance, sliding, or contact-transition gaps over the analytical model.
- [ ] **P9.5 Predictive uncertainty** — model and calibrate aleatoric and epistemic uncertainty with ensembles and add latent variables or variational inference only if observable state is insufficient.
- [ ] **P9.6 Explicit model-based planning** — implement random shooting or cross-entropy planning with uncertainty penalties, horizon limits, confidence fallback, and the Dyna and PETS foundations needed to interpret it.
- [ ] **P9.7 Learned latent-model baseline** — implement TD-MPC2 with TD-MPC foundations, or replace it with DreamerV3 only through the recorded partial-observability or pixel-observation gate; do not implement both.
- [ ] **P9.8 Road-agent tracking and prediction transfer** — reuse Kalman/UKF tracking, gating, association, and lifecycle and compare constant-velocity, constant-acceleration, constant-turn-rate, neural, hybrid, and justified multimodal predictors.
- [ ] **P9.9 Bounded risk-aware road decisions** — use predicted occupancy, time to collision, collision probability, calibration, and proceed/slow/stop/yield/replan decisions without building a complete self-driving stack.
- [ ] **P9.10 Core Intelligence Release** — compare analytical, neural, hybrid, learned latent, model-free, and classical approaches; reproduce the result; state whether the hypothesis is supported, rejected, or narrowed; profile ONNX Runtime or TensorRT only if required; and publish code, data, models, notes, safety evidence, negative results, and report.

Milestone `M5` exit: the Phase 9 core completion gate passes. The required project is finished.

## Optional extension

Do not activate this section before `P9.10` is complete. Deciding not to activate it does not leave the required project unfinished.

### M6 — Classical UAV extension

#### Phase 10 — UAV mechanics, estimation, planning, and classical control

- [ ] **P10.1 PX4 software-in-the-loop and multirotor model** — pin PX4 SITL and verify six-degree-of-freedom dynamics, inertia, thrust, reaction torque, rotor allocation, drag, wind, payload, and actuator mismatch.
- [ ] **P10.2 Classical flight control** — establish hover linearisation, cascaded position and attitude control, LQR understanding, constrained MPC where required, limits, latency, and saturation evidence.
- [ ] **P10.3 Flight estimation** — implement EKF and a bounded UKF comparison for IMU, GNSS, barometer, magnetometer, and optical flow with integrity and degraded GPS-denied behaviour.
- [ ] **P10.4 Flight sensing and scenarios** — add wind, mass, sensor, optical-flow, GPS-denial, dropout, inconsistency, and communication-loss cases.
- [ ] **P10.5 Three-dimensional planning** — implement the minimum 3D search, dynamic-obstacle tracking, predicted occupancy, time-to-conflict, and safe corridor capability.
- [ ] **P10.6 Energy, envelope, and mission executive** — enforce geofence, battery reserve, flight envelope, take-off, inspect, abort, return, land, hover, and emergency behaviour.
- [ ] **P10.7 Frozen classical UAV release** — measure estimation, tracking, control effort, energy, clearance, latency, intervention, and every declared minimal-risk state.

### M7 — UAV intelligence transfer

#### Phase 11 — UAV learned models and intelligence transfer

- [ ] **P11.1 Transfer audit** — verify frames, units, timing, state meaning, data support, reward and cost meaning, logging, planning, and safety assumptions before reuse.
- [ ] **P11.2 Analytical UAV predictor** — identify wind, drag, payload, and actuator mismatch and establish the analytical baseline.
- [ ] **P11.3 Neural and physics-plus-residual UAV predictors** — implement both bounded comparisons and evaluate one-step and rollout error.
- [ ] **P11.4 Flight uncertainty and predictive planning** — calibrate nominal and shifted uncertainty and plan with multi-hypothesis motion, chance-constrained corridors, confidence limits, and classical fallback.
- [ ] **P11.5 Optional transferred RL capability** — select at most one of fixed-log IQL, bounded-interaction RLPD, residual SAC/TD3, TD-MPC2 reuse, or PID-Lagrangian reuse under a declared flight-specific hypothesis.
- [ ] **P11.6 UAV transfer release** — compare classical, analytical, neural, hybrid, and any admitted learned component and state what transfers and what remains embodiment-specific.

### M8 — Integrated extension release

#### Phase 12 — Integrated multi-embodiment research release

- [ ] **P12.1 Freeze the research package** — freeze operational design domains, exclusions, benchmarks, protocols, baselines, ablations, metrics, seeds, failure policies, and artefact versions.
- [ ] **P12.2 Cross-embodiment evaluation and safety** — run activated benchmark, fault-injection, rare-event, distribution-shift, hazard, minimal-risk, and safety-monitor evidence without combining incompatible metrics.
- [ ] **P12.3 Documentation and reproduction** — finalise requirements, architecture, interfaces, hazards, data cards, model cards, build instructions, lecture-note book, technical report, demonstrations, and clean reproduction.
- [ ] **P12.4 Integrated release** — separate primary, transfer, negative, limitation, and future results and publish the optional multi-embodiment release.

## Skill coverage ledger

This ledger preserves the full learning scope from the archived checklist. It is a curriculum map, not a second task list. Study each item only when its named capability becomes active.

<details>
<summary>Phase 1 — Mathematics, geometry, mechanics, and control</summary>

- Linear algebra foundations: vectors, matrices, linear mappings, dimensions, coordinate columns, numerical conditioning, and solver use.
- Coordinate frames, unit conventions, active motion versus coordinate change, and frame-explicit quantities.
- Rotation matrices, homogeneous transformations, $SO(3)$, $SE(3)$, planar $SE(2)$, twists, and quaternion representation.
- Degrees of freedom, Jacobians, ordinary differential equations, numerical integration, and exact differential-drive integration.
- Differential-drive kinematics, nonholonomic constraints, Ackermann comparison, curvature, signed turning radius, steering limits, and the kinematic bicycle model.
- Velocity, acceleration, curvature, and jerk constraints for smooth ground, manipulation, and flight trajectories.
- Newtonian mechanics, force, torque, friction, actuator limits, feedback, proportional, integral, and derivative control.
- Stability intuition, transient response, delay, saturation, wind-up, disturbance rejection, watchdogs, emergency stop, and stopped-safe control.

</details>

<details>
<summary>Phase 2 — Probability, estimation, integrity, and tracking</summary>

- Conditional probability, Bayes' rule, Gaussian random variables, expectation, covariance, and recursive Bayesian filtering.
- Linear Kalman-filter derivation and implementation.
- Nonlinear measurement models, extended Kalman filters, unscented transforms, and the unscented Kalman filter.
- Observability, sensor bias, drift, latency, calibration, innovation statistics, uncertainty consistency, and numerical conditioning.
- Mahalanobis distance, statistical measurement gating, bounded nearest-neighbour data association, clutter, missed detections, and false positives.
- Track initiation, confirmation, coasting, deletion, crossing targets, redundant-sensor disagreement, estimator integrity, and degraded modes.

</details>

<details>
<summary>Phase 3 — Vision, machine learning, 3D perception, and tracking</summary>

- Camera and pinhole models, projective geometry, homogeneous image coordinates, rigid transforms, geometric error, optics, lighting, field of view, and resolution.
- Depth and LiDAR measurement geometry; 3D point coordinates, filtering, voxelisation, dominant-plane removal, clustering, and bounding geometry.
- Camera–range extrinsic calibration, temporal synchronisation, shared frames, and association between image and range observations.
- Neural networks, backpropagation, CNNs, representation learning, transfer learning, augmentation, and class imbalance.
- Precision, recall, confidence calibration, dataset and annotation quality, inference latency, and resource constraints.
- Multi-object identity and tracking metrics, domain shift, out-of-distribution inputs, blur, low light, occlusion, unfamiliar backgrounds, and sensor noise.

</details>

<details>
<summary>Phase 4 — Mapping, SLAM, dynamic worlds, and memory</summary>

- Occupancy grids, Bayesian map updates, localisation, mapping, and SLAM.
- Pose graphs, graph optimisation, factors, smoothing, loop closure, and GTSAM.
- Point-cloud registration residuals, correspondence, convergence, degeneracy, initialisation sensitivity, ICP, and conceptual NDT comparison.
- Static geometry, dynamic occupancy, moving-object filtering, temporal map confidence, and spatial indexing with nearest-neighbour retrieval.
- Working memory, spatial-semantic memory, episodic memory, replay, retrieval, forgetting, provenance, environmental change, and invalidation.
- Computational ideas from place cells, grid cells, predictive coding, and deterministic mission replay.

</details>

<details>
<summary>Phase 5 — Algorithms, planning, optimisation, and autonomous decisions</summary>

- Graphs, queues, heaps, complexity, Dijkstra, A*, and admissible heuristics.
- Configuration space, collision detection, sampling-based planning, RRT, and RRT*.
- Constrained optimisation, one justified solver, splines, trajectory smoothing, and model-predictive control.
- Expected utility, risk, constraints, chance constraints, and conservative fallback.
- Constant-velocity, constant-acceleration, and constant-turn-rate agent predictions.
- Multi-hypothesis futures, predicted occupancy, time to collision, collision probability, prediction confidence, and uncertainty-aware risk.
- Proceed, slow, stop, yield, and replan behaviours; behaviour trees; hierarchical planning; cancellation; recovery; and blocked goals.

</details>

<details>
<summary>Phase 6 — Reinforcement-learning foundations</summary>

- Markov decision processes, partial observability, policy gradients, actor-critic methods, recurrent RL, goal-conditioned RL, and hierarchical RL.
- PPO, SAC, deterministic policy gradients, DDPG foundations, and TD3 with twin critics, target-policy smoothing, and delayed updates.
- Replay, entropy, target networks, critic bias, reproducible environment contracts, and held-out evaluation.
- Constrained MDPs, separate reward and safety costs, Lagrangian relaxation, PID-Lagrangian updates, safe exploration, hard safety wrappers, and intervention logging.
- Behavioural cloning, imitation from logged trajectories, covariate shift, offline RL, fixed-log counterfactual limits, and offline-to-online learning.
- Dataset imbalance, rare safety-critical events, intervention labels, curriculum learning, domain randomisation, distribution shift, robust evaluation, multiple seeds, and interaction budgets.

</details>

<details>
<summary>Phase 7 — Classical manipulation</summary>

- Serial kinematic chains, revolute and prismatic joints, joint space, configuration space, and task space.
- Forward kinematics, product of exponentials, analytical and numerical inverse kinematics, geometric Jacobians, and differential inverse kinematics.
- Redundancy, null-space motion, singularities, manipulability, and joint position, velocity, acceleration, and torque limits.
- Rigid-body dynamics, mass matrix, gravity, Coriolis, centrifugal, friction, external contact, and inverse dynamics.
- End-effector and grasp frames, contact normals, friction cones, grasp stability, and grasp-state detection.
- Joint-space, task-space, impedance, and admittance control.
- Configuration-space collision checking, time-indexed collision prediction, swept volumes, safety envelopes, trajectory execution, planning timeouts, safe hold, retreat, and stopped-safe behaviour.

</details>

<details>
<summary>Phase 8 — Imitation, offline RL, and manipulation learning</summary>

- Expert demonstrations, behavioural cloning, covariate shift, compounding execution error, recovery demonstrations, interventions, and DAgger.
- Observation histories, temporal dependence, action chunking, multimodal expert behaviour, and conditional generative policies.
- ACT-, diffusion-, and flow-based policy concepts at the depth required by the selection gate.
- Goal-conditioned MDPs, sparse rewards, Hindsight Experience Replay, and goal-conditioned SAC.
- Offline support, out-of-distribution actions, expectile value regression, advantage-weighted extraction, IQL, and CQL as the conceptual pessimistic comparison.
- Demonstration-seeded replay, balanced offline and online sampling, critic ensembles, RLPD, and declared interaction budgets.
- Residual reinforcement learning, constrained policies, safety shielding, independent action validation, domain randomisation, out-of-distribution detection, and sim-to-real limits.

</details>

<details>
<summary>Phase 9 — World models, predictive planning, and road-agent transfer</summary>

- System identification, analytical manipulator dynamics, neural transition models, and physics-plus-residual dynamics.
- Probabilistic prediction, aleatoric and epistemic uncertainty, ensembles, calibration, latent variables, and variational inference when observable state is insufficient.
- One-step and rollout error, compounding model error, contact transitions, model exploitation, distribution shift, and confidence fallback.
- Random shooting, cross-entropy planning, uncertainty penalties, horizon limits, Dyna, PETS, and explicit model-based RL.
- TD-MPC, TD-MPC2, latent dynamics, temporal-difference value learning, terminal values, local trajectory optimisation, DreamerV3, and imagined latent rollouts.
- Road-agent Kalman and UKF tracking, gating, association, lifecycle, constant-velocity, constant-acceleration, and constant-turn-rate-and-velocity prediction.
- Neural, hybrid, and multimodal trajectory prediction; predicted occupancy; time to collision; collision probability; calibration; and bounded risk decisions.
- Experimental comparison of analytical, neural, hybrid, learned latent, model-free, and classical approaches with sample efficiency, task, safety, computation, and reproducibility evidence.

</details>

<details>
<summary>Phases 10–12 — UAV and transfer extension</summary>

- Three-dimensional frames, quaternions, angular velocity, attitude error, six-degree-of-freedom dynamics, inertia tensors, thrust, reaction torque, rotor allocation, drag, wind, payload, and actuator mismatch.
- Hover linearisation, cascaded position and attitude control, LQR, constrained MPC, saturation, and flight limits.
- IMU, GNSS, barometer, magnetometer, optical-flow, EKF, UKF, redundant-sensor integrity, GPS-denied navigation, and degraded estimation.
- Three-dimensional search, dynamic-obstacle tracking, predicted occupancy, time to conflict, multi-hypothesis motion, chance-constrained flight corridors, and prediction-aware planning.
- Energy, flight envelopes, geofencing, battery reserve, communication loss, failsafes, take-off, mission, abort, return, landing, hover, and emergency modes.
- Analytical, neural, and physics-plus-residual UAV transition models; flight-specific uncertainty; distribution shift; and confidence-triggered fallback.
- Fixed-log IQL, bounded-interaction RLPD, residual SAC or TD3, TD-MPC2 reuse, and PID-Lagrangian reuse only through a recorded flight-specific gate.
- Transfer hypotheses for software reuse, sample efficiency, predictive performance, mission performance, safety, and embodiment-specific limitations.
- Operational design domains, hazard analysis, safety goals, functional and technical safety requirements, minimal-risk conditions, cross-embodiment evaluation, and release reproduction.

</details>

## Tool and production-skill coverage

| Layer | Tools and skills retained | Introduction rule |
|---|---|---|
| Production foundation | Linux, WSL2, modern C++, Python, CMake, `colcon`, Git, formatting, linting, static analysis, unit and integration testing, Docker, and CI | Use only what the active capability or a clean reproduction boundary requires |
| Numerical work | Eigen, NumPy, SciPy, numerical conditioning, matrix decompositions, solver selection, and library-independent acceptance cases | Eigen begins in `P1.2`; solvers enter only with a specified optimisation problem |
| Robotics integration | ROS 2, messages, services and actions where required, `tf2`, `ros2_control`, Gazebo, `rosbag2`, and MCAP | Keep pure cores behind narrow adapters with explicit schemas, frames, units, time, validity, and failure behaviour |
| Classical autonomy | Nav2, MoveIt 2, Pinocchio, and one justified optimisation solver | Introduce after the project-owned mathematical or classical baseline passes |
| Observation and belief | OpenCV, the minimum PCL subset, and GTSAM | OpenCV/PCL enter in Phase 3; GTSAM enters after the project filters and factor-graph theory |
| Intelligence research | PyTorch, simulator-neutral environments, replay and trajectory data, experiment configuration, artefact tracking, checkpointing, and held-out evaluation | Keep learning, reward, cost, model, and evaluation logic independent of ROS where practical |
| Acceleration and deployment | CUDA through PyTorch, profiling, ONNX Runtime, and TensorRT | Add only after model selection and a measured deployment requirement; verify numerical equivalence and worst-case latency |
| Simulation | Gazebo as the authoritative integration simulator; MuJoCo only through a recorded contact, throughput, reproducibility, or parallel-sampling benchmark | Do not maintain a second simulator without a measured benefit and simulator-independent contracts |
| Concurrency | ROS 2 callback groups and executors, threads or processes, deterministic batching, queue bounds, ownership, synchronisation, cancellation, shutdown, timing, and profiling | Add concurrency only when the capability states rates, deadlines, failure behaviour, and a testable reason |
| Research engineering | Versioned data splits, seeds, configurations, checkpoints, simulator parameters, CPU/GPU/memory/latency measures, interaction counts, wall-clock cost, negative results, data cards, and model cards | Required when they affect a scientific or release claim |
| Experimental evaluation | Hypotheses and falsification conditions, independent and dependent variables, controls, baselines, ablations, failure and excluded-run policies, aggregation, mission success, completion time, collisions, clearance, pose and tracking error, grasp and recovery success, contact force, energy, accuracy, precision, recall, displacement error, negative log-likelihood, calibration, one-step and rollout error, sample efficiency, average and worst-case performance, latency, and safety interventions | Select only the measures needed to test the active capability or research claim |

## Shared evidence and quality gate

Apply this gate when closing a capability; do not copy it into every phase as another checklist.

- The learning note defines notation, assumptions, dimensions, units, frames, derivations, worked examples, limitations, retrieval checks, and sources in simple English.
- Requirements have measurable thresholds, operating conditions, verification methods, and traceability to mathematics, interfaces, implementation, and tests.
- Interfaces define schema, ownership, rates, timing, validity, uncertainty, stale and missing data, cancellation, and failure behaviour.
- The implementation has focused tests for project logic, known cases, edge cases, invariants, adapters, safety behaviour, and previously observed defects.
- Formatting, linting, configured static analysis, unit, integration, ROS interface, headless simulation, scenario, and fault-injection checks pass where applicable.
- Logs and diagnostics expose relevant timing, CPU, memory, GPU, decisions, uncertainty, interventions, and fallback behaviour.
- Software, data, models, configurations, seeds, containers where used, and evidence are reproducible and versioned.
- Consequential decisions, hazards, minimal-risk behaviour, negative results, limitations, data cards, and model cards are recorded where applicable.
- Quarto sources, equations, figures, cross-references, citations, answers, PDF, HTML, and document links pass for affected learning material.

## Core completion gate

- [ ] The mobile robot completes the bounded classical inspection mission.
- [ ] Classical, PPO, SAC, TD3, imitation, and the admitted PID-Lagrangian experiment are compared under declared scenarios and budgets.
- [ ] The classical manipulator completes grasp, reorientation, inspection, placement, and safe retreat.
- [ ] The admitted manipulation imitation, offline, online, and residual methods pass their pairwise gates under declared data and interaction budgets.
- [ ] Analytical, neural, hybrid, and the admitted learned latent-model planning approach are compared reproducibly on the primary manipulation task.
- [ ] The bounded road-agent benchmark compares classical, neural, hybrid, and justified multimodal prediction and calibrated risk decisions.
- [ ] Every learned component has a frozen classical baseline, independent action validation, and a safe fallback.
- [ ] The main hypothesis has an evidence-based conclusion; negative, transfer, limitation, safety, and distribution-shift results are explicit.
- [ ] Another person can reproduce the principal result and build the Core Intelligence Release from its documentation.

## Optional extension completion gate

- [ ] The frozen classical UAV completes the inspection-and-return mission under declared nominal and failure scenarios.
- [ ] Any transferred learned component is compared with its classical parent and Phase 6–9 antecedent under declared data and interaction budgets.
- [ ] Analytical, neural, hybrid, and any admitted learned planning approach are compared under nominal and shifted flight conditions.
- [ ] Transfer and embodiment-specific claims, operational design domains, hazards, minimal-risk behaviour, safety limits, and negative results are explicit.
- [ ] The complete lecture-note book, technical report, demonstrations, and integrated release reproduce from the documented environment.
