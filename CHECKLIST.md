# Project Intelligence Checklist (archived)

This checklist operationalises the twelve-phase roadmap in [PLAN.md](PLAN.md) under the project rules in [AGENTS.md](AGENTS.md). `PLAN.md` remains the source for project identity, research rationale, architecture, scope, and engineering method; this file records execution and evidence. Physical manipulation hardware remains deferred.

## How to use this checklist

- Keep only one implementation-sized capability active at a time.
- Complete the reusable gates for each capability after Phase 0.
- Treat each phase's capability order as a sequence of complete learning cycles, not as permission to learn the entire phase before implementing anything.
- For the active capability only, learn and review its minimum prerequisite concepts, specify it, implement it, verify it, and integrate it before opening the next capability's learning block.
- Revisit earlier theory through retrieval practice and implementation evidence, but draft new theory only when the next active capability requires it.
- Add a link or path to evidence when checking an important item.
- Mark a phase complete only when its required capability cycles are integrated and all exit evidence exists.
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
- [ ] Phase 6 — Reusable reinforcement-learning foundations.
- [ ] Phase 7 — Classical simulated manipulation.
- [ ] Phase 8 — Imitation and reinforcement learning for manipulation.
- [ ] Phase 9 — World models, road-agent prediction, and core research release.
- [ ] Phase 10 — UAV mechanics, estimation, planning, and classical control.
- [ ] Phase 11 — UAV learned models and intelligence transfer.
- [ ] Phase 12 — Integrated multi-embodiment research release.

### Rebaselined programme structure

| Phase | Main outcome | Selected self-driving contribution |
|---:|---|---|
| 1 | Geometry, mechanics, and control foundations | Nonholonomic model comparison, curvature, and smooth trajectories |
| 2 | Probability and reusable state-estimation primitives | UKF, gating, data association, and redundant-sensor integrity |
| 3 | Perception and semantic understanding | 3D perception, point clouds, multimodal calibration, and tracking |
| 4 | Mapping, SLAM, and memory | Scan matching, dynamic maps, and moving-object separation |
| 5 | Planning and autonomous decision-making | Agent prediction, behaviour selection, and risk-aware trajectories |
| 6 | Reusable RL foundations on one bounded mobile-robot task | Offline learning from logs, imitation, interventions, and constrained RL |
| 7 | Classical simulated manipulator baseline | Time-indexed collision prediction and safety envelopes |
| 8 | Imitation and reinforcement learning for manipulation | Intervention data, recovery learning, and safety shielding |
| 9 | World models, road-agent prediction, and Core Intelligence Release | Road-agent tracking, prediction, calibrated risk, and bounded decisions |
| 10 | UAV mechanics, estimation, planning, and classical control | Redundant estimation and dynamic-obstacle tracking |
| 11 | UAV learned models and intelligence transfer | Prediction-aware flight planning and learned residual models |
| 12 | Integrated multi-embodiment research release | Operational design domains, hazard analysis, and scenario testing |

The rebaseline brings simulated manipulation into scope as the primary learning domain, moves the main world-model comparison to contact-rich manipulation in Phase 9, limits self-driving work to a bounded road-agent intelligence benchmark, splits classical UAV foundations from learned transfer, and moves the integrated release from Phase 9 to Phase 12. The mobile robot supplies reusable foundations; manipulation supplies primary research evidence; road traffic and UAVs supply distinct transfer evidence.

### Reinforcement-learning algorithm allocation

| Phase | Required algorithmic contribution | Scope gate |
|---:|---|---|
| 6 | PPO, SAC, TD3, and one PID-Lagrangian constrained extension | Use one bounded mobile-robot task and one shared evaluation contract |
| 8 | Behavioural cloning, IQL, goal-conditioned SAC with HER, RLPD, and one residual policy | Advance through pairwise, stage-gated comparisons rather than an undifferentiated algorithm tournament |
| 9 | TD-MPC2 as the contemporary learned latent-model baseline | DreamerV3 may replace TD-MPC2 only when partial observability or pixels justify it; do not implement both for the core release |
| 10 | No learned controller | Freeze the classical UAV benchmark before transferring intelligence |
| 11 | Reuse selected Phase 6–9 methods | Introduce no new general-purpose RL family; select a transferred method only for a declared flight-specific hypothesis |
| 12 | No new algorithm | Integrate and reproduce only the methods admitted by earlier phase gates |

### Production and research tool allocation

The production stack exists to make the intelligence experiments credible, reproducible, measurable, and deployable. It is not a separate curriculum to finish before RL or world-model work, and each tool enters only through the active capability gate.

| Layer | Approved tools | Project role | Adoption gate |
|---|---|---|---|
| Production foundation | Linux, modern C++, Python, CMake, Git, automated testing, Docker and CI when justified | Reproducible builds, numerical software, diagnostics, concurrency, and release engineering | Add only the infrastructure required by the active capability or a clean reproduction boundary |
| Robotics integration | ROS 2, `tf2`, `ros2_control`, Gazebo, `rosbag2` with MCAP | Typed communication, frame transforms, hardware abstraction, system simulation, telemetry, and replay | Keep pure algorithms behind narrow adapters; Gazebo remains the primary integration simulator |
| Classical baselines | Nav2, MoveIt 2, Pinocchio, Eigen, and one justified optimisation solver | Frozen navigation, manipulation, dynamics, planning, control, and safety comparisons | Introduce each with its dependent capability; do not build parallel framework implementations |
| Observation and belief | OpenCV, the minimum required PCL subset, and GTSAM | Calibrated vision, bounded 3D geometry, estimation, smoothing, and SLAM | OpenCV/PCL begin in Phase 3; GTSAM follows foundational filters and pose-graph theory |
| Intelligence research | PyTorch, NumPy/SciPy, simulator-neutral RL environments, replay and trajectory contracts | Policies, offline and online RL, analytical/neural/hybrid world models, uncertainty, and predictive planning | Keep training and evaluation independent of ROS where practical and reuse the Phase 6 contracts in Phases 8–9 |
| Deployment | ONNX Runtime, CUDA profiling, and TensorRT | Selected-model inference optimisation on a declared NVIDIA target | Defer until profiling identifies a requirement and numerical-equivalence tests are defined |

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
- [ ] Before activating a phase, divide its first required outcome into an implementation-sized capability and identify only that capability's prerequisite learning block.
- [ ] Do not begin a later capability merely because its theory is interesting; require an approved dependency and a bounded engineering or experimental outcome.
- [ ] Treat the Phase 9 core release as a valid stopping point before committing to the optional UAV extension in Phases 10–11.
- [x] Formally rebaseline `PLAN.md` so its scope and phase numbering agree with this checklist.
- [ ] Before Phase 6 algorithm note drafting, establish an `AGENTS.md`-compliant primary-source route for PPO, SAC, TD3, and PID-Lagrangian constrained RL; the current textbook index routes their general foundations but not these specific algorithms.
- [ ] Before Phase 8 note drafting, establish an `AGENTS.md`-compliant primary-source route for behavioural cloning, IQL, RLPD, Hindsight Experience Replay, action chunking, and safe manipulation learning; the current textbook index does not route these topics explicitly.
- [ ] Before the Phase 9 learned-planning block, establish an `AGENTS.md`-compliant primary-source route for TD-MPC2 and DreamerV3 in addition to the textbook-routed model-based RL foundations.
- [ ] Before the Phase 5 dynamic-agent learning block, establish an `AGENTS.md`-compliant primary-source route for motion prediction and calibrated risk-aware decisions; extend it before Phase 9 to cover learned and multimodal road-agent prediction.
- [ ] Before Phase 10 note drafting, resolve the dedicated multirotor and aerospace source gap already declared by `textbooks/INDEX.md`.
- [ ] Resolve the tension between the read-only `textbooks/` rule and any future need to extend `textbooks/INDEX.md`; do not improvise an unapproved routing mechanism while drafting notes.
- [ ] For every proposed dependency, record the active capability, the requirement it satisfies, its narrower alternative, its lifecycle owner, and its removal or replacement condition.
- [ ] Keep the intelligence research core independent of ROS and simulator APIs where practical; require explicit adapters at production and simulation boundaries.
- [ ] Keep Gazebo as the primary integration simulator and admit a second simulator only through a recorded benchmark and architecture decision.
- [ ] Treat ONNX Runtime, custom CUDA work, TensorRT, distributed training, and specialised concurrency infrastructure as profiling-gated deployment or scale capabilities rather than default foundations.

## Reusable capability gates

Complete this dependency-gated cycle for each implementation-sized capability after Phase 0:

    Learn and write → Review → Specify → Implement and document → Verify

A phase contains several capability cycles. Start engineering when the active capability's prerequisite theory is reviewed and its minimum specification is ready; unrelated theory in the same phase need not be complete. After verification, use the result to identify the next capability's precise learning needs. Phase 0 and the Phase 12 release-integration work are the only exceptions that do not introduce ordinary learn-and-implement capability cycles.

### Capability working cycle

- [x] Select one active capability and identify its prerequisites.
- [x] Draft or update only the prerequisite learning material.
- [ ] Review the material and pass the relevant retrieval or cumulative test.
- [x] Define minimum requirements, interfaces, acceptance cases, and exclusions.
- [x] Create or update an implementation companion when implementation begins; do not create an empty placeholder.
- [x] Implement the simplest credible baseline and its tests.
- [x] Run the acceptance cases and record evidence.
- [ ] Integrate the capability or place non-blocking work in the backlog.

### A. Learn, review, and specify gate

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

Before passing the review and specification gate:

- [ ] Start later sessions with two or three retrieval questions from earlier concepts.
- [ ] Complete any cumulative test applicable to the prerequisite learning block.
- [ ] Correct failed prerequisite concepts.
- [ ] Schedule non-critical weaknesses for spaced review.
- [ ] Add tests, answers, hints, or worked solutions to the lecture-note source.
- [ ] Compile the prerequisite learning block successfully as part of the lecture-note book.
- [ ] Write measurable capability requirements informed by the documented theory.
- [ ] Define the simplest credible baseline.
- [ ] Define interfaces and architecture implications sufficiently for implementation.
- [ ] Define the acceptance scenario before implementation.
- [ ] State what is excluded from the active capability.
- [ ] Record traceability from equations to requirements and planned tests.
- [ ] Confirm the learning record and engineering specification are ready before implementation begins.

### B. Implementation and documentation gate

- [ ] Assign unique IDs to requirements.
- [ ] Trace infrastructure work to an engineering requirement.
- [ ] Define module responsibilities.
- [ ] Define interfaces, schemas, units, frames, and timestamps.
- [ ] Define valid ranges and uncertainty representation.
- [ ] Define invalid, missing, and stale-data behaviour.
- [ ] Keep configuration separate from source code.
- [ ] Separate mathematical, learning, and evaluation cores from ROS, simulator, storage, and deployment adapters where practical.
- [ ] Define callback, worker, queue, deadline, cancellation, and shutdown behaviour where concurrency is present.
- [x] Implement the simplest credible baseline first.
- [x] Create or extend the implementation companion alongside the first implementation work.
- [x] Record reusable equation mappings, contracts, pseudocode, snippets, invariants, tests, and cautions in the companion.
- [x] Keep code modular and testable.
- [ ] Add structured logging and diagnostics.
- [x] Add unit tests.
- [x] Add package integration tests.
- [ ] Add ROS interface tests where applicable.
- [ ] Add a headless simulation test where applicable.
- [ ] Add failure handling and safe fallback where applicable.
- [ ] Pin material dependencies and configurations.
- [x] Record the link between equations, requirements, implementation, and tests.

### C. Verification and integration gate

- [ ] State the hypothesis and falsification condition.
- [ ] Declare independent, dependent, and controlled variables.
- [ ] Freeze baselines and ablations.
- [ ] Freeze scenarios and random seeds.
- [ ] Define metrics and aggregation.
- [ ] Define failure and excluded-run policies.
- [ ] Record software, data, model, and configuration versions.
- [ ] Record dataset or episode splits, interaction counts, checkpoints, simulator parameters, and wall-clock cost where they affect a scientific claim.
- [x] Run the acceptance scenarios.
- [x] Record requirement results.
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

- Environment setup record: [docs/environment/environment_setup.md](docs/environment/environment_setup.md)
- Verification report: [docs/environment/environment_verification.md](docs/environment/environment_verification.md)

## Phase 1 — Geometry, mechanics, and control

### Capability order

Complete the motion-model capability already in progress, including its still-open review and specification gate, before starting spatial-geometry implementation. Then move serially through spatial geometry, wheel odometry, its ROS 2 and Gazebo acceptance path, and the dynamics-and-control capabilities. Introduce the Ackermann and smooth-trajectory comparison only when learning trajectory generation; it is a bounded modelling exercise, not a second vehicle implementation.

### Learn, review, and specify

- [x] Create the unified notation and conventions note.
- [x] Create the Quarto book structure and introductory index.
- [x] Draft the linear algebra foundations chapter.
- [x] Review and approve `notes/01_linear_algebra_foundations.qmd`.
- [x] Draft coordinate frames and unit conventions.
- [x] Review and approve `notes/02_geometry_and_coordinate_frames.qmd`.
- [x] Draft the kinematics and numerical integration chapter.
- [x] Review and approve `notes/03_kinematics_and_numerical_integration.qmd`.
- [x] Draft `notes/06_planar_rigid_body_motion_se2_and_twists.qmd` from the routed textbook sections.
- [x] Review and approve the planar rigid-body motion, $SE(2)$, and twists chapter.
- [ ] Draft `notes/07_degrees_of_freedom_and_spatial_motion_so3_se3.qmd` from the routed textbook sections.
- [ ] Review and approve the degrees of freedom and spatial motion, $SO(3)$, and $SE(3)$ chapter.
- [ ] Draft `notes/08_wheeled_robot_constraints_jacobians_and_odometry.qmd` from the routed textbook sections.
- [ ] Review and approve the wheeled-robot constraints, Jacobians, and odometry chapter.
- [ ] Specify the bounded spatial rigid-body geometry capability, including interfaces, exclusions, and acceptance cases traced to Chapter 7.
- [ ] Specify the bounded wheel-odometry capability, including interfaces, exclusions, and acceptance cases traced to Chapter 8.
- [ ] Confirm that each implementation or integration slice below fits within one or two focused development days; split or reduce any slice that does not.
- [ ] Draft `notes/09_dynamics_forces_torque_friction_and_actuator_limits.qmd` from the routed textbook sections.
- [ ] Review and approve the dynamics, forces, torque, friction, and actuator limits chapter.
- [x] Select the pure differential-drive motion model as the first active implementation-sized capability.
- [x] Draft the minimum motion-model requirements, interfaces, acceptance cases, and exclusions.
- [ ] Pass the applicable retrieval and cumulative test in `notes/03_kinematics_and_numerical_integration.qmd`.
- [x] Rotation matrices.
- [ ] Homogeneous transformations.
- [ ] Jacobians.
- [x] Ordinary differential equations.
- [x] Numerical integration.
- [x] Differential-drive kinematics.
- [ ] Nonholonomic constraints shared by differential-drive and Ackermann-steered vehicles.
- [ ] Curvature, signed turning radius, steering limits, and the kinematic bicycle model as a comparative worked example.
- [ ] Velocity, acceleration, curvature, and jerk constraints for smooth trajectories across ground, manipulation, and flight embodiments.
- [ ] Newtonian mechanics.
- [ ] Force, torque, friction, and actuator limits.
- [ ] Feedback and proportional control.
- [ ] Integral and derivative control.
- [ ] Stability intuition and transient response.
- [ ] Delay, saturation, wind-up, and disturbance rejection.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 1 test.
- [x] Compile the current notes as a Quarto HTML book.
- [ ] Compile each prerequisite learning block before implementing its dependent capability.

### Implement and document

Work through the following slices serially. Each slice must remain independently testable and small enough for one or two focused development days.

- [ ] Complete the review and specification gate for the first differential-drive motion capability.
- [x] Create `notes/04_kinematics_and_numerical_integration_implementation.qmd` alongside the first implementation block.
- [x] Create and revise the general ROS 2 package-development workflow in `notes/05_ros2_packages_and_development_workflow.qmd`.
- [x] Scaffold the `differential_drive_motion_model` ROS 2 Python package with its metadata and resource marker.
- [x] Implement the wheel-to-body velocity mapping with explicit input validation.
- [x] Add and pass focused wheel-to-body unit tests.
- [x] Implement the differential-drive kinematic model.

#### Spatial rigid-body geometry slice — target: 1–2 days

- [ ] Implement only the pure spatial-geometry operations required by the next capability: validate $SO(3)$ rotations, compose and invert $SE(3)$ transforms, transform a point, and embed a planar pose in $SE(3)$.
- [ ] Introduce Eigen with the first C++ spatial-geometry or numerical implementation, covering fixed-size matrices and vectors, geometric transforms, decompositions, solver use, and numerical-conditioning checks required by that implementation.
- [ ] Keep the mathematical acceptance cases independent of Eigen so they verify the model rather than the library.
- [ ] Convert planar yaw to the normalised quaternion representation required by ROS 2 messages.
- [ ] Add focused acceptance tests for identity, composition order, inverse round trips, point transformation, non-planar rotation, and planar embedding.
- [ ] Exclude a general Lie-group library, exponential and logarithm maps, multiple Euler-angle conventions, optimisation, and uncertainty propagation.

#### Wheel-odometry core slice — target: 1–2 days

- [ ] Implement a pure, stateless wheel-odometry update from previous and current wheel angles, elapsed time, geometry, and previous pose.
- [ ] Reuse the existing differential-drive mappings and exact integration instead of duplicating their equations.
- [ ] Return the updated planar pose and body twist with explicit frames, units, and timestamp assumptions.
- [ ] Add focused acceptance tests for no motion, straight motion, rotation in place, curved motion, variable intervals, wheel ordering, and invalid inputs.
- [ ] Exclude covariance, encoder noise, slip estimation, encoder rollover, filtering, and control.

#### ROS 2 odometry adapter slice — target: 1 day

- [ ] Add one minimal ROS 2 node that subscribes to wheel joint states and publishes `nav_msgs/Odometry` plus the `odom` to `base_link` transform.
- [ ] Declare only the required parameters: wheel names, wheel radius, track width, and frame names.
- [ ] Define first-sample, duplicate-timestamp, out-of-order, missing-joint, and non-finite-input behaviour.
- [ ] Add focused ROS interface tests without adding unrelated launch or telemetry infrastructure.

#### Gazebo acceptance slice — target: 1–2 days

- [ ] Add the smallest differential-drive Gazebo model and launch path needed to exercise the odometry node.
- [ ] Run one deterministic acceptance sequence containing straight motion, rotation in place, and a curved segment.
- [ ] Compare published odometry with simulator ground truth using declared position and heading tolerances.
- [ ] Exclude sensor noise studies, slip modelling, visual tooling, controller comparison, and general simulation infrastructure from this slice.

#### Dynamics and control capabilities — begin after the odometry acceptance slice

- [ ] Implement trajectory generation.
- [ ] Enforce declared velocity, acceleration, curvature where applicable, and jerk limits in trajectory generation without creating a production self-driving-car stack.
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

### Verify, integrate, and exit

- [ ] Freeze straight and curved trajectory scenarios.
- [ ] Test sensor noise.
- [ ] Test command latency.
- [ ] Test actuator saturation.
- [ ] Test model mismatch.
- [ ] Test external disturbances.
- [ ] Compare open-loop, proportional, and PID control.
- [ ] Measure tracking error, overshoot, settling time, and control effort.
- [ ] Verify the trajectory generator respects its velocity, acceleration, curvature, and jerk constraints.
- [ ] Verify constraint violations remain within requirements.
- [ ] Verify watchdog and emergency-stop behaviour.
- [ ] Explain the observed behaviour from the documented equations.
- [ ] Complete the Phase 1 review and release.

Evidence:

- Learning and requirements record: [docs/01_motion_models/differential_drive_motion_model.md](docs/01_motion_models/differential_drive_motion_model.md)
- Unified notation: [notes/notation.qmd](notes/notation.qmd)
- Linear algebra chapter draft: [notes/01_linear_algebra_foundations.qmd](notes/01_linear_algebra_foundations.qmd) — reviewed
- Geometry chapter draft: [notes/02_geometry_and_coordinate_frames.qmd](notes/02_geometry_and_coordinate_frames.qmd) — reviewed
- Kinematics and numerical integration chapter: [notes/03_kinematics_and_numerical_integration.qmd](notes/03_kinematics_and_numerical_integration.qmd) — reviewed
- Implementation companion: [notes/04_kinematics_and_numerical_integration_implementation.qmd](notes/04_kinematics_and_numerical_integration_implementation.qmd)
- ROS 2 package workflow: [notes/05_ros2_packages_and_development_workflow.qmd](notes/05_ros2_packages_and_development_workflow.qmd)
- Planar rigid-body motion, $SE(2)$, and twists: [notes/06_planar_rigid_body_motion_se2_and_twists.qmd](notes/06_planar_rigid_body_motion_se2_and_twists.qmd) — reviewed
- Degrees of freedom and spatial motion, $SO(3)$, and $SE(3)$: [notes/07_degrees_of_freedom_and_spatial_motion_so3_se3.qmd](notes/07_degrees_of_freedom_and_spatial_motion_so3_se3.qmd) — drafting and review in progress
- Wheeled-robot constraints, Jacobians, and odometry: `notes/08_wheeled_robot_constraints_jacobians_and_odometry.qmd` — planned
- Dynamics, forces, torque, friction, and actuator limits: `notes/09_dynamics_forces_torque_friction_and_actuator_limits.qmd` — planned; the current draft still requires renaming
- Package source: [ros_ws/src/differential_drive_motion_model](ros_ws/src/differential_drive_motion_model)
- Deterministic motion-model verification: [ros_ws/src/differential_drive_motion_model/test](ros_ws/src/differential_drive_motion_model/test) — 50 tests, 0 errors, 0 failures, and 0 skipped through `colcon test`
- Release: _TBD_

## Phase 2 — Probability and state estimation

### Capability order

Complete separate cycles for the odometry-only and naive-fusion baselines, the Kalman filter, the extended Kalman filter, estimator-consistency monitoring, and finally the UKF and object-tracking primitives. Learn gating and data association only after Gaussian state estimation is understood and verified.

### Learn, review, and specify

- [ ] Conditional probability and Bayes' rule.
- [ ] Gaussian random variables.
- [ ] Expectation and covariance.
- [ ] Recursive Bayesian filtering.
- [ ] Kalman-filter derivation.
- [ ] Nonlinear measurement models.
- [ ] Extended Kalman filters.
- [ ] Unscented transforms and the unscented Kalman filter.
- [ ] Observability.
- [ ] Sensor bias, drift, latency, and calibration.
- [ ] Innovation statistics and uncertainty consistency.
- [ ] Mahalanobis distance and statistical measurement gating.
- [ ] Nearest-neighbour data association and the assumptions that bound its use.
- [ ] Track initiation, confirmation, coasting, and deletion under missed detections and false positives.
- [ ] Redundant-sensor disagreement and estimator-integrity monitoring.
- [ ] Numerical conditioning.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 2 test.
- [ ] Compile each prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Define wheel-odometry sensor and process models.
- [ ] Define the IMU model.
- [ ] Define landmark or simulated-position observations.
- [ ] Implement the odometry-only baseline.
- [ ] Implement a naive-fusion baseline.
- [ ] Implement the Kalman filter.
- [ ] Implement the extended Kalman filter.
- [ ] Implement a bounded UKF comparison only after the EKF capability passes its acceptance cases.
- [ ] Publish covariance.
- [ ] Monitor innovations.
- [ ] Publish sensor-health flags.
- [ ] Implement reusable measurement gating and a position-and-velocity tracking baseline for later perception capabilities.
- [ ] Define track lifecycle and invalid, stale, duplicate, and out-of-order measurement behaviour.
- [ ] Detect persistent disagreement between redundant measurements.
- [ ] Inject noise, bias, latency, outliers, and dropout.
- [ ] Add estimator unit, integration, and simulation tests.

### Verify, integrate, and exit

- [ ] Compare odometry only, naive fusion, tuned EKF, and mis-specified EKF.
- [ ] Test sensor dropout and recovery.
- [ ] Measure position and orientation error.
- [ ] Evaluate innovation statistics.
- [ ] Evaluate uncertainty consistency.
- [ ] Compare EKF and UKF behaviour on one declared nonlinear case without treating either method as universally superior.
- [ ] Test gating and data association with clutter, missed detections, crossing targets, and incorrect noise assumptions.
- [ ] Verify sensor disagreement becomes observable before it can silently dominate the estimate.
- [ ] Verify incorrect assumptions are detectable.
- [ ] Verify sensor loss triggers a degraded mode.
- [ ] Complete the Phase 2 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 3 — Perception and semantic understanding

### Capability order

Complete separate cycles for calibrated sensor preprocessing, the simplest credible detector or segmenter, confidence calibration, three-dimensional geometric perception, and multi-object tracking. Use simulated or classical detections before adding a learned 3D detector so tracking and fusion do not depend on an unnecessarily large perception model.

### Learn, review, and specify

- [ ] Camera and pinhole models.
- [ ] Projective geometry and homogeneous image coordinates.
- [ ] Rigid transforms and geometric error.
- [ ] Optics, lighting, field of view, and resolution.
- [ ] Depth and LiDAR measurement geometry.
- [ ] Three-dimensional point-cloud coordinates, filtering, voxelisation, and dominant-plane removal.
- [ ] Camera–range-sensor extrinsic calibration and temporal synchronisation.
- [ ] Three-dimensional bounding geometry and association between camera and range detections.
- [ ] Neural networks and backpropagation.
- [ ] CNNs and representation learning.
- [ ] Transfer learning.
- [ ] Augmentation and class imbalance.
- [ ] Precision, recall, and calibration.
- [ ] Multi-object tracking outputs, identity management, and tracking metrics.
- [ ] Inference latency and resource constraints.
- [ ] Domain shift and out-of-distribution inputs.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 3 test.
- [ ] Compile each prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Calibrate camera and range-sensor models using documented mathematics and OpenCV only as the bounded implementation layer.
- [ ] Implement sensor preprocessing with the minimum required OpenCV modules.
- [ ] Implement the minimum point-cloud filtering and clustering needed by a bounded 3D perception capability using one declared PCL subset; do not duplicate the capability in Open3D.
- [ ] Synchronise multimodal observations and transform them into a shared frame with explicit timestamp tolerances.
- [ ] Define and version the dataset.
- [ ] Write annotation and data-quality rules.
- [ ] Train or adapt a detector or segmenter.
- [ ] Calibrate model confidence.
- [ ] Add object tracking.
- [ ] Publish position, orientation where observable, velocity where estimated, bounding geometry, timestamp, frame, confidence, covariance, and track identifier through a shared 3D observation interface.
- [ ] Project detections into the shared world frame.
- [ ] Create the training and evaluation pipeline.
- [ ] Register model artefacts and configurations.
- [ ] Implement the ROS inference node.
- [ ] Add latency, resource, and failure telemetry.

### Verify, integrate, and exit

- [ ] Test normal conditions.
- [ ] Test blur.
- [ ] Test low light.
- [ ] Test partial occlusion.
- [ ] Test unfamiliar backgrounds.
- [ ] Test sensor noise.
- [ ] Test calibration error, cross-sensor timestamp offset, missed detections, false positives, and crossing tracks.
- [ ] Measure accuracy, calibration, latency, and resource use.
- [ ] Measure downstream navigation impact.
- [ ] Verify output frames and timestamps.
- [ ] Verify confidence degrades under adverse conditions.
- [ ] Verify fused outputs preserve frame, time, covariance, and provenance information needed by manipulation, road-agent prediction, and UAV planning.
- [ ] Reproduce evaluation from versioned data and model artefacts.
- [ ] Complete the Phase 3 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Dataset and model: _TBD_
- Implementation: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 4 — Mapping, SLAM, and memory

### Capability order

Complete separate cycles for occupancy mapping, localisation and SLAM integration, one bounded scan-matching capability, static-versus-dynamic world-state separation, and finally semantic and episodic memory. Do not implement multiple registration algorithms merely to fill a catalogue.

### Learn, review, and specify

- [ ] Occupancy grids and Bayesian map updates.
- [ ] Localisation, mapping, and SLAM.
- [ ] Pose graphs and graph optimisation.
- [ ] Loop closure.
- [ ] Point-cloud registration residuals, correspondence, convergence, degeneracy, and initialisation sensitivity.
- [ ] Iterative Closest Point as the required scan-matching method and Normal Distributions Transform at comparative conceptual depth.
- [ ] Static geometry, dynamic occupancy, moving-object filtering, and temporal map confidence.
- [ ] Spatial indexing and nearest-neighbour retrieval.
- [ ] Working memory.
- [ ] Spatial-semantic memory.
- [ ] Episodic memory.
- [ ] Replay, retrieval, forgetting, and invalidation.
- [ ] Computational ideas from place cells, grid cells, and predictive coding.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 4 test.
- [ ] Compile each prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Implement or integrate occupancy mapping.
- [ ] Reuse the project-owned Phase 2 foundational filters without wrapping them in GTSAM, then introduce GTSAM for the bounded pose-graph, smoothing, or SLAM capability that requires factor graphs.
- [ ] Integrate SLAM while keeping the measurement front end, factor definitions, frame conventions, and failure handling explicit rather than hidden behind GTSAM.
- [ ] Implement or integrate one bounded ICP-based scan-matching capability with declared convergence and failure behaviour.
- [ ] Keep dynamic agents out of the persistent static map and represent their time-indexed occupancy separately.
- [ ] Attach semantic observations to the map.
- [ ] Define the current working-state representation.
- [ ] Define the episodic event schema.
- [ ] Include provenance, time, confidence, and invalidation fields.
- [ ] Implement event retrieval.
- [ ] Implement deterministic mission replay.
- [ ] Version maps and memory stores.
- [ ] Implement environmental change detection.
- [ ] Age or invalidate dynamic and changed map content using time, confidence, and provenance.
- [ ] Implement stale-memory invalidation.

### Verify, integrate, and exit

- [ ] Compare no persistent memory, geometric memory, and geometric-plus-episodic memory.
- [ ] Run repeated missions.
- [ ] Run missions in changed environments.
- [ ] Test registration under poor initialisation, sparse geometry, repeated structure, and moving-object contamination.
- [ ] Verify dynamic objects cannot silently become permanent obstacles or corrupt loop closure.
- [ ] Measure mission efficiency and retrieval cost.
- [ ] Measure stale-memory failures.
- [ ] Verify memory improves at least one mission measure.
- [ ] Verify stale memories cannot silently dominate decisions.
- [ ] Complete the Phase 4 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 5 — Planning and autonomous decision-making

### Capability order

Complete separate cycles for mission execution, global planning, static local collision avoidance, trajectory optimisation or MPC, and only then prediction-aware planning around dynamic agents. The dynamic-agent capability consumes tracking output from Phase 3 and time-indexed world state from Phase 4.

### Learn, review, and specify

- [ ] Graphs, queues, heaps, and complexity.
- [ ] Dijkstra and A*.
- [ ] Admissible heuristics.
- [ ] Configuration space and collision detection.
- [ ] Sampling-based planning, RRT, and RRT*.
- [ ] Constrained optimisation.
- [ ] Splines and trajectory smoothing.
- [ ] Model-predictive control.
- [ ] Expected utility, risk, and constraints.
- [ ] Constant-velocity, constant-acceleration, and constant-turn-rate motion predictions for dynamic agents.
- [ ] Multi-hypothesis futures, predicted occupancy, time to collision, collision probability, and uncertainty-aware risk.
- [ ] Candidate behaviours such as proceed, slow, stop, yield, and replan.
- [ ] Chance constraints and conservative fallback when prediction confidence is inadequate.
- [ ] Behaviour trees and hierarchical planning.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 5 test.
- [ ] Compile each prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Define a validated mission schema.
- [ ] Implement the mission executive.
- [ ] Implement A* global planning.
- [ ] Implement a local collision-avoidance baseline.
- [ ] Integrate Nav2 only after the project-owned global-planning and local-avoidance baselines pass, and use it as the bounded production navigation baseline rather than a replacement for their documented algorithms.
- [ ] Evaluate one sampling-based planner.
- [ ] Select one optimisation solver only after writing the trajectory-optimisation or MPC problem, dimensions, constraints, tolerances, failure behaviour, and benchmark; do not add multiple solver stacks.
- [ ] Implement trajectory optimisation or MPC behind a solver-independent problem and result interface.
- [ ] Add a dynamic-agent prediction interface that supplies trajectories, probabilities or covariance, time horizon, and provenance.
- [ ] Evaluate candidate actions against predicted occupancy and declared risk thresholds.
- [ ] Add proceed, slow, stop, yield, and replan behaviours without building road-lane or traffic-rule infrastructure.
- [ ] Handle planner timeout.
- [ ] Handle infeasible goals.
- [ ] Implement replanning.
- [ ] Log alternatives, costs, constraints, and selection.
- [ ] Keep the safety supervisor authoritative.

### Verify, integrate, and exit

- [ ] Test different obstacle densities.
- [ ] Test narrow passages.
- [ ] Test moving obstacles.
- [ ] Test multimodal or incorrect agent predictions, occlusion, delayed tracks, horizon truncation, and overconfident uncertainty.
- [ ] Test localisation uncertainty.
- [ ] Test blocked goals.
- [ ] Test limited computation.
- [ ] Test energy-aware route costs.
- [ ] Measure success, path cost, clearance, latency, and energy.
- [ ] Measure missed conflicts, unnecessary stops, minimum separation, progress, and prediction-to-decision latency.
- [ ] Verify planner failure triggers fallback.
- [ ] Complete the mobile-robot inspection mission.
- [ ] Complete the Phase 5 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Implementation: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 6 — Reusable reinforcement-learning foundations

### Capability order

Use exactly one bounded mobile-robot task and complete separate cycles for the environment and logging contract, the classical baseline, PPO, SAC, TD3, log-based imitation and offline evaluation, and finally one constrained-policy experiment. Reuse the resulting actor-critic, replay, cost, logging, evaluation, and inference interfaces in Phase 8; do not reimplement general PPO, SAC, or TD3 infrastructure for the manipulator.

### Learn, review, and specify

- [ ] MDPs and partial observability.
- [ ] Policy gradients.
- [ ] Actor-critic methods.
- [ ] PPO.
- [ ] SAC.
- [ ] Deterministic policy gradients and DDPG as prerequisites for understanding TD3; do not require a separate DDPG benchmark.
- [ ] TD3, twin critics, target-policy smoothing, and delayed policy updates.
- [ ] Replay, entropy, target networks, and critic bias.
- [ ] Recurrent and goal-conditioned RL.
- [ ] Hierarchical RL.
- [ ] Constrained MDPs, distinct reward and safety-cost signals, Lagrangian relaxation, PID-Lagrangian multiplier updates, and safe exploration.
- [ ] Behavioural cloning, imitation from logged trajectories, and covariate shift.
- [ ] Offline RL, counterfactual limits of fixed logs, and offline-to-online learning.
- [ ] Dataset imbalance, rare safety-critical events, and intervention-labelled data.
- [ ] Curriculum learning and domain randomisation.
- [ ] Distribution shift and robust evaluation.
- [ ] Complete a quick test after every major concept.
- [ ] Pass the cumulative Phase 6 test.
- [ ] Compile each prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Select exactly one bounded RL task.
- [ ] Explain why learning may add value.
- [ ] Freeze the classical baseline.
- [ ] Freeze a simulator-neutral environment and evaluation API expressed with explicit NumPy/PyTorch-compatible observations, actions, terminations, truncations, rewards, safety costs, and task context.
- [ ] Keep reward, safety-cost, replay, trajectory, model, and held-out evaluation logic independent of ROS; connect ROS and Gazebo through bounded adapters.
- [ ] Define reward, each safety cost, its aggregation horizon, and its allowed budget independently of the hard safety supervisor.
- [ ] Define and version a reusable episodic trajectory schema with observations, actions, rewards, safety costs, terminations, timestamps, task context, and safety interventions.
- [ ] Use NumPy/SciPy for transparent numerical baselines and PyTorch for learned models; do not introduce a general RL framework unless it supplies a stated requirement without hiding the algorithm under study.
- [ ] Define one structured experiment-configuration and artefact-tracking workflow for seeds, configurations, checkpoints, metrics, failures, interaction counts, and wall-clock cost.
- [ ] Add deterministic batched or multiprocessing environment collection only after the single-environment path passes; record worker seeding, episode ownership, queue bounds, cancellation, and shutdown behaviour.
- [ ] Implement or reproduce PPO.
- [ ] Implement or reproduce SAC.
- [ ] Implement or reproduce TD3 using the same environment, observation, action, and evaluation contracts.
- [ ] Implement one PID-Lagrangian constrained extension of PPO or SAC only after its unconstrained parent baseline passes.
- [ ] Keep the classical safety wrapper authoritative; the learned cost critic and multiplier must not replace hard action validation or fallback.
- [ ] Track seeds and configurations.
- [ ] Track checkpoints and training curves.
- [ ] Preserve failure episodes and implement one bounded behavioural-cloning baseline from the frozen mobile-robot logs.
- [ ] Keep offline evaluation claims separate from online or simulator-interaction evidence.
- [ ] Add curriculum or domain randomisation only with a stated hypothesis.
- [ ] Add the classical safety wrapper.
- [ ] Implement the ROS inference interface as a narrow adapter over the framework-independent policy contract.
- [ ] Define safe behaviour when the policy is missing or invalid.

### Verify, integrate, and exit

- [ ] Compare the classical baseline, PPO, SAC, and TD3 under matched scenarios and declared interaction budgets.
- [ ] Compare the PID-Lagrangian variant with its unconstrained parent using matched initial conditions, reward, safety costs, and hard-safety limits.
- [ ] Compare the log-based behavioural-cloning baseline without requiring it to outperform interactive RL.
- [ ] Evaluate multiple seeds.
- [ ] Evaluate held-out scenarios.
- [ ] Measure average and worst-case performance.
- [ ] Measure sample efficiency and failure rate.
- [ ] Measure cumulative safety cost, budget exceedance, constraint violations, multiplier response, and reward–constraint trade-offs.
- [ ] Measure robustness and inference latency.
- [ ] Record safety interventions.
- [ ] Test missing, stale, non-finite, out-of-range, and late policy outputs independently of task reward.
- [ ] Verify the constrained learner cannot bypass the classical safety wrapper and does not turn an average cost budget into a per-step safety guarantee.
- [ ] Retain a learned policy only if it earns a measured advantage.
- [ ] Verify safe operation without the policy.
- [ ] Complete the Phase 6 review and release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Training artefacts: _TBD_
- Reward, safety-cost, constraint-budget, and intervention traces: _TBD_
- Implementation: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 7 — Classical simulated manipulation

### Capability order

Complete separate cycles for the arm model and forward kinematics, inverse and differential kinematics, planning-scene collision checking, trajectory execution and control, grasping, and finally the classical inspection executive. Use simulator ground-truth object poses until the classical manipulation baseline passes; perception integration is a later bounded capability, not a prerequisite for validating arm motion.

### Learn, review, and specify

- [ ] Serial kinematic chains and revolute and prismatic joints.
- [ ] Joint space, configuration space, and task space.
- [ ] Forward kinematics and the product-of-exponentials representation.
- [ ] Analytical and numerical inverse kinematics.
- [ ] Geometric Jacobians and differential inverse kinematics.
- [ ] Redundancy, null-space motion, singularities, and manipulability.
- [ ] Joint position, velocity, acceleration, and torque limits.
- [ ] Manipulator rigid-body dynamics, gravity, Coriolis, centrifugal, friction, and external-contact terms.
- [ ] End-effector frames, grasp frames, contact normals, friction cones, and grasp stability.
- [ ] Joint-space, task-space, impedance, and admittance control at the depth required by the baseline.
- [ ] Configuration-space collision checking, time-indexed collision prediction, swept volumes, and safety envelopes.
- [ ] Specify one inspection-oriented grasp, reorientation, and placement task with safe retreat behaviour.
- [ ] Complete quick tests after each major concept and cumulative tests after each capability-sized learning block.
- [ ] Compile each approved prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Add one simulated six- or seven-degree-of-freedom manipulator; exclude multiple arm platforms and physical hardware.
- [ ] Define its URDF, SRDF, frames, joints, limits, collision geometry, and controllers.
- [ ] Integrate `ros2_control` and MoveIt 2 through requirements-traced interfaces.
- [ ] Introduce Pinocchio as the bounded articulated-kinematics and dynamics library after the corresponding derivations are approved; keep MoveIt 2 responsible for production manipulation integration and planning.
- [ ] Implement or verify forward kinematics against known configurations and cross-check Pinocchio, MoveIt 2, and independently derived acceptance cases without treating agreement between two libraries as ground truth.
- [ ] Implement or integrate inverse kinematics with explicit convergence, joint-limit, and singularity behaviour.
- [ ] Verify Pinocchio Jacobian, inverse-dynamics, mass-matrix, gravity, and nonlinear-effect outputs required by the baseline against known cases and physical invariants.
- [ ] Establish the planning scene and environment and self-collision checking.
- [ ] Generate and execute joint-space and Cartesian trajectories with declared velocity, acceleration, and jerk limits.
- [ ] Add gripper control and grasp-state detection.
- [ ] Add dynamic-obstacle predictions and safety envelopes to trajectory validation only after static planning passes.
- [ ] Implement a deterministic inspection executive for reach, grasp, lift, reorient, inspect, place, retreat, and stopped-safe states.
- [ ] Define planning timeout, unreachable goal, invalid state, collision, failed grasp, stale object pose, and excessive-force behaviour.
- [ ] Record joint state, end-effector pose, commands, planning results, contact events, safety interventions, and timing.

### Verify, integrate, and exit

- [ ] Test reachable, unreachable, multiple-solution, near-singular, and joint-limit cases.
- [ ] Test environment collision, self-collision, moving-obstacle, and planning-timeout cases.
- [ ] Test object-pose error, failed grasp, changed mass, friction variation, and safe retreat.
- [ ] Measure task success, end-effector error, planning and execution latency, path length, clearance, peak contact force, and control effort.
- [ ] Verify unsafe trajectories are rejected before execution.
- [ ] Verify every declared failure reaches a bounded hold, retreat, or stopped-safe state.
- [ ] Freeze the classical manipulation baseline and its benchmark before starting Phase 8 learning experiments.
- [ ] Complete the Phase 7 review and capability release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Manipulator description and classical implementation: _TBD_
- Classical benchmark: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 8 — Imitation and reinforcement learning for manipulation

### Capability order

Complete separate cycles for the demonstration-data contract, pointwise behavioural cloning, recovery data, IQL on the frozen dataset, action chunking if justified, goal-conditioned SAC with hindsight replay, RLPD for offline-to-online learning, and one residual policy. Advance through the declared pairwise gates rather than training every method concurrently. Add at most one generative imitation policy after simpler baselines reveal a specific multimodality limitation.

### Learn, review, and specify

- [ ] Expert demonstrations and behaviour cloning.
- [ ] Covariate shift and compounding execution error.
- [ ] Recovery demonstrations, interventions, and DAgger.
- [ ] Observation histories and action chunking.
- [ ] Multimodal expert behaviour and conditional generative policies at the depth required to choose one experiment.
- [ ] Goal-conditioned MDPs, sparse rewards, and Hindsight Experience Replay.
- [ ] Offline dataset support, out-of-distribution actions, expectile value regression, advantage-weighted policy extraction, and IQL.
- [ ] Conservative value learning and CQL at the conceptual depth required to contrast it with IQL; do not require a second offline-RL implementation without a specific pessimism hypothesis.
- [ ] Demonstration-seeded replay, balanced offline and online sampling, critic ensembles, and RLPD for offline-to-online learning.
- [ ] Residual reinforcement learning over a classical controller.
- [ ] Constrained policies, safety shielding, and independent action validation.
- [ ] Domain randomisation, out-of-distribution detection, and sim-to-real limits.
- [ ] Specify the hypotheses, baselines, dataset splits, interventions, reward terms, constraints, and falsification conditions before training.
- [ ] Complete quick tests after each major concept and cumulative tests after each capability-sized learning block.
- [ ] Compile each approved prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Reuse the Phase 6 trajectory schema and extend it only for manipulator state, object state, task context, contact, and intervention data.
- [ ] Keep the manipulation learning environment and policies behind the Phase 6 simulator-neutral contracts; use Gazebo for authoritative integration and evaluation.
- [ ] Consider a second simulator only if a recorded Phase 8 benchmark demonstrates a necessary contact, throughput, reproducibility, or parallel-sampling advantage and quantifies model-conversion and cross-simulator discrepancy.
- [ ] Collect versioned scripted-expert or teleoperated demonstrations with episode-level training, validation, and held-out splits.
- [ ] Implement a pointwise behavioural-cloning baseline.
- [ ] Collect and evaluate recovery and intervention-labelled demonstrations.
- [ ] Audit state-action coverage, demonstrator quality, interventions, failures, and held-out support before making an offline-RL claim.
- [ ] Implement IQL as the principal fixed-dataset RL baseline using the same frozen data splits as behavioural cloning.
- [ ] Add observation history or action chunking only under a stated temporal-dependence hypothesis.
- [ ] Reuse the Phase 6 SAC infrastructure for goal-conditioned SAC with hindsight replay.
- [ ] Implement RLPD using the frozen demonstration dataset and a declared simulator-interaction budget only after the behavioural-cloning, IQL, and online SAC baselines are frozen.
- [ ] Implement one residual policy that corrects a frozen classical controller.
- [ ] Add at most one ACT-, diffusion-, or flow-based policy only if pointwise or chunked cloning demonstrably averages incompatible actions.
- [ ] Keep the Phase 7 planner, controller, trajectory validator, and safety supervisor available and authoritative.
- [ ] Reject missing, stale, late, non-finite, out-of-range, collision-inducing, and constraint-violating learned actions.
- [ ] Record dataset, model, optimiser, seed, checkpoint, latency, intervention, and safety metadata.

### Verify, integrate, and exit

- [ ] Compare behavioural cloning with IQL under identical fixed data, splits, observations, and evaluation scenarios.
- [ ] Compare goal-conditioned SAC with HER against RLPD under matched online-interaction budgets and identical prior data.
- [ ] Compare the residual policy with its frozen classical parent and the relevant non-residual learner.
- [ ] Summarise the admitted classical, behavioural-cloning, recovery-informed, IQL, goal-conditioned SAC, RLPD, and residual results without treating unmatched data or interaction budgets as a fair leaderboard.
- [ ] Evaluate multiple seeds and held-out object poses, masses, friction values, geometries, backgrounds, and pose errors.
- [ ] Test partial observation, disturbed grasps, inference delay, missing policy, invalid policy output, and safety-wrapper intervention.
- [ ] Measure success, data and environment-step efficiency, collision and constraint violations, peak contact force, recovery, generalisation, latency, and worst-case performance.
- [ ] Test IQL under low-coverage and mixed-quality datasets and report where fixed-data support prevents a justified policy-improvement claim.
- [ ] Test whether RLPD improves interaction efficiency rather than merely benefiting from more total data or computation.
- [ ] Retain a learned method only if it earns a declared advantage over the relevant simpler baseline.
- [ ] Verify the manipulator remains operational and safe without any learned policy.
- [ ] Preserve negative results and observed reward or dataset failure modes.
- [ ] Complete the Phase 8 review and capability release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Demonstration dataset and data card: _TBD_
- Dataset coverage and offline-RL admissibility audit: _TBD_
- Training artefacts and models: _TBD_
- Verification report: _TBD_
- Release: _TBD_

## Phase 9 — World models, road-agent prediction, and core research release

### Capability order

Complete separate cycles for the manipulator analytical model and data service, the neural transition model, the physics-plus-residual model, predictive uncertainty, explicit model-based planning, one TD-MPC2 learned latent-model baseline, road-agent tracking, road-agent prediction, and the bounded risk-aware decision benchmark. Freeze and reproduce the core release only after these capabilities pass their own gates.

### Learn, review, and specify

- [ ] System identification and analytical manipulator dynamics.
- [ ] Neural transition and residual dynamics models.
- [ ] Probabilistic prediction, aleatoric and epistemic uncertainty, ensembles, and calibration.
- [ ] Latent variables and variational inference only if observable state proves insufficient.
- [ ] One-step and rollout error, compounding model error, and model exploitation.
- [ ] Random shooting, cross-entropy planning, uncertainty penalties, and horizon limits.
- [ ] Dyna, PETS, and explicit model-based RL as foundations for planning with learned dynamics.
- [ ] TD-MPC and TD-MPC2, including latent dynamics, temporal-difference value learning, terminal-value estimates, and local trajectory optimisation.
- [ ] DreamerV3 and imagined latent rollouts at the conceptual depth required to recognise when partial observability or pixels justify it as an alternative.
- [ ] Select TD-MPC2 by default; permit DreamerV3 to replace it through a recorded decision only when the observation model requires latent memory or visual representation learning, and exclude implementing both for the core release.
- [ ] Road-agent Kalman and UKF tracking, gating, association, and track lifecycle as applications of Phases 2–3.
- [ ] Constant-velocity, constant-acceleration, and constant-turn-rate-and-velocity prediction.
- [ ] Neural, physics-plus-residual, and multimodal trajectory prediction.
- [ ] Predicted occupancy, time to collision, collision probability, calibration, and bounded proceed, slow, stop, yield, or replan decisions.
- [ ] Specify manipulation as the primary hypothesis test and road-agent prediction as secondary transfer evidence.
- [ ] Exclude a complete self-driving stack, lane perception, traffic-rule implementation, detailed tyre dynamics, and vehicle hardware.
- [ ] Complete quick tests after each major concept and cumulative tests after each capability-sized learning block.
- [ ] Compile each approved prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Reuse and version the trajectory-data schema and collection service from Phases 6 and 8.
- [ ] Define one simulator- and ROS-independent transition-model contract accepting state, action, and context and returning a next-state predictive distribution, uncertainty, validity, and provenance.
- [ ] Implement the analytical manipulator transition model using the approved mechanics and bounded Pinocchio computations, with simulator-derived quantities excluded unless they are available to every compared model under the frozen observation contract.
- [ ] Implement the neural manipulator transition model.
- [ ] Implement the physics-plus-residual manipulator model for declared gaps such as friction, payload, delay, compliance, sliding, or contact transitions.
- [ ] Estimate and calibrate predictive uncertainty.
- [ ] Build one-step, contact-transition, and long-horizon rollout evaluation.
- [ ] Implement one random-shooting or cross-entropy planner and integrate uncertainty penalties, horizon limits, and confidence-triggered fallback.
- [ ] Implement or reproduce one bounded TD-MPC2 baseline on the same manipulator task, observation contract, action contract, and evaluation scenarios after the explicit-model planners pass.
- [ ] If the recorded selection gate admits DreamerV3 instead, replace the preceding TD-MPC2 item rather than adding a second learned latent-model implementation.
- [ ] Define one versioned recorded or procedurally generated road-agent dataset and its allowed use, splits, contexts, and limitations.
- [ ] Reuse Phase 2 gating and tracking interfaces to produce imperfect road-agent tracks.
- [ ] Implement constant-velocity, constant-turn-rate, neural, and physics-plus-residual trajectory predictors; add a multimodal predictor only under a stated hypothesis.
- [ ] Implement the bounded proceed, slow, stop, yield, or replan decision interface using predicted occupancy and risk thresholds.
- [ ] Keep the core road benchmark prediction- and risk-decision-based; do not add end-to-end driving RL before the Core Intelligence Release.
- [ ] Keep manipulation and road experiments on the same prediction, uncertainty, logging, and evaluation abstractions where their meanings genuinely agree.

### Verify, integrate, and core release

- [ ] Compare manipulator analytical, neural, and hybrid models on one-step and long-horizon prediction, sample efficiency, calibration, out-of-distribution behaviour, computation, and task outcomes.
- [ ] Compare analytical-model planning, neural-model planning, hybrid-model planning, TD-MPC2 or its approved DreamerV3 replacement, the Phase 8 model-free winner, and the classical Phase 7 baseline.
- [ ] Measure learned latent-model interaction efficiency, rollout or latent-prediction quality, task performance, training cost, planning computation, inference latency, and fallback use under matched evaluation scenarios.
- [ ] Test manipulator model exploitation and verify uncertainty can trigger a useful classical fallback.
- [ ] Compare road constant-velocity, constant-turn-rate, neural, and hybrid predictors using displacement error, negative log-likelihood, calibration, missed modes, and long-horizon degradation.
- [ ] Measure road missed conflicts, unnecessary stops, minimum separation, progress, and decision latency under occlusion, delayed tracks, and unfamiliar motion.
- [ ] State whether the main physics-plus-residual hypothesis is supported, rejected, or narrowed by the primary manipulation experiment.
- [ ] State separately whether the road-agent experiment supports cross-domain transfer; do not use secondary evidence to rescue a failed primary hypothesis.
- [ ] Freeze manipulation and road benchmarks, baselines, ablations, metrics, seeds, trial counts, and failure policies.
- [ ] Reproduce the principal core result from a clean environment.
- [ ] Profile the selected release model and add ONNX Runtime or TensorRT only if a declared NVIDIA deployment target fails its latency or resource requirement; verify numerical equivalence and worst-case latency against the PyTorch reference.
- [ ] Publish a versioned Core Intelligence Release containing the mobile robot, manipulator, road benchmark, data and model documentation, decision traces, negative results, and research conclusion.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- Manipulation dataset and models: _TBD_
- TD-MPC2 or DreamerV3 selection record and learned latent-model artefacts: _TBD_
- Road-agent dataset and models: _TBD_
- Core verification report: _TBD_
- Research conclusion: _TBD_
- Core release: _TBD_

## Phase 10 — UAV mechanics, estimation, planning, and classical control

### Capability order

Phases 10–11 are an optional extension after the Core Intelligence Release. If activated, complete separate cycles for PX4 software-in-the-loop, multirotor dynamics and actuator allocation, classical state estimation, cascaded control, three-dimensional planning, energy and flight-envelope management, and the inspection-and-return executive. Introduce no RL algorithm in Phase 10 and freeze the classical UAV before transferring any learned component in Phase 11.

### Learn, review, and specify

- [ ] Revisit three-dimensional frames, quaternions, angular velocity, and attitude error from the approved spatial-motion foundations.
- [ ] Six-degree-of-freedom rigid-body dynamics and inertia tensors.
- [ ] Thrust, reaction torque, rotor allocation, drag, wind, and payload effects.
- [ ] Hover linearisation, cascaded position and attitude control, LQR, and constrained MPC.
- [ ] IMU, GNSS, barometer, magnetometer, and optical-flow measurement models.
- [ ] EKF and UKF attitude and position estimation, redundant-sensor disagreement, and estimator integrity.
- [ ] GPS-denied navigation and degraded estimation.
- [ ] Three-dimensional search representations, dynamic-obstacle tracking, predicted occupancy, and time to conflict.
- [ ] Energy consumption, flight envelopes, geofencing, battery reserve, communication loss, and failsafe behaviour.
- [ ] Event-driven take-off, mission, abort, return, landing, and emergency modes.
- [ ] Complete quick tests after each major concept and cumulative tests after each capability-sized learning block.
- [ ] Compile each approved prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Establish a pinned PX4 software-in-the-loop environment and record its boundary with ROS 2.
- [ ] Implement or verify the multirotor and actuator-allocation models.
- [ ] Establish and instrument the classical attitude and position controller.
- [ ] Establish the EKF baseline and one bounded UKF comparison where nonlinearity justifies it.
- [ ] Add wind, payload, sensor, optical-flow, and GPS-denial scenarios.
- [ ] Implement the minimum three-dimensional planner and dynamic-obstacle interface required by the mission.
- [ ] Add energy, flight-envelope, geofence, and reserve constraints.
- [ ] Implement take-off, inspection, abort, return, landing, and emergency states.
- [ ] Define invalid estimate, sensor disagreement, communication loss, low battery, planner failure, and controller failure behaviour.
- [ ] Reuse mission, perception, mapping, memory, telemetry, and safety interfaces only where their contracts remain physically valid.

### Verify, integrate, and exit

- [ ] Test nominal inspection and return, wind, changed mass, GPS loss, optical-flow degradation, sensor dropout, estimator inconsistency, communication loss, low battery, and planner failure.
- [ ] Measure estimation error and consistency, tracking error, control effort, energy, minimum clearance, latency, and safety interventions.
- [ ] Verify every declared critical failure enters a defined hover, abort, return, land, or terminated-safe mode.
- [ ] Document which interfaces transfer unchanged and which require UAV-specific adaptation.
- [ ] Freeze the classical UAV benchmark before Phase 11.
- [ ] Complete the Phase 10 safety and architecture review and capability release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- PX4 and classical UAV implementation: _TBD_
- Classical UAV benchmark: _TBD_
- Verification and safety report: _TBD_
- Release: _TBD_

## Phase 11 — UAV learned models and intelligence transfer

### Capability order

Complete separate cycles for the transfer-interface audit, analytical UAV predictor, neural predictor, physics-plus-residual predictor, calibrated uncertainty, predictive flight planning, and at most one justified transferred RL capability. Introduce no new general-purpose RL family. Reuse Phase 6–9 algorithms and abstractions only after verifying their frames, units, timing, state semantics, data support, cost semantics, and safety assumptions for flight.

### Learn, review, and specify

- [ ] System identification for wind, drag, payload, and actuator mismatch.
- [ ] Neural and physics-plus-residual UAV transition models.
- [ ] Flight-specific uncertainty calibration and distribution shift.
- [ ] Prediction-aware flight planning, multi-hypothesis obstacle motion, and chance-constrained flight corridors.
- [ ] Offline learning from flight logs, intervention and failsafe records, and their counterfactual limitations.
- [ ] Selection criteria for reusing IQL on strictly fixed logs or RLPD when bounded simulator interaction is allowed; do not select both without a comparative hypothesis.
- [ ] Selection criteria for reusing SAC or TD3 in a residual policy and TD-MPC2 in learned-model planning.
- [ ] Reuse of Phase 6 reward–cost separation and PID-Lagrangian constraints without treating them as a replacement for the flight envelope.
- [ ] Confidence-triggered fallback and optional residual policies over classical control.
- [ ] Specify transfer hypotheses separately for software reuse, sample efficiency, predictive performance, mission performance, and safety.
- [ ] Complete quick tests after each major concept and cumulative tests after each capability-sized learning block.
- [ ] Compile each approved prerequisite learning block before implementing its dependent capability.

### Implement and document

- [ ] Audit the Phase 9 mission, world-state, trajectory, model, uncertainty, planning, logging, and safety interfaces against UAV requirements.
- [ ] Implement the analytical UAV predictive model.
- [ ] Implement the neural UAV transition model.
- [ ] Implement the physics-plus-residual model for declared wind, drag, payload, or actuator gaps.
- [ ] Estimate and calibrate predictive uncertainty under nominal and shifted flight conditions.
- [ ] Integrate one learned-model predictive planner with uncertainty penalties, horizon limits, flight-envelope constraints, and confidence-triggered classical fallback.
- [ ] Reuse TD-MPC2 components only if the explicit analytical, neural, and hybrid planning comparison exposes a specific learned-planning gap.
- [ ] Add at most one residual SAC or TD3 policy only after model-based comparisons pass and a specific remaining control gap is demonstrated.
- [ ] If a policy-learning experiment uses fixed flight logs, select IQL; if it combines prior logs with bounded simulator interaction, select RLPD instead and declare the interaction budget.
- [ ] Reuse the PID-Lagrangian mechanism only with flight-specific costs and budgets while keeping the Phase 10 flight envelope and failsafes authoritative.
- [ ] Record which software, data, model, and safety components transfer unchanged, adapt, or cannot transfer.

### Verify, integrate, and exit

- [ ] Compare classical, analytical-model, neural-model, and hybrid-model flight under nominal and shifted wind, mass, battery, sensor, and communication conditions.
- [ ] Compare one-step and rollout prediction, sample efficiency, calibration, mission success, energy, computation, and safety interventions.
- [ ] Compare any transferred RL capability with its classical parent and relevant Phase 6–9 antecedent under matched flight scenarios and declared data and interaction budgets.
- [ ] Test model exploitation, overconfident prediction, late inference, missing models, and invalid outputs.
- [ ] Verify learned components cannot bypass the classical safety supervisor or flight envelope.
- [ ] Retain a learned component only if it earns a declared advantage and the UAV remains safe without it.
- [ ] State which intelligence claims transfer from manipulation and road-agent prediction and which remain embodiment-specific.
- [ ] Complete the Phase 11 research, safety, and capability release.

Evidence:

- Learning and requirements record: _TBD_
- Lecture notes and tests: _TBD_
- UAV dataset and models: _TBD_
- Transfer audit: _TBD_
- Transferred-RL selection record, data budget, and interaction budget: _TBD_
- Verification and safety report: _TBD_
- Release: _TBD_

## Phase 12 — Integrated multi-embodiment research release

Phase 12 introduces no planned scientific or algorithmic capability. If evaluation exposes a knowledge or implementation gap, return that gap to a bounded capability cycle in the responsible earlier phase, verify it there, and then resume release integration.

### Freeze the research package

- [ ] Define the operational design domain and explicit exclusions for every mobile-robot, manipulator, road-agent, and UAV benchmark included in the release.
- [ ] Freeze benchmark scenarios, evaluation protocols, baselines, ablations, metrics, seeds, trial counts, and failure policies.
- [ ] Freeze software, data, model, configuration, and container versions.
- [ ] Freeze the distinction between primary manipulation evidence, secondary road and UAV transfer evidence, and supporting mobile-robot evidence.

### Complete evaluation and safety evidence

- [ ] Run the complete mobile-robot, manipulator, road-agent, and activated UAV benchmark suites.
- [ ] Run fault-injection, rare-event, and distribution-shift campaigns.
- [ ] Complete cross-embodiment baseline and ablation matrices without combining incompatible metrics.
- [ ] Complete hazard analysis, safety goals, functional and technical safety requirements, minimal-risk conditions, and hazard-to-test traceability.
- [ ] Verify safety-monitor independence and replay representative critical events.
- [ ] Preserve unsuccessful, excluded, and negative results with reasons.
- [ ] Reproduce the principal result from a clean environment.

### Complete engineering and research evidence

- [ ] Finalise requirements, verification results, architecture, interfaces, hazards, data cards, model cards, build instructions, and reproduction instructions.
- [ ] Verify the complete automated test suite and release containers where used.
- [ ] Produce representative mission demonstrations and interpretable decision, prediction, uncertainty, intervention, and fallback traces.
- [ ] Compile the full lecture-note book to PDF and HTML.
- [ ] Verify notation, terminology, cumulative tests, answers, and cross-references across the complete book.
- [ ] Complete the technical research report and state whether the primary hypothesis is supported, rejected, or narrowed.
- [ ] Separate primary results, transfer results, limitations, boundary conditions, negative results, and future hypotheses.
- [ ] Complete the final research, architecture, safety, and engineering reviews.
- [ ] Publish the integrated multi-embodiment research release.

Evidence:

- Frozen benchmarks and operational design domains: _TBD_
- Hazard analysis and safety evidence: _TBD_
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
- [ ] Every benchmark defines its operational design domain and explicit exclusions.
- [ ] Requirements have unique IDs and measurable thresholds.
- [ ] Requirements include operating conditions and verification methods.
- [ ] Interfaces define schemas, units, frames, timing, and invalid states.
- [ ] Architecture reflects the implemented system.
- [ ] Hazards have controls and verification evidence.
- [ ] Hazards trace through safety goals and functional and technical safety requirements to acceptance or fault-injection evidence.
- [ ] Requirements trace to architecture, implementation, and tests.
- [ ] Consequential decisions have decision records.
- [ ] Each subsystem defines fallback behaviour.
- [ ] Design reviews occur before phase release.
- [ ] Verification results are preserved with release evidence.
- [ ] Data cards and model cards record provenance, intended use, limitations, splits, configurations, and known failure modes.

## Software-engineering quality checklist

- [ ] Algorithmic code traces to documented mathematics.
- [ ] Infrastructure code traces to requirements.
- [ ] C++ is used appropriately for timing-sensitive and performance-critical nodes.
- [ ] Python and PyTorch are used appropriately for learning, data, and evaluation.
- [ ] Eigen, OpenCV, PCL, GTSAM, Nav2, MoveIt 2, Pinocchio, and optimisation dependencies appear only in capabilities with a documented need and acceptance boundary.
- [ ] Mathematical, learning, and evaluation cores remain testable without ROS, Gazebo, storage, or deployment runtimes where practical.
- [ ] ROS, simulator, storage, and deployment adapters preserve schemas, units, frames, timestamps, validity, uncertainty, and failure semantics.
- [ ] Concurrent callbacks and workers have declared ownership, rates, deadlines, queue bounds, synchronisation, cancellation, shutdown, and deterministic-test behaviour.
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
- [ ] `rosbag2` with MCAP or an explicitly justified alternative records the system topics required for replay and verification.
- [ ] Datasets, episode splits, configurations, checkpoints, simulator parameters, and evaluation protocols are versioned.
- [ ] CPU, memory, and GPU use are observable where relevant.
- [ ] Custom CUDA, distributed training, ONNX Runtime, and TensorRT are introduced only after profiling and have correctness and performance evidence.
- [ ] Builds are reproducible.
- [ ] Containers and CI are added when they create a declared clean-build, headless-test, training, or release boundary rather than as speculative infrastructure.
- [ ] Releases are versioned.

## Core completion criteria — Phase 9

- [ ] The mobile robot completes the defined inspection mission.
- [ ] The Phase 6 classical, PPO, SAC, and TD3 baselines and the selected PID-Lagrangian extension have been compared under matched scenarios, interaction budgets, and explicit safety-cost accounting.
- [ ] The classical manipulator completes the grasp, reorientation, inspection, placement, and safe-retreat mission.
- [ ] Manipulation behavioural cloning, IQL, goal-conditioned SAC with HER, RLPD, and residual RL have passed their stage gates and have been compared with the relevant frozen baselines under declared data and interaction budgets.
- [ ] The bounded road-agent benchmark compares analytical, neural, and hybrid predictors and risk-aware decisions.
- [ ] Analytical, neural, hybrid, and TD-MPC2 or approved DreamerV3 manipulator planning approaches have been compared reproducibly.
- [ ] The primary hypothesis has an evidence-based conclusion from manipulation, with road evidence reported separately as transfer evidence.
- [ ] Every learned component in the Core Intelligence Release has a classical baseline and safe fallback.
- [ ] Safety, data, model, and distribution-shift limitations are explicit.
- [ ] Another person can reproduce the principal core experiment from the documentation.

## Extended completion criteria — Phase 12

- [ ] The UAV completes the transferred inspection-and-return mission if Phases 10–11 are activated.
- [ ] Classical, neural, and physics-plus-residual UAV models have been compared under nominal and shifted conditions.
- [ ] Transferred and embodiment-specific intelligence components are distinguished by evidence.
- [ ] Perception, belief, memory, planning, control, prediction, learning, and safety use documented interfaces.
- [ ] Every learned component has a classical baseline.
- [ ] Every learned component has a safe fallback.
- [ ] Analytical, neural, hybrid, and the admitted learned latent-model planning approach have been compared reproducibly.
- [ ] Any UAV RL capability reuses a Phase 6–9 method under a recorded transfer hypothesis; no new general-purpose RL family is introduced during integration.
- [ ] The primary hypothesis has an evidence-based conclusion.
- [ ] Every released benchmark has an operational design domain, hazard traceability, and defined minimal-risk behaviour.
- [ ] Safety and distribution-shift limitations are explicit.
- [ ] The complete lecture-note book compiles to PDF and HTML.
- [ ] Another person can reproduce the principal experiment from the documentation.
