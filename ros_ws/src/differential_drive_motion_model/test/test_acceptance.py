"""Capability-level acceptance tests for the differential-drive model."""

from math import cos, sin

import pytest

from differential_drive_motion_model import (
    PlanarPose,
    integrate_exact,
    wheel_to_body,
)


def test_mot_acc_opposite_wheels_produce_pure_rotation() -> None:
    body_velocity = wheel_to_body(
        left_angular_speed_rad_s=2.0,
        right_angular_speed_rad_s=-2.0,
        wheel_radius_m=0.10,
        track_width_m=0.50,
    )

    result = integrate_exact(
        pose=PlanarPose(
            position_x_m=0.0,
            position_y_m=0.0,
            heading_rad=0.0,
        ),
        forward_speed_m_s=body_velocity.forward_speed_m_s,
        yaw_rate_rad_s=body_velocity.yaw_rate_rad_s,
        time_step_s=1.0,
    )

    assert body_velocity.forward_speed_m_s == pytest.approx(0.0)
    assert body_velocity.yaw_rate_rad_s == pytest.approx(-0.80)
    assert result.position_x_m == pytest.approx(0.0)
    assert result.position_y_m == pytest.approx(0.0)
    assert result.heading_rad == pytest.approx(-0.80)


def test_mot_acc_003_wheel_speeds_produce_expected_curved_pose() -> None:
    body_velocity = wheel_to_body(
        left_angular_speed_rad_s=1.0,
        right_angular_speed_rad_s=3.0,
        wheel_radius_m=0.10,
        track_width_m=0.50,
    )

    result = integrate_exact(
        pose=PlanarPose(
            position_x_m=0.0,
            position_y_m=0.0,
            heading_rad=0.0,
        ),
        forward_speed_m_s=body_velocity.forward_speed_m_s,
        yaw_rate_rad_s=body_velocity.yaw_rate_rad_s,
        time_step_s=1.0,
    )

    assert body_velocity.forward_speed_m_s == pytest.approx(0.20)
    assert body_velocity.yaw_rate_rad_s == pytest.approx(0.40)
    assert result.position_x_m == pytest.approx(
        0.50 * sin(0.40),
        abs=1e-12,
    )
    assert result.position_y_m == pytest.approx(
        0.50 * (1.0 - cos(0.40)),
        abs=1e-12,
    )
    assert result.heading_rad == pytest.approx(0.40)
