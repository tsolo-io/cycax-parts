# SPDX-FileCopyrightText: 2025 Apache-2.0
#
# SPDX-License-Identifier: Apache-2.0

from pathlib import Path

from cycax.cycad import Print3D
from cycax.cycad.engines.part_server import PartEngineServer
from cycax.cycad.features import NutCutOut


class ConnCube(Print3D):
    """A cube use for fixing 3 sides together with M3 bolts."""

    def __init__(self):
        super().__init__(part_no="conn-cube", x_size=11, y_size=11, z_size=11)

    def definition(self):
        """Calculate the conn cube."""
        nut_spec = NutCutOut.nut_specifications["M3"]
        nut_thick = nut_spec["thickness"]
        nut_width = nut_spec["side_to_side"]
        half_nut_width = nut_width / 2
        for side, xb, yb in (
            (self.front, False, True),
            (self.bottom, False, False),
            (self.right, True, True),
        ):
            x = 7 if xb else 4
            y = 7 if yb else 4
            pos = (x, y)
            side.hole(pos=pos, diameter=3.2, external_subtract=True)
            side.hole(pos=pos, diameter=3.0, depth=3)
            side.hole(pos=pos, diameter=2.9)  # Through everything
            side.nut(pos=pos, nut_type="M3", sink=1, vertical=xb)  # Coordinates based on center of the Nut.

        # Create the holes for the nuts to slide in.
        self.top.box(pos=(11 - 7 - half_nut_width, 1), depth=5, width=nut_thick, length=nut_width)
        self.top.box(
            pos=(10 - nut_thick, 7 - half_nut_width),
            depth=5,
            width=nut_width,
            length=nut_thick,
        )
        self.back.box(pos=(7 - half_nut_width, 1), depth=5, width=nut_thick, length=nut_width)
        # Trim the cube so we dont print unesesary.
        self.top.box(pos=(0, 11 - 4), length=6, width=4, depth=4)
        self.top.box(pos=(0, 11 - 6), length=4, width=6, depth=4)
        self.top.box(pos=(0, 11 - 4), length=4, width=4, depth=6)
        self.top.hole(pos=(4, 11 - 4), diameter=4, depth=4)
        self.back.hole(pos=(11 - 4, 11 - 4), diameter=4, depth=4)
        self.left.hole(pos=(4, 11 - 4), diameter=4, depth=4)
        self.top.sphere(pos=(4, 11 - 4), diameter=4, sink=4)


if __name__ == "__main__":
    part = ConnCube()
    part.save(Path("./build"))
    cycax_server = PartEngineServer()
    cycax_server.build(part)
