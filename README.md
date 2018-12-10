# PythoNode
Python/Qt frontend &amp; NodeJS backend (just for fun).

PythoNode is just a simple proof of concept.  It is an easy way to
give NodeJs a non-browser GUI.  It basically runs a Node instance
along side a Python/Qt5 instance and uses a pipe as a communication
channel.

The idea of it is to give a programmer the same experience of
building a native GUI graphically and writing the code behind it in
Javascript.  To assist the GUI building, the .ui file can be opened
and manipulated with QT Creator.

The cool thing about it is it runs as a native GUI (desktop) app
on all OS'es and uses all free tools to author.  It uses Javascript
but does not require a browser.

It didn't exist so I wrote it.  :-)

To run it, download the files into a folder and...

    node app.js

To modify the form, open the file (app_win_frm_src.ui) using Qt Creator.
When you have made your desired changes, save the file and...

    pyuic5 app_win_frm_src.ui -o app_win_frm.py

This will use the .ui xml file to generate the python (app_win_frm.py)
that would effectively draw the window natively using the Qt5 system.
