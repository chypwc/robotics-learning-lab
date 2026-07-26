"""Python installation metadata for the motion-model package."""

from setuptools import find_packages, setup

package_name = "differential_drive_motion_model"

setup(
    name=package_name,
    version="0.1.0",
    packages=find_packages(exclude=["test"]),
    data_files=[
        (
            "share/ament_index/resource_index/packages",
            [f"resource/{package_name}"],
        ),
        (
            f"share/{package_name}",
            ["package.xml"],
        ),
    ],
    install_requires=["setuptools"],
    zip_safe=True,
    maintainer="maxwell",
    maintainer_email="chienyeh5@gmail.com",
    description=(
        "Deterministic differential-drive velocity mappings "
        "and pose integration."
    ),
    license="Apache-2.0",
    extras_require={"test": ["pytest"]},
    entry_points={"console_scripts": []},
)