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
        # Top is the Sticker.
        # Back is where the C14 AC connector is, the back of the server.
        x = 4.4  # Assume the hole placement is the same from both sides.
        y = (self.z_size - 32) / 2  # Holes are 32mm apart
        self.back.hole(pos=(self.x_size - x, y), diameter=4.2, depth=4.0)
        self.back.hole(pos=(self.x_size - x, y), diameter=3.2, external_subtract=True)
        self.back.hole(pos=(self.x_size - x, y + 32), diameter=4.2, depth=4.0)
        self.back.hole(pos=(self.x_size - x, y + 32), diameter=3.2, external_subtract=True)
        self.back.hole(pos=(x, 36), diameter=4.2, depth=4.0)
        self.back.hole(pos=(x, 36), diameter=3.2, external_subtract=True)
        self.back.hole(pos=(15.2, 37), diameter=4.2, depth=4.0)
        self.back.hole(pos=(15.2, 37), diameter=3.2, external_subtract=True)
        # TODO: Define box for C14 power ports.
        # self.back.box(pos=(2, 2), length=24, width=32, external_subtract=True)

        # TODO: Define Airvent holes.
        # TODO: Define construction box for internal fan.
        # TODO: Define construction box for cables out of PSU.

        # The following holes void the warranty when used.
        # Since we have to remove the screws holding the PSU together.
        # In some applications that was the only option for mounting the PSU.
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
            side.hole(pos=(x, from_bottom), diameter=3.0, depth=4)
