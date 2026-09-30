"""Place holder for GPU."""


from cycax.cycad import  Cuboid


PCIE_HEAD = 11.43  # How much the PCIe card head protrudes from the bracket.
PCIE_HEIGHT = 120


class GPU(Cuboid):
    """Place holder GPU creator.

    The GPU is viewed as it would when plugged into a PCIe slot of a motherboard flat on the table.
     - The PCIe port is at the bottom.
     - The Video ports are at the left.
     - The fans are at the front.

    GPU dimensions are based on GEFORCE RTX 5080 16GB because it has the most overhang above the PCIE.
    """

    def __init__(self, *, pcie_width: int = 3):
        self.pcie_width = pcie_width
        name = f"gpu-{pcie_width}"
        super().__init__(
            part_no=name,
            x_size=328 + PCIE_HEAD,
            y_size=pcie_width * 18.42 + 4,
            z_size=PCIE_HEIGHT + 30,  # GPU extends 30mm above PCIe.
        )
        self.colour = "green"

    def definition(self):
        """Calculate GPU."""

        self.front.box(pos=(0.0, 0.0), length=PCIE_HEAD, width=PCIE_HEIGHT - 1)  # PCIe mounting bracket.
        self.front.box(pos=(0.0, 120), length=PCIE_HEAD, width=30)  # PCIe mounting bracket.
        self.front.box(pos=(PCIE_HEAD + 1, 0), length=self.x_size, width=20)  # Space under PCIe port.
        self.front.box(
            pos=(PCIE_HEAD + 1, 0),
            length=self.x_size,
            width=27.24 + 2,
            depth=self.y_size - 2,
        )  # Next to PCIe port PCB.
        self.front.box(pos=(PCIE_HEAD + 1 + 15, 0), length=41.21 - 13, width=27.24)  # gap in front of PCIe port
        self.front.box(
            pos=(PCIE_HEAD + 1 + 56.21 + 1.854 + 62.77, 0),
            length=self.x_size,
            width=27.24,
        )  # gap after PCIe port

        # Pretend Fans
        y = self.z_size / 2 + 8
        x = self.x_size / 2
        self.front.hole(pos=(x, y), diameter=80, depth=2)
        self.front.hole(pos=(x - 90, y), diameter=80, depth=2)
        self.front.hole(pos=(x + 90, y), diameter=80, depth=2)
