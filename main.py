import sys
import re
from bs4 import BeautifulSoup
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QFileDialog, QMessageBox

card = "automation.html"

class HTMLUpdaterApp(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        # Layout
        layout = QVBoxLayout()

        # Name label and input
        self.label_name = QLabel("Enter your name and surname:")
        self.label_name.setStyleSheet("font-family: Arial; font-size: 16px;")
        layout.addWidget(self.label_name)
        self.entry_name = QLineEdit()
        self.entry_name.setStyleSheet("font-family: Arial; font-size: 14px;")
        layout.addWidget(self.entry_name)

        # URL label and input
        self.label_url = QLabel("Enter the new URL for the image:")
        self.label_url.setStyleSheet("font-family: Arial; font-size: 16px;")
        layout.addWidget(self.label_url)
        self.entry_url = QLineEdit()
        self.entry_url.setStyleSheet("font-family: Arial; font-size: 14px;")
        layout.addWidget(self.entry_url)

        # Submit button
        self.submit_button = QPushButton("Submit")
        self.submit_button.setStyleSheet("font-family: Arial; font-size: 16px; background-color: #add8e6;")
        self.submit_button.clicked.connect(self.submit)
        layout.addWidget(self.submit_button)

        # Set layout and window size
        self.setLayout(layout)
        self.setWindowTitle("HTML Updater")
        self.resize(400, 200)  # Set initial window size

    def get_valid_name(self, name_surname):
        if not name_surname.strip():
            raise ValueError("Name and surname cannot be empty.")

        return name_surname

    def get_valid_url(self, url):
        if not url.strip():
            raise ValueError("URL cannot be empty.")
        return url

    def update_html(self, name_surname, url, save_path):
        with open(card, 'r', encoding='utf-8') as html_file:
            content = html_file.read()

        soup = BeautifulSoup(content, 'html.parser')
        tags = soup.find("img")

        tags['alt'] = name_surname
        tags['src'] = url

        updated_content = soup.prettify()

        with open(save_path, 'w', encoding='utf-8') as html_file:
            html_file.write(updated_content)

    def submit(self):
        try:
            name_surname = self.get_valid_name(self.entry_name.text())
            url = self.get_valid_url(self.entry_url.text())
            save_path, _ = QFileDialog.getSaveFileName(self, "Save File", "", "HTML Files (*.html)")
            if not save_path:
                return
            self.update_html(name_surname, url, save_path)
            QMessageBox.information(self, "Success", "HTML file updated and saved successfully.")
        except Exception as e:
            QMessageBox.critical(self, "Error", str(e))
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ex = HTMLUpdaterApp()
    ex.show()
    sys.exit(app.exec_())
