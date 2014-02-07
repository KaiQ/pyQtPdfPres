#!/usr/bin/env python
# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import popplerqt4
import ui
import sys

class MainWindow(QtGui.QWidget):

  def _minimal_image(self, label, page):
    return self.doc.page(page).renderToImage(label.widthMM(), label.heightMM())

  def _maximal_image(self, label, page):
    return self.doc.page(page).renderToImage(label.logicalDpiX() * self.scale, label.logicalDpiY() * self.scale)

  def load(self, label, page, size = _minimal_image):
    image = size(self, label, page)
    label.setPixmap(QtGui.QPixmap.fromImage(image))


  def __init__(self, parent=None):
    super(MainWindow, self).__init__(parent)
    self.ui = ui.Ui_Episoder()
    self.ui.setupUi(self)
    self.scale = 0.3
    self.doc = popplerqt4.Poppler.Document.load('leisefuchs.pdf')
    self.load(self.ui.prev, 0)
    self.load(self.ui.active, 1, MainWindow._maximal_image)
    self.load(self.ui.next, 2)

if __name__ == "__main__":
  app = QtGui.QApplication(sys.argv)
  mainWindow = MainWindow()
  mainWindow.show()
  sys.exit(app.exec_())
