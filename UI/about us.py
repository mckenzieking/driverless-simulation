import sys
import subprocess
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import GLib, Gio, Gtk


MENU_XML = """
<?xml version="1.0" encoding="UTF-8"?>
<interface>
  <menu id="app-menu">
    <section>
      <attribute name="label" translatable="yes">Overview</attribute>
      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">Moving around:
   u    i    o
   j    k    l
   m    ,    .

q/z : increase/decrease max speeds by 10%
w/x : increase/decrease only linear speed by 10%
e/c : increase/decrease only angular speed by 10%
anything else : stop</attribute>
        <attribute name="label" translatable="yes">Instructions</attribute>
      </item>

      <item>
        <attribute name="action">win.change_label</attribute>
        <attribute name="target">About us
        We are the driverless car simulation team made up of 5 individuals, 
        all who took on different areas of the project to see it's completion. It is made 
        up of Jonathan Wells, Kenzie King, Carl Lane, Vivek Upadhyaya and Julian Ajja. 
        Jonathan Wells, Vivek, Julian and Kenzie are all currently pursuing an undergraduate education in computer science. 
        Carl is working towards his undergrad in information technology.
</attribute>
        <attribute name="label" translatable="yes">About us</attribute>
      </item>
    </section>
    <section>
      <item>
        <attribute name="action">win.maximize</attribute>
        <attribute name="label" translatable="yes">Maximize</attribute>
      </item>
      <item>
        <attribute name="action">app.quit</attribute>
        <attribute name="label" translatable="yes">_Quit</attribute>
        <attribute name="accel">&lt;Primary&gt;q</attribute>
    </item>
    </section>
  </menu>
</interface>
"""

class AppWindow(Gtk.ApplicationWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # This will be in the windows group and have the "win" prefix
        max_action = Gio.SimpleAction.new_stateful(
            "maximize", None, GLib.Variant.new_boolean(False)
        )
        max_action.connect("change-state", self.on_maximize_toggle)
        self.add_action(max_action)

        # Keep it in sync with the actual state
        self.connect(
            "notify::is-maximized",
            lambda obj, pspec: max_action.set_state(
                GLib.Variant.new_boolean(obj.props.is_maximized)
            ),
        )

        lbl_variant = GLib.Variant.new_string("WELCOME!")
        lbl_action = Gio.SimpleAction.new_stateful(
            "change_label", lbl_variant.get_type(), lbl_variant
        )
        lbl_action.connect("change-state", self.on_change_label_state)
        self.add_action(lbl_action)

        self.label = Gtk.Label(label=lbl_variant.get_string(), margin=30)
        self.add(self.label)
        self.label.show()




        action = Gio.SimpleAction.new("Begin", None)
        action.connect("activate", self.on_begin)
        self.add_action(action)

    def on_begin(self, widget):
        subprocess.run(['python3', '/home/cl2/Documents/GitHub/driverless-simulation/UI/Demo.py'])





    def on_change_label_state(self, action, value):
        action.set_state(value)
        self.label.set_text(value.get_string())

    def on_maximize_toggle(self, action, value):
        action.set_state(value)
        if value.get_boolean():
            self.maximize()
        else:
            self.unmaximize()



class Application(Gtk.Application):
    def __init__(self, *args, **kwargs):
        super().__init__(
            *args,
            application_id="org.example.myapp",
            flags=Gio.ApplicationFlags.HANDLES_COMMAND_LINE,
            **kwargs
        )
        self.window = None

        self.add_main_option(
            "test",
            ord("t"),
            GLib.OptionFlags.NONE,
            GLib.OptionArg.NONE,
            "Command line test",
            None,
        )

    def do_startup(self):
        Gtk.Application.do_startup(self)

        action = Gio.SimpleAction.new("quit", None)
        action.connect("activate", self.on_quit)
        self.add_action(action)

        action = Gio.SimpleAction.new("Begin", None)
        action.connect("activate", self.on_begin)
        self.add_action(action)

        builder = Gtk.Builder.new_from_string(MENU_XML, -1)
        self.set_app_menu(builder.get_object("app-menu"))

    def do_activate(self):
        if not self.window:
            
            self.window = AppWindow(application=self, title="AI CAR SIMULATION")

        self.window.present()

    def do_command_line(self, command_line):
        options = command_line.get_options_dict()
        # convert GVariantDict -> GVariant -> dict
        options = options.end().unpack()

        if "test" in options:
            # This is printed on the main instance
            print("Test argument recieved: %s" % options["test"])

        self.activate()
        return 0

    def on_about(self, action, param):
        about_dialog = Gtk.AboutDialog(transient_for=self.window, modal=True)
        about_dialog.present()

    def on_quit(self, action, param):
        self.quit()

    def on_begin(self, value):
        subprocess.run(['python3', '/home/cl2/Documents/GitHub/driverless-simulation/UI/Demo.py'])
if __name__ == "__main__":
    app = Application()
    app.run(sys.argv)