import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

class MyWindow(Gtk.Window):
    def __init__(self):
        super().__init__(title="RPG Compendium")
        self.set_border_width(10)

        vbox = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

        rpgclasses_list = Gtk.ListStore(str)
        rpgclasses = [
            "Barbarian",
            "Bard",
        ]
        for rpgclass in rpgclasses:
            rpgclasses_list.append([rpgclass])

        rpgclasses_combo= Gtk.ComboBox.new_with_model(rpgclasses_list)
        renderer_text = Gtk.CellRendererText()
        rpgclasses_combo.pack_start(renderer_text, True)
        rpgclasses_combo.add_attribute(renderer_text, "text", 0)

        vbox.pack_start(rpgclasses_combo, False, False, True)

if __name__ == "__main__":
    win = MyWindow()
    win.connect("destroy", Gtk.main_quit)
    win.show_all()
    Gtk.main()
