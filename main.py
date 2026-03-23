import sys
from pathlib import Path

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from pypdftools.gui.main_window import MainWindow
from pypdftools.gui.theme import ThemeManager


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PyPDF Tools")

    # Set app icon
    icon_paths = [
        Path(__file__).parent / "pypdftools" / "resources" / "icons" / "app_icon.png",
        Path(sys._MEIPASS) / "pypdftools" / "resources" / "icons" / "app_icon.png"
        if hasattr(sys, "_MEIPASS") else None,
    ]
    for p in icon_paths:
        if p and p.exists():
            app.setWindowIcon(QIcon(str(p)))
            break

    theme_manager = ThemeManager()
    theme_manager.apply(app)

    window = MainWindow(theme_manager)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
