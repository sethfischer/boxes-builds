"""Record of boxes.py builds."""
from __future__ import annotations

import os
from pathlib import Path

from invoke import task

BUILD_DIR = "_build"


def output(slug: str, thickness: float = 3, extension="svg") -> Path:
    """Generate output pathname."""
    filename = f"{slug}_{thickness}mm.{extension}"

    client_id = os.environ.get("BOXES_CLIENT_ID", None)

    if client_id:
        filename = f"{client_id}_{filename}"

    return Path(BUILD_DIR, filename)


@task
def mkdir_build(c):
    """Create build directory."""
    c.run(f"mkdir -p {BUILD_DIR}")


@task(pre=[mkdir_build])
def clean(c):
    """Clean build directory."""
    c.run(f"rm -rf {BUILD_DIR}/*.svg")


@task(pre=[mkdir_build])
def sharpening_stone(c):
    """Sharpening stone two piece box."""
    thickness = 3

    internal_x = 215
    internal_y = 60
    internal_h = 30

    c.run(
        f"boxes TwoPiece --outside=0 "
        f"--thickness={thickness} "
        f"--x={internal_x} --y={internal_y} --h={internal_h} "
        f"--output={output('sharpening-stone', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def slip_stone(c):
    """Slip stone two piece box."""
    thickness = 3

    internal_x = 118
    internal_y = 47
    internal_h = 15

    c.run(
        f"boxes TwoPiece --outside=0 "
        f"--thickness={thickness} "
        f"--x={internal_x} --y={internal_y} --h={internal_h} "
        f"--output={output('slip-stone', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def ottodiy(c):
    """Otto DIY.

    https://www.ottodiy.com/
    """
    thickness = 3

    c.run(
        f"boxes OttoBody --thickness={thickness} "
        f"--output={output('otto-body', thickness=thickness)}"
    )
    c.run(
        f"boxes OttoLegs --thickness={thickness} "
        f"--output={output('otto-legs', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def stationary_engine(c):
    """Stationary engine box."""
    thickness = 3

    height = 80
    sections_x = "65:90"
    sections_y = "25:55:130"

    lid_height = 10

    c.run(
        f"boxes TrayLayout --outside=0 "
        f"--thickness={thickness} "
        f'--h={height} --hi=0 --sx="{sections_x}" --sy="{sections_y}" '
        f'--input="layouts/stationary_engine.txt" '
        f'--Lid_style="overthetop" --Lid_height={lid_height} '
        f"--output={output('stationary-engine', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def spool_din_100(c):
    """DIN 100 wire spool."""
    thickness = 3

    inner_height = 100 - (2 * thickness)
    outer_diameter = 100
    inner_diameter = 64
    axle_diameter = 16
    sides = 16
    reinforcements = 0
    reinforcement_height = 0

    c.run(
        f"boxes Spool "
        f"--thickness={thickness} "
        f'--h={inner_height} --outer_diameter="{outer_diameter}" --inner_diameter="{inner_diameter}" --axle_diameter="{axle_diameter}" '
        f'--sides="{sides}" '
        f'--reinforcements="{reinforcements}" --reinforcement_height="{reinforcement_height}" '
        f"--output={output('spool-din-100', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def spool_din_100_half(c):
    """DIN 100 half-width wire spool."""
    thickness = 3

    inner_height = (100 / 2) - (2 * thickness)
    outer_diameter = 100
    inner_diameter = 64
    axle_diameter = 16
    sides = 16
    reinforcements = 0
    reinforcement_height = 0

    c.run(
        f"boxes Spool "
        f"--thickness={thickness} "
        f'--h={inner_height} --outer_diameter="{outer_diameter}" --inner_diameter="{inner_diameter}" --axle_diameter="{axle_diameter}" '
        f'--sides="{sides}" '
        f'--reinforcements="{reinforcements}" --reinforcement_height="{reinforcement_height}" '
        f"--output={output('spool-din-100-half', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def spool_din_80(c):
    """DIN 80 wire spool."""
    thickness = 3

    inner_height = 80 - (2 * thickness)
    outer_diameter = 80
    inner_diameter = 50
    axle_diameter = 16
    sides = 16
    reinforcements = 0
    reinforcement_height = 0

    c.run(
        f"boxes Spool "
        f"--thickness={thickness} "
        f'--h={inner_height} --outer_diameter="{outer_diameter}" --inner_diameter="{inner_diameter}" --axle_diameter="{axle_diameter}" '
        f'--sides="{sides}" '
        f'--reinforcements="{reinforcements}" --reinforcement_height="{reinforcement_height}" '
        f"--output={output('spool-din-80', thickness=thickness)}"
    )


@task(pre=[mkdir_build])
def spool_din_80_half(c):
    """DIN 80 half-width wire spool."""
    thickness = 3

    inner_height = (80 / 2) - (2 * thickness)
    outer_diameter = 80
    inner_diameter = 50
    axle_diameter = 16
    sides = 16
    reinforcements = 0
    reinforcement_height = 0

    c.run(
        f"boxes Spool "
        f"--thickness={thickness} "
        f'--h={inner_height} --outer_diameter="{outer_diameter}" --inner_diameter="{inner_diameter}" --axle_diameter="{axle_diameter}" '
        f'--sides="{sides}" '
        f'--reinforcements="{reinforcements}" --reinforcement_height="{reinforcement_height}" '
        f"--output={output('spool-din-80-half', thickness=thickness)}"
    )
