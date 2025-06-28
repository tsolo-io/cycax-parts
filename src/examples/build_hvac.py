# SPDX-FileCopyrightText: 2025 Tsolo.io
#
# SPDX-License-Identifier: Apache-2.0

"""Create some examples to demonstrate the HVAC components.

FANS:
    The fans Fan80x80x25, Fan40x40x10, and Fan120x120x25 are displayed in an assembly
    with and upright where the Fan vents are cut in and a base plate.
    On each assembly two fans are placed on set as external fan and one as internal fan.
    The external fan has fents and the internal fan has a large hole in the center.
"""

from pathlib import Path
from cycax.cycad import Assembly, SheetMetal
from cycax.cycad.engines.part_build123d import PartEngineBuild123d
from cycax.cycad.engines.assembly_build123d import AssemblyBuild123d

from cycax_parts.hvac.fan import Fan
from cycax_parts.hvac.fan import Fan120x120x25
from cycax_parts.hvac.fan import Fan40x40x10
from cycax_parts.hvac.fan import Fan80x80x25


def fan_case(fans: list[Fan]):
    """Create a simple case, just two sides, to hold the fans.

    Note: Fans must be the same size.

    Args:
        fans (list[Fan]): List of fans to be placed in the case.

    Returns:
        Assembly: The assembled case with fans.
    """
    name = fans[0].part_no
    assembly = Assembly(f"{name}_case")
    x_size = 20 + len(fans) * (fans[0].x_size + 10)
    base = SheetMetal(x_size=x_size, y_size=fans[0].z_size + 10, z_size=2, part_no=f"{name}-base")
    upright = SheetMetal(x_size=x_size, y_size=fans[0].y_size + 10, z_size=2, part_no=f"{name}-upright")

    assembly.add(upright)
    assembly.add(base)
    upright.rotate("x")
    base.level(front=upright.back, bottom=upright.bottom, left=upright.left)

    for order, fan in enumerate(fans):
        assembly.add(fan)
        fan.rotate("x")

        fan.level(front=upright.back, bottom=base.top, left=base.left)
        fan.move(x=10 + order * (10 + fan.x_size))
        fan.level(front=upright.back, bottom=base.top, subtract=True)
    return assembly


def main():
    build_dir = Path("./build")
    build_dir.mkdir(parents=True, exist_ok=True)

    part_classes = [Fan80x80x25, Fan40x40x10, Fan120x120x25]
    for part_class in part_classes:
        assembly = fan_case((part_class(internal=False), part_class(internal=True)))
        assembly.save(build_dir / assembly.name)
        assembly.build(engine=AssemblyBuild123d(assembly.name), part_engines=[PartEngineBuild123d()])


if __name__ == "__main__":
    main()
