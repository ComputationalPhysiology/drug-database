from __future__ import annotations

import json
from functools import lru_cache
from pathlib import Path

here = Path(__file__).absolute().parent


@lru_cache
def get_drug_factors() -> dict[str, dict[str, dict[str, float]]]:
    return json.loads((here / "drug_factors.json").read_text())
