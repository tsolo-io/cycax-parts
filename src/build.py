# SPDX-FileCopyrightText: 2025 Tsolo.io
#
# SPDX-License-Identifier: Apache-2.0

import logging
import os
from pathlib import Path
from cycax.cycad import Assembly, SheetMetal
from cycax.cycad.engines.part_build123d import PartEngineBuild123d
from cycax.cycad.engines.assembly_build123d import AssemblyBuild123d
from dotenv import load_dotenv

from cycax_parts.computerboards.atx import MicroATX, StandardATX, MiniITX
from cycax_parts.computerboards.mini_itx import MiniItxMbLpPcie
from cycax_parts.construction.conn_cube import ConnCube
from cycax_parts.powersupplies.apevia import ApeviaFlexATX
from cycax_parts.powersupplies.meanwell import Meanwell15V
from cycax_parts.powersupplies.silverstonetek import SilverstonetekFlexATX

load_dotenv()
if os.environ.get("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)


def motherboard_case(motherboard):
    name = motherboard.part_no
    assembly = Assembly(f"{name}_case")
    assembly.add(motherboard)
    upright = SheetMetal(
        x_size=motherboard.x_size + 20, y_size=motherboard.z_size + 10, z_size=2, part_no=f"{name}-upright"
    )
    base = SheetMetal(x_size=motherboard.x_size + 20, y_size=motherboard.y_size + 10, z_size=2, part_no=f"{name}-base")

    assembly.add(upright)
    assembly.add(base)
    upright.rotate("x")
    base.level(front=upright.back, bottom=upright.bottom, left=upright.left)
    motherboard.level(front=upright.back, bottom=base.top, left=base.left)
    motherboard.move(x=10)
    motherboard.level(front=upright.back, bottom=base.top, subtract=True)
    return assembly


def main():
    build_dir = Path("./build")
    build_dir.mkdir(parents=True, exist_ok=True)
    part_classes = [ConnCube, SilverstonetekFlexATX, Meanwell15V, ApeviaFlexATX]
    for part_class in part_classes:
        part = part_class()
        part.save(build_dir)
        cycax_server = PartEngineBuild123d()
        cycax_server.build(part)

    part_classes = [MiniItxMbLpPcie, StandardATX, MicroATX, MiniITX]
    for part_class in part_classes:
        part = part_class()
        assembly = motherboard_case(part)
        assembly.save(build_dir / assembly.name)
        cycax_server = PartEngineBuild123d()
        assembly.build(engine=AssemblyBuild123d(part.part_no), part_engines=[cycax_server])


if __name__ == "__main__":
    main()
