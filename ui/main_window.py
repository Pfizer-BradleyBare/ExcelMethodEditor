from __future__ import annotations

import pandas as pd
import plotly.express as px
from PySide6.QtCore import Qt
from PySide6.QtGui import QCloseEvent
from PySide6.QtWidgets import QApplication, QMainWindow
from ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self: MainWindow) -> None:
        super().__init__()
        self.setupUi(self)
        self.setWindowFlag(Qt.WindowType.WindowMinimizeButtonHint, False)
        self.setWindowFlag(Qt.WindowType.WindowMaximizeButtonHint, False)

        self.button_main_home.setChecked(True)
        self.pages_main.setCurrentIndex(0)

    def closeEvent(self: MainWindow, event: QCloseEvent) -> None:
        event.accept()

    def button_main_home_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(0)

    def button_main_method_tools_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(1)

    def button_main_devices_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(2)

    def button_main_notifications_shortcut_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(3)

    def button_main_deck_loading_shortcut_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(4)

    def button_main_debug_clicked(self: MainWindow) -> None:
        self.pages_main.setCurrentIndex(5)

    def button_home_reload_gantt_clicked(self: MainWindow) -> None:
        df = pd.DataFrame(
            [
                dict(
                    Task="Job A",
                    Start="1970-01-01 00:00",
                    Finish="1970-01-01 23:10",
                    Resource="Alex",
                ),
                dict(
                    Task="Job B",
                    Start="1970-01-01 00:12",
                    Finish="1970-01-01 00:24",
                    Resource="Alex",
                ),
                dict(
                    Task="Job C",
                    Start="1970-01-01 00:05",
                    Finish="1970-01-01 00:20",
                    Resource="Max",
                ),
            ],
        )

        fig = px.timeline(
            df,
            x_start="Start",
            x_end="Finish",
            y="Task",
        )
        html = fig.to_html(include_plotlyjs="cdn")

        self.web_home_gantt.setHtml(html)


app = QApplication()

window = MainWindow()

window.show()
app.exec()
