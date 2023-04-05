from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.uic import loadUi
from PyQt5.QtWidgets import QStackedWidget


class WelcomePage(QtWidgets.QDialog):
    def __init__(self):
        super(WelcomePage, self).__init__()
        loadUi('mad_welcome.ui',self)
        self.connectEvents()
    def connectEvents(self):
        self.madlib1btn.clicked.connect(self.gotomadone)
        self.madlib2btn.clicked.connect(self.gotomadtwo)


    def gotomadone(self):
        mad1 = Mad1()
        widget.addWidget(mad1)
        widget.setCurrentIndex(widget.currentIndex() + 1)
        widget.setGeometry(300, 60, 699, 637)
        widget.setFixedWidth(699)
        widget.setFixedHeight(637)
        widget.setWindowTitle("MadLib Game in Python")

    def gotomadtwo(self):
        madtwo = Mad2()
        widget.addWidget(madtwo)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setWindowTitle("Mad Lib Game in Python")
        widget.setGeometry(300,50,698,640)
        widget.setFixedWidth(698)
        widget.setFixedHeight(640)




class Mad1(QtWidgets.QDialog):
    def __init__(self):
        super(Mad1, self).__init__()
        loadUi('mad-p2.ui', self)
        self.connectEvents()

    def connectEvents(self):

        self.madlibbtn.clicked.connect(self.generate_madlib)
        self.clearbtn.clicked.connect(self.clear)
        self.clearallbtn.clicked.connect(self.clearAll)
        self.backbtn.clicked.connect(self.goback)

    def generate_madlib(self):
            my_lib = 'Hi! My name is [name1] and I have a secret ' \
                     'to share with you. I\'m a normal child by day, and a ' \
                     '[Noun/Thing1] by night. Only you and my best friend [name2] ' \
                     'knows my secret. You may be wondering how this happened? Well, ' \
                     'one night I was [Verb/Action1] at home, and then BOOM!. The lights ' \
                     'went out and [name3] showed up. He/she said in a booming voice, because your favorite ' \
                     'color is [Color] you have been chosen to be a [Noun/Thing2]. ' \
                     'My mission is to save the people of [City/State] by doing my favorite things: ' \
                     '[Verb/Action2], [Verb/Action3], and [Verb/Action4]. This may sound easy, but it is no walk in the park. ' \
                     'It requires hard work and [Noun/Thing3]. My weakness is eating [Food]. ' \
                     'They are gross!!. Keep that away from me! I save the world every night. But when ' \
                     'I wake up in the morning, I go back to my normal life at [School]!'

            #     Filling the blanks into the madlib
            my_lib = my_lib.replace('[name1]', self.name1.text())
            my_lib = my_lib.replace('[Noun/Thing1]', self.noun1.text())
            my_lib = my_lib.replace('[name2]', self.name2.text())
            my_lib = my_lib.replace('[Verb/Action1]', self.verb1.text())
            my_lib = my_lib.replace('[Noun/Thing2]', self.noun2.text())
            my_lib = my_lib.replace('[name3]', self.name3.text())
            my_lib = my_lib.replace('[Color]', self.color.text())
            my_lib = my_lib.replace('[City/State]', self.city.text())
            my_lib = my_lib.replace('[Verb/Action2]', self.verb2.text())
            my_lib = my_lib.replace('[Verb/Action3]', self.verb3.text())
            my_lib = my_lib.replace('[Verb/Action4]', self.verb4.text())
            my_lib = my_lib.replace('[Noun/Thing3]', self.noun3.text())
            my_lib = my_lib.replace('[Food]', self.food.text())
            my_lib = my_lib.replace('[School]', self.school.text())

            #Check the condition if not empty

            self.textEdit.setPlainText(my_lib)
            self.textEdit.setStyleSheet('font-weight:bold;color:red;'
                                'font-size:18px')


    def clear(self):
        self.name1.setText("")
        self.name2.setText("")
        self.name3.setText("")
        self.noun1.setText("")
        self.noun2.setText("")
        self.noun3.setText("")
        self.verb1.setText("")
        self.verb2.setText("")
        self.verb3.setText("")
        self.verb4.setText("")
        self.city.setText("")
        self.food.setText("")
        self.school.setText("")

    def clearAll(self):
            self.clear()
            self.textEdit.setText("")


    def goback(self):
        welcome = WelcomePage()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setGeometry(500, 200, 450, 350)
        widget.setFixedWidth(450)
        widget.setFixedHeight(350)
        widget.setWindowTitle("MadLib Game in Python")

class Mad2(QtWidgets.QDialog):
    def __init__(self):
        super(Mad2, self).__init__()
        loadUi('mad-p3.ui',self)
        self.connectEvents()

    def connectEvents(self):
        self.backbtn.clicked.connect(self.goback)

    def goback(self):
        welcome = WelcomePage()
        widget.addWidget(welcome)
        widget.setCurrentIndex(widget.currentIndex()+1)
        widget.setGeometry(500, 200, 450, 350)
        widget.setFixedWidth(450)
        widget.setFixedHeight(350)
        widget.setWindowTitle("MadLib Game in Python")

app = QtWidgets.QApplication([])
game = WelcomePage()
widget = QStackedWidget()
widget.addWidget(game)
widget.setGeometry(500,200,450,350)
widget.setFixedWidth(450)
widget.setFixedHeight(350)
widget.setWindowTitle("MadLib Game in Python")
widget.show()
app.exec_()
