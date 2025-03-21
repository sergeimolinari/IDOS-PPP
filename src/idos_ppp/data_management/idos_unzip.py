import zipfile
from pathlib import Path

from idos_ppp.config import BLD

bld_file = BLD

if not bld_file.exists():
    bld_file.mkdir()
    print("Directory created")
else:
    print("Directory already exists")


path_to_zip_file = (
    Path(__file__).parent.parent
    / "data"
    / "continents-according-to-our-world-in-data.filtered.zip"
)

bld_dir = bld_file / "data_continents"

with zipfile.ZipFile(path_to_zip_file, "r") as zip_ref:
    zip_ref.extractall(bld_dir)
