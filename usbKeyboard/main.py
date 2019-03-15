import pyb
kb = pyb.USB_HID()
buf = bytearray(8)
# Sending T
# Do the key down
buf[0] = 0x02 # LEFT_SHIFT
buf[2] = 0x17 # keycode for 't/T'
kb.send(buf)
pyb.delay(5)
# Do the key up
buf[0] = 0x00
buf[2] = 0x00
kb.send(buf)
