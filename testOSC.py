from OSC import *

c = OSCStreamingClient()
c.connect(('192.168.0.20', 3032))

def eos_out_handler(addr, tags, stuff, source):
	# print(addr, tags, stuff, source)
	pass

c.addMsgHandler('default', eos_out_handler)

while True:
	c.sendOSC(OSCMessage(f"/eos/cue/{input('Cue: ')}/fire"))

c.close()