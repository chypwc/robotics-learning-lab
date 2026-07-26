"""Unit tests for planar pose integration."""

from dataclasses import FrozenInstanceError
from math import cos, hypot, inf, nan, pi, sin

import pytest

from differential_drive_motion_model.integration import (
    PlanarPose,
    integrate_exact,
    integrate_forward_euler,
)


def test_planar_pose_stores_position_and_unwrapped_heading() -> None:
    pose = PlanarPose(
        position_x_m=1.25,
        position_y_m=-0.50,
        heading_rad=3 * pi,
    )

    assert pose.position_x_m == pytest.approx(1.25)
    assert pose.position_y_m == pytest.approx(-0.50)
    assert pose.heading_rad == pytest.approx(3 * pi)


def test_planar_pose_is_immutable() -> None:
    pose = PlanarPose(
        position_x_m=0.0,
        position_y_m=0.0,
        heading_rad=0.0,
    )

    with pytest.raises(FrozenInstanceError):
        pose.heading_rad = 1.0


def test_exact_integration_handles_straight_motion() -> None:
    initial_pose = PlanarPose(
        position_x_m=1.0,
        position_y_m=-2.0,
        heading_rad=pi / 2,
    )

    result = integrate_exact(
        pose=initial_pose,
        forward_speed_m_s=0.50,
        yaw_rate_rad_s=0.0,
        time_step_s=2.0,
    )

    assert result.position_x_m == pytest.approx(1.0, abs=1e-12)
    assert result.position_y_m == pytest.approx(-1.0, abs=1e-12)
    assert result.heading_rad == pytest.approx(pi / 2)


def test_exact_integration_handles_curved_motion() -> None:
    """Verify the exact constant-curvature update for ω ≠ 0.

    For initial pose (x, y, θ), constant forward speed v, yaw rate ω,
    and time step Δt, the exact update is

        x_next = x + (v / ω)[sin(θ + ωΔt) - sin(θ)]
        y_next = y + (v / ω)[cos(θ) - cos(θ + ωΔt)]
        θ_next = θ + ωΔt

    This test uses x = y = θ = 0, v = 0.20, ω = 0.40, and Δt = 1.
    Therefore, v / ω = 0.50 and the expected pose is

        x_next = 0.50 sin(0.40)
        y_next = 0.50[1 - cos(0.40)]
        θ_next = 0.40
    """
    initial_pose = PlanarPose(
        position_x_m=0.0,
        position_y_m=0.0,
        heading_rad=0.0,
    )

    result = integrate_exact(
        pose=initial_pose,
        forward_speed_m_s=0.20,
        yaw_rate_rad_s=0.40,
        time_step_s=1.0,
    )

    assert result.position_x_m == pytest.approx(
        0.50 * sin(0.40),
        abs=1e-12,
    )
    assert result.position_y_m == pytest.approx(
        0.50 * (1.0 - cos(0.40)),
        abs=1e-12,
    )
    assert result.heading_rad == pytest.approx(0.40)


def test_exact_integration_handles_pure_rotation_without_wrapping() -> None:
    initial_pose = PlanarPose(
        position_x_m=1.20,
        position_y_m=-0.80,
        heading_rad=3 * pi,
    )

    result = integrate_exact(
        pose=initial_pose,
        forward_speed_m_s=0.0,
        yaw_rate_rad_s=0.75,
        time_step_s=2.0,
    )

    assert result.position_x_m == pytest.approx(1.20)
    assert result.position_y_m == pytest.approx(-0.80)
    assert result.heading_rad == pytest.approx(3 * pi + 1.50)


@pytest.mark.parametrize(
    "invalid_pose",
    [
        PlanarPose(
            position_x_m=inf,
            position_y_m=0.0,
            heading_rad=0.0,
        ),
        PlanarPose(
            position_x_m=0.0,
            position_y_m=nan,
            heading_rad=0.0,
        ),
        PlanarPose(
            position_x_m=0.0,
            position_y_m=0.0,
            heading_rad=-inf,
        ),
    ],
)
def test_exact_integration_rejects_non_finite_pose(
    invalid_pose: PlanarPose,
) -> None:
    with pytest.raises(ValueError, match="finite"):
        integrate_exact(
            pose=invalid_pose,
            forward_speed_m_s=0.20,
            yaw_rate_rad_s=0.40,
            time_step_s=1.0,
        )


@pytest.mark.parametrize(
    ("forward_speed_m_s", "yaw_rate_rad_s", "time_step_s"),
    [
        (inf, 0.0, 1.0),
        (0.0, -inf, 1.0),
        (0.0, 0.0, nan),
    ],
)
def test_exact_integration_rejects_non_finite_motion_input(
    forward_speed_m_s: float,
    yaw_rate_rad_s: float,
    time_step_s: float,
) -> None:
    with pytest.raises(ValueError, match="finite"):
        integrate_exact(
            pose=PlanarPose(
                position_x_m=0.0,
                position_y_m=0.0,
                heading_rad=0.0,
            ),
            forward_speed_m_s=forward_speed_m_s,
            yaw_rate_rad_s=yaw_rate_rad_s,
            time_step_s=time_step_s,
        )


@pytest.mark.parametrize("invalid_time_step_s", [0.0, -0.10])
def test_exact_integration_rejects_non_positive_time_step(
    invalid_time_step_s: float,
) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        integrate_exact(
            pose=PlanarPose(
                position_x_m=0.0,
                position_y_m=0.0,
                heading_rad=0.0,
            ),
            forward_speed_m_s=0.20,
            yaw_rate_rad_s=0.40,
            time_step_s=invalid_time_step_s,
        )


def test_forward_euler_is_exact_for_straight_motion() -> None:
    initial_pose = PlanarPose(
        position_x_m=1.0,
        position_y_m=-2.0,
        heading_rad=pi / 2,
    )

    result = integrate_forward_euler(
        pose=initial_pose,
        forward_speed_m_s=0.50,
        yaw_rate_rad_s=0.0,
        time_step_s=2.0,
    )

    assert result.position_x_m == pytest.approx(1.0, abs=1e-12)
    assert result.position_y_m == pytest.approx(-1.0, abs=1e-12)
    assert result.heading_rad == pytest.approx(pi / 2)


def test_forward_euler_turning_uses_beginning_heading() -> None:
    """Verify that Forward Euler does not follow the arc within one step.

    With θ = 0, Forward Euler evaluates the initial position derivative as

        x_dot = v cos(0) = v
        y_dot = v sin(0) = 0

    It therefore moves only along world-frame x during this step, even
    though the heading changes. The exact update follows a curved arc and
    produces a positive world-frame y displacement.
    """
    initial_pose = PlanarPose(
        position_x_m=0.0,
        position_y_m=0.0,
        heading_rad=0.0,
    )

    euler_result = integrate_forward_euler(
        pose=initial_pose,
        forward_speed_m_s=0.20,
        yaw_rate_rad_s=0.40,
        time_step_s=1.0,
    )
    exact_result = integrate_exact(
        pose=initial_pose,
        forward_speed_m_s=0.20,
        yaw_rate_rad_s=0.40,
        time_step_s=1.0,
    )

    assert euler_result.position_x_m == pytest.approx(0.20)
    assert euler_result.position_y_m == pytest.approx(0.0)
    assert euler_result.heading_rad == pytest.approx(0.40)

    assert exact_result.position_y_m > 0.0
    assert euler_result.position_y_m != pytest.approx(
        exact_result.position_y_m,
        abs=1e-12,
    )


@pytest.mark.parametrize(
    "invalid_pose",
    [
        PlanarPose(
            position_x_m=inf,
            position_y_m=0.0,
            heading_rad=0.0,
        ),
        PlanarPose(
            position_x_m=0.0,
            position_y_m=nan,
            heading_rad=0.0,
        ),
        PlanarPose(
            position_x_m=0.0,
            position_y_m=0.0,
            heading_rad=-inf,
        ),
    ],
)
def test_forward_euler_rejects_non_finite_pose(
    invalid_pose: PlanarPose,
) -> None:
    with pytest.raises(ValueError, match="finite"):
        integrate_forward_euler(
            pose=invalid_pose,
            forward_speed_m_s=0.20,
            yaw_rate_rad_s=0.40,
            time_step_s=1.0,
        )


@pytest.mark.parametrize(
    ("forward_speed_m_s", "yaw_rate_rad_s", "time_step_s"),
    [
        (inf, 0.0, 1.0),
        (0.0, -inf, 1.0),
        (0.0, 0.0, nan),
    ],
)
def test_forward_euler_rejects_non_finite_motion_input(
    forward_speed_m_s: float,
    yaw_rate_rad_s: float,
    time_step_s: float,
) -> None:
    with pytest.raises(ValueError, match="finite"):
        integrate_forward_euler(
            pose=PlanarPose(
                position_x_m=0.0,
                position_y_m=0.0,
                heading_rad=0.0,
            ),
            forward_speed_m_s=forward_speed_m_s,
            yaw_rate_rad_s=yaw_rate_rad_s,
            time_step_s=time_step_s,
        )


@pytest.mark.parametrize("invalid_time_step_s", [0.0, -0.10])
def test_forward_euler_rejects_non_positive_time_step(
    invalid_time_step_s: float,
) -> None:
    with pytest.raises(ValueError, match="greater than zero"):
        integrate_forward_euler(
            pose=PlanarPose(
                position_x_m=0.0,
                position_y_m=0.0,
                heading_rad=0.0,
            ),
            forward_speed_m_s=0.20,
            yaw_rate_rad_s=0.40,
            time_step_s=invalid_time_step_s,
        )


def test_forward_euler_global_position_error_is_first_order() -> None:
    """Verify first-order global convergence over a fixed duration.

    Position error is measured against the exact final position:

        E(Δt) = hypot(x_euler − x_exact, y_euler − y_exact)

    For a first-order method in the asymptotic regime:

        E(Δt) / E(Δt / 2) ≈ 2
    """
    initial_pose = PlanarPose(
        position_x_m=0.0,
        position_y_m=0.0,
        heading_rad=0.0,
    )
    exact_result = integrate_exact(
        pose=initial_pose,
        forward_speed_m_s=1.0,
        yaw_rate_rad_s=1.0,
        time_step_s=1.0,
    )

    integration_cases = (
        (0.100, 10),
        (0.050, 20),
        (0.025, 40),
    )
    position_errors_m: list[float] = []

    for time_step_s, step_count in integration_cases:
        euler_pose = initial_pose

        for _ in range(step_count):
            euler_pose = integrate_forward_euler(
                pose=euler_pose,
                forward_speed_m_s=1.0,
                yaw_rate_rad_s=1.0,
                time_step_s=time_step_s,
            )

        position_error_m = hypot(
            euler_pose.position_x_m - exact_result.position_x_m,
            euler_pose.position_y_m - exact_result.position_y_m,
        )
        position_errors_m.append(position_error_m)

    assert position_errors_m[0] > position_errors_m[1]
    assert position_errors_m[1] > position_errors_m[2]

    error_ratios = (
        position_errors_m[0] / position_errors_m[1],
        position_errors_m[1] / position_errors_m[2],
    )
    for error_ratio in error_ratios:
        assert 1.8 <= error_ratio <= 2.2