"""Planar pose integration for differential-drive motion."""

from dataclasses import dataclass
from math import cos, isfinite, sin


@dataclass(frozen=True, slots=True)
class PlanarPose:
    """Pose of the robot's axle midpoint in the world frame.

    Position is measured in metres. Heading is measured in radians,
    increases counter-clockwise, and remains unwrapped.

    Attributes:
        position_x_m: World-frame x-coordinate in metres.
        position_y_m: World-frame y-coordinate in metres.
        heading_rad: Counter-clockwise heading from the world-frame
            positive x-axis in radians.
    """

    position_x_m: float
    position_y_m: float
    heading_rad: float


def _sinc(value: float) -> float:
    """Return the unnormalised sinc function, including its value at zero."""
    if value == 0.0:
        return 1.0

    return sin(value) / value


def integrate_exact(
    *,
    pose: PlanarPose,
    forward_speed_m_s: float,
    yaw_rate_rad_s: float,
    time_step_s: float,
) -> PlanarPose:
    """Advance a planar pose under constant ideal body velocity.

    The exact constant-input update is

        Δθ = ω Δt
        x_next = x + v Δt sinc(Δθ / 2) cos(θ + Δθ / 2)
        y_next = y + v Δt sinc(Δθ / 2) sin(θ + Δθ / 2)
        θ_next = θ + Δθ

    where

    sinc(z) = sin(z) / z  for z ≠ 0
    sinc(0) = 1

    Here, v is forward speed, ω is yaw rate, Δt is the time step,
    and θ is the initial heading.

    Args:
        pose: Initial axle-midpoint pose in the world frame.
        forward_speed_m_s: Constant signed body-forward speed in metres
            per second.
        yaw_rate_rad_s: Constant signed counter-clockwise yaw rate in
            radians per second.
        time_step_s: Positive integration duration in seconds.

    Returns:
        The pose at the end of the time step.

    Raises:
        ValueError: If any numeric input is non-finite or if the time
            step is not greater than zero.
    """
    values = (
        pose.position_x_m,
        pose.position_y_m,
        pose.heading_rad,
        forward_speed_m_s,
        yaw_rate_rad_s,
        time_step_s,
    )
    if not all(isfinite(value) for value in values):
        raise ValueError("pose, velocity, and time step must be finite")

    if time_step_s <= 0.0:
        raise ValueError("time_step_s must be greater than zero")

    heading_change_rad = yaw_rate_rad_s * time_step_s
    half_heading_change_rad = heading_change_rad / 2
    midpoint_heading_rad = pose.heading_rad + half_heading_change_rad

    signed_displacement_m = (
        forward_speed_m_s
        * time_step_s
        * _sinc(half_heading_change_rad)
    )

    return PlanarPose(
        position_x_m=(
            pose.position_x_m
            + signed_displacement_m * cos(midpoint_heading_rad)
        ),
        position_y_m=(
            pose.position_y_m
            + signed_displacement_m * sin(midpoint_heading_rad)
        ),
        heading_rad=pose.heading_rad + heading_change_rad,
    )


def integrate_forward_euler(
    *,
    pose: PlanarPose,
    forward_speed_m_s: float,
    yaw_rate_rad_s: float,
    time_step_s: float,
) -> PlanarPose:
    """Advance a planar pose by one Forward Euler step.

    Forward Euler evaluates the pose derivative using the heading at the
    beginning of the time step:

        x_next = x + v Δt cos(θ)
        y_next = y + v Δt sin(θ)
        θ_next = θ + ω Δt

    Here, x and y are world-frame position, θ is the initial heading,
    v is body-forward speed, ω is yaw rate, and Δt is the time step.

    Args:
        pose: Initial axle-midpoint pose in the world frame.
        forward_speed_m_s: Constant signed body-forward speed in metres
            per second.
        yaw_rate_rad_s: Constant signed counter-clockwise yaw rate in
            radians per second.
        time_step_s: Positive integration duration in seconds.

    Returns:
        The Forward Euler approximation at the end of the time step.

    Raises:
        ValueError: If any numeric input is non-finite or if the time
            step is not greater than zero.
    """
    values = (
        pose.position_x_m,
        pose.position_y_m,
        pose.heading_rad,
        forward_speed_m_s,
        yaw_rate_rad_s,
        time_step_s,
    )
    if not all(isfinite(value) for value in values):
        raise ValueError("pose, velocity, and time step must be finite")

    if time_step_s <= 0.0:
        raise ValueError("time_step_s must be greater than zero")

    return PlanarPose(
        position_x_m=(
            pose.position_x_m
            + time_step_s * forward_speed_m_s * cos(pose.heading_rad)
        ),
        position_y_m=(
            pose.position_y_m
            + forward_speed_m_s * time_step_s * sin(pose.heading_rad)
        ),
        heading_rad=pose.heading_rad + time_step_s * yaw_rate_rad_s,
    )
