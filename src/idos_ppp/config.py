"""All the general configuration of the project."""

from pathlib import Path

PROJECT = Path(__file__).parent.resolve()
SRC = Path(__file__).parent.parent.resolve()
ROOT = PROJECT.joinpath("..", "..").resolve()

BLD = ROOT.joinpath("bld").resolve()

# Folders inside project_mbb
DATA = PROJECT.joinpath("data").resolve()
DATA_MGT = PROJECT.joinpath("data_management").resolve()
ANALYSIS = PROJECT.joinpath("analysis").resolve()
FINAL = PROJECT.joinpath("final").resolve()

DOCUMENTS = ROOT.joinpath("documents").resolve()
