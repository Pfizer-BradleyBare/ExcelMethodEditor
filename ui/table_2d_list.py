from __future__ import annotations

from typing import Any

from PySide6.QtCore import QAbstractTableModel, QModelIndex, QPersistentModelIndex, Qt


class Table2DList(QAbstractTableModel):
    def __init__(self: Table2DList) -> None:
        super().__init__()
        self._data: list[list[Any]] = []

    def rowCount(self, parent: QModelIndex | QPersistentModelIndex) -> int:
        return len(self._data)

    def columnCount(self, parent: QModelIndex | QPersistentModelIndex) -> int:
        try:
            return max(len(row) for row in self._data)
        except ValueError:
            return 0

    def data(
        self,
        index: QModelIndex | QPersistentModelIndex,
        role: Qt.ItemDataRole,
    ) -> Any:
        if role != Qt.ItemDataRole.DisplayRole:
            return None

        return str(self._data[index.row()][index.column()])

    def change_data(self: Table2DList, data: list[list[Any]]) -> None:
        self.beginResetModel()
        self._data = data
        self.endResetModel()
