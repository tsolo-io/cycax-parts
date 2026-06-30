"Various Models of Odroids"

from cycax.cycad import Cuboid
from cycax.cycad.engines.part_build123d import PartEngineBuild123d


class OdroidH3(Cuboid):
    """The Odroid H2 and Odroid H3 are the same size and have the same mounting holes.

    Dimensions are based on the Odroid H3.

    https://wiki.odroid.com/odroid-h3/hardware#board_dimensions
    """

    def __init__(self, *, standoff: float = 12):
        self.length = 110
        self.width = 110
        self.overhang = 5  # Overhang of connectors in front of board
        if standoff > 10:  # Components reach 10 mm below the board
            self.height = 2 + 19 + 16 + standoff
        else:
            msg = "The length of the standoff must be greater than 10 mm."
            raise ValueError(msg)
        super().__init__(
            part_no="OdroidH3",
            x_size=self.length,
            y_size=self.width + self.overhang,
            z_size=self.height,
        )

    def definition(self):
        """Define the Odroid H3. Connectors are in the front."""

        # To represent the side with the connectors. Not to scale.
        for sq_x in (15, 45, 75):
            sq_y = 5
            self.front.box(pos=(sq_x, sq_y), length=10, width=10, depth=5)

        # Mounting holes
        self.bottom.hole(pos=(3.81, 3.81), diameter=3.51)
        self.bottom.hole(pos=(3.81, 3.81), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81), diameter=3.51)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(3.81, 3.81 + 88.41), diameter=3.51)
        self.bottom.hole(pos=(3.81, 3.81 + 88.41), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81 + 81.43), diameter=3.51)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81 + 81.43), diameter=3.7, external_subtract=True)


class OdroidH4(Cuboid):
    """The Odroid H4 is the same size as the Nano-ITX. However, the mounting holes are different.

    Dimensions are based on the Odroid H4.

    https://wiki.odroid.com/odroid-h4/hardware#board_dimensions
    """

    def __init__(self, *, standoff: float = 6):
        self.length = 120
        self.width = 120
        self.overhang = 5  # Overhang of connectors in front of board
        if standoff > 5:  # Components reach 5.2 mm below the board
            self.height = 2 + 35 + standoff
        else:
            msg = "The length of the standoff must be greater than 5 mm."
            raise ValueError(msg)
        super().__init__(
            part_no="OdroidH4",
            x_size=self.length,
            y_size=self.width + self.overhang,
            z_size=self.height,
        )

    def definition(self):
        """Define the Odroid H4. Connectors are in the front."""

        # To represent the side with the connectors. Not to scale.
        for sq_x in (15, 30, 45, 60):
            sq_y = 5
            self.front.box(pos=(sq_x, sq_y), length=10, width=10, depth=5)

        # Mounting holes
        self.bottom.hole(pos=(3.81, 3.81), diameter=3.51)
        self.bottom.hole(pos=(3.81, 3.81), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81), diameter=3.51)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(3.81, 3.81 + 98.41), diameter=3.51)
        self.bottom.hole(pos=(3.81, 3.81 + 98.41), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(3.81 + 16.36, 3.81 + 72.37), diameter=3.51)
        self.bottom.hole(pos=(3.81 + 16.36, 3.81 + 72.37), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(self.x_size - 12.7, 3.81 + 91.42), diameter=3.51)
        self.bottom.hole(pos=(self.x_size - 12.7, 3.81 + 91.42), diameter=3.7, external_subtract=True)


class OdroidH5(Cuboid):
    """The Odroid H5 is the same size as the Nano-ITX. However, the mounting holes are different.

    Dimensions are based on the Odroid H5.

    https://wiki.odroid.com/odroid-h5/hardware#board_dimensions
    """

    def __init__(self, *, standoff: float = 6):
        self.length = 120
        self.width = 120
        self.overhang = 3  # Overhang of connectors in front of board
        if standoff > 5:  # Components reach 5.2 mm below the board
            self.height = 2 + 31 + standoff
        else:
            msg = "The length of the standoff must be greater than 5 mm."
            raise ValueError(msg)
        super().__init__(
            part_no="OdroidH5",
            x_size=self.length,
            y_size=self.width + self.overhang,
            z_size=self.height,
        )

    def definition(self):
        """Define the Odroid H5. Connectors are in the front."""

        # To represent the side with the connectors. Not to scale.
        for sq_x in (15, 30, 45, 60, 75):
            sq_y = 5
            self.front.box(pos=(sq_x, sq_y), length=10, width=10, depth=5)

        # Mounting holes
        self.bottom.hole(pos=(3.81, 3.81), diameter=3.51)
        self.bottom.hole(pos=(3.81, 3.81), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81), diameter=3.51)
        self.bottom.hole(pos=(self.x_size - 3.96, 3.81), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(3.81, 3.81 + 98.41), diameter=3.51)
        self.bottom.hole(pos=(3.81, 3.81 + 98.41), diameter=3.7, external_subtract=True)
        self.bottom.hole(pos=(self.x_size - 12.7, 3.81 + 91.42), diameter=3.51)
        self.bottom.hole(pos=(self.x_size - 12.7, 3.81 + 91.42), diameter=3.7, external_subtract=True)
