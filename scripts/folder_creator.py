import os
from pathlib import Path

def apply(path):
    if not Path(path).exists():
        Path(path).mkdir(parents=True, exist_ok=True)
