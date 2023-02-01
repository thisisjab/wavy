from PyQt6.QtWidgets import QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QSizePolicy, QSplitter, QScrollBar
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QIcon, QPixmap
from .font_loader import load_fonts
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
        load_fonts()

    def __configure_window(self) -> None:
        self.setWindowTitle("Wavy")
        self.setMinimumSize(750, 500)
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
        self.__add_widgets()

    def __configure(self) -> None:
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("center_panel")
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(0)
        self.setLayout(self.widget_layout)

    def __add_widgets(self) -> None:
        self.widget_layout.addWidget(_CenterPanelSplitter())


class _CenterPanelSplitter(QSplitter):

    def __init__(self) -> None:
        super(_CenterPanelSplitter, self).__init__()

        self.__add_widgets()

    def __add_widgets(self) -> None:
        self.addWidget(_SplitterMainPane())
        self.addWidget(_SplitterMusicPane())


class _SplitterMainPane(QWidget):

    def __init__(self) -> None:
        super(_SplitterMainPane, self).__init__()

        self.__configure()

    def __configure(self) -> None:
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("splitter_main_pane")
        self.widget_layout = QHBoxLayout()
        self.setLayout(self.widget_layout)


class _SplitterMusicPane(QWidget):

    def __init__(self) -> None:
        super(_SplitterMusicPane, self).__init__()

        self.__configure()
        self.__add_widgets()

    def __configure(self) -> None:
        self.setFixedWidth(300)
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("splitter_music_pane")
        self.widget_layout = QVBoxLayout()
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(0)
        self.widget_layout.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.setLayout(self.widget_layout)

    def __add_widgets(self) -> None:
        # This is an empty label only to add margin from top
        margin_label = QLabel()
        margin_label.setContentsMargins(0,0,0,12)
        self.widget_layout.addWidget(margin_label)

        self.music_thumbnail_label = QLabel()
        self.music_thumbnail_label.setFixedSize(250, 250)
        self.music_thumbnail_label.setPixmap(QPixmap("static/image/app/album.png"))
        self.music_thumbnail_label.setScaledContents(True)
        self.music_thumbnail_label.setObjectName("music_pane_music_thumbnail_label")
        self.widget_layout.addWidget(self.music_thumbnail_label)

        self.music_title = QLabel("Hey you")
        self.music_title.setWordWrap(True)
        self.music_title.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.music_title.setObjectName("music_pane_music_title")
        self.widget_layout.addWidget(self.music_title)

        self.music_artist = QLabel("Pink Floyd")
        self.music_artist.setWordWrap(True)
        self.music_artist.setObjectName("music_pane_music_artist")
        self.music_artist.setAlignment(Qt.AlignmentFlag.AlignHCenter)
        self.widget_layout.addWidget(self.music_artist)

        self.music_scrollbar = QScrollBar()
        self.music_scrollbar.setFixedHeight(5)
        self.music_scrollbar.setOrientation(Qt.Orientation.Horizontal)
        self.music_scrollbar.setObjectName("music_pane_music_scroller")
        self.widget_layout.addWidget(self.music_scrollbar)

        self.widget_layout.addWidget(_SplitterMusicPaneButtons())

        self.widget_layout.addStretch()


class _SplitterMusicPaneButtons(QWidget):

    def __init__(self) -> None:
        super(_SplitterMusicPaneButtons, self).__init__()

        self.__configure__()
        self.__add_widgets()

    def __configure__(self) -> None:
        self.setAttribute(Qt.WidgetAttribute.WA_StyledBackground, True)
        self.setAutoFillBackground(True)
        self.setObjectName("splitter_music_pane_buttons")
        self.widget_layout = QHBoxLayout()
        self.widget_layout.setContentsMargins(0, 0, 0, 0)
        self.widget_layout.setSpacing(0)
        self.widget_layout.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.setLayout(self.widget_layout)

    def __add_widgets(self) -> None:
        self.shuffle_button = QPushButton()
        self.shuffle_button.setIcon(QIcon("static/image/icons/shuffle.svg"))
        self.shuffle_button.setObjectName("splitter_music_pane_button")
        self.widget_layout.addWidget(self.shuffle_button)

        self.skip_previous_button = QPushButton()
        self.skip_previous_button.setIcon(QIcon("static/image/icons/skip_previous.svg"))
        self.skip_previous_button.setObjectName("splitter_music_pane_button")
        self.widget_layout.addWidget(self.skip_previous_button)

        self.play_pause_button = QPushButton()
        self.play_pause_button.setIcon(QIcon("static/image/icons/play.svg"))
        self.play_pause_button.setObjectName("splitter_music_pane_button")
        self.widget_layout.addWidget(self.play_pause_button)

        self.stop_button = QPushButton()
        self.stop_button.setIcon(QIcon("static/image/icons/stop.svg"))
        self.stop_button.setObjectName("splitter_music_pane_button")
        self.widget_layout.addWidget(self.stop_button)

        self.skip_next_button = QPushButton()
        self.skip_next_button.setIcon(QIcon("static/image/icons/skip_next.svg"))
        self.skip_next_button.setObjectName("splitter_music_pane_button")
        self.widget_layout.addWidget(self.skip_next_button)

        self.repeat_button = QPushButton()
        self.repeat_button.setIcon(QIcon("static/image/icons/repeat.svg"))
        self.repeat_button.setObjectName("splitter_music_pane_button")
        self.widget_layout.addWidget(self.repeat_button)
