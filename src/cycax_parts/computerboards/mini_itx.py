# SPDX-FileCopyrightText: 2025 Apache-2.0
#
# SPDX-License-Identifier: Apache-2.0

from cycax.cycad import Print3D

MINIITX_PCB = 170  # Size of the PCB of a mini-itx board. The PCB is square.
MINIITX_X_SIZE = 173  # From Spec: 172.62 = 6.35 + 7.52 + 158.75
MINIITX_Y_SIZE = 172  #  Measure 2mm over.


def mini_itx_mounting_holes():
    """
    Back is the connectors.
    Left is the PCIe slot.
    Top is the component side.
    """
    # This is the mounting holes as seen from the top.
    # Mounting holes
    lr_holes = 157.48  # Distance between Left-Right holes.
    lfb_holes = 154.94  # Distance betweem Front-Back holes on the left.
    rfb_holes = 132.08  # Distance betweem Front-Back holes on the right.
    l_edge = 6.35  # Holes on left from edge
    f_edge = MINIITX_PCB - lfb_holes - 10.16  # The spec gives the distance from the back.

    return (
        (l_edge, f_edge),
        (l_edge, f_edge + lfb_holes),
        (l_edge + lr_holes, f_edge),
        (l_edge + lr_holes, f_edge + rfb_holes),
    )


class MiniItxMb(Print3D):
    """Mini-ITX motherboard.

    This is for a typical desktop style Mini-ITX not the thin (44mm) or thinner (25mm)
    boards used in the all-in-one computer & screen builds.
    Including 8mm standoffs, for mounting motherboard to case.
    """

    def __init__(self):
        super().__init__(
            part_no="mini-itx-motherboard",
            x_size=MINIITX_X_SIZE,
            y_size=MINIITX_Y_SIZE,
            z_size=53,
        )
        self.colour = "blue"

    def definition(self):
        for pos in mini_itx_mounting_holes():
            self.top.hole(pos=pos, diameter=4)
            bpos = (pos[0], self.y_size - pos[1])
            self.bottom.hole(pos=bpos, diameter=3.2, external_subtract=True)
            # A few silly features to identify the back.
            self.back.hole(pos=(20, 20), diameter=10, depth=5)
            self.back.hole(pos=(40, 20), diameter=10, depth=5)
            self.back.hole(pos=(60, 20), diameter=10, depth=5)


pcie_extra = 8  # The extra space needed for the PCIe card.
# !! Note this is from long edge of PCIe bracket to motherboard and excludes the mounting "lip", thats and extra 4mm.
# This asume we remove the PCIe bracket shipped with the NIC.


class MiniItxMbLpPcie(Print3D):
    """Mini-ITX motherboard with a low profile PCIe card.

    Including 8mm standoffs, for mounting motherboard to case.
    """

    def __init__(self):
        super().__init__(
            part_no="mini-itx-motherboard-lp-pci",
            x_size=MINIITX_X_SIZE + pcie_extra,
            y_size=MINIITX_Y_SIZE,
            z_size=82,
        )
        self.colour = "blue"

    def definition(self):
        # TODO: Add mounting holes for PCIe card.
        # TODO: Add vent holes/slots for NIC.
        for _pos in mini_itx_mounting_holes():
            pos = (_pos[0] + pcie_extra, _pos[1])
            self.top.hole(pos=pos, diameter=4)
            bpos = (pos[0], self.y_size - pos[1])
            self.bottom.hole(pos=bpos, diameter=3.2, external_subtract=True)
            # A few silly features to identify the back.
            self.back.hole(pos=(20, 20), diameter=10, depth=5)
            self.back.hole(pos=(40, 20), diameter=10, depth=5)
            self.back.hole(pos=(60, 20), diameter=10, depth=5)
