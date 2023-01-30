# -*- coding: utf-8 -*-

from pyqtgraph.Qt import QtWidgets, QtGui
import pyqtgraph.opengl as gl
import pyqtgraph as pg
import numpy as np
import sys



def main(plot_data_x, plot_data_y, plot_data_z):
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)

    w = gl.GLViewWidget()
    w.resize(600,400)
    w.opts['distance'] = 40
    w.show()
    w.setWindowTitle(u'Julia+PyQtGraph サンプル')

    x = plot_data_x
    y = plot_data_y
    for i in range(len(y)):
        yi = [y[i]]*len(x)
        z = plot_data_z[:,i]
        pts = np.vstack([x,yi,z]).transpose()
        plt = gl.GLLinePlotItem(pos=pts, color=pg.glColor((i,len(y)*1.3)), width=(i+1)/10., antialias=True)
        w.addItem(plt)

    app.exec()

if __name__ == '__main__':
    main(plot_data_x, plot_data_y, plot_data_z)