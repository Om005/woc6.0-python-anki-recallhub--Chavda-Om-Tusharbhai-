import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QLineEdit, QPushButton, QGridLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calculator")

        # Create central widget and layout
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout(central_widget)

        # Create entry widget for input
        self.entry = QLineEdit()
        self.entry.setFixedHeight(50)
        font = QFont("Arial", 20)
        self.entry.setFont(font)
        self.entry.setAlignment(Qt.AlignRight)
        layout.addWidget(self.entry)

        # Create buttons for digits and operations
        buttons = [
            ('7', 0, 0), ('8', 0, 1), ('9', 0, 2), ('/', 0, 3),
            ('4', 1, 0), ('5', 1, 1), ('6', 1, 2), ('*', 1, 3),
            ('1', 2, 0), ('2', 2, 1), ('3', 2, 2), ('-', 2, 3),
            ('C', 3, 0), ('0', 3, 1), ('=', 3, 2), ('+', 3, 3)
        ]

        grid_layout = QGridLayout()
        for (text, row, column) in buttons:
            button = QPushButton(text)
            button.setFixedSize(50, 50)
            button.clicked.connect(lambda _, t=text: self.on_button_click(t))
            grid_layout.addWidget(button, row, column)

        layout.addLayout(grid_layout)

    def on_button_click(self, value):
        if value == 'C':
            self.entry.clear()
        elif value == '=':
            try:
                result = eval(self.entry.text())
                self.entry.setText(str(result))
            except Exception as e:
                self.entry.setText("Error")
        else:
            self.entry.insert(value)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
