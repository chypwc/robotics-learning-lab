"""Ideal differential-drive velocity kinematics."""

from dataclasses import dataclass
from math import isfinite


@dataclass(frozen=True, slots=True)
class BodyVelocity:
    """Reduced planar body velocity in SI units"""

    forward_speed_m_s: float
    yaw_rate_rad_s: float


def wheel_to_body(
    *,
    left_angular_speed_rad_s: float,
    right_angular_speed_rad_s: float,
    wheel_radius_m: float,
    track_width_m: float,
) -> BodyVelocity:
    """Convert signed wheel angular speeds into ideal planar body velocity.

    The no-slip differential-drive equations are:

        v = r(φ̇_R + φ̇_L) / 2
        ω = r(φ̇_R - φ̇_L) / L

    Here, v is body-forward speed, ω is yaw rate, r is wheel radius,
    L is track width, and φ̇_L and φ̇_R are the signed left and right
    wheel angular speeds.

    Positive wheel angular speed rolls the corresponding wheel forward.
    Positive forward speed lies along the body-frame positive x-axis, and
    positive yaw rate turns the robot counter-clockwise about its upward
    body-frame z-axis.

    Args:
        left_angular_speed_rad_s: Signed left-wheel angular speed in radians
            per second.
        right_angular_speed_rad_s: Signed right-wheel angular speed in radians
            per second.
        wheel_radius_m: Common effective rolling radius in metres; must be
            finite and greater than zero.
        track_width_m: Lateral distance between the wheel ground-contact
            centre lines in metres; must be finite and greater than zero.

    Returns:
        The resulting body-forward speed in metres per second and yaw rate in
        radians per second.

    Raises:
        ValueError: If any input is non-finite, or if the wheel radius or track
            width is not greater than zero.
    """
    inputs = (
        left_angular_speed_rad_s,
        right_angular_speed_rad_s,
        wheel_radius_m,
        track_width_m,
    )
    if not all(isfinite(value) for value in inputs):
        raise ValueError("all inputs must be finite")

    if wheel_radius_m <= 0.0:
        raise ValueError("wheel_radius_m must be greater than zero")

    if track_width_m <= 0.0:
        raise ValueError("track_width_m must be greater than zero")

    forward_speed_m_s = (
        wheel_radius_m / 2
        * (right_angular_speed_rad_s + left_angular_speed_rad_s)
    )
    yaw_rate_rad_s = (
        wheel_radius_m / track_width_m
        * (right_angular_speed_rad_s - left_angular_speed_rad_s)
    )

    return BodyVelocity(
        forward_speed_m_s=forward_speed_m_s,
        yaw_rate_rad_s=yaw_rate_rad_s,
    )


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
    """Convert ideal planar body velocity into signed wheel angular speeds.

    The no-slip differential-drive inverse equations are:

        φ̇_L = v / r - Lω / (2r)
        φ̇_R = v / r + Lω / (2r)

    Here, v is body-forward speed, ω is yaw rate, r is wheel radius,
    L is track width, and φ̇_L and φ̇_R are the resulting signed left and
    right wheel angular speeds.

    Positive forward speed lies along the body-frame positive x-axis.
    Positive yaw rate turns the robot counter-clockwise about its upward
    body-frame z-axis. Positive wheel angular speed rolls that wheel
    forward.

    Args:
        forward_speed_m_s: Signed body-forward speed in metres per second.
        yaw_rate_rad_s: Signed counter-clockwise yaw rate in radians per
            second.
        wheel_radius_m: Common effective rolling radius in metres; must be
            finite and greater than zero.
        track_width_m: Lateral distance between the wheel ground-contact
            centre lines in metres; must be finite and greater than zero.

    Returns:
        Signed left and right wheel angular speeds in radians per second.

    Raises:
        ValueError: If any input is non-finite, or if the wheel radius or
            track width is not greater than zero.
    """
    inputs = (
        forward_speed_m_s,
        yaw_rate_rad_s,
        wheel_radius_m,
        track_width_m,
    )
    if not all(isfinite(value) for value in inputs):
        raise ValueError("all inputs must be finite")

    if wheel_radius_m <= 0.0:
        raise ValueError("wheel_radius_m must be greater than zero")

    if track_width_m <= 0.0:
        raise ValueError("track_width_m must be greater than zero")

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
