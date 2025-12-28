from PyQt5 import uic, QtWidgets, QtGui, QtCore
import sys

from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLineEdit, QPushButton

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()
        
        # Erstelle eine Liste von QLineEdit-Objekten
        self.line_edits = [QLineEdit(self) for _ in range(1, 10)]
        
        # Layout für die QLineEdit-Objekte
        layout = QVBoxLayout()
        for line_edit in self.line_edits:
            print(line_edit.objectName())
            layout.addWidget(line_edit)
        print(self.line_edits[2].objectName())
        # Button zum Auslesen der QLineEdit-Objekte
        self.button = QPushButton("Auslesen", self)
        self.button.clicked.connect(self.read_line_edits)
        layout.addWidget(self.button)
        
        self.setLayout(layout)
    
    def read_line_edits(self):
        # Iteriere über die QLineEdit-Objekte und lese die Texte aus
        for i, line_edit in enumerate(self.line_edits, start=1):
            text = line_edit.text()
            print(f"QLineEdit {i}: {text}")

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()