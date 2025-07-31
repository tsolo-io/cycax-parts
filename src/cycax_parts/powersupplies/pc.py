# SPDX-FileCopyrightText: 2025 Tsolo.io
#
# SPDX-License-Identifier: Apache-2.0
"""Generic PC Power Supplies."""

from cycax.cycad import Print3D


class ATX(Print3D):
    """See ATXPS2-3.jpg.

    Note: This only defines the PS2 ATX PSU and not the PS3 model, the PS3 has the same mounting holes but is shorter.
    """

    def __init__(self):
        super().__init__(part_no="psu-atx-generic", x_size=150.0, y_size=140.0, z_size=86.0)
        self.colour = "black"
        # There is a 2mm overhang at the back and left for the connector plate, if that is builtin.

    def definition(self):
        # Top is the Sticker.
        # Back is where the C14 AC connector is, the back of the server.
        from_edge = (self.x_size - 138) / 2
        self.back.hole(pos=(from_edge, self.z_size - from_edge), diameter=3, depth=4.0)
        self.back.hole(pos=(from_edge, self.z_size - from_edge), diameter=3.2, external_subtract=True)
        self.back.hole(pos=(from_edge + 138, self.z_size - from_edge), diameter=3, depth=4.0)
        self.back.hole(pos=(from_edge + 138, self.z_size - from_edge), diameter=3.2, external_subtract=True)
        self.back.hole(pos=(from_edge, self.z_size - from_edge - 64), diameter=3, depth=4.0)
        self.back.hole(pos=(from_edge, self.z_size - from_edge - 64), diameter=3.2, external_subtract=True)
        self.back.hole(pos=(from_edge + 114, from_edge), diameter=3, depth=4.0)
        self.back.hole(pos=(from_edge + 114, from_edge), diameter=3.2, external_subtract=True)

        # Define large box for C14 power ports, on/off switch etc.
        self.back.box(pos=(10, 10), length=self.x_size - 20, width=self.z_size - 20, external_subtract=True)

        # TODO: Define Airvent holes.
        # TODO: Define construction box for internal fan.
        # TODO: Define construction box for cables out of PSU.
