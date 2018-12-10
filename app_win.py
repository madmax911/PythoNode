#!/usr/bin/env python3

import threading
import sys
import queue

from PyQt5 import QtWidgets
from app_win_frm import *

global mesg_q
mesg_q = queue.Queue()

global Quitting
Quitting = False

def worker(mesg_q=mesg_q):
    app = QtWidgets.QApplication(sys.argv)
    window = QtWidgets.QMainWindow()
    ui = Ui_window()
    ui.setupUi(window)

    def cmdOk_Click():
        print(ui.txtName.text(), flush=True)

    ui.cmdOk.clicked.connect(cmdOk_Click)

    window.move(0, 0)

    window.show()

    def onCloseWindow():
        Quitting = True
        app.quit()
        sys.exit(0)

    window.destroyed.connect(onCloseWindow)

    def MsgAction(TextRcv):
        ui.txtName.setText(TextRcv)

    def ChkInputs():
        if Quitting:
            ui.tmrTimer.stop()
        else:
            if not mesg_q.empty():
                MsgAction(mesg_q.get())

    ui.tmrTimer = QtCore.QTimer()
    ui.tmrTimer.setInterval(50)
    ui.tmrTimer.timeout.connect(ChkInputs)
    ui.tmrTimer.start()

    sys.exit(app.exec_())

WindowThd = threading.Thread(target=worker)
# WindowThd.daemon = True
WindowThd.start()

line = ""

while not Quitting:
    line = input()
    
    if line != "":
        mesg_q.put(line)
        line = ""
