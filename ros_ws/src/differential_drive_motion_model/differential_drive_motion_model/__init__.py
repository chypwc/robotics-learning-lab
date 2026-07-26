"""Public interface for the differential-drive motion-model library."""

from .integration import (
    PlanarPose,
    integrate_exact,
    integrate_forward_euler,
)
from .kinematics import (
    BodyVelocity,
    wheel_to_body,
    WheelAngularSpeeds,
    body_to_wheel,
)

__all__ = [
    "BodyVelocity",
    "PlanarPose",
    "WheelAngularSpeeds",
    "wheel_to_body",
    "body_to_wheel",
    "integrate_exact",
    "integrate_forward_euler",
]