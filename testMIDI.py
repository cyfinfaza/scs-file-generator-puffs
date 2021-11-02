import time
import rtmidi
from rtmidi.midiconstants import PROGRAM_CHANGE, CONTROL_CHANGE

midiout = rtmidi.MidiOut()
available_ports = midiout.get_ports()

print(available_ports)
print("Using Port:", available_ports[1])

# if available_ports:
midiout.open_port(1)
# else:
#     midiout.open_virtual_port("My virtual output")

with midiout:
    # note_on = [0x90, 60, 112] # channel 1, middle C, velocity 112
    # note_off = [0x80, 60, 0]
    # midiout.send_message(note_on)
    # time.sleep(0.5)
    # midiout.send_message(note_off)
    # time.sleep(0.1)
    # send midi program change channel 3 number 5
    midiout.send_message([0b11010001, 6, 0])
    # midiout.send_message([0b11000010, 3])

del midiout