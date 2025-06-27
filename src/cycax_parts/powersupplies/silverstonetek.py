# SPDX-FileCopyrightText: 2025 Tsolo.io
#
# SPDX-License-Identifier: Apache-2.0

from cycax.cycad import Print3D


class SilverstonetekFlexATX(Print3D):
    def __init__(self):
        super().__init__(part_no="psu-flexatx-silverstonetek", x_size=81.5, y_size=150, z_size=40.50)
        self.colour = "black"
        # There is a 2mm overhang at the back and left for the connector plate, if that is builtin.

    def definition(self):
        # Back is where the C14 AC connector is, the back of the server.
        # Top is the Sticker.
        # Holes are 32mm apart
        x = 4  # TODO: Measured, not defined on drawing.
        y = (self.y_size - 32) / 2
        self.back.hole(pos=(x, y), diameter=4.2, external_subtract=True)
        self.back.hole(pos=(x, y + 32), diameter=4.2, external_subtract=True)
        # TODO: Define box for C14 power ports.
        # TODO: Define holes for screws under C14 power ports.
        # TODO: Define Airvent holes.
        # TODO: Define construction box for internal fan.
        # TODO: Define construction box for cables out of PSU.
        from_bottom = 8.2 + 2.6  # Measured
        from_front_0 = 6.0 + 2.6  # Measured
        from_front_r = 128.6 + 2.6  # Measured
        from_front_l = 120 + 2.6  # Measured
        hole_pos = (
            (self.left, self.y_size - from_front_0),
            (self.left, self.y_size - from_front_l),
            (self.right, from_front_0),
            (self.right, from_front_r),
        )
        for side, x in hole_pos:
            side.hole(pos=(x, from_bottom), diameter=3.2, external_subtract=True)
            side.hole(pos=(x, from_bottom), diameter=3.0, depth=41)
