from __future__ import annotations

import pathlib
from dataclasses import dataclass
from typing import Any, ClassVar, cast


@dataclass
class BlockBase:
    blocks: ClassVar[dict[str, type[BlockBase]]] = {}

    book_path: pathlib.Path

    row_index: int
    """Row index where the title of the block is found."""

    col_index: int
    """col index where the title of the block is found."""

    def __init_subclass__(cls: type[BlockBase]) -> None:
        BlockBase.blocks[cls.__name__.lower()] = cls

    def get_value(self: BlockBase, row_offset: int, col_offset: int) -> Any:

        from excel_method_editor.method_reader import open

        # circular reference error fix.

        method = open(self.book_path)

        range_values: list[list[Any]] = cast(
            Any,
            method.used_range.options(ndim=2).value,
        )

        return range_values[self.col_index + row_offset][self.row_index + col_offset]
