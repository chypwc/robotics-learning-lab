# Project Intelligence Notes

This directory is the single source for the project's theory book. Its chapters combine mathematics, physics, algorithms, and engineering interpretation around autonomous-system problems instead of separating those subjects into different folders.

## Organisation

- Keep every source chapter directly in this directory.
- Order chapter filenames numerically, such as `01_linear_algebra_foundations.qmd`, `02_geometry_and_coordinate_frames.qmd`, and `03_kinematics_and_numerical_integration.qmd`.
- Use the headings below as book parts, not as subdirectories.
- Use [the textbook index](../textbooks/INDEX.md) to find relevant sources.
- Add a chapter to this table of contents only when its note file exists.
- Keep generated HTML and PDF output outside this source directory.

## Planned book structure

### Front matter

- Purpose, prerequisites, notation, units, and conventions

### Part I — Motion, mechanics, and control

- Linear algebra foundations
- Geometry and coordinate frames
- Kinematics and numerical integration
- Dynamics, forces, torque, friction, and actuator limits
- Feedback, stability, PID control, and constraint handling

### Part II — Uncertainty and state estimation

- Probability and stochastic models
- Bayesian inference and filtering
- Observability, Kalman filtering, and sensor fusion

### Part III — Perception and world representation

- Image formation and camera geometry
- Features, recognition, depth, and motion
- Mapping, SLAM, semantic representation, and memory

### Part IV — Planning, learning, and prediction

- Search and geometric motion planning
- Planning under dynamics and uncertainty
- Markov decision processes and reinforcement learning
- Model-predictive control, learned dynamics, and world models

### Part V — Safe embodied intelligence

- Multirotor dynamics and UAV transfer
- Safety supervision, uncertainty awareness, and failure handling
- Integrated autonomous inspection mission

## Chapter structure

Each chapter should be self-contained:

1. motivating capability and intended robot behaviour;
2. prerequisites, assumptions, notation, units, and frames;
3. mathematical and physical model with step-by-step derivations;
4. algorithms and pseudocode after the model is understood;
5. worked examples and engineering interpretation;
6. limitations, failure conditions, and implementation implications;
7. short retrieval tests after major concepts;
8. a cumulative chapter test with answers or hints;
9. cited textbook sections and any supplementary authoritative sources.

## Compilation

The chapters are Quarto Markdown (`.qmd`) sources ordered by `_quarto.yml`. Render the complete book from this directory:

```zsh
cd /home/maxwell/Repos/robotics_autonomous/notes
quarto render
```

The configured output directory is `output/book` at the repository root. Treat that directory as generated output rather than source material.



```python
@dataclass(frozen=True, slots=True)
class WheelAngularSpeeds:
    """Signed left and right wheel angular speeds in radians per second."""

    left_angular_speed_rad_s: float
    right_angular_speed_rad_s: float


def body_to_wheel(
    *,
    forward_speed_m_s: float,
    yaw_rate_rad_s: float,
    wheel_radius_m: float,
    track_width_m: float,
) -> WheelAngularSpeeds:
    """Apply the body-to-wheel equations to validated inputs."""
    forward_component_rad_s = forward_speed_m_s / wheel_radius_m
    turning_component_rad_s = (
        track_width_m * yaw_rate_rad_s / (2 * wheel_radius_m)
    )
    left_angular_speed_rad_s = (
        forward_component_rad_s - turning_component_rad_s
    )
    right_angular_speed_rad_s = (
        forward_component_rad_s + turning_component_rad_s
    )

    return WheelAngularSpeeds(
        left_angular_speed_rad_s=left_angular_speed_rad_s,
        right_angular_speed_rad_s=right_angular_speed_rad_s,
    )
```
```python
@dataclass(frozen=True, slots=True)
class WheelAngularSpeeds:
    """Signed left and right wheel angular speeds in radians per second."""

    left_angular_speed_rad_s: float
    right_angular_speed_rad_s: float


def body_to_wheel(
    *,
    forward_speed_m_s: float,
    yaw_rate_rad_s: float,
    wheel_radius_m: float,
    track_width_m: float,
) -> WheelAngularSpeeds:
    """Apply the body-to-wheel equations to validated inputs."""
    forward_component_rad_s = forward_speed_m_s / wheel_radius_m
    turning_component_rad_s = (
        track_width_m * yaw_rate_rad_s / (2 * wheel_radius_m)
    )
    left_angular_speed_rad_s = (
        forward_component_rad_s - turning_component_rad_s
    )
    right_angular_speed_rad_s = (
        forward_component_rad_s + turning_component_rad_s
    )

    return WheelAngularSpeeds(
        left_angular_speed_rad_s=left_angular_speed_rad_s,
        right_angular_speed_rad_s=right_angular_speed_rad_s,
    )
```