# -*- coding: utf-8 -*-

from pyqtgraph.Qt import QtWidgets, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys

def main(plot_data_x, plot_data_y, plot_data_z):
    app = pg.mkQApp()
    mw = QtWidgets.QMainWindow()
    mw.setWindowTitle(u'Julia+PyQtGraph サンプルです')
    mw.resize(1280,768) #Window size

    cw = QtWidgets.QWidget()
    button = QtWidgets.QPushButton("Quit")

    mw.setCentralWidget(cw)
    l = QtWidgets.QVBoxLayout()

    w = gl.GLViewWidget()
    #w.resize(600,400)
    w.opts['distance'] = 40
    x = plot_data_x
    y = plot_data_y
    for i in range(len(y)):
        yi = [y[i]]*len(x)
        z = plot_data_z[:,i]
        pts = np.vstack([x,yi,z]).transpose()
        plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i,len(y)*1.3)), width=(i+1)/10., antialias=True)
        w.addItem(plt)
    
    l.addWidget(w)
    l.addWidget(button)


    def clicked():
        mw.close()

    button.clicked.connect(clicked)

    cw.setLayout(l)
    mw.show()
    pg.exec()



if __name__ == '__main__':
    main(plot_data_x, plot_data_y, plot_data_z)