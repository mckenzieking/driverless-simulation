import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.ApplicationWindow):
    def __init__(self):
        Gtk.Window.__init__(self, title="AI Car Simulation")
        self.set_border_width(10)

        hbox = Gtk.Box(spacing=6)
        self.add(hbox)




        self.button = Gtk.Button(label="launch About us")
        self.button.connect("clicked", self.on_button_clicked)
        hbox.pack_start(self.button, True, True, 0) #not needed without example
        self.add(self.button)

        self.button = Gtk.Button(label="launch Program")
        self.button.connect("clicked", self.on_program_clicked)
        hbox.pack_start(self.button, True, True, 0) #not needed without example
        self.add(self.button)

    def on_button_clicked(self, widget):
        subprocess.run(['python3', '/home/cl2/Documents/GitHub/driverless-simulation/UI/about us.py'])
    def on_program_clicked(self, widget):
        subprocess.run(['python3', '/home/cl2/Documents/GitHub/driverless-simulation/UI/Design.py'])
        


win = MyWindow()
win.connect("destroy", Gtk.main_quit)
win.show_all()
Gtk.main()