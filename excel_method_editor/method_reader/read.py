from __future__ import annotations

import pathlib
from typing import Any, cast

import xlwings

from excel_method_editor.blocks import BlockBase


def read(method: xlwings.Sheet):

    range_values: list[list[Any]] = cast(Any, method.used_range.options(ndim=2).value)

    blocks: list[BlockBase] = []

    for col_index, col in enumerate(range_values):
        for row_index, cell in enumerate(col):
            if not isinstance(cell, str):
                continue

            if "(click here to update)" in cell.lower():
                block_name = (
                    cell.lower().replace(" ", "").replace("-(clickheretoupdate)", "")
                )

                blocks.append(
                    BlockBase.blocks[block_name](
                        pathlib.Path(method.book.fullname),
                        row_index,
                        col_index,
                    ),
                )

    print(blocks[0].get_type())


read(
    xlwings.books.open(
        pathlib.Path(
            "C:\\Users\\BAREB\\OneDrive - Pfizer\\Desktop\\Projects\\ExcelMethodEditor\\tests\\template.xlsm",
        ),
    ).sheets["Method"],
)
