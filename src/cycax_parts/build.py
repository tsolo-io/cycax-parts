
import logging
import os
from pathlib import Path

from cycax.cycad.engines.part_server import PartEngineServer
from cycax_parts.computerboards.mini_itx import MiniItxMbLpPcie
from cycax_parts.construction.conn_cube import ConnCube
from cycax_parts.powersupplies.silverstonetek import SilverstonetekFlexATX
from cycax_parts.powersupplies.meanwell import Meanwell15V
from cycax_parts.powersupplies.apevia import ApeviaFlexATX

from dotenv import load_dotenv

load_dotenv()
if os.environ.get("DEBUG"):
    logging.basicConfig(level=logging.DEBUG)
else:
    logging.basicConfig(level=logging.INFO)

def main():
    build_dir = Path("./build")
    build_dir.mkdir(parents=True, exist_ok=True)
    part_classes = [
            MiniItxMbLpPcie,
            ConnCube,
            SilverstonetekFlexATX,
            Meanwell15V,
            ApeviaFlexATX,
            ]
    for part_class in part_classes:
        part = part_class()
        part.save(build_dir)
        cycax_server = PartEngineServer()
        cycax_server.build(part)


if __name__ == '__main__':
    main()
