import sys
from PySide6.QtWidgets import QApplication
from pypdftools.gui.main_window import MainWindow
from pypdftools.gui.theme import ThemeManager


def main():
    app = QApplication(sys.argv)
    app.setApplicationName("PyPDF Tools")

    theme_manager = ThemeManager()
    theme_manager.apply(app)

    window = MainWindow(theme_manager)
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
