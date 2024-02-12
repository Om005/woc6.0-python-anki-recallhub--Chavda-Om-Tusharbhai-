import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Hello world")

        self.setLayout(qtw.QVBoxLayout())

        # create a label
        my_label = qtw.QLabel("Hello world, what's your name?")

        #change font size of the label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        self.layout().addWidget(my_label)

        # create a entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        self.layout().addWidget(my_entry)

        # create a button
        my_button = qtw.QPushButton("Button", clicked = lambda: press_it())
        self.layout().addWidget(my_button)


        def press_it():
            my_label.setText(f"Hello {my_entry.text()}!!")
            my_entry.setText("")

        self.show()

app = qtw.QApplication([])
mw = MainWindow()

app.exec_()

# import PyQt5.QtWidgets as qtw
# import PyQt5.QtGui as qtg

# class MainWindow(qtw.QWidget):
#     def __init__(self):
#         super().__init__()
#         # title
#         self.setWindowTitle("Combo box")
#         self.setLayout(qtw.QVBoxLayout())

#         #lable
#         my_label = qtw.QLabel("Pick something:")
#         my_label.setFont(qtg.QFont('Helvetica', 18))
#         self.layout().addWidget(my_label)

#         # create a combo box
#         my_combo = qtw.QComboBox(self, editable = True, insertPolicy = qtw.QComboBox.InsertAtTop)
#         # Add item to combo box
#         my_combo.addItem("ok1", "ok")
#         my_combo.addItem("ok2", )
#         my_combo.addItem("ok3", "god")
#         my_combo.addItem("ok4", qtw.QWidget)
#         my_combo.addItems(["1234", "2134", "3756"])
#         self.layout().addWidget(my_combo)

#         #button
#         my_button = qtw.QPushButton("Select", clicked = lambda: press_it())
#         self.layout().addWidget(my_button)

#         def press_it():
#             my_label.setText(f"You picked {my_combo.currentIndex()}!!")
#             my_label.setText(f"You picked {my_combo.currentData()}!!")
#             my_label.setText(f"You picked {my_combo.currentText()}!!")
#         self.show()

# app = qtw.QApplication([])
# mw = MainWindow()

# app.exec_()
