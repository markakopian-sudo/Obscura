import sys
from PyQt6.QtCore import QUrl
from PyQt6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                             QHBoxLayout, QLineEdit, QPushButton, QWidget)
from PyQt6.QtWebEngineCore import QWebEnginePage
from PyQt6.QtWebEngineWidgets import QWebEngineView

class SimpleBrowser(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My Custom Browser")
        self.setGeometry(100, 100, 1024, 768)

        # Main layout container
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout()
        central_widget.setLayout(main_layout)

        # Navigation bar layout
        nav_layout = QHBoxLayout()
        main_layout.addLayout(nav_layout)

        # Navigation buttons
        self.back_btn = QPushButton("←")
        self.back_btn.clicked.connect(self.browser_back)
        nav_layout.addWidget(self.back_btn)

        self.forward_btn = QPushButton("→")
        self.forward_btn.clicked.connect(self.browser_forward)
        nav_layout.addWidget(self.forward_btn)

        self.reload_btn = QPushButton("⟳")
        self.reload_btn.clicked.connect(self.browser_reload)
        nav_layout.addWidget(self.reload_btn)

        # Address bar
        self.address_bar = QLineEdit()
        self.address_bar.returnPressed.connect(self.load_url)
        nav_layout.addWidget(self.address_bar)

        # Web View (The area where web pages render)
        self.web_view = QWebEngineView()
        self.web_view.setUrl(QUrl("https://www.google.com"))
        self.web_view.urlChanged.connect(self.update_address_bar)
        main_layout.addWidget(self.web_view)

    def load_url(self):
        text = self.address_bar.text()
        # Add https:// if the user forgot it
        if not text.startswith("http://") and not text.startswith("https://"):
            text = "https://" + text
        self.web_view.setUrl(QUrl(text))

    def update_address_bar(self, url):
        self.address_bar.setText(url.toString())

    def browser_back(self):
        self.web_view.back()

    def browser_forward(self):
        self.web_view.forward()

    def browser_reload(self):
        self.web_view.reload()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    browser = SimpleBrowser()
    browser.show()
    sys.exit(app.exec())
