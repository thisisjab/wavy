from PyQt6.QtGui import QFontDatabase
import logging
import os
import pathlib


def load_fonts(fonts_path: str = './static/font'):
    """
    Loads fonts into PyQt font database so that the entire app has access to all fonts
    """
    result = []
    for root, directory, files in os.walk(os.path.join(os.getcwd(), fonts_path)):
        for file in files:
            if pathlib.Path(file).suffix == '.ttf':
                font_id = QFontDatabase.addApplicationFont(os.path.join(root, file))
                if font_id != -1:
                    result.append((font_id, file))
                else:
                    logging.error("Font not loaded: " + os.path.join(root, file))

    logging.info("Fonts loaded: " + str(result))
