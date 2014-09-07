import sys
from PyQt4 import QtGui, QtCore
from PyQt4.QtCore import Qt


class Main(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
        self.fileName = ""
        self.initUI()

    def initToolBar(self):
        # For New file
        self.newAction = QtGui.QAction(QtGui.QIcon("icons/new.png"), "New",
                                       self)
        self.newAction.setStatusTip("Create new file")
        self.newAction.setShortcut("Ctrl+N")
        self.newAction.triggered.connect(self.new)

        # To Open existing file
        self.openAction = QtGui.QAction(QtGui.QIcon("icons/open.png"), "Open",
                                        self)
        self.openAction.setStatusTip("Open a file")
        self.openAction.setShortcut("Ctrl+O")
        self.openAction.triggered.connect(self.open)

        # To save a file
        self.saveAction = QtGui.QAction(QtGui.QIcon("icons/save.png"),
                                        "Save", self)
        self.saveAction.setStatusTip("Save file")
        self.saveAction.setShortcut("Ctrl+S")
        self.saveAction.triggered.connect(self.save)

        # To print the file
        self.printAction = QtGui.QAction(QtGui.QIcon("icons/print.png"),
                                         "Print", self)
        self.printAction.setStatusTip("Print the file")
        self.printAction.setShortcut("Ctrl+P")
        self.printAction.triggered.connect(self.prnt)

        # Print preview a file
        self.previewAction = QtGui.QAction(QtGui.QIcon("icons/preview.png"),
                                           "Print Preview", self)
        self.printAction.setStatusTip("Print preview" + self.fileName)
        self.previewAction.setShortcut("Ctrl+Shift+P")
        self.previewAction.triggered.connect(self.preview)

        # Cut action
        self.cutAction = QtGui.QAction(QtGui.QIcon("icons/cut.png"), "Cut",
                                       self)
        self.cutAction.setStatusTip("Cut to clipboard")
        self.cutAction.setShortcut("Ctrl+X")
        self.cutAction.triggered.connect(self.text.cut)

        # Copy action
        self.copyAction = QtGui.QAction(QtGui.QIcon("icons/copy.png"), "Copy",
                                        self)
        self.copyAction.setStatusTip("Copy to clipboard")
        self.copyAction.setShortcut("Ctrl+C")
        self.copyAction.triggered.connect(self.text.copy)

        # Paste action
        self.pasteAction = QtGui.QAction(QtGui.QIcon("icons/paste.png"),
                                         "Paste", self)
        self.pasteAction.setStatusTip("Paste from clipboard")
        self.pasteAction.setShortcut("Ctrl+V")
        self.pasteAction.triggered.connect(self.text.paste)

        # Undo action
        self.undoAction = QtGui.QAction(QtGui.QIcon("icons/undo.png"), "Undo",
                                        self)
        self.undoAction.setStatusTip("Undo last action")
        self.undoAction.setShortcut("Ctrl+Z")
        self.undoAction.triggered.connect(self.text.undo)

        # Redo action
        self.redoAction = QtGui.QAction(QtGui.QIcon("icons/redo.png"), "Redo",
                                        self)
        self.redoAction.setStatusTip("Redo last undone thing")
        self.redoAction.setShortcut("Ctrl+Y")
        self.redoAction.triggered.connect(self.text.redo)

        # Bullets
        self.bulletAction = QtGui.QAction(QtGui.QIcon("icons/bullet.png"),
                                          "Insert bullet list", self)
        self.bulletAction.setStatusTip("Insert bullet list")
        self.bulletAction.setShortcut("Ctrl+Shift+B")
        self.bulletAction.triggered.connect(self.bulletList)

        # Numbered list
        self.numberedAction = QtGui.QAction(QtGui.QIcon("icons/number.png"),
                                            "Insert numbered list", self)
        self.numberedAction.setStatusTip("Insert numbered list")
        self.numberedAction.setShortcut("Ctrl+Shift+L")
        self.numberedAction.triggered.connect(self.numberList)

        # Now instantiate a toolbar of the class addToolBar

        self.toolBar = self.addToolBar("Options")

        self.toolBar.addAction(self.newAction)
        self.toolBar.addAction(self.openAction)
        self.toolBar.addAction(self.saveAction)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.printAction)
        self.toolBar.addAction(self.previewAction)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.cutAction)
        self.toolBar.addAction(self.copyAction)
        self.toolBar.addAction(self.pasteAction)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.undoAction)
        self.toolBar.addAction(self.redoAction)

        self.toolBar.addSeparator()
        self.toolBar.addAction(self.bulletAction)
        self.toolBar.addAction(self.numberedAction)

        self.toolBar.addSeparator()

        self.addToolBarBreak()

    def initFormatBar(self):
        self.formatBar = self.addToolBar("Format")

    def initMenuBar(self):
        menuBar = self.menuBar()
        file = menuBar.addMenu("File")
        edit = menuBar.addMenu("Edit")
        view = menuBar.addMenu("View")
        insert = menuBar.addMenu("Insert")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)
        file.addAction(self.printAction)
        file.addAction(self.previewAction)

        edit.addAction(self.undoAction)
        edit.addAction(self.redoAction)
        edit.addAction(self.cutAction)
        edit.addAction(self.copyAction)
        edit.addAction(self.pasteAction)

        insert.addAction(self.bulletAction)
        insert.addAction(self.numberedAction)

    def initUI(self):
        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)

        # Sets tab stop. Should be 8 spaces which was equal to 33 px in
        # tutorial
        self.text.setTabStopWidth(33)

        # To keep a track of current line and column number
        self.text.cursorPositionChanged.connect(self.cursorPosition)
        self.setWindowIcon(QtGui.QIcon("icons/icon.png"))

        self.initToolBar()
        self.initFormatBar()
        self.initMenuBar()

        # Initialize status bar for the window.
        self.statusBar = self.statusBar()

        """x and y coordinates on the screen, width and height"""
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("qteditor")

    def cursorPosition(self):
        cursor = self.text.textCursor()
        line = cursor.blockNumber() + 1
        col = cursor.columnNumber()

        self.statusBar.showMessage("Line: {} | Column: {}".format(line, col))

    def new(self):
        spawn = Main(self)
        spawn.show()

    def open(self):
        self.fileName = QtGui.QFileDialog.getOpenFileName(self, 'Open File',
                                                          ".", "(*.writer)")

        if self.fileName:
            with open(self.fileName, "rt") as fil:
                self.text.setText(fil.read())

    def save(self):
        # Open dialog box if file is not already saved.
        if not self.fileName:
            self.fileName = QtGui.QFileDialog.getSaveFileName(self, "Save "
                                                              "File")
        # Append extension if none exists
        if not self.fileName.endsWith(".writer"):
            self.fileName += ".writer"

        with open(self.fileName, "wt") as fil:
            fil.write(self.text.toHtml())

    def preview(self):
        # Open preview dialog
        preview = QtGui.QPrintPreviewDialog()

        # If a print is requested, open print dialog
        preview.paintRequested.connect(lambda p: self.text.print_(p))

        preview.exec_()

    def prnt(self):
        # Open print dialog
        dialog = QtGui.QPrintDialog()

        if dialog.exec_() == QtGui.QDialog.Accepted:
            self.text.document().print_(dialog.printer())

    def bulletList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDisc)

    def numberList(self):
        cursor = self.text.textCursor()
        cursor.insertList(QtGui.QTextListFormat.ListDecimal)

def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
