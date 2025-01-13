from cycax.cycad import Print3D


class ApeviaFlexATX(Print3D):
    def __init__(self):
        super().__init__(
            part_no="psu-apevia", x_size=81.5, y_size=150, z_size=40.50
        )  # using size dimentions as for silverstonetek.
        # Own messurements :82,86 x 150.5 x 41
        self.colour = "black"
        # There is a 2mm overhang at the back and left for the connector plate, if that is builtin.

    def definition(self):
        hole_from_back_left = 4.1
        hole_from_front_right = 24.04
        hole_from_top_all = 10.2
        hole_from_front_left = 4.1
        hole_from_back_right = 4.1

        x = self.x_size
        y = self.z_size

        self.left.hole(pos=(hole_from_back_left, y - hole_from_top_all), diameter=3.2, external_subtract=True)
        self.left.hole(pos=(x - hole_from_front_left, y - hole_from_top_all), diameter=3.2, external_subtract=True)
        self.right.hole(pos=(hole_from_front_right, y - hole_from_top_all), diameter=3.2, external_subtract=True)
        self.right.hole(pos=(x - hole_from_back_right, y - hole_from_top_all), diameter=3.2, external_subtract=True)
