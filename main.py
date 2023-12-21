from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication
import sys


def new():
    text.setText("")

def bold():
    if text.fontWeight != QFont.Bold:
        text.setFontWeight(QFont.Bold)
        return
    text.setFontWeight(QFont.Normal)

def italic():
    state = text.fontItalic()
    text.setFontItalic(not (state))

def underline():
    state = text.fontUnderline()
    text.setFontUnderline(not (state))

def strike():
    f = text.font()
    if (f.strikeOut()):
        f.setStrikeOut(False)
    else:
        f.setStrikeOut(True)
    text.setFont(f)

def color():
    newColorDialog = QColorDialog()
    newColor = newColorDialog.getColor()
    text.setTextColor(QColor(newColor.name()))

def highlight():
    newColorDialog = QColorDialog()
    newColor = newColorDialog.getColor()
    text.setTextBackgroundColor(QColor(newColor.name()))

def SetFontSize():
    text.setFontPointSize(fontSize.value())

def SetFontName():
    text.setCurrentFont(QFont(fontName.currentText()))


def SaveTextFile():
    document = text.document()
    file = QFile("file.html")
    if file.open(QFile.WriteOnly):
        OutputText = document.toHtml()
        file.write(OutputText.encode('utf-8'))
        file.close()
        return True
    else:
        return False

def LoadTextFile():
    f = QFile("file.html")
    f.open(QFile.ReadOnly | QFile.Text)
    istream = QTextStream(f)
    text.setHtml(istream.readAll())
    f.close()