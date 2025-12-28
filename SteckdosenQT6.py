from PyQt6.QtWidgets import *
from PyQt6 import QtCore, QtGui
from PyQt6.QtGui import *
from PyQt6.QtCore import *
from PyQt6 import uic
import sys 
import serial
import configparser as cp
from Einstellungen6 import Ui_Einstellungen as uie

class Steckdosen(QMainWindow):
    def __init__(self, parent=None):
        super(Steckdosen, self).__init__(parent=None)
        self.setFixedSize(465,125)

        self.config = cp.ConfigParser()
        self.config.read('Steckdosen.ini')
        self.text = self.config['Text']
        self.Farben = self.config['Farben']

        self.pb1 = QPushButton(self)
        self.pb1.setGeometry(QRect(10, 10, 84, 28))
        self.pb1.setObjectName("pb1")
        self.pb1.setText("Steckdose 1")
        self.pb1.clicked.connect(lambda: self.Schalten(1))
        self.pb2 = QPushButton(self)
        self.pb2.setGeometry(QRect(100, 10, 84, 28))
        self.pb2.setObjectName("pb2")
        self.pb2.setText("Steckdose 2")
        self.pb2.clicked.connect(lambda: self.Schalten(2))
        self.pb3 = QPushButton(self)
        self.pb3.setGeometry(QRect(190, 10, 84, 28))
        self.pb3.setObjectName("pb3")
        self.pb3.setText("Steckdose 3")
        self.pb3.clicked.connect(lambda: self.Schalten(3))
        self.pb4 = QPushButton(self)
        self.pb4.setGeometry(QRect(280, 10, 84, 28))
        self.pb4.setObjectName("pb4")
        self.pb4.setText("Steckdose 4")
        self.pb4.clicked.connect(lambda: self.Schalten(4))
        self.pban = QPushButton(self)
        self.pban.setGeometry(QRect(370, 10, 84, 28))
        self.pban.setObjectName("pban")
        self.pban.setText("Alle an")
        self.pban.clicked.connect(lambda: self.Schalten(9))
        self.pb5 = QPushButton(self)
        self.pb5.setGeometry(QRect(10, 50, 84, 28))
        self.pb5.setObjectName("pb5")
        self.pb5.setText("Steckdose 5")
        self.pb5.clicked.connect(lambda: self.Schalten(5))
        self.pb6 = QPushButton(self)
        self.pb6.setGeometry(QRect(100, 50, 84, 28))
        self.pb6.setObjectName("pb6")
        self.pb6.setText("Steckdose 6")
        self.pb6.clicked.connect(lambda: self.Schalten(6))
        self.pb7 = QPushButton(self)
        self.pb7.setGeometry(QRect(190, 50, 84, 28))
        self.pb7.setObjectName("pb7")
        self.pb7.setText("Steckdose 7")
        self.pb7.clicked.connect(lambda: self.Schalten(7))
        self.pb8 = QPushButton(self)
        self.pb8.setGeometry(QRect(280, 50, 84, 28))
        self.pb8.setObjectName("pb8")
        self.pb8.setText("Steckdose 8")
        self.pb8.clicked.connect(lambda: self.Schalten(8))
        self.pbaus = QPushButton(self)
        self.pbaus.setGeometry(QRect(370, 50, 84, 28))
        self.pbaus.setObjectName("pbaus")
        self.pbaus.setText("Alle aus")
        self.pbaus.clicked.connect(lambda: self.Schalten(10))
        self.pbFarben = QPushButton(self)
        self.pbFarben.setGeometry(QRect(180, 90, 84, 28))
        self.pbFarben.setObjectName("pbFarben")
        self.pbFarben.setText("Einstellungen")
        self.pbFarben.clicked.connect(self.Farbene)
        
        self.loadPosition()
        self.loadText()
        self.update_buttons()

    def keyPressEvent(self, event):
        #print(event.text())
        taste_num = event.text()
        #print(event.key())
        if taste_num == '1':
            self.Schalten(1)
        if taste_num == '2':
            self.Schalten(2)
        if taste_num == '3':
            self.Schalten(3)
        if taste_num == '4':
            self.Schalten(4)
        if taste_num == '5':
            self.Schalten(5)
        if taste_num == '6':
            self.Schalten(6)
        if taste_num == '7':
            self.Schalten(7)
        if taste_num == '8':
            self.Schalten(8)
        if taste_num == '+':
            self.Schalten(9)
        if taste_num == '-':
            self.Schalten(10)
        if event.key() == 16777216 or event.key() == 16777221 or event.key() == 16777220:
            self.close()

    def loadPosition(self):
        self.config = cp.ConfigParser()
        self.config.read('Steckdosen.ini')
        self.geometrie = self.config['Geometrie']
        x = int(self.geometrie['x'])
        y = int(self.geometrie['y'])
        self.move(x,y)

    def closeEvent(self, event):
        # Your function to execute before closing
        self.config = cp.ConfigParser()
        self.config.read('Steckdosen.ini')
        if not 'Geometrie' in self.config:
            self.config['Geometrie'] = {}
        self.geometrie = self.config['Geometrie']
        self.geometrie['x'] = str(self.pos().x())
        self.geometrie['y'] = str(self.pos().y())
        with open('Steckdosen.ini', 'w') as configfile:
            self.config.write(configfile)
        print("Application is closing...")
        event.accept()
           
    def update_buttons(self):
        self.config = cp.ConfigParser()
        self.config.read('Steckdosen.ini')
        self.text = self.config['Text']
        self.Farben = self.config['Farben']
        for i in range(1,9):
            if f'pushbutton{i}_fg' in self.Farben:
                setfg = str(self.config['Farben'][f'pushbutton{i}_fg'])
            else:
                setfg ="(255,255,255,255)"
            if f'pushbutton{i}_bg' in self.Farben:
                setbg = str(self.config['Farben'][f'pushbutton{i}_bg'])
            else:
                setbg ="(70,70,70,255)"
            setf =f"self.pb{i}.setStyleSheet('color: rgba{str(setfg)}; background-color: rgba{str(setbg)};')"
            exec(setf)

    def loadText(self):
        self.config = cp.ConfigParser()
        self.config.read('Steckdosen.ini')
        self.farben = self.config['Farben']
        self.text = self.config['Text']
        self.port = self.config['Port']

        self.pb1.setText(self.text['btn_text_1'])
        self.pb2.setText(self.text['btn_text_2'])
        self.pb3.setText(self.text['btn_text_3'])
        self.pb4.setText(self.text['btn_text_4'])
        self.pb5.setText(self.text['btn_text_5'])
        self.pb6.setText(self.text['btn_text_6'])
        self.pb7.setText(self.text['btn_text_7'])
        self.pb8.setText(self.text['btn_text_8'])


    def Schalten(self, Zahl):
        ser = serial.Serial(port='/dev/ttyUSB0', baudrate=2400)
        m_string = chr(13) + chr(1) + "T" + str(int(Zahl)) + chr(110 - int(Zahl))
        #print(m_string)
        if (Zahl == 9):
            m_string = "b'\r\x01S9f"
        if (Zahl == 10):
            m_string = "b'\r\x01C9v"
        mstring = m_string.encode("utf-8")
        #print(mstring)
        mstring = mstring + mstring
        mstring = mstring + mstring
        ser.write(mstring)
        ser.close

    def Farbene(self):
        self.ein = Einstellungen()
        self.ein.show()

class Einstellungen(QDialog):
        def __init__(self):
            super(Einstellungen, self).__init__(Steckdosen)
            uic.loadUi('Einstellungen.ui', self)
            self.move((Steckdosen.x() + Steckdosen.width() + 50), Steckdosen.y())

            self.config = cp.ConfigParser()
            self.config.read('Steckdosen.ini')
            self.farben = self.config['Farben']
            self.text = self.config['Text']
            self.port = self.config['Port']

            self.getText()

            self.btn_bg_1.clicked.connect(self.getColor)
            self.btn_bg_2.clicked.connect(self.getColor)
            self.btn_bg_3.clicked.connect(self.getColor)
            self.btn_bg_4.clicked.connect(self.getColor)
            self.btn_bg_5.clicked.connect(self.getColor)
            self.btn_bg_6.clicked.connect(self.getColor)
            self.btn_bg_7.clicked.connect(self.getColor)
            self.btn_bg_8.clicked.connect(self.getColor)
            self.btn_fg_1.clicked.connect(self.getColor)
            self.btn_fg_2.clicked.connect(self.getColor)
            self.btn_fg_3.clicked.connect(self.getColor)
            self.btn_fg_4.clicked.connect(self.getColor)
            self.btn_fg_5.clicked.connect(self.getColor)
            self.btn_fg_6.clicked.connect(self.getColor)
            self.btn_fg_7.clicked.connect(self.getColor)
            self.btn_fg_8.clicked.connect(self.getColor)
            self.btn_text_speichern.clicked.connect(self.setText)
            self.btn_farben_scliessen.clicked.connect(self.close)


        def getColor(self):
            color = QColorDialog.getColor()
            color1 = color.getRgb()
            btnname = self.sender().objectName()
            #print(self.sender())
            if btnname[4] == "b":
                Bu = f"""self.{btnname}.setStyleSheet(\"background-color: rgba{str(color1)};\")"""
                exec(Bu)
                self.farben[f'pushbutton{btnname[-1]}_bg'] = str(color1)
                with open('Steckdosen.ini', 'w') as configfile:
                    self.config.write(configfile)
            
            else:
                Bu = f"""self.{btnname}.setStyleSheet(\"background-color: rgba{str(color1)};\")"""
                exec(Bu)
                self.farben[f'pushbutton{btnname[-1]}_fg'] = f"{str(color1)}"
                with open('Steckdosen.ini', 'w') as configfile:
                    self.config.write(configfile)

            Steckdosen.update_buttons()

        def setText(self):
            self.config = cp.ConfigParser()
            self.config.read('Steckdosen.ini')
            self.farben = self.config['Farben']
            self.text = self.config['Text']
            self.port = self.config['Port']

            self.text['btn_text_1'] = str(self.ip_st1.text())
            self.text['btn_text_2'] = str(self.ip_st2.text())
            self.text['btn_text_3'] = str(self.ip_st3.text())
            self.text['btn_text_4'] = str(self.ip_st4.text())
            self.text['btn_text_5'] = str(self.ip_st5.text())
            self.text['btn_text_6'] = str(self.ip_st6.text())
            self.text['btn_text_7'] = str(self.ip_st7.text())
            self.text['btn_text_8'] = str(self.ip_st8.text())

            with open('Steckdosen.ini', 'w') as configfile:
                    self.config.write(configfile)

            Steckdosen.loadText()

        def getText(self):
            self.config = cp.ConfigParser()
            self.config.read('Steckdosen.ini')
            self.farben = self.config['Farben']
            self.text = self.config['Text']
            self.port = self.config['Port']

            self.ip_st1.setText(self.text['btn_text_1'])
            Steckdosen.pb1.setText(self.text['btn_text_1'])
            self.ip_st2.setText(self.text['btn_text_2'])
            Steckdosen.pb2.setText(self.text['btn_text_2'])
            self.ip_st3.setText(self.text['btn_text_3'])
            Steckdosen.pb3.setText(self.text['btn_text_3'])
            self.ip_st4.setText(self.text['btn_text_4'])
            Steckdosen.pb4.setText(self.text['btn_text_4'])
            self.ip_st5.setText(self.text['btn_text_5'])
            Steckdosen.pb5.setText(self.text['btn_text_5'])
            self.ip_st6.setText(self.text['btn_text_6'])
            Steckdosen.pb6.setText(self.text['btn_text_6'])
            self.ip_st7.setText(self.text['btn_text_7'])
            Steckdosen.pb7.setText(self.text['btn_text_7'])
            self.ip_st8.setText(self.text['btn_text_8'])
            Steckdosen.pb8.setText(self.text['btn_text_8'])


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Steckdosen = Steckdosen()
    Steckdosen.show()
    sys.exit(app.exec())

            

#     def __init__(self):
#         #E = QToplevel(app)
#         super().__init__()
#         if not self.objectName():
#             self.setObjectName(u"Farbene")
#         self.resize(300, 340)
#         self.setFixedSize(290, 340)
#         self.setWindowTitle(u"Einstellungen")

#         self.config = cp.ConfigParser()
#         self.config.read('Steckdosen.ini')
#         #self.config['Farben']  = {}
#         self.farben = self.config['Farben']

#         self.label = QLabel(self)
#         self.label.setObjectName(u"label")
#         self.label.setGeometry(QRect(154, 10, 21, 18))
#         self.label.setText(u"bg")

#         self.label_2 = QLabel(self)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setGeometry(QRect(194, 10, 21, 18))
#         self.label_2.setText(u"fg")

#         self.label_3 = QLabel(self)
#         self.label_3.setObjectName(u"label_3")
#         self.label_3.setGeometry(QRect(10, 320, 291, 18))
#         self.label_3.setText(u"bg = Hintergrundfarbe ; fg = Fordergrundfarbe")

#     # Label erstellen
#         p = 44
#         for x in range(40,120,10):
#             label = f"""self.label_{x} = QLabel(self)
# self.label_{x}.setObjectName(u'label_{x}')
# self.label_{x}.setGeometry(QRect(66, {p}, 81, 18))
# self.label_{x}.setText(u'Steckdose {int((x-30)/10)}')"""
#             p +=30
#             exec(label)
        
#     # Button erstellen Background
#         p = 40
#         self.btn_grp1 = QButtonGroup()
#         for i in range(1,9):
#             Buttonbg = f"""self.pushButton{i} = QPushButton(self)
# self.pushButton{i}.setObjectName(f'pushButton{i}')
# self.pushButton{i}.setGeometry(QRect(146, {p}, 31, 28))
# self.pushButton{i}.clicked.connect(self.getColor)
# self.btn_grp1.addButton(self.pushButton{i})"""
#             p += 30
#             exec(Buttonbg)

#     # Button erstellen Foreground
#         p = 40
#         self.btn_grp2 = QButtonGroup()
#         for i in range(11,19):
#             Buttonfg = f"""self.pushButton{i} = QPushButton(self)
# self.pushButton{i}.setObjectName(u'pushButton{i}')
# self.pushButton{i}.setGeometry(QRect(186, {p}, 31, 28))
# self.pushButton{i}.clicked.connect(self.getColor)
# self.btn_grp2.addButton(self.pushButton{i})"""
#             p += 30
#             exec(Buttonfg)
        
#         self.pushButton = QPushButton(self)
#         self.pushButton.setObjectName(u"pushButton")
#         self.pushButton.setGeometry(QRect(43, 290, 201, 28))
#         self.pushButton.setText(u"Schliessen")

