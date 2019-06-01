from PySide2.QtWidgets import*
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QFile
from PySide2.QtGui import *
from matplotlib.backends.backend_qt5agg import (
        FigureCanvas, NavigationToolbar2QT as NavigationToolbar)
from matplotlib.figure import Figure
import numpy as np

# ------------------ MplWidget ------------------
class MplWidget(QWidget):
    def __init__(self, parent = None):    
        QWidget.__init__(self, parent)    
        self.canvas = FigureCanvas(Figure())    
        vertical_layout = QVBoxLayout()
        vertical_layout.addWidget(self.canvas)
        vertical_layout.addWidget(NavigationToolbar(self.canvas, self))
        self.canvas.axes = self.canvas.figure.add_subplot(111)
        self.setLayout(vertical_layout)    
