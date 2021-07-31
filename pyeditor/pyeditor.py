from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtPrintSupport import *
import sys
class PYEditor(QMainWindow):
    def __init__(self):
        super(PYEditor,self).__init__()
        self.editor=QTextEdit()
        self.editor.setFontPointSize(20)
        self.font_size=QSpinBox()
        self.setCentralWidget(self.editor)
        self.showMaximized()
        self.setWindowTitle('PyPDF Editor')
        self.create_toolbar()
        self.create_menu_bar()

    def create_toolbar(self):
        tool_bar=QToolBar()

        undo_action=QAction(QIcon('undo.png'),'undo',self)
        undo_action.triggered.connect(self.editor.undo)
        tool_bar.addAction(undo_action)

        redo_action=QAction(QIcon('redo.png'),'redo',self)
        redo_action.triggered.connect(self.editor.redo)
        tool_bar.addAction(redo_action)

        tool_bar.addSeparator()

        cut_action=QAction(QIcon('cut.png'),'cut',self)
        cut_action.triggered.connect(self.editor.cut)
        tool_bar.addAction(cut_action)

        copy_action=QAction(QIcon('copy.png'),'copy',self)
        copy_action.triggered.connect(self.editor.copy)
        tool_bar.addAction(copy_action)

        paste_action=QAction(QIcon('paste.png'),'paste',self)
        paste_action.triggered.connect(self.editor.paste)
        tool_bar.addAction(paste_action)

        tool_bar.addSeparator()

        self.font_size.setValue(20)
        self.font_size.valueChanged.connect(self.set_font_size)

        tool_bar.addWidget(self.font_size)
        self.addToolBar(tool_bar)

    def set_font_size(self):
        value=self.font_size.value()
        self.editor.setFontPointSize(value)

    def create_menu_bar(self):
        menu_bar=QMenuBar()

        file_menu = QMenu('File',self)
        menu_bar.addMenu(file_menu)

        save_as_pdf=QAction('save as pdf',self)
        save_as_pdf.triggered.connect(self.save_as_pdf_method)
        file_menu.addAction(save_as_pdf)
        
        edit_menu = QMenu('Edit',self)
        menu_bar.addMenu(edit_menu)

        view_menu = QMenu('View',self)
        menu_bar.addMenu(view_menu)

        self.setMenuBar(menu_bar)

    def save_as_pdf_method(self):
        file_path,_=QFileDialog.getSaveFileName(self,'Export PDF',None,'PDF files(*.pdf)')
        printer = QPrinter(QPrinter.HighResolution)
        printer.setOutputFormat(QPrinter.PdfFormat)
        printer.setOutputFileName(file_path)
        self.editor.document().print_(printer)

app=QApplication(sys.argv)
window=PYEditor()
window.show()
sys.exit(app.exec_())
     