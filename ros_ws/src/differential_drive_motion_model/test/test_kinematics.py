"""Unit tests for ideal differential-drive velocity kinematics."""

from math import inf, nan

import pytest

from differential_drive_motion_model.kinematics import (
    wheel_to_body,
    body_to_wheel,
)


def test_equal_wheel_speeds_produce_straight_motion() -> None:
    result = wheel_to_body(
        left_angular_speed_rad_s=2.0,
        right_angular_speed_rad_s=2.0,
        wheel_radius_m=0.10,
        track_width_m=0.50,
    )

    assert result.forward_speed_m_s == pytest.approx(0.20)
    assert result.yaw_rate_rad_s == pytest.approx(0.0)


def test_opposite_wheel_speeds_produce_pure_rotation() -> None:
    result = wheel_to_body(
        left_angular_speed_rad_s=2.0,
        right_angular_speed_rad_s=-2.0,
        wheel_radius_m=0.10,
        track_width_m=0.50,
    )

    assert result.forward_speed_m_s == pytest.approx(0.0)
    assert result.yaw_rate_rad_s == pytest.approx(-0.80)


@pytest.mark.parametrize(
    ("wheel_radius_m", "track_width_m"),
    [
        (0.0, 0.50),    # zero wheel radius
        (-0.10, 0.50),  # negative wheel radius
        (0.10, 0.0),    # zero track width
        (0.10, -0.50),  # negative track width
    ]
)
def test_non_positive_geometry_is_rejected(
    wheel_radius_m: float,
    track_width_m: float,
) -> None:
    with pytest.raises(ValueError):
        wheel_to_body(
            left_angular_speed_rad_s=2.0,
            right_angular_speed_rad_s=2.0,
            wheel_radius_m=wheel_radius_m,
            track_width_m=track_width_m,
        )


@pytest.mark.parametrize("invalid_speed", [inf, -inf, nan])
def test_non_finite_wheel_speed_is_rejected(invalid_speed: float) -> None:
    # check it raises ValueError and the exception message contains "finite"
    with pytest.raises(ValueError, match="finite"):
        wheel_to_body(
            left_angular_speed_rad_s=invalid_speed,
            right_angular_speed_rad_s=2.0,
            wheel_radius_m=0.10,
            track_width_m=0.50,
        )

    with pytest.raises(ValueError, match="finite"):
        wheel_to_body(
            left_angular_speed_rad_s=2.0,
            right_angular_speed_rad_s=invalid_speed,
            wheel_radius_m=0.10,
            track_width_m=0.50,
        )


def test_straight_body_velocity_produces_equal_wheel_speeds() -> None:
    result = body_to_wheel(
        forward_speed_m_s=0.20,
        yaw_rate_rad_s=0.0,
        wheel_radius_m=0.10,
        track_width_m=0.50,
    )

    assert result.left_angular_speed_rad_s == pytest.approx(2.0)
    assert result.right_angular_speed_rad_s == pytest.approx(2.0)


def test_positive_yaw_rate_produces_opposite_wheel_speeds() -> None:
    result = body_to_wheel(
        forward_speed_m_s=0.0,
        yaw_rate_rad_s=0.80,
        wheel_radius_m=0.10,
        track_width_m=0.50,
    )

    assert result.left_angular_speed_rad_s == pytest.approx(-2.0)
    assert result.right_angular_speed_rad_s == pytest.approx(2.0)


def test_body_to_wheel_round_trip_recovers_body_velocity() -> None:
    wheel_speeds = body_to_wheel(
        forward_speed_m_s=0.35,
        yaw_rate_rad_s=-0.60,
        wheel_radius_m=0.08,
        track_width_m=0.42,
    )

    recovered = wheel_to_body(
        left_angular_speed_rad_s=wheel_speeds.left_angular_speed_rad_s,
        right_angular_speed_rad_s=wheel_speeds.right_angular_speed_rad_s,
        wheel_radius_m=0.08,
        track_width_m=0.42,
    )

    assert recovered.forward_speed_m_s == pytest.approx(0.35, abs=1e-12)
    assert recovered.yaw_rate_rad_s == pytest.approx(-0.60, abs=1e-12)


@pytest.mark.parametrize("invalid_value", [inf, -inf, nan])
def test_non_finite_body_velocity_is_rejected(
    invalid_value: float,
) -> None:
    with pytest.raises(ValueError, match="finite"):
        body_to_wheel(
            forward_speed_m_s=invalid_value,
            yaw_rate_rad_s=0.0,
            wheel_radius_m=0.10,
            track_width_m=0.50,
        )

    with pytest.raises(ValueError, match="finite"):
        body_to_wheel(
            forward_speed_m_s=0.0,
            yaw_rate_rad_s=invalid_value,
            wheel_radius_m=0.10,
            track_width_m=0.50,
        )


@pytest.mark.parametrize(
    ("wheel_radius_m", "track_width_m"),
    [
        (0.0, 0.50),
        (-0.10, 0.50),
        (0.10, 0.0),
        (0.10, -0.50),
        (inf, 0.50),
        (nan, 0.50),
        (0.10, inf),
        (0.10, nan),
    ],
)
def test_invalid_geometry_is_rejected_by_body_to_wheel(
    wheel_radius_m: float,
    track_width_m: float,
) -> None:
    with pytest.raises(ValueError):
        body_to_wheel(
            forward_speed_m_s=0.20,
            yaw_rate_rad_s=0.40,
            wheel_radius_m=wheel_radius_m,
            track_width_m=track_width_m,
        )