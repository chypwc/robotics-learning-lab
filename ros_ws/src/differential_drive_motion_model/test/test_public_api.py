"""Tests for the package's supported public interface."""

import differential_drive_motion_model as motion_model


def test_public_api_exposes_supported_names() -> None:
    expected_names = {
        "BodyVelocity",
        "PlanarPose",
        "WheelAngularSpeeds",
        "body_to_wheel",
        "wheel_to_body",
        "integrate_exact",
        "integrate_forward_euler",
    }

    assert set(motion_model.__all__) == expected_names

    for name in expected_names:
        assert hasattr(motion_model, name)