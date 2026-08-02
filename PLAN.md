# Project Intelligence Plan

## 1. Project identity

**Project Intelligence** is a production-style autonomous-intelligence research platform for studying how an embodied agent perceives, estimates, remembers, predicts, plans, learns, and acts safely under uncertainty.

The project is organised around one central question:

> **How can we understand and build intelligence that constructs useful internal models of the world, reasons about possible futures, and safely pursues long-term goals under uncertainty?**

The robot is the experimental platform, not the final intellectual objective. The project must produce three connected outcomes:

1. **Knowledge:** a coherent set of lecture notes covering the mathematics, physics, robotics, aerospace engineering, AI, and reinforcement learning required by the project.
2. **Engineering:** tested autonomous capabilities and shared interfaces across bounded simulated embodiments, built with ROS 2, PyTorch, modern C++, Python, simulation, telemetry, and reproducible environments.
3. **Research:** an evidence-based investigation of physics-informed world models for safe long-horizon decision-making.

## 2. Research missions and releases

The project uses several bounded simulated missions to study common intelligence rather than treating any single robot as the final objective. Across the missions, the system must:

1. receive a structured mission;
2. enter a previously unseen environment;
3. estimate its position, orientation, and motion;
4. detect inspection targets, obstacles, and hazards;
5. construct a geometric and semantic world representation;
6. remember important previous observations;
7. predict robot, object, agent, and environmental dynamics where relevant;
8. evaluate alternative future trajectories;
9. choose safe actions under uncertainty;
10. adapt to disturbances and model errors;
11. respect embodiment-specific motion, force, energy, and safety constraints;
12. report its beliefs, uncertainty, decisions, and safety interventions.

The mobile robot first establishes reusable estimation, mapping, planning, control, safety, and reinforcement-learning foundations through an autonomous inspection mission. A simulated manipulator then becomes the primary learning and world-model research platform: it must grasp an object, reorient it to expose required surfaces for inspection, place it safely, and recover from declared planning, perception, grasp, contact, and model failures. A bounded road-agent benchmark tests whether the prediction, uncertainty, and decision abstractions transfer to a dynamic multi-agent domain without building a complete self-driving-car stack.

Phase 9 produces the **Core Intelligence Release** containing the mobile-robot foundation, the manipulation experiments, the road-agent transfer study, and the primary research conclusion. Phases 10–11 are a separately gated UAV extension: a classical multirotor inspection-and-return baseline is established before learned models are introduced. Phase 12 produces the integrated multi-embodiment release if the UAV extension is activated.

## 3. Scope

### Included

- mathematical foundations for autonomous systems;
- rigid-body mechanics and aerospace dynamics;
- state estimation and uncertainty;
- computer vision and sensor perception;
- mapping, SLAM, semantic representation, and memory;
- search, planning, optimisation, and control;
- advanced reinforcement learning;
- simulated manipulator kinematics, dynamics, planning, grasping, contact-aware control, imitation learning, and reinforcement learning;
- system identification and learned world models;
- model-based planning and imagination;
- selected self-driving intelligence: multi-sensor estimation primitives, dynamic-agent tracking and prediction, risk-aware decisions, and automotive-inspired scenario and safety methods;
- ROS 2 and PX4 integration;
- software engineering, systems engineering, safety, testing, CI, telemetry, and reproducibility;
- a compiled lecture-note book and final research report.

### Deferred until the core platform is complete

- physical robot, manipulator, or UAV hardware;
- humanoids, mobile manipulation, multiple manipulator platforms, and robot swarms;
- fixed-wing aerodynamics;
- a complete self-driving-car stack, road-vehicle hardware, detailed tyre or suspension models, lane and traffic-rule infrastructure, HD-map production, and V2X;
- end-to-end vision-to-motor policies as the primary architecture;
- large vision-language-action models;
- custom foundation models;
- biologically realistic brain simulation;
- multiple simulator stacks without a defined comparison experiment;
- Kubernetes or unnecessary cloud infrastructure.

Depth, evidence, and completion take priority over adding technologies.

## 4. Environment decision

The initial project environment is:

```text
Windows 11 host
└── WSL2 Ubuntu 24.04
    ├── ROS 2 Jazzy
    ├── Gazebo Harmonic
    ├── ros2_control and MoveIt 2 when manipulation begins
    ├── PyTorch with CUDA
    ├── Python and modern C++
    ├── Quarto and LaTeX
    ├── Docker when justified
    └── PX4 software-in-the-loop in the UAV phase
```

### Environment rules

- The authoritative project checkout will live in the WSL Linux filesystem, for example `~/repos/robotics_autonomous`, rather than under `/mnt/c` or `/mnt/d`.
- The Codex desktop app may run on Windows while accessing the WSL checkout; all project build, installation, simulation, and verification commands will execute through Ubuntu WSL2. Installing the Codex CLI inside WSL is optional.
- The NVIDIA driver remains installed on Windows; CUDA-enabled PyTorch runs inside WSL2.
- The currently empty second SSD does not need to be dedicated to Ubuntu. It may later hold the WSL virtual disk, datasets, telemetry, model artefacts, Docker storage, or backups.
- Native Ubuntu is postponed until WSL2 causes a demonstrated limitation involving hardware access, DDS networking, real-time timing, simulator graphics, CUDA profiling, or PX4 hardware-in-the-loop.
- A future dedicated desktop may use native Ubuntu. Its exact Ubuntu, ROS, CUDA, and simulator versions will be selected at purchase time.

### Docker policy

Docker supports reproducibility but must not delay the first capability.

1. Establish ROS 2, Gazebo, PyTorch, and the document toolchain directly in WSL2.
2. Record versions and installation decisions.
3. Prove the first ROS workspace builds, launches, and tests correctly.
4. Reproduce that working environment in one development container.
5. Use containers for CI and headless simulation.
6. Add separate training or runtime images only when an actual dependency or deployment boundary appears.

### Tooling and research architecture

1. **Research primacy:** Treat production robotics tools as the experimental platform for the main reinforcement-learning and world-model hypothesis, not as a prerequisite catalogue to complete before intelligence research. Add a tool only when the active capability requires a bounded production, baseline, measurement, safety, or research function.
2. **Layered responsibilities:** Use Linux, modern C++, Python, CMake, Git, automated testing, and justified containers as the production foundation; ROS 2, `tf2`, `ros2_control`, Gazebo, and `rosbag2` with MCAP as the integration platform; Nav2, MoveIt 2, Pinocchio, Eigen, and selected optimisation solvers for classical baselines; OpenCV, PCL, and GTSAM for observation and belief; and PyTorch with NumPy/SciPy for learning, world models, uncertainty, and predictive planning.
3. **Phase-gated adoption:** Introduce Eigen with the first required C++ spatial or numerical capability, OpenCV and the minimum required PCL subset with perception, GTSAM after foundational estimators and pose graphs are understood, Nav2 with bounded mobile-robot integration, and MoveIt 2 plus Pinocchio with classical manipulation. Do not install, teach, or integrate these merely because they appear in the roadmap.
4. **Research-core boundary:** Keep learning environments, replay and trajectory-data contracts, analytical and learned transition models, rewards, safety costs, and evaluation logic independent of ROS where practical. Connect them to ROS, simulators, and deployed nodes through narrow adapters with explicit schemas, units, frames, timestamps, validity, and failure behaviour.
5. **Classical controls:** Every learned policy, predictor, or planner must be compared with the relevant frozen classical baseline and remain subject to an independent action validator and safety supervisor. Production frameworks supply controls and fallbacks; they do not determine the research result.
6. **Simulator policy:** Keep Gazebo as the primary integration and acceptance simulator. Add a second simulator, including MuJoCo, only after a bounded benchmark demonstrates a necessary contact-fidelity, throughput, reproducibility, or parallel-sampling advantage, and preserve simulator-independent task, data, and evaluation contracts.
7. **Acceleration and deployment gate:** Use CUDA through PyTorch before writing custom kernels. Introduce ONNX Runtime or TensorRT only after a selected model has a stated deployment target, measured latency or resource requirement, numerical-equivalence checks, and a reproducible benchmark; do not optimise every research candidate for deployment.
8. **Concurrency discipline:** Treat concurrency as a cross-cutting engineering concern. Specify callback groups, executors, rates, deadlines, queue bounds, ownership, synchronisation, cancellation, and shutdown behaviour; separate control-loop work from blocking I/O and learning; prefer deterministic batching or multiprocessing before distributed infrastructure; and add Ray, custom CUDA streams, or lock-free structures only after profiling justifies them.
9. **Reproducible intelligence experiments:** Version datasets, episode splits, configurations, seeds, checkpoints, simulator parameters, model artefacts, and evaluation protocols. Preserve failures and interventions, keep training separate from held-out evaluation, and record CPU, GPU, memory, latency, interaction count, and wall-clock cost when they affect a claim.

## 5. Research structure

### Supporting research questions

| Capability | Research question |
|---|---|
| Perception | How should raw observations become useful objects and geometry? |
| Belief | How can the system estimate hidden state from noisy and incomplete information? |
| Representation | What internal state is sufficient for decision-making? |
| Memory | What should persist from previous experience? |
| Prediction | How can the system predict the consequences of its actions? |
| Planning | How should it compare possible futures? |
| Learning | When should experience improve or replace explicit engineering? |
| Manipulation | How should intelligence act when contact, friction, grasping, and multiple valid behaviours make explicit modelling incomplete? |
| Dynamic agents | How should tracked agents become calibrated future predictions and bounded risk-aware decisions? |
| Safety | How should it behave when its model or confidence is unreliable? |
| Transfer | Which interfaces, models, learning methods, and safety mechanisms transfer among a mobile robot, manipulator, road-agent benchmark, and UAV? |

### Main hypothesis

> On the primary contact-rich manipulation task, a hybrid world model combining known physical dynamics with learned residual dynamics will require fewer samples, generalise better, and support safer planning than a purely neural dynamics model.

The road-agent and UAV experiments provide secondary transfer evidence. They test whether the same prediction, uncertainty, and fallback abstractions remain useful in different dynamics, but they cannot rescue a failed primary manipulation hypothesis.

### Main comparisons

- classical controller and planner;
- behavioural cloning and recovery-informed imitation;
- goal-conditioned and residual reinforcement learning;
- analytical physics model with model-predictive control;
- model-free reinforcement learning;
- purely neural dynamics model;
- physics model plus learned residual;
- predictive planning using analytical, neural, and hybrid models;
- learned decision system with a classical safety supervisor.

### Primary measures

- mission success and completion time;
- collision and safety-violation rate;
- minimum obstacle clearance;
- manipulation pose error, grasp and recovery success, peak contact force, and joint or force constraint violations;
- road-agent displacement error, negative log-likelihood, calibration, missed conflicts, unnecessary stops, and minimum separation;
- energy use and return reserve;
- localisation and trajectory-tracking error;
- perception accuracy, latency, and calibration;
- one-step and long-horizon prediction error;
- uncertainty calibration and out-of-distribution detection;
- training sample efficiency;
- demonstration efficiency and environment interaction count;
- average, worst-case, and distribution-shift performance;
- planning, inference, and control latency.

## 6. Project operating method

Every implementation-sized capability follows one dependency-gated cycle:

    Learn and write → Review → Specify → Implement and document → Verify

A project phase contains several such cycles. Work forward through one active capability at a time; do not require unrelated theory from the rest of the phase to be complete before useful engineering begins. Treat each phase's capability order as a sequence of complete cycles, not as a phase-wide waterfall. Phase 0 is an environment bootstrap exception, and Phase 12 integrates already verified capabilities rather than introducing planned scientific or algorithmic work.

### Step 1 — Learn and write

Learn and document the theory required by the active capability. Begin from the intended robot behaviour and develop the mathematical model, notation, units, assumptions, prerequisites, and limitations before translating it into software.

Learning is interleaved with short retrieval tests:

    Learn one concept
          ↓
    Complete a quick closed-book test
          ↓
    Check the answer and correct misconceptions
          ↓
    Continue to the next concept

Each quick test should normally take 5–15 minutes and combine a small selection of:

- recall: define the concept and notation;
- explanation: describe the idea in plain language;
- derivation: reproduce one essential mathematical step;
- application: solve a short representative problem;
- judgement: identify assumptions, units, or failure conditions.

If a test exposes a gap, review only the missed concept and test it again; do not restart the chapter. Begin later study sessions with two or three questions from earlier concepts, and finish each chapter with one cumulative test. Record important misconceptions so they can be corrected in the learning note or revisited later.

### Step 2 — Review and specify

The prerequisite learning is ready for engineering when its central ideas can be explained, derived, applied, connected to engineering decisions, and bounded by explicit assumptions and limitations. The relevant retrieval tests must be satisfactory; if the prerequisite learning block completes a chapter, its cumulative test must also pass. Correct a failed prerequisite before continuing, but schedule non-critical weaknesses for spaced review.

Define the minimum engineering commitments for the active capability:

- measurable requirements;
- the simplest credible baseline;
- interfaces and architectural boundaries;
- predefined acceptance cases;
- explicit exclusions.

Engineering may begin when the prerequisite theory has been reviewed and these commitments are coherent enough to guide implementation and verification. Project-specific specifications belong in the docs directory rather than in timeless learning notes.

### Step 3 — Implement and document

Develop the smallest credible implementation in an order that preserves traceability:

    Mathematical model
          ↓
    Pure implementation and unit tests
          ↓
    Subsystem interface and integration tests
          ↓
    Simulation integration

Create an implementation companion only when implementation of its first capability begins; do not create an empty placeholder chapter. The companion records durable implementation know-how: the equation-to-software mapping, interface contract, implementation-independent pseudocode, one small reference snippet when useful, invariants and test cases, and numerical or physical cautions.

Keep production code in ros_ws/src, project-specific requirements and interfaces in docs, verification evidence in reports, and progress tracking in CHECKLIST.md.

### Step 4 — Verify and integrate

Run the predefined acceptance cases and record requirement results, relevant performance measures, safety and failure observations, known limitations, and deferred improvements. Correct blocking defects before integration and place non-blocking improvements in the backlog.

Integrate a capability only after its acceptance cases pass. Revise a learning note only to correct an error or add a durable lesson; do not repeat the entire learning cycle after ordinary implementation feedback.

A phase is complete when its required capability cycles have been integrated and the phase-level exit criteria and acceptance scenarios pass.

### Time allocation

Use these ranges as guidance across a capability rather than as fixed quotas:

- 25–35%: learning, review, and note writing;
- 50–60%: specification and implementation;
- 10–20%: verification and integration.

Theory must be coherent and sufficient, not encyclopaedic.

## 7. Intelligence architecture

```text
Mission request
      │
      ▼
Mission validation and goal decomposition
      │
      ▼
Mission executive
      │
      ├────────────── World state and memory ───────────────┐
      │                                                      │
      ▼                                                      ▼
Global planning                                      Predictive world model
      │                                                      │
      ▼                                                      │
Local trajectory planning ◄──── imagined trajectories ───────┘
      │
      ▼
Safety supervisor
      │
      ▼
Guidance and control
      │
      ▼
Mobile robot, manipulator, or UAV
      │
      ▼
Sensors
      │
      ├──► Perception
      ├──► State estimation
      └──► Mapping and memory
```

### Architectural rules

1. Downstream modules consume timestamped state estimates and uncertainty, not unqualified guesses.
2. Frames, units, timing, valid ranges, and stale-data behaviour are explicit.
3. Classical mechanics, estimation, control, and planning are used where structure is known.
4. Learning is used for uncertain patterns, residuals, or bounded decisions where it demonstrates value.
5. Every learned component has a classical baseline and fallback.
6. The safety supervisor can constrain, replace, or reject any proposed action.
7. Mission-level AI and language models cannot directly control actuators.
8. Simulation ground truth may evaluate the system but cannot leak into controller inputs.
9. Important beliefs, alternatives, predicted outcomes, decisions, and interventions are logged.
10. Shared interfaces are reused across embodiments only when their frames, units, timing, state semantics, constraints, and failure assumptions remain valid.
11. The road-agent benchmark reuses prediction, uncertainty, and decision interfaces but does not acquire an actuator-control stack.

## 8. Roadmap

At 8–12 focused hours per week, the Core Intelligence Release through Phase 9 is expected to take approximately 24–30 months. Completing the separately gated UAV extension and integrated Phase 12 release may extend the programme to approximately 32–42 months. Durations are planning ranges; exit evidence, rather than elapsed time, permits progression, and the Phase 9 core release is a valid stopping point.

### Phase 0 — Development environment

**Indicative duration:** 2–4 weeks

**Purpose:** Establish and verify the reproducible development environment required by the later learning, engineering, and release phases.

Phase 0 is an environment bootstrap phase rather than a capability-learning phase. It does not require a lecture-note chapter or the ordinary dependency-gated capability lifecycle.

#### Set up

- WSL2 Ubuntu environment;
- authoritative repository checkout in the WSL Linux filesystem;
- Codex operation inside WSL2;
- ROS 2 Jazzy and Gazebo Harmonic;
- modern C++ and Python toolchains;
- PyTorch with CUDA access;
- Quarto and LaTeX toolchain;
- recorded environment versions and installation decisions.

#### Verify

- build a minimal ROS workspace;
- run a minimal ROS publisher/subscriber smoke test;
- launch Gazebo Harmonic with a minimal documented command;
- verify PyTorch GPU access;
- compile a minimal Quarto/LaTeX document.

#### Exit evidence

- the authoritative checkout is under the WSL Linux home filesystem;
- a clean shell builds the minimal ROS workspace;
- the ROS and Gazebo smoke tests pass through documented commands;
- PyTorch detects the GPU;
- the document toolchain compiles a minimal document;
- environment versions and verification results are recorded.

### Phase 1 — Geometry, mechanics, and control

**Indicative duration:** 8–10 weeks

**Question:** How can desired motion be converted into stable physical action?

#### Learn and write

- vectors, matrices, frames, rotations, homogeneous transforms, and Jacobians;
- ordinary differential equations and numerical integration;
- differential-drive kinematics;
- nonholonomic constraints, curvature, Ackermann steering, and the kinematic bicycle model as a bounded comparison rather than a second vehicle implementation;
- velocity, acceleration, curvature, and jerk constraints for smooth trajectories;
- Newtonian mechanics, force, torque, friction, and actuator limits;
- feedback, PID, stability intuition, delay, saturation, and disturbance rejection.

#### Engineer

- minimal differential-drive simulation with odometry;
- transform utilities and kinematic model;
- trajectory generator;
- open-loop, proportional, and PID controllers;
- speed, acceleration, curvature where applicable, and jerk limits;
- command validation, watchdog, emergency stop, and stopped-safe fallback.

#### Verify

Compare controllers on straight and curved trajectories under noise, latency, saturation, disturbance, and model mismatch. Measure tracking error, overshoot, settling time, control effort, trajectory smoothness, and constraint violations.

#### Exit evidence

- tracking requirements pass across the fixed scenarios;
- controllers remain bounded under declared disturbances;
- safety tests pass;
- the observed behaviour can be explained from the theory chapter.

### Phase 2 — Probability and state estimation

**Indicative duration:** 8–10 weeks

**Question:** How can the robot infer hidden state from noisy and incomplete measurements?

#### Learn and write

- conditional probability, Bayes' rule, Gaussian variables, and covariance;
- recursive Bayesian filtering and the Kalman filter;
- nonlinear measurement models, extended Kalman filters, unscented transforms, and a bounded UKF comparison;
- Mahalanobis gating, nearest-neighbour data association, track lifecycle, and redundant-sensor disagreement;
- observability, sensor bias, drift, latency, calibration, estimator integrity, and numerical conditioning.

#### Engineer

- wheel-odometry, IMU, and landmark or position sensor models;
- odometry-only and naive-fusion baselines;
- Kalman and extended Kalman filters;
- bounded UKF comparison and reusable position-and-velocity tracking primitives;
- covariance output, innovation monitoring, and sensor-health flags;
- measurement gating, data association, track lifecycle, and redundant-sensor disagreement detection;
- noise, bias, latency, outlier, and dropout injection.

#### Verify

Compare odometry only, naive fusion, correctly tuned EKF, incorrectly tuned EKF, a justified UKF case, and dropout cases. Test gating and association under clutter and missed detections. Measure state error, innovation statistics, uncertainty consistency, integrity detection, and recovery.

#### Exit evidence

- state and covariance requirements pass;
- incorrect assumptions produce detectable inconsistency;
- sensor loss triggers defined degraded behaviour.

### Phase 3 — Perception and semantic understanding

**Indicative duration:** 10–12 weeks

**Question:** How can sensory signals become task-relevant objects, geometry, and meaning?

#### Learn and write

- camera models, projective geometry, rigid transforms, and geometric error;
- optics, depth sensing, LiDAR geometry, resolution, lighting, and noise;
- point-cloud coordinates, filtering, voxelisation, clustering, and three-dimensional bounding geometry;
- camera–range-sensor extrinsic calibration, temporal synchronisation, and multimodal association;
- neural networks, backpropagation, CNNs, and transfer learning;
- augmentation, class imbalance, calibration, latency, domain shift, and multi-object tracking metrics.

#### Engineer

- calibrated camera and range preprocessing;
- the minimum 3D point-cloud processing required by a bounded geometric perception capability;
- transfer-learned detector or segmenter;
- confidence calibration, track identity, covariance, lifecycle, and object tracking;
- projection into the shared world frame;
- versioned dataset, annotation rules, training pipeline, model registry, and ROS inference node.

#### Verify

Evaluate normal, blurred, low-light, occluded, and unfamiliar-background scenarios together with calibration error, timestamp offset, missed detections, false positives, and crossing tracks. Measure task accuracy, tracking quality, confidence calibration, latency, resource use, and downstream navigation impact.

#### Exit evidence

- outputs use correct frames and timestamps;
- confidence degrades detectably under adverse conditions;
- inference meets the timing budget;
- data, model, and evaluation versions reproduce the result.

### Phase 4 — Mapping, SLAM, and memory

**Indicative duration:** 8–10 weeks

**Question:** What should the system remember, and when should previous experience influence a current decision?

#### Learn and write

- occupancy grids, SLAM, pose graphs, loop closure, and graph optimisation;
- point-cloud registration, ICP, convergence, degeneracy, and initialisation sensitivity, with NDT at comparative conceptual depth;
- static geometry, dynamic occupancy, moving-object filtering, temporal confidence, and map ageing;
- spatial indexing and nearest-neighbour retrieval;
- working, spatial-semantic, episodic, and learned memory;
- replay, retrieval, forgetting, and stale-memory risk;
- useful computational ideas from place cells, grid cells, and predictive coding.

#### Engineer

- occupancy map and SLAM integration;
- one bounded ICP-based scan-matching capability;
- separation of persistent static geometry from time-indexed dynamic agents;
- semantic observations attached to the map;
- episodic event schema and retrieval;
- deterministic mission replay;
- map and memory versioning;
- environmental change detection and invalidation rules.

#### Verify

Compare no persistent memory, geometric memory, and geometric-plus-episodic memory across repeated and changed missions. Test registration under poor initialisation, sparse or repeated geometry, and moving-object contamination.

#### Exit evidence

- memory improves at least one mission measure;
- stored information has provenance, time, confidence, and invalidation rules;
- stale memory cannot silently dominate decisions.

### Phase 5 — Planning and autonomous decision-making

**Indicative duration:** 8–10 weeks

**Question:** How can the robot compare alternative futures and pursue long-term goals?

#### Learn and write

- graphs, queues, heaps, complexity, Dijkstra, and A*;
- configuration space, collision detection, RRT, and RRT*;
- constrained optimisation, splines, trajectory smoothing, and MPC;
- analytical dynamic-agent motion prediction, multi-hypothesis futures, and predicted occupancy;
- time to collision, collision probability, chance constraints, and conservative fallback;
- expected utility, risk, proceed, slow, stop, yield, and replan behaviours, behaviour trees, and hierarchical planning.

#### Engineer

- validated mission schema;
- behaviour-tree or state-machine executive;
- A* global planner;
- local collision-avoidance baseline;
- sampling-based planning experiment;
- trajectory optimisation or MPC;
- a dynamic-agent prediction interface and risk-aware candidate-action evaluation;
- timeout, infeasibility, replanning, and decision logging.

#### Verify

Test obstacle density, narrow passages, moving obstacles, localisation uncertainty, blocked goals, limited computation, energy-aware costs, incorrect or delayed predictions, occlusion, horizon truncation, and overconfident uncertainty. Measure missed conflicts, unnecessary stops, minimum separation, progress, and decision latency in addition to ordinary planning measures.

#### Exit evidence

- the mobile robot completes the inspection mission;
- planner failures trigger a defined fallback;
- decision logs record alternatives, costs, constraints, and selection.

### Phase 6 — Reusable reinforcement-learning foundations

**Indicative duration:** 8–10 weeks

**Question:** When does learned behaviour provide value beyond explicit controllers and planners?

#### Learn and write

- MDPs, partial observability, policy gradients, and actor-critic methods;
- PPO, SAC, replay, entropy, and critic bias;
- recurrent, goal-conditioned, hierarchical, constrained, and offline RL;
- behavioural cloning from logged trajectories, covariate shift, offline-to-online learning, dataset imbalance, and intervention-labelled data;
- safe exploration, curriculum learning, domain randomisation, and distribution shift.

#### Engineer

Select one bounded task: energy-aware subgoal selection, dynamic-obstacle avoidance, precision docking, or adaptive disturbance rejection.

- freeze a classical baseline and shared evaluation interface;
- define a reusable episodic trajectory schema and preserve failure and intervention records;
- implement or reproduce PPO and SAC;
- implement one bounded behavioural-cloning baseline from frozen mobile-robot logs;
- track seeds, configurations, checkpoints, and training curves;
- add a safety wrapper and ROS inference interface.

#### Verify

Compare the classical, behavioural-cloning, PPO, and SAC baselines. Measure average and worst-case performance, sample efficiency, failure rate, robustness, inference latency, and safety interventions. Test missing, stale, late, invalid, and out-of-range policy outputs independently of reward.

#### Exit evidence

- a learned policy is integrated only if it demonstrates a meaningful advantage;
- held-out scenarios and multiple seeds support the result;
- the system remains operational and safe without the policy.

### Phase 7 — Classical simulated manipulation

**Indicative duration:** 10–12 weeks

**Question:** How can an articulated robot manipulate an inspection object reliably using explicit geometry, dynamics, contact models, planning, and control?

#### Learn and write

- serial kinematic chains, joint, configuration, and task spaces;
- forward, inverse, and differential kinematics;
- Jacobians, redundancy, null-space motion, singularities, and manipulability;
- manipulator dynamics, gravity, Coriolis, centrifugal, friction, and external-contact terms;
- grasp frames, contact normals, friction cones, and grasp stability;
- joint-space, task-space, impedance, and admittance control;
- configuration-space planning, time-indexed collision prediction, swept volumes, and safety envelopes.

#### Engineer

- one simulated six- or seven-degree-of-freedom arm with URDF, SRDF, `ros2_control`, MoveIt 2, and explicit limits;
- forward and inverse kinematics acceptance paths;
- planning-scene environment and self-collision checking;
- joint-space and Cartesian trajectory generation and execution;
- gripper and grasp-state handling;
- deterministic reach, grasp, lift, reorient, inspect, place, retreat, and stopped-safe executive;
- explicit timeout, unreachable goal, collision, failed grasp, stale pose, and excessive-force behaviour.

#### Verify

Test reachable and unreachable poses, multiple inverse solutions, singularities, joint limits, collisions, moving obstacles, planning timeout, object-pose error, failed grasps, changed mass, friction variation, and safe retreat. Measure success, pose error, latency, path length, clearance, peak contact force, and control effort.

#### Exit evidence

- the classical inspection manipulation mission passes its frozen nominal scenarios;
- unsafe trajectories are rejected before execution;
- declared failures reach a bounded hold, retreat, or stopped-safe state;
- the classical baseline and benchmark are frozen before learning begins.

### Phase 8 — Imitation and reinforcement learning for manipulation

**Indicative duration:** 10–14 weeks

**Question:** When do demonstrations and reinforcement learning improve contact-rich manipulation beyond the frozen classical baseline?

#### Learn and write

- behaviour cloning, covariate shift, and compounding execution error;
- recovery demonstrations, interventions, and DAgger;
- observation histories, action chunking, and multimodal expert behaviour;
- goal-conditioned MDPs, sparse rewards, Hindsight Experience Replay, and demonstration-seeded replay;
- offline-to-online and residual reinforcement learning;
- constrained policies, safety shielding, domain randomisation, and out-of-distribution detection.

#### Engineer

- versioned manipulation demonstrations extending the Phase 6 trajectory schema;
- pointwise behavioural cloning and recovery-informed cloning;
- observation history or action chunking only under a stated temporal hypothesis;
- reuse of the Phase 6 SAC infrastructure for goal-conditioned SAC with hindsight replay;
- one residual policy over a frozen classical controller;
- at most one generative imitation policy after a simpler baseline demonstrates a specific multimodality failure;
- independent action validation and the authoritative Phase 7 safety supervisor.

#### Verify

Compare the classical baseline, behavioural cloning, recovery-informed cloning, goal-conditioned SAC, and residual RL over multiple seeds and held-out object poses, masses, friction values, geometries, backgrounds, and pose errors. Measure data and interaction efficiency, success, collisions, constraint violations, contact force, recovery, latency, and worst-case performance.

#### Exit evidence

- learned methods are retained only when they earn a declared advantage;
- training, evaluation, interventions, and negative results are reproducible;
- the manipulator remains operational and safe without a learned policy.

### Phase 9 — World models, road-agent prediction, and Core Intelligence Release

**Indicative duration:** 12–16 weeks

**Question:** Do physics-informed learned world models improve contact-rich manipulation, and do their prediction and uncertainty abstractions transfer to road-agent motion?

#### Learn and write

- system identification, analytical dynamics, neural transitions, and learned residuals;
- probabilistic prediction, ensembles, aleatoric and epistemic uncertainty, and calibration;
- latent variables only when observable state proves insufficient;
- one-step and rollout error, model exploitation, random shooting, cross-entropy planning, and model-based RL;
- road-agent tracking, constant-velocity, constant-acceleration, and constant-turn-rate prediction;
- neural, residual, and multimodal trajectory prediction;
- predicted occupancy, time to collision, collision probability, and bounded proceed, slow, stop, yield, or replan decisions.

#### Models

Analytical model:

$$
\hat{s}_{t+1}=f_{\text{physics}}(s_t,a_t)
$$

Neural model:

$$
\hat{s}_{t+1}=f_\theta(s_t,a_t)
$$

Hybrid model:

$$
\hat{s}_{t+1}=f_{\text{physics}}(s_t,a_t)+r_\theta(s_t,a_t)
$$

#### Engineer

- analytical, neural, and physics-plus-residual manipulator models;
- calibrated predictive uncertainty, one-step and rollout evaluation, and one predictive planner with horizon and fallback limits;
- one versioned recorded or procedurally generated road-agent dataset;
- imperfect tracking followed by analytical, neural, and hybrid road-agent predictors;
- one bounded road decision interface using predicted occupancy and declared risk thresholds;
- shared prediction, uncertainty, logging, and evaluation abstractions only where their semantics genuinely agree.

#### Verify and release

Compare manipulation models on prediction, sample efficiency, calibration, out-of-distribution behaviour, computation, planning, safety, and task outcomes. Test model exploitation and uncertainty-triggered fallback. Compare road predictors on displacement error, likelihood, calibration, missed modes, conflicts, unnecessary stops, separation, progress, and latency under occlusion and unfamiliar motion.

- conclude the primary hypothesis from manipulation evidence;
- report road-agent results separately as transfer evidence;
- freeze benchmarks, baselines, ablations, metrics, seeds, and failure policies;
- reproduce the principal result from a clean environment;
- publish the Core Intelligence Release with the mobile robot, manipulator, road benchmark, data and model documentation, decision traces, negative results, and research conclusion.

### Phase 10 — UAV mechanics, estimation, planning, and classical control

**Indicative duration:** 12–16 weeks

**Question:** How can a multirotor estimate and control its three-dimensional motion safely using explicit models?

Phases 10–11 are a separately gated extension after the Core Intelligence Release. Phase 10 must freeze a valid classical UAV before learned components are introduced.

#### Learn and write

- three-dimensional frames, quaternions, angular velocity, attitude error, and six-degree-of-freedom dynamics;
- inertia, thrust, reaction torque, rotor allocation, drag, wind, and payload effects;
- hover linearisation, cascaded control, LQR, and constrained MPC;
- IMU, GNSS, barometer, magnetometer, optical flow, EKF, UKF, and estimator integrity;
- GPS-denied navigation, three-dimensional planning, dynamic-obstacle tracking, and predicted occupancy;
- energy, flight envelopes, geofencing, battery reserve, communication loss, and failsafe modes.

#### Engineer

- pinned PX4 software-in-the-loop and ROS 2 boundary;
- multirotor and actuator-allocation models;
- classical attitude and position controller;
- EKF baseline and one justified UKF comparison;
- wind, payload, optical-flow, and GPS-denial scenarios;
- minimum three-dimensional planner, dynamic-obstacle interface, energy and flight-envelope constraints;
- take-off, inspection, abort, return, landing, and emergency executive.

#### Verify

Test nominal inspection and return, wind, mass change, GPS loss, optical-flow degradation, sensor inconsistency, communication loss, low battery, and planner failure. Measure estimation consistency, tracking error, control effort, energy, clearance, latency, and safety interventions.

#### Exit evidence

- the classical UAV completes the inspection-and-return mission;
- every declared critical failure reaches a defined hover, abort, return, land, or terminated-safe mode;
- transferred and UAV-specific interfaces are distinguished;
- the classical benchmark is frozen before Phase 11.

### Phase 11 — UAV learned models and intelligence transfer

**Indicative duration:** 8–12 weeks

**Question:** Which learned prediction, planning, uncertainty, and safety components transfer from manipulation and road-agent intelligence to flight?

#### Learn and write

- system identification for wind, drag, payload, and actuator mismatch;
- neural and physics-plus-residual UAV dynamics;
- flight-specific calibration and distribution shift;
- prediction-aware planning, multi-hypothesis obstacles, and chance-constrained flight corridors;
- offline learning from flight, intervention, and failsafe logs;
- confidence-triggered fallback and residual policies over classical control.

#### Engineer

- transfer audit for mission, world state, trajectory data, models, uncertainty, planning, logging, and safety interfaces;
- analytical, neural, and physics-plus-residual UAV predictors;
- calibrated uncertainty under nominal and shifted conditions;
- one learned-model predictive planner with flight-envelope constraints and classical fallback;
- optional residual control only after a specific remaining gap is demonstrated.

#### Verify

Compare classical, analytical-model, neural-model, and hybrid-model flight under nominal and shifted wind, mass, battery, sensor, and communication conditions. Test model exploitation, overconfidence, late inference, missing models, invalid outputs, and the independence of the safety supervisor.

#### Exit evidence

- learned components are retained only when they earn a declared advantage;
- the UAV remains safe and operational without learned models;
- transferred and embodiment-specific intelligence claims are separated by evidence.

### Phase 12 — Integrated multi-embodiment research release

**Indicative duration:** 8–10 weeks

Phase 12 introduces no planned scientific or algorithmic capability. Evaluation gaps return to bounded capability cycles in the responsible earlier phase before release integration resumes.

#### Produce

- operational design domains and explicit exclusions for every released benchmark;
- frozen benchmarks, evaluation protocols, baselines, ablations, metrics, seeds, and versions;
- mobile-robot, manipulator, road-agent, and activated UAV evaluation suites;
- fault-injection, rare-event, and distribution-shift campaigns;
- hazard analysis, safety goals, functional and technical safety requirements, minimal-risk conditions, and hazard-to-test traceability;
- final architecture, interface, data, model, safety, and verification evidence;
- compiled lecture-note book and technical research report;
- representative demonstrations and interpretable decision, prediction, uncertainty, intervention, and fallback traces;
- explicit negative results, limitations, boundary conditions, and future questions.

An optional language interface may translate natural-language missions into a validated structured schema. It cannot generate actuator commands.

#### Exit evidence

- a clean environment reproduces the principal result;
- primary manipulation evidence, road and UAV transfer evidence, and supporting mobile-robot evidence remain distinct;
- claims are supported by versioned configurations, logs, tables, plots, and safety evidence;
- the main hypothesis has a defensible conclusion;
- demonstrated conclusions are separated from future hypotheses.

## 9. Lecture-note plan

The canonical learning artefact will be a Quarto book that can compile to PDF and HTML. Notebooks may generate calculations and figures, but they do not become the canonical narrative.

### Proposed parts

1. **Mathematical foundations**
   - linear algebra and coordinate geometry;
   - calculus and differential equations;
   - probability and Bayesian inference;
   - numerical methods and optimisation;
   - experimental and statistical methods.
2. **Mechanics and control**
   - kinematics;
   - Newtonian and rigid-body mechanics;
   - feedback and stability;
   - PID, state-space control, LQR, and MPC.
3. **Perception and belief**
   - sensor physics;
   - state estimation;
   - projective geometry and computer vision;
   - mapping, SLAM, and uncertainty.
4. **Planning and autonomy**
   - graph search;
   - motion and trajectory planning;
   - dynamic-agent prediction and risk-aware decisions;
   - behaviour trees and decision theory;
   - safety and degraded modes.
5. **Learning and intelligence**
   - neural representations;
   - reinforcement learning, imitation learning, offline learning, and safe exploration;
   - demonstrations, interventions, action chunking, and residual policies;
   - system identification and model-based reinforcement learning.
6. **Manipulation and contact**
   - serial-chain kinematics, Jacobians, inverse kinematics, and singularities;
   - manipulator dynamics, trajectory generation, and control;
   - grasping, contact, force, impedance, and safety envelopes;
   - classical, imitation, and reinforcement-learning manipulation.
7. **World models and dynamic agents**
   - system identification;
   - analytical, neural, and physics-plus-residual world models;
   - predictive uncertainty, imagined trajectories, and model exploitation;
   - road-agent tracking, trajectory prediction, and bounded risk-aware decisions.
8. **Aerospace systems**
   - multirotor dynamics;
   - estimation, GPS-denied navigation, planning, and flight control;
   - wind, energy, flight envelopes, learned residuals, and UAV autonomy.
9. **Research results**
   - experimental design;
   - benchmark definitions;
   - primary manipulation world-model comparison;
   - road and UAV transfer studies;
   - ablations, integrated safety evidence, limitations, and open questions.

### Source readiness

Before drafting a new mathematical, physical, algorithmic, or theoretical learning block, resolve its primary-source route under `AGENTS.md` and `textbooks/INDEX.md`. Existing sources cover manipulation mechanics well, but the project must establish approved routes for imitation and offline manipulation learning before Phase 8, learned and multimodal road-agent prediction before Phase 9, and dedicated multirotor and aerospace theory before Phase 10. The read-only `textbooks/` rule must be reconciled with any future need to extend the routing index; no learning block may improvise an unapproved substitute.

### Chapter standard

Each chapter contains:

1. motivation and learning objectives;
2. prerequisites;
3. notation and conventions;
4. assumptions;
5. central derivation;
6. worked example;
7. short self-tests after major concepts;
8. engineering interpretation;
9. connection to the implemented subsystem;
10. failure modes and limitations;
11. cumulative chapter test and exercises;
12. answers, hints, or worked solutions placed after the questions or in an appendix;
13. references.

### Implementation companions

Create an implementation companion only when implementation of its first capability begins; do not create empty placeholder chapters. One companion may serve a closely related theory cluster.

Each implementation block records durable know-how:

- the source equation, assumptions, and units;
- the software contract, including types, frames, valid ranges, and failure behaviour;
- implementation-independent pseudocode;
- one small reference snippet when useful;
- invariants and test cases;
- numerical and physical cautions.

Keep project-specific requirements, interfaces, and acceptance thresholds in docs; production code in ros_ws/src; verification evidence in reports. Implementation companions remain timeless and omit progress or implementation-status commentary.

## 10. Industry engineering standards

### Systems engineering

Maintain one living set of each of the following:

- concept of operations and mission scenarios;
- functional and non-functional requirements;
- logical and physical architecture;
- interface-control definitions;
- hazard and risk register;
- operational design domains and explicit exclusions for each benchmark;
- data cards and model cards for learned capabilities;
- requirement-to-verification matrix;
- architecture decision records for consequential decisions;
- subsystem design reviews;
- release verification reports.

Every subsystem must answer:

1. What problem does it solve?
2. What assumptions does it make?
3. How is it verified?
4. What happens when it fails?

### Requirement format

Every requirement includes:

- unique ID;
- rationale;
- operating conditions;
- measurable threshold;
- verification method;
- final result.

Example:

> `SAFE-REQ-012`: In nominal static-obstacle scenarios, the robot shall maintain at least 0.5 m clearance in 99% of evaluation runs. Verification uses ground-truth simulation trajectories from the frozen benchmark suite.

### Interface format

Every interface defines:

- schema and meaning;
- units and coordinate frame;
- timestamps and clock source;
- expected frequency and latency;
- valid ranges;
- uncertainty representation;
- invalid, missing, and stale-data behaviour.

### Software engineering

- modern C++ for control, safety, and performance-sensitive ROS nodes;
- Python and PyTorch for training, data, evaluation, and suitable inference;
- small packages with explicit responsibilities;
- configuration separated from source code;
- deterministic fixtures and explicit random seeds;
- automated formatting, linting, and static analysis;
- unit, integration, simulation, and fault-injection tests;
- structured logging and diagnostics;
- dependency pinning and reproducible builds;
- review before integration;
- versioned capability releases.

### Testing pyramid

```text
Unit tests
    ↓
Package integration tests
    ↓
ROS interface tests
    ↓
Headless simulation smoke tests
    ↓
Scenario acceptance tests
    ↓
Monte Carlo evaluation
    ↓
Fault injection
```

### CI progression

Initial CI:

- formatting and linting;
- build;
- unit tests;
- lecture-note compilation.

Mature CI:

- static analysis;
- ROS integration tests;
- headless simulation;
- coverage reporting;
- container build;
- deterministic evaluation subset;
- document link and citation checks.

Long RL training and full Monte Carlo evaluation run on scheduled or manually triggered pipelines, not on every commit.

### Observability

Record at minimum:

- timestamp and simulation time;
- estimated pose and covariance;
- embodiment state, object state, agent tracks, and their uncertainty where relevant;
- sensor-health state;
- detected objects and confidence;
- map and model versions;
- planner alternatives and predicted trajectories;
- selected action;
- controller error;
- contact events, peak force, joint or flight-envelope state, and constraint violations where relevant;
- safety interventions;
- CPU, memory, and GPU use;
- experiment configuration and software version.

### Safety

The platform will include:

- command validation;
- speed and acceleration limits;
- manipulator joint, force, collision, and safety-envelope constraints;
- watchdogs and emergency stop;
- stale-data rejection;
- uncertainty-triggered fallback;
- geofencing in the UAV phase;
- battery reserve;
- degraded operating modes;
- fault-injection tests.

Safety evidence adopts transferable ideas from automotive systems engineering without claiming ISO 26262 compliance. Each released benchmark defines its operational design domain, hazards, safety goals, functional and technical safety requirements, minimal-risk conditions, and hazard-to-test traceability.

## 11. Experiment contract

Every substantive comparison declares before execution:

- hypothesis and falsification condition;
- baseline and ablations;
- operational design domain and explicit exclusions;
- independent, dependent, and controlled variables;
- scenario set and random seeds;
- trial count;
- metrics and aggregation;
- failure definition;
- excluded-run policy;
- dataset split, intervention, reset, and safety-supervisor policies where learning is involved;
- software, data, and model versions.

Results must include failures and negative outcomes, not only successful demonstrations.

## 12. First 12 weeks

During every capability cycle, learn one concept, complete a quick closed-book test, correct misconceptions, and continue. Use cumulative checks when a prerequisite learning block reaches a chapter boundary.

### Weeks 1–4 — Development environment

- establish WSL2 Ubuntu 24.04;
- configure Codex to run inside WSL2;
- confirm the authoritative checkout is in the WSL Linux filesystem;
- install and verify ROS 2 Jazzy and Gazebo Harmonic;
- verify PyTorch GPU access;
- establish C++ and Python toolchains;
- establish the Quarto/LaTeX compiler;
- build a minimal ROS workspace;
- run minimal ROS, Gazebo, GPU, and document-compilation smoke tests;
- record versions, commands, and verification results.

### Weeks 5–6 — Coordinate-transformation capability

- review linear algebra, coordinate frames, rotations, notation, and units;
- learn and write any missing prerequisite material for homogeneous transformations and Jacobians;
- pass the applicable retrieval or cumulative tests;
- specify the coordinate-transform interfaces and acceptance cases;
- implement and unit-test only the reviewed transformation operations.

### Weeks 7–8 — Motion-model capability

- review kinematics, ordinary differential equations, numerical integration, and model-error assumptions;
- pass the applicable tests and specify the differential-drive model, integrator, and acceptance cases;
- create the implementation companion when implementation begins;
- implement the pure motion model and numerical integrator with unit tests;
- verify straight and curved motion against analytical expectations.

### Weeks 9–10 — Initial control capability

- learn and review feedback, proportional control, transient response, saturation, delay, and disturbances;
- pass the applicable retrieval tests and define the open-loop and proportional-control contracts;
- implement the simplest open-loop and proportional baselines;
- add unit tests and compare the baselines in simulation.

### Weeks 11–12 — Integrate and verify

- integrate the accepted motion and control capabilities in simulation;
- add structured telemetry and failure diagnostics;
- run the predefined straight and curved trajectory cases;
- measure tracking error, transient response, constraint violations, and control effort;
- record evidence, limitations, and deferred work.

PID, safety fallback, and the remaining Phase 1 capability cycles continue afterward.

## 13. Scope-control rules

A proposed addition enters the active plan only if it:

1. directly tests a research question;
2. unblocks the current capability;
3. has a simpler baseline;
4. has measurable acceptance criteria;
5. does not displace a more important foundation.

Only one implementation-sized capability is active at a time. New ideas go to the backlog rather than expanding the current gate.

Only one embodiment is under active implementation at a time. The simulated manipulator is limited to one arm and one inspection task for the Core Intelligence Release. Self-driving content is limited to transferable foundations and the bounded Phase 9 road-agent prediction and decision benchmark. The UAV extension begins only after the Phase 9 release decision and freezes a classical flight baseline before learned transfer.

## 14. Principal risks

| Risk | Control |
|---|---|
| Theory expands without implementation | Time-box learning and use dependency-gated capability cycles |
| Technology breadth prevents completion | One embodiment and one simulator at a time; preserve Phase 9 as a valid core stopping point |
| Documentation becomes bureaucracy | Keep one living artefact per systems-engineering concern |
| WSL graphics or networking limits simulation | Maintain headless tests and migrate only after demonstrated failure |
| ROS and Python dependency conflicts | Pin dependencies and isolate environments |
| RL consumes excessive time and compute | One bounded task with a frozen classical baseline |
| Demonstration or logged data create misleading results | Version datasets, split by episode and scenario, preserve interventions and failures, and test covariate shift |
| Manipulator contact instability obscures intelligence results | Freeze a classical arm, grasp, controller, and contact benchmark before learning or world-model comparisons |
| Learned components hide unsafe failures | Independent supervisor, uncertainty thresholds, and fallback |
| World-model planner exploits model errors | Short horizons, uncertainty penalties, ensembles, and OOD tests |
| Road content expands into a complete self-driving stack | Restrict implementation to tracking, prediction, calibrated risk, and bounded decisions |
| Shared interfaces conceal incompatible embodiment semantics | Audit frames, units, timing, state meaning, constraints, and failure assumptions before reuse |
| UAV complexity destabilises the project | Begin only after the Core Intelligence Release and freeze classical flight before learned transfer |
| Missing primary-source routes block compliant note drafting | Resolve imitation, road-prediction, and aerospace source gaps before their dependent learning blocks |
| Positive-result bias weakens research | Predeclare experiments and preserve negative results |

## 15. Completion criteria

### Core Intelligence Release — Phase 9

The first complete research release is achieved when:

- the mobile robot completes the defined inspection mission and supplies the reusable autonomy and RL foundations;
- the classical manipulator completes grasp, reorientation, inspection, placement, and safe retreat;
- manipulation imitation and reinforcement-learning methods are compared with the frozen classical baseline;
- analytical, neural, and hybrid manipulator world models are compared reproducibly;
- the bounded road-agent benchmark compares analytical, neural, and hybrid prediction and risk-aware decisions;
- the primary hypothesis has an evidence-based conclusion from manipulation, with road evidence reported separately as transfer evidence;
- every learned component has a classical baseline and safe fallback;
- safety, data, model, and distribution-shift limitations are explicit;
- another person can reproduce the principal core experiment from the documentation.

### Integrated multi-embodiment release — Phase 12

The extended release is achieved when:

- the UAV completes the transferred inspection-and-return mission if Phases 10–11 are activated;
- classical, neural, and physics-plus-residual UAV models are compared under nominal and shifted conditions;
- transferred and embodiment-specific intelligence components are distinguished by evidence;
- perception, belief, memory, planning, control, prediction, learning, and safety communicate through documented and semantically valid interfaces;
- every released benchmark has an operational design domain, hazard traceability, and defined minimal-risk behaviour;
- the complete lecture notes compile to PDF and HTML;
- the integrated results, negative outcomes, limitations, and future hypotheses are reproducible and clearly separated.

Completion does not mean intelligence has been solved. It means the project has produced a coherent, falsifiable, and reusable account of how embodied intelligence can form beliefs, learn from experience, predict physical and agent futures, and act safely across manipulation, navigation, dynamic-agent reasoning, and optional flight under uncertainty.
