# SPDX-FileCopyrightText: 2025 Tsolo.io
#
# SPDX-License-Identifier: Apache-2.0

from cycax.cycad import Print3D


class Meanwell15V(Print3D):
    def __init__(self):
        super().__init__(part_no="psu-meanwell-15v", x_size=114.3, y_size=215, z_size=50)
        self.colour = "red"

    def definition(self):
        for x in (32, self.x_size - 32):
            for y in (32, self.y_size - 32):
                self.bottom.hole(pos=(x, y), diameter=4.2, external_subtract=True)
