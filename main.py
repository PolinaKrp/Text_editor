from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow, QAction, qApp, QApplication,QFileDialog,QHBoxLayout,QWidget,QApplication
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

def SaveAsTextFile(self):
    fileName, _ = QFileDialog.getSaveFileName(win,"Сохранить файл","","HTML (*.html)")
    if fileName:
        document = text.document()
        file = QFile(f"{fileName}.html")
        if file.open(QFile.WriteOnly):
            OutputText = document.toHtml()
            file.write(OutputText.encode('utf-8'))
            file.close()
            return True
        else:
            return False

def LoadTextFile():
    fileName=QFileDialog.getOpenFileName(win,"Открыть файл","","HTML (*.html)")

    if (fileName[0]):
        f = QFile(fileName[0])
        f.open(QFile.ReadOnly | QFile.Text)
        istream = QTextStream(f)
        text.setHtml(istream.readAll())
        f.close()


app = QApplication(sys.argv)
win = QWidget()
win.resize(975, 500)
layout = QVBoxLayout()
layout.setContentsMargins(0, 0, 0, 0)
text = QTextEdit()

#menu bar
MenuBar = QMenuBar()

FileMenu = QMenu("Файл")
MenuBar.addMenu(FileMenu)

NewMenu = QAction(QIcon("icons/new.png"), "Новый")
NewMenu.setShortcut("Ctrl+N")
NewMenu.triggered.connect(new)
FileMenu.addAction(NewMenu)
FileMenu.addSeparator()
OpenMenu = QAction(QIcon("icons/open.png"), "Открыть")
OpenMenu.setShortcut("Ctrl+O")
OpenMenu.triggered.connect(LoadTextFile)
FileMenu.addAction(OpenMenu)
SaveMenu = QAction(QIcon("icons/save.png"), "Сохранить")
SaveMenu.setShortcut("Ctrl+S")
SaveMenu.triggered.connect(SaveTextFile)
FileMenu.addAction(SaveMenu)
SaveAsMenu = QAction(QIcon("icons/save.png"), "Сохранить как")
SaveAsMenu.triggered.connect(SaveAsTextFile)
FileMenu.addAction(SaveAsMenu)
FileMenu.addSeparator()
QuitMenu = QAction("Выход")
QuitMenu.setShortcut("Ctrl+Q")
QuitMenu.triggered.connect(app.quit)
FileMenu.addAction(QuitMenu)

EditMenu = QMenu("Правка")
MenuBar.addMenu(EditMenu)
UndoMenu = QAction(QIcon("icons/undo.png"), "Отменить")
UndoMenu.setShortcut("Ctrl+Z")
UndoMenu.triggered.connect(text.undo)
EditMenu.addAction(UndoMenu)
RedoMenu = QAction(QIcon("icons/redo.png"), "Возвращать")
RedoMenu.setShortcut("Ctrl+R")
RedoMenu.triggered.connect(text.redo)
EditMenu.addAction(RedoMenu)
EditMenu.addSeparator()
CopyMenu = QAction(QIcon("icons/copy.png"), "Копировать")
CopyMenu.setShortcut("Ctrl+C")
CopyMenu.triggered.connect(text.copy)
EditMenu.addAction(CopyMenu)
CutMenu = QAction(QIcon("icons/cut.png"), "Вырезать")
CutMenu.setShortcut("Ctrl+X")
CutMenu.triggered.connect(text.cut)
EditMenu.addAction(CutMenu)
PasteMenu = QAction(QIcon("icons/paste.png"), "Вставить")
PasteMenu.setShortcut("Ctrl+V")
PasteMenu.triggered.connect(text.paste)
EditMenu.addAction(PasteMenu)
EditMenu.addSeparator()

FontMenu = QMenu("Шрифт")
MenuBar.addMenu(FontMenu)
BoldMenu = QAction(QIcon("icons/bold.png"), "Жирный")
BoldMenu.setShortcut("Ctrl+B")
BoldMenu.triggered.connect(bold)
FontMenu.addAction(BoldMenu)
ItalicMenu = QAction(QIcon("icons/italic.png"), "Курсив")
ItalicMenu.setShortcut("Ctrl+I")
ItalicMenu.triggered.connect(italic)
FontMenu.addAction(ItalicMenu)
UnderlineMenu = QAction(QIcon("icons/underline.png"), "Подчеркнутый")
UnderlineMenu.setShortcut("Ctrl+U")
UnderlineMenu.triggered.connect(underline)
FontMenu.addAction(UnderlineMenu)
StrikeMenu = QAction(QIcon("icons/strike.png"), "Зачеркнутый")
StrikeMenu.setShortcut("Ctrl+Y")
StrikeMenu.triggered.connect(strike)
FontMenu.addAction(StrikeMenu)
FontMenu.addSeparator()
TextColorMenu = QAction(QIcon("icons/font-color.png"), "Цвет текста")
TextColorMenu.setShortcut("Ctrl+M")
TextColorMenu.triggered.connect(color)
FontMenu.addAction(TextColorMenu)
HighLightColorMenu = QAction(QIcon("icons/highlight.png"), "Цвет выделения")
HighLightColorMenu.setShortcut("Ctrl+H")
HighLightColorMenu.triggered.connect(highlight)
FontMenu.addAction(HighLightColorMenu)
FontMenu.addSeparator()
LeftAlignMenu = QAction(QIcon("icons/align-left.png"), "Выравнивание по левому краю")
LeftAlignMenu.setShortcut("Ctrl+L")
LeftAlignMenu.triggered.connect(lambda : text.setAlignment(Qt.AlignLeft))
FontMenu.addAction(LeftAlignMenu)
CenterAlignMenu = QAction(QIcon("icons/align-center.png"), "Выравнивание посередине")
CenterAlignMenu.setShortcut("Ctrl+E")
CenterAlignMenu.triggered.connect(lambda : text.setAlignment(Qt.AlignCenter))
FontMenu.addAction(CenterAlignMenu)
RightAlignMenu = QAction(QIcon("icons/align-right.png"), "Выравнивание по правому краю")
RightAlignMenu.setShortcut("Ctrl+T")
RightAlignMenu.triggered.connect(lambda : text.setAlignment(Qt.AlignRight))
FontMenu.addAction(RightAlignMenu)
JustifyAlignMenu = QAction(QIcon("icons/align-justify.png"), "Выравнивание по ширине")
JustifyAlignMenu.setShortcut("Ctrl+J")
JustifyAlignMenu.triggered.connect(lambda : text.setAlignment(Qt.AlignJustify))
FontMenu.addAction(JustifyAlignMenu)

layout.addWidget(MenuBar)
#menu bar end