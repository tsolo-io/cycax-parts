# SPDX-FileCopyrightText: 2025 Apache-2.0
#
# SPDX-License-Identifier: Apache-2.0

"""
Orientation of the mother board:

+---------+   qqqq is the connector side.
|m  l    k|   pppp is the PCIe slots.
|j  h sr g|   a,b,c,f,g,h,j,k,l,m,r,s is the mounting holes.
|f  c  b a|
+qqqq-pppp+
"""

from cycax.cycad import Print3D


def atx_mounting_holes():
    """
    Front is the connectors.
    Right is the PCIe slot.
    Top is the component side.
    """
    # This is the mounting holes as seen from the top.
    # Mounting holes

    return (  # TODO: complete the list of mounting holes
        (1, 1),  # hole f
    )


def atx_connectors():
    """ """
    return ((20, 20), (40, 20), (60, 20))


class BaseATX(Print3D):
    """ """

    def definition(self):
        for pos in atx_mounting_holes():
            if pos[0] < self.x_size and pos[1] < self.y_size:
                self.top.hole(pos=pos, diameter=4)
                bpos = (pos[0], self.y_size - pos[1])
                self.bottom.hole(pos=bpos, diameter=3.2, external_subtract=True)
        # A few silly features to identify the back.
        for pos in atx_connectors():
            if pos[0] < self.x_size and pos[1] < self.z_size:
                self.back.hole(pos=pos, diameter=10, depth=5)


class StandardATX(BaseATX):
    """Standard ATX motherboard.

    This is for a typical desktop style ATX motherboard.
    Including 8mm standoffs, for mounting motherboard to case.
    """

    def __init__(self, standoff=8):
        super().__init__(
            part_no="atx-motherboard",
            x_size=305,  # TODO
            y_size=244,  # TODO
            z_size=47 + (standoff - 2),
        )
        self.colour = "blue"


class MicroATX(BaseATX):
    """Micro ATX motherboard.

    This is for a micro style ATX motherboard.
    Including 8mm standoffs, for mounting motherboard to case.
    """

    def __init__(self, standoff=8):
        super().__init__(
            part_no="atx-motherboard",
            x_size=243.84,  # TODO a bit extra for the connector section that can hang over the edge of the PCB.
            y_size=243.84,
            z_size=47 + (standoff - 2),
        )
        self.colour = "blue"
