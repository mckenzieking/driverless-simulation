import sys

import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk


class MyWindow(Gtk.Window):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.init_ui()

    def init_ui(self):    

        self.set_border_width(10)

        image = Gtk.Image()
        image.set_from_file("/home/Downloads/undefined3.png")

        self.add(image)

        self.set_title("Red Rock")
        self.connect("destroy", Gtk.main_quit)

win = MyWindow()
win.show_all()
Gtk.main()