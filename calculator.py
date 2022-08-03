from PyQt5.QtWidgets import QLabel, QPushButton, QGridLayout, QApplication, QMainWindow, \
    QWidget, QVBoxLayout, QMenu, QMenuBar
import sys


class my_calculator(QWidget):
    def __init__(self, application):
        super().__init__()
        self.stack = 0
        self.string_holder = ""
        self.setWindowTitle("Calculator made by Barış Giray Akman")
        self.setGeometry(200, 200, 300, 300)
        self.show()
        self.application = application
        self.set_calculator()
        self.set_events()
        self.application.exec_()

    def events(self):
        if self.sender().text() == "CLEAR":
            self.string_holder = ""
            self.label.setText(self.string_holder)
        elif self.sender().text() == "=":
            self.string_holder = str(calculator(self.string_holder))
            self.label.setText(str(self.string_holder))

        elif self.sender().text() == "DEL":
            if len(self.string_holder) == 1:
                self.string_holder = ""
                self.label.setText(self.string_holder)
            else:
                self.string_holder = self.string_holder[0:len(self.string_holder) - 1]
                self.label.setText(self.string_holder)
        elif self.sender().text() in "+-x/":
            if len(self.string_holder) != 0 and self.string_holder[len(self.string_holder) - 1] in "0123456789)":
                self.string_holder += self.sender().text()
                self.label.setText(self.string_holder)
        elif self.sender().text() == "(":
            if len(self.string_holder) == 0:
                self.string_holder += self.sender().text()
                self.label.setText(self.string_holder)
                self.stack += 1
            elif len(self.string_holder) != 0 and self.string_holder[len(self.string_holder) - 1] in "+-x/":
                self.string_holder += self.sender().text()
                self.label.setText(self.string_holder)
                self.stack += 1
        elif self.sender().text() == ")":
            if len(self.string_holder) != 0 and self.string_holder[len(self.string_holder) - 1] in "0123456789)" \
                    and len(self.string_holder) != 1 and self.stack != 0:
                self.string_holder += self.sender().text()
                self.label.setText(self.string_holder)
                self.stack -= 1
        elif self.sender().text() == ".":
            if len(self.string_holder) != 0 and self.string_holder[len(self.string_holder) - 1] in "0123456789":
                self.string_holder += self.sender().text()
                self.label.setText(self.string_holder)
        else:
            if len(self.string_holder) == 1 and self.string_holder == "0":
                self.string_holder = self.sender().text()
                self.label.setText(self.string_holder)

            elif len(self.string_holder) >= 2 and \
                    self.string_holder[-2] in ["+", "-", "x", "/"] and self.string_holder[-1] == "0":
                self.string_holder = self.string_holder[0:len(self.string_holder) - 1] + self.sender().text()
                self.label.setText(self.string_holder)
            else:
                self.string_holder += self.sender().text()
                self.label.setText(self.string_holder)

    def set_calculator(self):
        self.vertical_layout = QVBoxLayout()
        self.second_vertical_layout = QVBoxLayout()
        self.label = QLabel()
        self.label.setStyleSheet("background-color:white;")
        self.label.setFixedSize(260, 40)
        self.box_layout = QGridLayout()
        self.first_button = QPushButton("0")
        self.first_button.setFixedSize(50, 50)
        self.second_button = QPushButton("1")
        self.second_button.setFixedSize(50, 50)
        self.third_button = QPushButton("2")
        self.third_button.setFixedSize(50, 50)
        self.fourth_button = QPushButton("3")
        self.fourth_button.setFixedSize(50, 50)
        self.fifth_button = QPushButton("4")
        self.fifth_button.setFixedSize(50, 50)
        self.sixth_button = QPushButton("5")
        self.sixth_button.setFixedSize(50, 50)
        self.seventh_button = QPushButton("6")
        self.seventh_button.setFixedSize(50, 50)
        self.eightth_button = QPushButton("7")
        self.eightth_button.setFixedSize(50, 50)
        self.nineth_button = QPushButton("8")
        self.nineth_button.setFixedSize(50, 50)
        self.tenth_button = QPushButton("9")
        self.tenth_button.setFixedSize(50, 50)
        self.eleventh_button = QPushButton("(")
        self.eleventh_button.setFixedSize(50, 50)
        self.twelveth_button = QPushButton(")")
        self.twelveth_button.setFixedSize(50, 50)
        self.thirteenth_button = QPushButton("DEL")
        self.thirteenth_button.setFixedSize(50, 50)
        self.fourteeenth_button = QPushButton("+")
        self.fourteeenth_button.setFixedSize(50, 50)
        self.fifteenth_button = QPushButton("-")
        self.fifteenth_button.setFixedSize(50, 50)
        self.sixteenth_button = QPushButton("x")
        self.sixteenth_button.setFixedSize(50, 50)
        self.seventeenth_button = QPushButton("/")
        self.seventeenth_button.setFixedSize(50, 50)
        self.eighteenth_button = QPushButton(".")
        self.eighteenth_button.setFixedSize(50, 50)
        self.twelveth_button.setFixedSize(50, 50)
        self.nineteenth_button = QPushButton("=")
        self.nineteenth_button.setFixedSize(50, 50)
        self.twentieenth_button = QPushButton("CLEAR")
        self.twentieenth_button.setFixedSize(50, 50)
        self.box_layout.addWidget(self.first_button, 0, 0)
        self.box_layout.addWidget(self.second_button, 0, 1)
        self.box_layout.addWidget(self.third_button, 0, 2)
        self.box_layout.addWidget(self.fourth_button, 1, 0)
        self.box_layout.addWidget(self.fifth_button, 1, 1)
        self.box_layout.addWidget(self.sixth_button, 1, 2)
        self.box_layout.addWidget(self.seventh_button, 2, 0)
        self.box_layout.addWidget(self.eightth_button, 2, 1)
        self.box_layout.addWidget(self.nineth_button, 2, 2)
        self.box_layout.addWidget(self.tenth_button, 3, 0)
        self.box_layout.addWidget(self.eleventh_button, 3, 1)
        self.box_layout.addWidget(self.twelveth_button, 3, 2)
        self.box_layout.addWidget(self.thirteenth_button, 4, 0)
        self.box_layout.addWidget(self.fourteeenth_button, 4, 1)
        self.box_layout.addWidget(self.fifteenth_button, 4, 2)
        self.box_layout.addWidget(self.sixteenth_button, 5, 0)
        self.box_layout.addWidget(self.seventeenth_button, 5, 1)
        self.box_layout.addWidget(self.eighteenth_button, 5, 2)
        self.box_layout.addWidget(self.nineteenth_button, 6, 0)
        self.box_layout.addWidget(self.twentieenth_button, 6, 1)
        self.second_vertical_layout.addWidget(self.label)
        self.vertical_layout.addLayout(self.second_vertical_layout)
        self.vertical_layout.addLayout(self.box_layout)
        self.setLayout(self.vertical_layout)

    def set_events(self):
        self.first_button.clicked.connect(self.events)
        self.second_button.clicked.connect(self.events)
        self.third_button.clicked.connect(self.events)
        self.fourth_button.clicked.connect(self.events)
        self.fifth_button.clicked.connect(self.events)
        self.sixth_button.clicked.connect(self.events)
        self.seventh_button.clicked.connect(self.events)
        self.eightth_button.clicked.connect(self.events)
        self.nineth_button.clicked.connect(self.events)
        self.tenth_button.clicked.connect(self.events)
        self.eleventh_button.clicked.connect(self.events)
        self.twelveth_button.clicked.connect(self.events)
        self.thirteenth_button.clicked.connect(self.events)
        self.fourteeenth_button.clicked.connect(self.events)
        self.fifteenth_button.clicked.connect(self.events)
        self.sixteenth_button.clicked.connect(self.events)
        self.seventeenth_button.clicked.connect(self.events)
        self.eighteenth_button.clicked.connect(self.events)
        self.nineteenth_button.clicked.connect(self.events)
        self.twentieenth_button.clicked.connect(self.events)


def calculator(my_string: "str") -> str:
    operands, operators, number, priority_operation, stack, matcher = [], [], "", "", 0, 0
    for y in range(len(my_string)):
        if my_string[y] == "(":
            if stack > 0:
                priority_operation += my_string[y]
            matcher += 1
            stack += 1
        elif stack > 0 and my_string[y] != ")":
            priority_operation += my_string[y]
        elif my_string[y] == ")":
            matcher -= 1
            if matcher == 0:
                operands.append(calculator(priority_operation))
                priority_operation = ""
                stack = 0
            else:
                priority_operation += my_string[y]
        elif my_string[y] in "0123456789" or my_string[y] == ".":
            if (y + 1 <= len(my_string) - 1 and my_string[y + 1] in "0123456789") or \
                    (y + 1 <= len(my_string) - 1 and my_string[y + 1] == "."):
                number = number + my_string[y]
            else:
                number = number + my_string[y]
                if "." in number:
                    operands.append(float(number))
                else:
                    operands.append(int(number))
                number = ""
        else:
            operators.append(my_string[y])
    x = 0
    while x <= len(operators) - 1:
        if operators[x] == "+":
            if x + 1 <= len(operators) - 1 and operators[x + 1] not in ["x", "/", "*"]:
                operands[x] = operands[x] + operands[x + 1]
                operators.remove(operators[x])
                operands.remove(operands[x + 1])
            else:
                x += 1
        elif operators[x] == "-":
            if x + 1 <= len(operators) - 1 and operators[x + 1] not in ["x", "/", "*"]:
                operands[x] = operands[x] - operands[x + 1]
                operators.remove(operators[x])
                operands.remove(operands[x + 1])

            else:
                x += 1
        elif operators[x] == "x" or operators[x] == "*":
            operands[x] = operands[x] * operands[x + 1]
            operands.remove(operands[x + 1])
            operators.remove(operators[x])
        elif operators[x] == "/":
            operands[x] = operands[x] / operands[x + 1]
            operands.remove(operands[x + 1])
            operators.remove(operators[x])
        else:
            return "Calculator can't realize that process. Unknown marks detected."

    for z in range(len(operators)):
        if operators[z] == "+":
            operands[0] = operands[0] + operands[z + 1]
        else:
            operands[0] = operands[0] - operands[z + 1]

    return operands[0]


def main():
    application = QApplication(sys.argv)
    window = my_calculator(application)

main()
