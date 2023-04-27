"""Record of boxes.py builds."""

import os
from pathlib import Path

from invoke import task

BUILD_DIR = "_build"


def output(slug: str, extension="svg") -> Path:
    """Generate output pathname."""
    filename = f"{slug}.{extension}"

    client_id = os.environ.get("BOXES_CLIENT_ID", None)

    if client_id:
        filename = f"{client_id}_{filename}"

    return Path(BUILD_DIR, filename)


@task
def clean(c):
    """Clean build directory."""
    c.run("rm -rf _build/*")


@task
def sharpening_stone(c):
    """Sharpening stone two piece box."""
    internal_x = 215
    internal_y = 60
    internal_h = 30

    c.run(
        f"boxes TwoPiece --output {output('sharpening_stone')} "
        f"--x={internal_x} --y={internal_y} --h={internal_h}"
    )


@task
def slip_stone(c):
    """Slip stone two piece box."""
    internal_x = 118
    internal_y = 47
    internal_h = 15

    c.run(
        f"boxes TwoPiece --output {output('slip_stone')} "
        f"--x={internal_x} --y={internal_y} --h={internal_h}"
    )
