"""Top-level package for drug-database."""
from importlib.metadata import metadata

from ._drug_database import get_drug_factors

meta = metadata("drug_database")
__version__ = meta["Version"]
__author__ = meta["Author"]
__license__ = meta["License"]
__email__ = meta["Author-email"]
__program_name__ = meta["Name"]

__all__ = ["get_drug_factors"]
