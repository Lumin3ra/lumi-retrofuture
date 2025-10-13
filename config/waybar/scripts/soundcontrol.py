import pulsectl
import os
import subprocess
import gi
gi.require_version("Gtk", "4.0")
from gi.repository import Gtk


pulse = pulsectl.Pulse('lumi-sink-lister')

sink_objects = pulse.sink_list()
sink_names = [sink.name for sink in sink_objects]
sink_descriptions = [sink.description for sink in sink_objects]

pulse.close()


def button_pressed(sink_name):
    os.system("pactl set-default-sink " + sink_name)
    exit()

def on_activate(app):
    win = Gtk.ApplicationWindow(application=app)
    box = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=6)

    for i, x in enumerate(sink_names):
        btn = Gtk.Button(label=sink_descriptions[i])
        btn.connect('clicked', lambda y, sink_name = x: button_pressed(sink_name))
        box.append(btn)

    win.set_child(box)
    win.present()

app = Gtk.Application(application_id='org.gtk.LumiSoundControl')
app.connect('activate', on_activate)
app.run(None)