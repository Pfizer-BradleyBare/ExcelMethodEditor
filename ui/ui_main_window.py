################################################################################
## Form generated from reading UI file 'MainWindowLsPDwL.ui'
##
## Created by: Qt User Interface Compiler version 6.6.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QAbstractItemView,
    QButtonGroup,
    QHBoxLayout,
    QLabel,
    QPushButton,
    QScrollArea,
    QStackedWidget,
    QTableView,
    QVBoxLayout,
    QWidget,
)


class Ui_MainWindow:
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1168, 663)
        MainWindow.setMinimumSize(QSize(1168, 663))
        MainWindow.setMaximumSize(QSize(1168, 663))
        MainWindow.setWindowTitle("Automation Bare Necessities")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayoutWidget.setGeometry(QRect(30, 20, 1111, 80))
        self.layout_main_menu_bar = QHBoxLayout(self.horizontalLayoutWidget)
        self.layout_main_menu_bar.setObjectName("layout_main_menu_bar")
        self.layout_main_menu_bar.setContentsMargins(0, 0, 0, 0)
        self.button_main_home = QPushButton(self.horizontalLayoutWidget)
        self.group_main_menu_bar = QButtonGroup(MainWindow)
        self.group_main_menu_bar.setObjectName("group_main_menu_bar")
        self.group_main_menu_bar.addButton(self.button_main_home)
        self.button_main_home.setObjectName("button_main_home")
        self.button_main_home.setMinimumSize(QSize(0, 50))
        self.button_main_home.setMaximumSize(QSize(16777215, 16777215))
        self.button_main_home.setText("Home")
        self.button_main_home.setCheckable(True)

        self.layout_main_menu_bar.addWidget(self.button_main_home)

        self.button_main_method_tools = QPushButton(self.horizontalLayoutWidget)
        self.group_main_menu_bar.addButton(self.button_main_method_tools)
        self.button_main_method_tools.setObjectName("button_main_method_tools")
        self.button_main_method_tools.setMinimumSize(QSize(0, 50))
        self.button_main_method_tools.setMaximumSize(QSize(16777215, 16777215))
        self.button_main_method_tools.setText("Method Tools")
        self.button_main_method_tools.setCheckable(True)

        self.layout_main_menu_bar.addWidget(self.button_main_method_tools)

        self.button_main_devices = QPushButton(self.horizontalLayoutWidget)
        self.group_main_menu_bar.addButton(self.button_main_devices)
        self.button_main_devices.setObjectName("button_main_devices")
        self.button_main_devices.setMinimumSize(QSize(0, 50))
        self.button_main_devices.setMaximumSize(QSize(16777215, 16777215))
        self.button_main_devices.setText("Devices")
        self.button_main_devices.setCheckable(True)

        self.layout_main_menu_bar.addWidget(self.button_main_devices)

        self.button_main_notifications_shortcut = QPushButton(
            self.horizontalLayoutWidget,
        )
        self.group_main_menu_bar.addButton(self.button_main_notifications_shortcut)
        self.button_main_notifications_shortcut.setObjectName(
            "button_main_notifications_shortcut",
        )
        self.button_main_notifications_shortcut.setMinimumSize(QSize(0, 50))
        self.button_main_notifications_shortcut.setMaximumSize(
            QSize(16777215, 16777215),
        )
        self.button_main_notifications_shortcut.setText("Notifications Shortcut")
        self.button_main_notifications_shortcut.setCheckable(True)

        self.layout_main_menu_bar.addWidget(self.button_main_notifications_shortcut)

        self.button_main_deck_loading_shortcut = QPushButton(
            self.horizontalLayoutWidget,
        )
        self.group_main_menu_bar.addButton(self.button_main_deck_loading_shortcut)
        self.button_main_deck_loading_shortcut.setObjectName(
            "button_main_deck_loading_shortcut",
        )
        self.button_main_deck_loading_shortcut.setMinimumSize(QSize(0, 50))
        self.button_main_deck_loading_shortcut.setMaximumSize(QSize(16777215, 16777215))
        self.button_main_deck_loading_shortcut.setText("Deck Loading Shortcut")
        self.button_main_deck_loading_shortcut.setCheckable(True)

        self.layout_main_menu_bar.addWidget(self.button_main_deck_loading_shortcut)

        self.pages_main = QStackedWidget(self.centralwidget)
        self.pages_main.setObjectName("pages_main")
        self.pages_main.setGeometry(QRect(30, 110, 1111, 531))
        self.page_main_home = QWidget()
        self.page_main_home.setObjectName("page_main_home")
        self.label_home_log_header = QLabel(self.page_main_home)
        self.label_home_log_header.setObjectName("label_home_log_header")
        self.label_home_log_header.setGeometry(QRect(10, 0, 361, 41))
        font = QFont()
        font.setPointSize(13)
        self.label_home_log_header.setFont(font)
        # if QT_CONFIG(tooltip)
        self.label_home_log_header.setToolTip("")
        # endif // QT_CONFIG(tooltip)
        self.table_view_home_log = QTableView(self.page_main_home)
        self.table_view_home_log.setObjectName("table_view_home_log")
        self.table_view_home_log.setGeometry(QRect(0, 40, 1111, 491))
        self.table_view_home_log.setSelectionMode(
            QAbstractItemView.SelectionMode.ContiguousSelection
        )
        self.table_view_home_log.setSelectionBehavior(
            QAbstractItemView.SelectionBehavior.SelectRows
        )
        self.table_view_home_log.horizontalHeader().setVisible(False)
        self.table_view_home_log.horizontalHeader().setCascadingSectionResizes(False)
        self.table_view_home_log.horizontalHeader().setStretchLastSection(True)
        self.table_view_home_log.verticalHeader().setVisible(False)
        self.table_view_home_log.verticalHeader().setCascadingSectionResizes(False)
        self.pages_main.addWidget(self.page_main_home)
        self.page_main_method_tools = QWidget()
        self.page_main_method_tools.setObjectName("page_main_method_tools")
        self.verticalLayoutWidget = QWidget(self.page_main_method_tools)
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayoutWidget.setGeometry(QRect(0, 0, 221, 531))
        self.layout_method_tools_menu_bar = QVBoxLayout(self.verticalLayoutWidget)
        self.layout_method_tools_menu_bar.setObjectName("layout_method_tools_menu_bar")
        self.layout_method_tools_menu_bar.setContentsMargins(0, 0, 0, 0)
        self.button_method_tools_show_queue = QPushButton(self.verticalLayoutWidget)
        self.group_method_tools_menu_bar = QButtonGroup(MainWindow)
        self.group_method_tools_menu_bar.setObjectName("group_method_tools_menu_bar")
        self.group_method_tools_menu_bar.addButton(self.button_method_tools_show_queue)
        self.button_method_tools_show_queue.setObjectName(
            "button_method_tools_show_queue",
        )
        self.button_method_tools_show_queue.setMinimumSize(QSize(0, 50))
        self.button_method_tools_show_queue.setText("Show Method Queue")

        self.layout_method_tools_menu_bar.addWidget(self.button_method_tools_show_queue)

        self.button_method_tools_queue_method = QPushButton(self.verticalLayoutWidget)
        self.group_method_tools_menu_bar.addButton(
            self.button_method_tools_queue_method,
        )
        self.button_method_tools_queue_method.setObjectName(
            "button_method_tools_queue_method",
        )
        self.button_method_tools_queue_method.setMinimumSize(QSize(0, 50))
        self.button_method_tools_queue_method.setText("Queue Method")

        self.layout_method_tools_menu_bar.addWidget(
            self.button_method_tools_queue_method,
        )

        self.button_method_tools_test_method = QPushButton(self.verticalLayoutWidget)
        self.group_method_tools_menu_bar.addButton(self.button_method_tools_test_method)
        self.button_method_tools_test_method.setObjectName(
            "button_method_tools_test_method",
        )
        self.button_method_tools_test_method.setMinimumSize(QSize(0, 50))
        self.button_method_tools_test_method.setText("Test Method")

        self.layout_method_tools_menu_bar.addWidget(
            self.button_method_tools_test_method,
        )

        self.button_method_tools_generate_prep_list = QPushButton(
            self.verticalLayoutWidget,
        )
        self.group_method_tools_menu_bar.addButton(
            self.button_method_tools_generate_prep_list,
        )
        self.button_method_tools_generate_prep_list.setObjectName(
            "button_method_tools_generate_prep_list",
        )
        self.button_method_tools_generate_prep_list.setMinimumSize(QSize(0, 50))
        self.button_method_tools_generate_prep_list.setText("Generate Preparation List")

        self.layout_method_tools_menu_bar.addWidget(
            self.button_method_tools_generate_prep_list,
        )

        self.pages_main.addWidget(self.page_main_method_tools)
        self.page_main_devices = QWidget()
        self.page_main_devices.setObjectName("page_main_devices")
        self.scrollArea = QScrollArea(self.page_main_devices)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollArea.setGeometry(QRect(0, 0, 221, 531))
        self.scrollArea.setMaximumSize(QSize(221, 531))
        self.scrollArea.setWidgetResizable(True)
        self.scroll_area_devices_menu_bar = QWidget()
        self.scroll_area_devices_menu_bar.setObjectName("scroll_area_devices_menu_bar")
        self.scroll_area_devices_menu_bar.setGeometry(QRect(0, 0, 202, 966))
        self.verticalLayout = QVBoxLayout(self.scroll_area_devices_menu_bar)
        self.verticalLayout.setObjectName("verticalLayout")
        self.layout_device_menu_bar = QVBoxLayout()
        self.layout_device_menu_bar.setObjectName("layout_device_menu_bar")
        self.button_devices_backend = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar = QButtonGroup(MainWindow)
        self.group_devices_menu_bar.setObjectName("group_devices_menu_bar")
        self.group_devices_menu_bar.addButton(self.button_devices_backend)
        self.button_devices_backend.setObjectName("button_devices_backend")
        self.button_devices_backend.setMinimumSize(QSize(0, 50))
        self.button_devices_backend.setText("Backend")

        self.layout_device_menu_bar.addWidget(self.button_devices_backend)

        self.button_devices_carrier = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_carrier)
        self.button_devices_carrier.setObjectName("button_devices_carrier")
        self.button_devices_carrier.setMinimumSize(QSize(0, 50))
        self.button_devices_carrier.setText("Carrier")

        self.layout_device_menu_bar.addWidget(self.button_devices_carrier)

        self.button_devices_carrier_loader = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_carrier_loader)
        self.button_devices_carrier_loader.setObjectName(
            "button_devices_carrier_loader",
        )
        self.button_devices_carrier_loader.setMinimumSize(QSize(0, 50))
        self.button_devices_carrier_loader.setText("Carrier Loader")

        self.layout_device_menu_bar.addWidget(self.button_devices_carrier_loader)

        self.button_devices_centrifuge = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_centrifuge)
        self.button_devices_centrifuge.setObjectName("button_devices_centrifuge")
        self.button_devices_centrifuge.setMinimumSize(QSize(0, 50))
        self.button_devices_centrifuge.setText("Centrifuge")

        self.layout_device_menu_bar.addWidget(self.button_devices_centrifuge)

        self.button_devices_closeable_container = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_closeable_container)
        self.button_devices_closeable_container.setObjectName(
            "button_devices_closeable_container",
        )
        self.button_devices_closeable_container.setMinimumSize(QSize(0, 50))
        self.button_devices_closeable_container.setText("Closeable Container")

        self.layout_device_menu_bar.addWidget(self.button_devices_closeable_container)

        self.button_devices_deck_location = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_deck_location)
        self.button_devices_deck_location.setObjectName("button_devices_deck_location")
        self.button_devices_deck_location.setMinimumSize(QSize(0, 50))
        self.button_devices_deck_location.setText("Deck Location")

        self.layout_device_menu_bar.addWidget(self.button_devices_deck_location)

        self.button_devices_door_lock = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_door_lock)
        self.button_devices_door_lock.setObjectName("button_devices_door_lock")
        self.button_devices_door_lock.setMinimumSize(QSize(0, 50))
        self.button_devices_door_lock.setText("Door Lock")

        self.layout_device_menu_bar.addWidget(self.button_devices_door_lock)

        self.button_devices_heat_cool_shake = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_heat_cool_shake)
        self.button_devices_heat_cool_shake.setObjectName(
            "button_devices_heat_cool_shake",
        )
        self.button_devices_heat_cool_shake.setMinimumSize(QSize(0, 50))
        self.button_devices_heat_cool_shake.setText("Heat Cool Shake")

        self.layout_device_menu_bar.addWidget(self.button_devices_heat_cool_shake)

        self.button_devices_labware = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_labware)
        self.button_devices_labware.setObjectName("button_devices_labware")
        self.button_devices_labware.setMinimumSize(QSize(0, 50))
        self.button_devices_labware.setText("Labware")

        self.layout_device_menu_bar.addWidget(self.button_devices_labware)

        self.button_devices_layout_item = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_layout_item)
        self.button_devices_layout_item.setObjectName("button_devices_layout_item")
        self.button_devices_layout_item.setMinimumSize(QSize(0, 50))
        self.button_devices_layout_item.setText("Layout Item")

        self.layout_device_menu_bar.addWidget(self.button_devices_layout_item)

        self.button_devices_magnetic_rack = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_magnetic_rack)
        self.button_devices_magnetic_rack.setObjectName("button_devices_magnetic_rack")
        self.button_devices_magnetic_rack.setMinimumSize(QSize(0, 50))
        self.button_devices_magnetic_rack.setText("Magnetic Rack")

        self.layout_device_menu_bar.addWidget(self.button_devices_magnetic_rack)

        self.button_devices_pipette = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_pipette)
        self.button_devices_pipette.setObjectName("button_devices_pipette")
        self.button_devices_pipette.setMinimumSize(QSize(0, 50))
        self.button_devices_pipette.setText("Pipette")

        self.layout_device_menu_bar.addWidget(self.button_devices_pipette)

        self.button_devices_storage_device = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_storage_device)
        self.button_devices_storage_device.setObjectName(
            "button_devices_storage_device",
        )
        self.button_devices_storage_device.setMinimumSize(QSize(0, 50))
        self.button_devices_storage_device.setText("Storage Device")

        self.layout_device_menu_bar.addWidget(self.button_devices_storage_device)

        self.button_devices_tip = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_tip)
        self.button_devices_tip.setObjectName("button_devices_tip")
        self.button_devices_tip.setMinimumSize(QSize(0, 50))
        self.button_devices_tip.setText("Tip")

        self.layout_device_menu_bar.addWidget(self.button_devices_tip)

        self.button_devices_transport = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_transport)
        self.button_devices_transport.setObjectName("button_devices_transport")
        self.button_devices_transport.setMinimumSize(QSize(0, 50))
        self.button_devices_transport.setText("Transport")

        self.layout_device_menu_bar.addWidget(self.button_devices_transport)

        self.button_devices_vacuum = QPushButton(self.scroll_area_devices_menu_bar)
        self.group_devices_menu_bar.addButton(self.button_devices_vacuum)
        self.button_devices_vacuum.setObjectName("button_devices_vacuum")
        self.button_devices_vacuum.setMinimumSize(QSize(0, 50))
        self.button_devices_vacuum.setText("Vacuum")

        self.layout_device_menu_bar.addWidget(self.button_devices_vacuum)

        self.button_devices_volume_measure = QPushButton(
            self.scroll_area_devices_menu_bar,
        )
        self.group_devices_menu_bar.addButton(self.button_devices_volume_measure)
        self.button_devices_volume_measure.setObjectName(
            "button_devices_volume_measure",
        )
        self.button_devices_volume_measure.setMinimumSize(QSize(0, 50))
        self.button_devices_volume_measure.setText("Volume Measure")

        self.layout_device_menu_bar.addWidget(self.button_devices_volume_measure)

        self.verticalLayout.addLayout(self.layout_device_menu_bar)

        self.scrollArea.setWidget(self.scroll_area_devices_menu_bar)
        self.pages_main.addWidget(self.page_main_devices)
        self.page_main_notifications_shortcut = QWidget()
        self.page_main_notifications_shortcut.setObjectName(
            "page_main_notifications_shortcut",
        )
        self.label_4 = QLabel(self.page_main_notifications_shortcut)
        self.label_4.setObjectName("label_4")
        self.label_4.setGeometry(QRect(150, 260, 49, 16))
        self.pages_main.addWidget(self.page_main_notifications_shortcut)
        self.page_main_deck_loading_shortcut = QWidget()
        self.page_main_deck_loading_shortcut.setObjectName(
            "page_main_deck_loading_shortcut",
        )
        self.label_5 = QLabel(self.page_main_deck_loading_shortcut)
        self.label_5.setObjectName("label_5")
        self.label_5.setGeometry(QRect(250, 180, 49, 16))
        self.pages_main.addWidget(self.page_main_deck_loading_shortcut)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.button_main_method_tools.clicked.connect(
            MainWindow.button_main_menu_bar_method_tools_clicked,
        )
        self.button_main_devices.clicked.connect(
            MainWindow.button_main_menu_bar_devices_clicked,
        )
        self.button_main_notifications_shortcut.clicked.connect(
            MainWindow.button_main_menu_bar_notifications_shortcut_clicked,
        )
        self.button_main_deck_loading_shortcut.clicked.connect(
            MainWindow.button_main_menu_bar_deck_loading_shortcut_clicked,
        )
        self.button_main_home.clicked.connect(
            MainWindow.button_main_menu_bar_home_clicked,
        )

        self.pages_main.setCurrentIndex(0)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowFilePath("")
        self.label_home_log_header.setText(
            QCoreApplication.translate(
                "MainWindow",
                "Automation Bare Necessities Trace",
                None,
            ),
        )
        self.label_4.setText(
            QCoreApplication.translate("MainWindow", "notifications", None),
        )
        self.label_5.setText(
            QCoreApplication.translate("MainWindow", "deck loading", None),
        )

    # retranslateUi
