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

        self.toolBar = self.addToolBar("Options")

        self.toolBar.addAction(self.newAction)
        self.toolBar.addAction(self.openAction)
        self.toolBar.addAction(self.saveAction)

        self.toolBar.addSeparator()

        self.addToolBarBreak()

    def initFormatBar(self):
        self.formatBar = self.addToolBar("Format")

    def initMenuBar(self):
        menuBar = self.menuBar()
        file = menuBar.addMenu("File")
        edit = menuBar.addMenu("Edit")
        view = menuBar.addMenu("View")

        file.addAction(self.newAction)
        file.addAction(self.openAction)
        file.addAction(self.saveAction)

    def initUI(self):
        self.text = QtGui.QTextEdit(self)
        self.setCentralWidget(self.text)

        self.initToolBar()
        self.initFormatBar()
        self.initMenuBar()

        # Initialize status bar for the window. It's different from tutorial.
        # Not used self.statusbar. Directly initialized self.statusBar()
        self.statusBar()

        """x and y coordinates on the screen, width and height"""
        self.setGeometry(100, 100, 1030, 800)
        self.setWindowTitle("qteditor")

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
        if not self.fileName.endswith(".writer"):
            self.fileName += ".writer"

        with open(self.fileName, "wt") as fil:
            fil.write(self.text.toHtml())



def main():
    app = QtGui.QApplication(sys.argv)
    main = Main()
    main.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
