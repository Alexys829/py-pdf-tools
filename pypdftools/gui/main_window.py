import os
import subprocess
import sys

from PySide6.QtCore import Qt, QSize
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QVBoxLayout, QHBoxLayout,
    QPushButton, QLabel, QStatusBar, QMenuBar, QMessageBox,
    QTabWidget,
)

from pypdftools.gui.theme import ThemeManager
from pypdftools.gui.pdf_tools import (
    _PageEditorTab, _MergeTab, _SplitTab, _RotateTab,
    _ExtractImagesTab, _ImagesToPdfTab, _CompressTab,
    _PasswordTab, _PageNumbersTab,
)


class MainWindow(QMainWindow):
    def __init__(self, theme_manager: ThemeManager):
        super().__init__()
        self._theme_manager = theme_manager

        self.setWindowTitle("PyPDF Tools")
        self.setMinimumSize(850, 650)

        self._setup_menu_bar()
        self._setup_ui()
        self._setup_status_bar()

    def _setup_menu_bar(self):
        menu_bar = QMenuBar()
        self.setMenuBar(menu_bar)

        file_menu = menu_bar.addMenu("File")
        file_menu.addAction("Watermark...", self._open_watermark)
        file_menu.addSeparator()
        file_menu.addAction("Settings...", self._open_settings)
        file_menu.addSeparator()
        file_menu.addAction("Exit", self.close)

        help_menu = menu_bar.addMenu("Help")
        help_menu.addAction("About...", self._show_about)

    def _setup_ui(self):
        central = QWidget()
        self.setCentralWidget(central)
        layout = QVBoxLayout(central)
        layout.setContentsMargins(16, 16, 16, 16)
        layout.setSpacing(12)

        title = QLabel("PyPDF Tools")
        title.setObjectName("titleLabel")
        layout.addWidget(title)

        tabs = QTabWidget()
        tabs.addTab(_PageEditorTab(), "Editor")
        tabs.addTab(_MergeTab(), "Merge")
        tabs.addTab(_SplitTab(), "Split")
        tabs.addTab(_RotateTab(), "Rotate")
        tabs.addTab(_ExtractImagesTab(), "Images")
        tabs.addTab(_ImagesToPdfTab(), "IMG to PDF")
        tabs.addTab(_CompressTab(), "Compress")
        tabs.addTab(_PasswordTab(), "Password")
        tabs.addTab(_PageNumbersTab(), "Page Numbers")
        layout.addWidget(tabs)

    def _setup_status_bar(self):
        self._status_bar = QStatusBar()
        self.setStatusBar(self._status_bar)
        self._status_bar.showMessage("Ready")

    def _open_watermark(self):
        from pypdftools.gui.watermark_dialog import WatermarkDialog
        dialog = WatermarkDialog(self)
        dialog.exec()

    def _open_settings(self):
        from PySide6.QtWidgets import QDialog, QComboBox, QGroupBox
        dialog = QDialog(self)
        dialog.setWindowTitle("Settings")
        dialog.setMinimumWidth(350)
        layout = QVBoxLayout(dialog)

        theme_group = QGroupBox("Appearance")
        theme_layout = QHBoxLayout(theme_group)
        theme_layout.addWidget(QLabel("Theme:"))
        combo = QComboBox()
        combo.addItems(["dark", "light"])
        combo.setCurrentText(self._theme_manager.current)
        theme_layout.addWidget(combo)
        layout.addWidget(theme_group)

        btn_layout = QHBoxLayout()
        btn_layout.addStretch()
        ok_btn = QPushButton("OK")
        ok_btn.clicked.connect(lambda: self._apply_theme(combo.currentText(), dialog))
        cancel_btn = QPushButton("Cancel")
        cancel_btn.clicked.connect(dialog.reject)
        btn_layout.addWidget(cancel_btn)
        btn_layout.addWidget(ok_btn)
        layout.addLayout(btn_layout)

        dialog.exec()

    def _apply_theme(self, theme, dialog):
        from PySide6.QtWidgets import QApplication
        self._theme_manager.set_theme(theme, QApplication.instance())
        dialog.accept()

    def _show_about(self):
        from pypdftools import __version__
        QMessageBox.about(
            self,
            "About PyPDF Tools",
            f"<h3>PyPDF Tools v{__version__}</h3>"
            f"<p>Universal PDF toolkit.</p>"
            f"<p>9 tools: page editor, merge, split, rotate, extract images, "
            f"images to PDF, compress, password, page numbers.</p>",
        )
