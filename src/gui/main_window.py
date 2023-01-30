from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon
import logging


class MainWindow(QWidget):
    """
    This is the main window of application.
    """

    def __init__(self) -> None:
        super(MainWindow, self).__init__()
        self.__configure_window()
        self.__load_styles()
        self.__add_widgets()

    def __configure_window(self) -> None:
        self.setWindowTitle("Wavy")
        self.setMinimumSize(500, 400)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)

        self.widget_layout = QHBoxLayout()
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(0)
        self.setLayout(self.widget_layout)

    def __load_styles(self) -> None:
        try:
            with open('static/style/main_window.css', 'r') as css_file:
                self.setStyleSheet(css_file.read())
                logging.info("Stylesheet for MainWindow is loaded successfully.")
        except (IOError, FileNotFoundError, OSError) as error:
            logging.error("Stylesheet for MainWindow failed to be loaded!")
            logging.error(error)

    def __add_widgets(self):
        self.widget_layout.addWidget(_LeftSidebar())
        self.widget_layout.addWidget(_CenterPanel())
        self.widget_layout.addWidget(_RightSidebar())


class _LeftSidebar(QWidget):
    """
    Left sidebar of the main window contains a few simple icons like home, playlists, settings, and etc.
    """

    def __init__(self) -> None:
        super(_LeftSidebar, self).__init__()
        self.__configure()
        self.__add_widgets()

    def __configure(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("left_sidebar")
        self.widget_layout = QVBoxLayout()
        self.setLayout(self.widget_layout)

    def __add_widgets(self) -> None:
        self.widget_layout.addStretch()

        home_button = QPushButton()
        home_button.setObjectName("left_sidebar_button")
        home_button.setIcon(QIcon("static/image/icons/home.svg"))
        self.widget_layout.addWidget(home_button)

        search_button = QPushButton()
        search_button.setObjectName("left_sidebar_button")
        search_button.setIcon(QIcon("static/image/icons/search.svg"))
        self.widget_layout.addWidget(search_button)

        playlists_button = QPushButton()
        playlists_button.setObjectName("left_sidebar_button")
        playlists_button.setIcon(QIcon("static/image/icons/playlists.svg"))
        self.widget_layout.addWidget(playlists_button)

        settings_button = QPushButton()
        settings_button.setObjectName("left_sidebar_button")
        settings_button.setIcon(QIcon("static/image/icons/settings.svg"))
        self.widget_layout.addWidget(settings_button)

        self.widget_layout.addStretch()


class _CenterPanel(QWidget):

    def __init__(self) -> None:
        super(_CenterPanel, self).__init__()
        self.__configure()
        # self.__add_widgets()

    def __configure(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("center_panel")
        self.widget_layout = QVBoxLayout()
        self.setLayout(self.widget_layout)


class _RightSidebar(QWidget):

    def __init__(self) -> None:
        super(_RightSidebar, self).__init__()
        self.__configure()

    def __configure(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("right_sidebar")
        self.widget_layout = QVBoxLayout()
        self.setLayout(self.widget_layout)
