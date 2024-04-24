from __future__ import annotations

from dataclasses import dataclass

from .block_base import BlockBase


@dataclass(kw_only=True)
class MixParams:
    aspirate: int = 0
    dispense: int = 0


@dataclass
class LiquidTransfer(BlockBase):
    def get_source(self: LiquidTransfer) -> str:
        return str(self.get_value(1, 1))

    def get_volume(self: LiquidTransfer) -> float:
        return float(self.get_value(2, 1))

    def get_mix(self: LiquidTransfer) -> MixParams:
        value = str(self.get_value(3, 1))

        if value.lower() == "no":
            return MixParams()

        return MixParams(
            **{
                item.split(":")[0]: int(item.split(":")[1])
                for item in value.lower().replace(" ", "").split("+")
            },
        )
