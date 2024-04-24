from __future__ import annotations

from dataclasses import dataclass

from .block_base import BlockBase


@dataclass
class Plate(BlockBase):
    def get_name(self: Plate) -> str:
        return str(self.get_value(1, 1))

    def get_type(self: Plate) -> str:
        return str(self.get_value(2, 1))
