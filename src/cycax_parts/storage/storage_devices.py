"""Data storage devices."""

from cycax.cycad import Cuboid
from cycax.cycad.engines.part_build123d import PartEngineBuild123d


class LFF(Cuboid):
    """Large Form Factor storage device device.

    These are Hard Disk Drive (HDD) storage devices and often called 3.5-inch drives.
    """

    def __init__(self, *, height: float = 26.1):
        self.height = height
        super().__init__(part_no=f"LFF-{int(height)}", x_size=101.6, y_size=147.0, z_size=height)

    def definition(self):
        """Define the LFF storage device.

        This method defines the geometry of the LFF storage device, including its dimensions,
        holes, and other features. It uses the Cycad library to create a 3D model of the device.

        The SAS/SATA connectors are located on the front of the device.

        https://support.wdc.com/images/kb/2579-771970-A03.pdf
        """

        for hole_x in (self.y_size - 28.5, self.y_size - (28.5 + 101.6)):
            self.left.hole(pos=(hole_x, 6.35), diameter=3.505)
            self.left.hole(pos=(hole_x, 6.35), diameter=3.7, external_subtract=True)
            self.right.hole(pos=(self.y_size - hole_x, 6.35), diameter=3.505)
            self.right.hole(pos=(self.y_size - hole_x, 6.35), diameter=3.7, external_subtract=True)

        for hole_y in (
            self.y_size - 41.28,
            self.y_size - (41.28 + 44.45),
            self.y_size - (41.28 + 76.2),
        ):
            # There are two standards for holes at the bottom of the devices.
            # The first (closest to the connector) is the same in both standards.
            # We will add all the hole combinations.
            self.bottom.hole(pos=(3.18, hole_y), diameter=3.505, depth=3.56)
            self.bottom.hole(pos=(3.18, hole_y), diameter=3.7, external_subtract=True)
            self.bottom.hole(pos=(self.x_size - 3.18, hole_y), diameter=3.505, depth=3.56)
            self.bottom.hole(pos=(self.x_size - 3.18, hole_y), diameter=3.7, external_subtract=True)

        self.front.box(pos=(10, 0), length=50, width=5, depth=5)


class SFF(Cuboid):
    """Small Form Factor storage device device.

    These are Hard Disk Drive (HDD) or Solid State Drive (SSD) storage devices and often called 2.5-inch drives.

    https://www.google.com/url?sa=t&source=web&rct=j&opi=89978449&url=https://members.snia.org/document/dl/25851&ved=2ahUKEwjTgauohcyOAxWjgf0HHXSgEMwQh-wKegQIDhAD&usg=AOvVaw3v9nFxBagSB7yN_q5gA0qq
    """

    def __init__(self, *, height: float = 6.7):  # Height = 7 + 0.2 - 0.5 = 6.7
        self.height = height
        super().__init__(part_no=f"SFF-{int(height)}", x_size=69.85, y_size=100.45, z_size=height)

    def definition(self):
        """Define the SFF storage device.

        This method defines the geometry of the SFF storage device, including its dimensions,
        holes, and other features. It uses the Cycad library to create a 3D model of the device.

        The SAS/SATA connectors are located on the front of the device.
        """

        for hole_x in (self.y_size - 14, self.y_size - 90.6):
            self.left.hole(pos=(hole_x, 3), diameter=3, depth=2)
            self.left.hole(pos=(hole_x, 3), diameter=3.2, depth=2, external_subtract=True)
            self.right.hole(pos=(self.y_size - hole_x, 3), diameter=3, depth=2)
            self.right.hole(
                pos=(self.y_size - hole_x, 3),
                diameter=3.2,
                depth=2,
                external_subtract=True,
            )

        for hole_y in (self.y_size - 14, self.y_size - 90.6):
            self.bottom.hole(pos=(4.07, hole_y), diameter=3, depth=2)
            self.bottom.hole(pos=(4.07, hole_y), diameter=3.2, depth=2, external_subtract=True)
            self.bottom.hole(pos=(self.x_size - 4.07, hole_y), diameter=3, depth=2)
            self.bottom.hole(
                pos=(self.x_size - 4.07, hole_y),
                diameter=3.2,
                depth=2,
                external_subtract=True,
            )

        self.front.box(pos=(13.43, 0), length=42.73, width=5, depth=5)
