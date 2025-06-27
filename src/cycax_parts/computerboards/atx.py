# SPDX-FileCopyrightText: 2025 Tsolo.io
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

    inches = {  # These values are in inches.
        "A": (11.35, 0.4),
        "B": (8.25, 0.4),
        "C": (6.45, 0.4),
        "F": (0.25, 1.3),
        "G": (11.35, 6.5),
        "H": (6.45, 6.5),
        "J": (0.25, 6.5),
        "K": (11.35, 9.35),
        "L": (6.45, 9.35),
        "M": (0.25, 9.35),
        "R": (9.05, 6.5),
        "S": (8.25, 6.5),
    }
    in_mm = {}
    for name, pos in inches.items():
        # Convert the inches to mm.
        in_mm[name] = (pos[0] * 25.4 + 3.8, pos[1] * 25.4 + 3.3)
    return in_mm


def atx_connectors():
    """Some random holes to mark the connector end of the Motherboard."""
    return ((20, 20), (40, 20), (60, 20))


class BaseATX(Print3D):
    """A Base class of ATX type mother boards.

    Note:
        Do not use this class directly. Use it to build other classes with.
    """

    board_x_size = 0
    board_y_size = 0

    def __init__(
        self, *, standoff: float = 8.0, desktop: bool = True, pcie_full_height: bool = False, pcie_cards: int = 1
    ):
        self.pcie_full_height = pcie_full_height
        self.pcie_cards = pcie_cards
        if pcie_cards < 1:
            part_no = self.part_no
        else:
            pci_type = "full" if self.pcie_full_height else "half"
            part_no = f"{self.part_no}-{pcie_cards}{pci_type}"
        super().__init__(
            part_no=part_no,
            x_size=self.board_x_size,
            y_size=self.board_y_size,
            z_size=47 + (standoff - 2),
        )
        self.colour = "blue"

    def definition(self):
        for pos in atx_mounting_holes().values():
            if pos[0] < self.x_size and pos[1] < self.y_size:
                self.top.hole(pos=pos, diameter=4)
                bpos = (pos[0], self.y_size - pos[1])
                self.bottom.hole(pos=bpos, diameter=3.2, external_subtract=True)
        # A few silly features to identify the connector end.
        for pos in atx_connectors():
            if pos[0] < self.x_size and pos[1] < self.z_size:
                self.front.hole(pos=pos, diameter=10, depth=5)
        # Trim off the material not part of the face.
        self.front.box(pos=(6.25 * 25.4, 0), depth=3.3, length=self.x_size, width=self.z_size)
        # self.left.box(pos=(self.y_size+3.3,10), depth=3.8, length=self.y_size, width=self.z_size-20)
        self.left.box(pos=(-3.3, 0), depth=3.8, length=self.y_size, width=self.z_size)
        # Cut out the io panel from attached material.
        self.front.box(pos=(3, 4.7), length=156.5, width=43.2, external_subtract=True)
        pci_h = 120 if self.pcie_full_height else 80
        for pci in range(self.pcie_cards):
            self.front.box(pos=(167 + pci * 20.32, 10), length=12.7, width=pci_h, external_subtract=True)


class StandardATX(BaseATX):
    """Standard ATX motherboard.

    This is for a typical desktop style ATX motherboard.
    Including 8mm standoffs, for mounting motherboard to case.
    """

    part_no = "motherboard-standard-atx"
    board_x_size = 305 + 3.8  # Motherboard + overhang
    board_y_size = 244 + 3.3  # Motherboard + overhang


class MicroATX(BaseATX):
    """Micro ATX motherboard.

    This is for a micro style ATX motherboard.
    Including 8mm standoffs, for mounting motherboard to case.
    """

    part_no = "motherboard-micro-atx"
    board_x_size = 244 + 3.8  # Motherboard + overhang
    board_y_size = 244 + 3.3  # Motherboard + overhang


class MiniITX(BaseATX):
    """Mini ITX motherboard.

    This is for a mini ITX motherboard.
    Including 8mm standoffs, for mounting motherboard to case.
    """

    part_no = "motherboard-mini-itx"
    board_x_size = 170 + 3.8  # Motherboard + overhang
    board_y_size = 170 + 3.3  # Motherboard + overhang
