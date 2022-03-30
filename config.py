from __future__ import annotations

from dataclasses import dataclass
import os

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CONFIG_PATH = os.path.join(ROOT_DIR, 'configuration.conf')


def getAssetPath(asset_path: str) -> str:
    return os.path.join(ROOT_DIR, "assets", asset_path)


def getConfig() -> Config:
    return Config()


@dataclass
class Config:
    pass
