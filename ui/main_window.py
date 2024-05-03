from __future__ import annotations

import random
from typing import cast

from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from table_2d_list import Table2DList
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self: MainWindow) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        self.button_main_home.setChecked(True)
        self.pages_main.setCurrentIndex(0)

        model = Table2DList()
        self.table_view_home_log.setModel(model)

    def closeEvent(self: MainWindow, event: QCloseEvent) -> None:
        event.accept()

    def button_main_menu_bar_home_clicked(self: MainWindow) -> None:
        model = cast(Table2DList, self.table_view_home_log.model())
        model.change_data(
            [[random.randint(1, 100) for j in range(20)] for i in range(100)],
        )
        self.pages_main.setCurrentIndex(0)

    def button_main_menu_bar_method_tools_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(1)

    def button_main_menu_bar_devices_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(2)

    def button_main_menu_bar_notifications_shortcut_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(3)

    def button_main_menu_bar_deck_loading_shortcut_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(4)


app = QApplication()

window = MainWindow()

window.show()
app.exec()
