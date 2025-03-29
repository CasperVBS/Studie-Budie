from PySide6.QtWidgets import *
import sys

app = QApplication(sys.argv)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Study-budy")

        self.button = QPushButton("Darkmode")
        self.button.setCheckable(True)
        self.button.clicked.connect(self.button_pressed)
        # Set the central widget of the Window.
        self.setCentralWidget(self.button)
        self.label = QLabel()
        self.input = QLineEdit()
        self.input.textChanged.connect(self.label.setText)

        layout = QVBoxLayout()
        layout.addWidget(self.input)
        layout.addWidget(self.label)
        layout.addWidget(self.button)

        container = QWidget()
        container.setLayout(layout)

        self.setCentralWidget(container)
    def button_pressed(self,cheked):
        print("pressed",cheked)
        self.button_cheked = cheked
        self.button.setEnabled(False)

window = MainWindow()
window.show()
app.exec()