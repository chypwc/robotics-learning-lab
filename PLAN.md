# Project Intelligence Plan

## 1. Project identity

**Project Intelligence** is a production-style autonomous-intelligence research platform for studying how an embodied agent perceives, estimates, remembers, predicts, plans, learns, and acts safely under uncertainty.

The project is organised around one central question:

> **How can we understand and build intelligence that constructs useful internal models of the world, reasons about possible futures, and safely pursues long-term goals under uncertainty?**

The robot is the experimental platform, not the final intellectual objective. The project must produce three connected outcomes:

1. **Knowledge:** a coherent set of lecture notes covering the mathematics, physics, robotics, aerospace engineering, AI, and reinforcement learning required by the project.
2. **Engineering:** a tested autonomous system built with ROS 2, PyTorch, modern C++, Python, simulation, telemetry, and reproducible environments.
3. **Research:** an evidence-based investigation of physics-informed world models for safe long-horizon decision-making.

## 2. Final mission

The final system will perform a simulated autonomous inspection mission.

It must:

1. receive a structured mission;
2. enter a previously unseen environment;
3. estimate its position, orientation, and motion;
4. detect inspection targets, obstacles, and hazards;
5. construct a geometric and semantic world representation;
6. remember important previous observations;
7. predict vehicle and environmental dynamics;
8. evaluate alternative future trajectories;
9. choose safe actions under uncertainty;
10. adapt to disturbances and model errors;
11. manage energy and return safely;
12. report its beliefs, uncertainty, decisions, and safety interventions.

The mission will first be completed by a simulated differential-drive mobile robot. The resulting intelligence architecture will then be transferred to a simulated multirotor UAV.

## 3. Scope

### Included

- mathematical foundations for autonomous systems;
- rigid-body mechanics and aerospace dynamics;
- state estimation and uncertainty;
- computer vision and sensor perception;
- mapping, SLAM, semantic representation, and memory;
- search, planning, optimisation, and control;
- advanced reinforcement learning;
- system identification and learned world models;
- model-based planning and imagination;
- ROS 2 and PX4 integration;
- software engineering, systems engineering, safety, testing, CI, telemetry, and reproducibility;
- a compiled lecture-note book and final research report.

### Deferred until the core platform is complete

- physical robot or UAV hardware;
- humanoids, manipulators, and robot swarms;
- fixed-wing aerodynamics;
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
| Safety | How should it behave when its model or confidence is unreliable? |
| Transfer | Which capabilities transfer from a mobile robot to a UAV? |

### Main hypothesis

> A hybrid world model combining known physical dynamics with learned residual dynamics will require fewer samples, generalise better, and support safer planning than a purely neural dynamics model.

### Main comparisons

- classical controller and planner;
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
- energy use and return reserve;
- localisation and trajectory-tracking error;
- perception accuracy, latency, and calibration;
- one-step and long-horizon prediction error;
- uncertainty calibration and out-of-distribution detection;
- training sample efficiency;
- average, worst-case, and distribution-shift performance;
- planning, inference, and control latency.

## 6. Project operating method

Every capability follows one deliberately simple lifecycle:

```text
Learn and write → Engineer → Verify and release
```

This replaces a repeated build-fail-study-rebuild loop that could prevent the project from progressing.

### Step 1 — Learn and write

Learn the required theory and produce the corresponding lecture-note chapter before subsystem implementation begins.

Begin from the phase question and intended robot behaviour in the roadmap. Do not create a separate definition stage. Develop the mathematical model, notation, units, assumptions, prerequisites, and limitations as part of learning. As understanding becomes sufficient, translate the theory into:

- measurable capability requirements;
- a simplest credible baseline;
- architecture and interface implications;
- predefined acceptance scenarios;
- explicit exclusions.

These engineering commitments are outputs of learning, not assumptions that must be settled before learning starts.

Learning is interleaved with short retrieval tests:

```text
Learn one concept
      ↓
Complete a quick closed-book test
      ↓
Check the answer and correct misconceptions
      ↓
Continue to the next concept
```

Each quick test should normally take 5–15 minutes and include a small mixture of:

- recall: define the concept and notation;
- explanation: describe the idea in plain language;
- derivation: reproduce one essential mathematical step;
- application: solve a short representative problem;
- judgement: identify assumptions, units, or failure conditions.

If a test exposes a gap, review only the missed concept and test it again; do not restart the chapter. Begin later study sessions with two or three questions from earlier concepts, and finish each chapter with one cumulative test. Record important misconceptions so that they can be addressed in the lecture note or a later review. This retrieval practice is part of learning, not a new open-ended project cycle.

The learning gate passes when the central ideas can be:

- explained clearly;
- derived mathematically;
- applied to representative problems;
- connected to engineering decisions;
- bounded by explicit assumptions and limitations.

The learning gate also requires satisfactory completion of the chapter's cumulative test. A failed prerequisite concept is corrected before engineering begins; non-critical weaknesses are scheduled for spaced review rather than blocking the project indefinitely.

Before engineering begins, the documented mathematics, requirements, baseline, interfaces, acceptance scenarios, and exclusions must be coherent enough to guide implementation and verification.

Small numerical calculations may be used when they materially clarify the theory, but a separate numerical-model phase is not mandatory.

### Step 2 — Engineer

After the learning gate passes, develop the capability using an industry-style lifecycle:

```text
Requirements
    ↓
Architecture and interfaces
    ↓
Implementation
    ↓
Unit and integration tests
    ↓
Simulation verification
    ↓
Integration into the complete system
```

### Step 3 — Verify and release

Run the predefined acceptance scenarios and record:

- requirement results;
- relevant performance measures;
- safety and failure observations;
- known limitations;
- deferred improvements.

Blocking defects are corrected before release. Non-blocking improvements enter the backlog. The theory chapter is revised only to correct an error or incorporate an important engineering result; the entire learning cycle is not repeated.

### Time allocation

Within a typical capability phase:

- 25–35%: learning and lecture-note writing;
- 50–60%: engineering;
- 10–20%: verification, integration, and release.

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
Robot or UAV
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

## 8. Roadmap

At 8–12 focused hours per week, the complete programme is expected to take approximately 18–24 months. Durations are planning ranges; exit evidence, rather than elapsed time, permits progression.

### Phase 0 — Development environment

**Indicative duration:** 2–4 weeks

**Purpose:** Establish and verify the reproducible development environment required by the later learning, engineering, and release phases.

Phase 0 is an environment bootstrap phase rather than a capability-learning phase. It does not require a lecture-note chapter or the three-stage capability lifecycle.

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
- Newtonian mechanics, force, torque, friction, and actuator limits;
- feedback, PID, stability intuition, delay, saturation, and disturbance rejection.

#### Engineer

- minimal differential-drive simulation with odometry;
- transform utilities and kinematic model;
- trajectory generator;
- open-loop, proportional, and PID controllers;
- speed and acceleration limits;
- command validation, watchdog, emergency stop, and stopped-safe fallback.

#### Verify

Compare controllers on straight and curved trajectories under noise, latency, saturation, disturbance, and model mismatch. Measure tracking error, overshoot, settling time, control effort, and constraint violations.

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
- nonlinear measurement models and extended Kalman filters;
- observability, sensor bias, drift, latency, calibration, and numerical conditioning.

#### Engineer

- wheel-odometry, IMU, and landmark or position sensor models;
- odometry-only and naive-fusion baselines;
- Kalman and extended Kalman filters;
- covariance output, innovation monitoring, and sensor-health flags;
- noise, bias, latency, outlier, and dropout injection.

#### Verify

Compare odometry only, naive fusion, correctly tuned EKF, incorrectly tuned EKF, and dropout cases. Measure state error, innovation statistics, uncertainty consistency, and recovery.

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
- neural networks, backpropagation, CNNs, and transfer learning;
- augmentation, class imbalance, calibration, latency, and domain shift.

#### Engineer

- calibrated camera and range preprocessing;
- transfer-learned detector or segmenter;
- confidence calibration and object tracking;
- projection into the shared world frame;
- versioned dataset, annotation rules, training pipeline, model registry, and ROS inference node.

#### Verify

Evaluate normal, blurred, low-light, occluded, and unfamiliar-background scenarios. Measure task accuracy, confidence calibration, latency, resource use, and downstream navigation impact.

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
- spatial indexing and nearest-neighbour retrieval;
- working, spatial-semantic, episodic, and learned memory;
- replay, retrieval, forgetting, and stale-memory risk;
- useful computational ideas from place cells, grid cells, and predictive coding.

#### Engineer

- occupancy map and SLAM integration;
- semantic observations attached to the map;
- episodic event schema and retrieval;
- deterministic mission replay;
- map and memory versioning;
- environmental change detection and invalidation rules.

#### Verify

Compare no persistent memory, geometric memory, and geometric-plus-episodic memory across repeated and changed missions.

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
- expected utility, risk, constraints, behaviour trees, and hierarchical planning.

#### Engineer

- validated mission schema;
- behaviour-tree or state-machine executive;
- A* global planner;
- local collision-avoidance baseline;
- sampling-based planning experiment;
- trajectory optimisation or MPC;
- timeout, infeasibility, replanning, and decision logging.

#### Verify

Test obstacle density, narrow passages, moving obstacles, localisation uncertainty, blocked goals, limited computation, and energy-aware costs.

#### Exit evidence

- the mobile robot completes the inspection mission;
- planner failures trigger a defined fallback;
- decision logs record alternatives, costs, constraints, and selection.

### Phase 6 — Advanced reinforcement learning

**Indicative duration:** 8–10 weeks

**Question:** When does learned behaviour provide value beyond explicit controllers and planners?

#### Learn and write

- MDPs, partial observability, policy gradients, and actor-critic methods;
- PPO, SAC, replay, entropy, and critic bias;
- recurrent, goal-conditioned, hierarchical, constrained, and offline RL;
- safe exploration, imitation, curriculum learning, domain randomisation, and distribution shift.

#### Engineer

Select one bounded task: energy-aware subgoal selection, dynamic-obstacle avoidance, precision docking, or adaptive disturbance rejection.

- freeze a classical baseline and shared evaluation interface;
- implement or reproduce PPO and SAC;
- track seeds, configurations, checkpoints, and training curves;
- add a safety wrapper and ROS inference interface.

#### Verify

Measure average and worst-case performance, sample efficiency, failure rate, robustness, inference latency, and safety interventions.

#### Exit evidence

- a learned policy is integrated only if it demonstrates a meaningful advantage;
- held-out scenarios and multiple seeds support the result;
- the system remains operational and safe without the policy.

### Phase 7 — World models and imagined futures

**Indicative duration:** 12–16 weeks

**Question:** Can an internal predictive model improve long-horizon decisions?

#### Learn and write

- system identification and analytical dynamics;
- neural and residual dynamics models;
- probabilistic prediction, ensembles, and uncertainty calibration;
- latent variables and variational inference when observable state is insufficient;
- one-step and rollout error, model exploitation, Dyna, PETS, Dreamer, and TD-MPC;
- random shooting, cross-entropy planning, and model-based RL.

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

- versioned trajectory-data schema and collection service;
- analytical, neural, and hybrid residual models;
- predictive uncertainty;
- one-step and rollout evaluation;
- random-shooting or cross-entropy planner;
- learned-model MPC, uncertainty penalties, horizon limits, and fallback thresholds.

#### Verify

Compare prediction error, calibration, sample efficiency, out-of-distribution behaviour, mission performance, safety, energy, and computation. Compare analytical MPC, neural-model MPC, hybrid-model MPC, and model-free RL.

#### Exit evidence

- the primary hypothesis is supported, rejected, or narrowed;
- uncertainty is useful for triggering fallback;
- planning does not silently exploit known model defects.

### Phase 8 — Aerospace theory and UAV transfer

**Indicative duration:** 12–16 weeks

**Question:** Which intelligence components transfer across embodiments, and which must change with vehicle physics?

#### Learn and write

- three-dimensional frames, quaternions, angular velocity, and six-degree-of-freedom dynamics;
- inertia tensors, thrust, reaction torque, rotor allocation, drag, and wind;
- energy consumption and flight envelopes;
- hover linearisation, cascaded control, LQR, and constrained MPC;
- geofencing, battery reserve, and failsafe behaviour.

#### Engineer

- PX4 software-in-the-loop;
- multirotor model and position/attitude control baseline;
- wind, payload, and energy models;
- flight-envelope and reserve constraints;
- transfer of mission, perception, memory, planning, telemetry, and safety interfaces.

#### Verify

Test nominal missions, wind, changed mass, estimator degradation, sensor dropout, model mismatch, communication loss, low battery, and planner failure.

#### Exit evidence

- the UAV completes inspection and return missions;
- declared failures enter a defined safe mode;
- transferred and UAV-specific components are distinguished.

### Phase 9 — Integrated research release

**Indicative duration:** 8–10 weeks

#### Produce

- frozen benchmark and evaluation protocol;
- baseline and ablation matrix;
- fault-injection and distribution-shift campaign;
- reproducible mobile-robot and UAV missions;
- data and model documentation;
- final architecture, safety, and verification reviews;
- compiled lecture-note book;
- technical research report;
- representative demonstrations and decision traces;
- explicit negative results, limitations, and future questions.

An optional language interface may translate natural-language missions into a validated structured schema. It cannot generate actuator commands.

#### Exit evidence

- a clean environment reproduces the principal result;
- claims are supported by versioned configurations, logs, tables, and plots;
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
   - behaviour trees and decision theory;
   - safety and degraded modes.
5. **Learning and intelligence**
   - neural representations;
   - advanced reinforcement learning;
   - system identification;
   - world models and model-based reasoning.
6. **Aerospace systems**
   - multirotor dynamics;
   - flight control;
   - wind, energy, flight envelopes, and UAV autonomy.
7. **Research results**
   - experimental design;
   - benchmark definitions;
   - world-model comparison;
   - ablations, integrated results, limitations, and open questions.

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

## 10. Industry engineering standards

### Systems engineering

Maintain one living set of each of the following:

- concept of operations and mission scenarios;
- functional and non-functional requirements;
- logical and physical architecture;
- interface-control definitions;
- hazard and risk register;
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
- sensor-health state;
- detected objects and confidence;
- map and model versions;
- planner alternatives and predicted trajectories;
- selected action;
- controller error;
- safety interventions;
- CPU, memory, and GPU use;
- experiment configuration and software version.

### Safety

The platform will include:

- command validation;
- speed and acceleration limits;
- watchdogs and emergency stop;
- stale-data rejection;
- uncertainty-triggered fallback;
- geofencing in the UAV phase;
- battery reserve;
- degraded operating modes;
- fault-injection tests.

## 11. Experiment contract

Every substantive comparison declares before execution:

- hypothesis and falsification condition;
- baseline and ablations;
- independent, dependent, and controlled variables;
- scenario set and random seeds;
- trial count;
- metrics and aggregation;
- failure definition;
- excluded-run policy;
- software, data, and model versions.

Results must include failures and negative outcomes, not only successful demonstrations.

## 12. First 12 weeks

During all theory weeks, use the sequence `learn one concept → quick closed-book test → correct misconceptions → continue`. End Weeks 6, 8, and 10 with cumulative checks covering the material learned so far.

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

### Weeks 5–6 — Mathematical language

Learn and write:

- vectors and matrices;
- coordinate frames and rotations;
- homogeneous transformations;
- Jacobians;
- notation and unit conventions.

Complete representative derivations and exercises.

### Weeks 7–8 — Kinematics and mechanics

Learn and write:

- differential-drive kinematics;
- velocity relationships;
- ordinary differential equations and numerical integration;
- force, torque, friction, and actuator limits;
- sources of model error.

### Weeks 9–10 — Control theory

Learn and write:

- feedback and proportional control;
- integral and derivative action;
- transient response and stability intuition;
- saturation, wind-up, delay, and disturbance rejection.

Compile the first complete lecture-note part before control implementation begins.

### Weeks 11–12 — First engineering capability

- implement coordinate-transform utilities;
- implement trajectory generation;
- implement open-loop and proportional control;
- add unit tests and structured telemetry;
- run the first controlled trajectory benchmark.

PID, safety fallback, and the complete Phase 1 release continue immediately afterward.

## 13. Scope-control rules

A proposed addition enters the active plan only if it:

1. directly tests a research question;
2. unblocks the current capability;
3. has a simpler baseline;
4. has measurable acceptance criteria;
5. does not displace a more important foundation.

Only one capability phase is active at a time. New ideas go to the backlog rather than expanding the current gate.

## 14. Principal risks

| Risk | Control |
|---|---|
| Theory expands without implementation | Time-box learning and use a defined learning gate |
| Technology breadth prevents completion | One embodiment and one simulator at a time |
| Documentation becomes bureaucracy | Keep one living artefact per systems-engineering concern |
| WSL graphics or networking limits simulation | Maintain headless tests and migrate only after demonstrated failure |
| ROS and Python dependency conflicts | Pin dependencies and isolate environments |
| RL consumes excessive time and compute | One bounded task with a frozen classical baseline |
| Learned components hide unsafe failures | Independent supervisor, uncertainty thresholds, and fallback |
| World-model planner exploits model errors | Short horizons, uncertainty penalties, ensembles, and OOD tests |
| UAV complexity destabilises the project | Transfer only after the mobile-robot mission passes |
| Positive-result bias weakens research | Predeclare experiments and preserve negative results |

## 15. Completion criteria

The first complete research release is achieved when:

- the mobile robot completes the defined inspection mission;
- the UAV completes the transferred inspection-and-return mission;
- perception, belief, memory, planning, control, prediction, learning, and safety communicate through documented interfaces;
- every learned component has a classical baseline and safe fallback;
- analytical, neural, and hybrid world models have been compared reproducibly;
- the primary hypothesis has an evidence-based conclusion;
- safety and distribution-shift limitations are explicit;
- the complete lecture notes compile to PDF and HTML;
- another person can reproduce the principal experiment from the documentation.

Completion does not mean intelligence has been solved. It means the project has produced a coherent, falsifiable, and reusable account of how an embodied agent can form beliefs, retain useful experience, imagine possible futures, and act safely toward long-term goals under uncertainty.
