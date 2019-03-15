# ESP8266 ([Huzzah Feather](https://www.adafruit.com/product/2821)) Instructions and Links

* [Adafruit Instructions](https://learn.adafruit.com/micropython-basics-how-to-load-micropython-on-a-board/esp8266?view=all)
* [ESPTool](https://github.com/espressif/esptool/) (Notice **-p COM#** for Windows machines)
* [Micropython Instructions](http://docs.micropython.org/en/latest/esp8266/esp8266/tutorial/intro.html)
* [USB Device Drivers](https://www.silabs.com/products/development-tools/software/usb-to-uart-bridge-vcp-drivers)

>The REPL is always available on the UART0 serial peripheral, which is connected to the pins GPIO1 for TX and GPIO3 for RX. The baudrate of the **REPL is 115200**. If your board has a USB-serial convertor on it then you should be able to access the REPL directly from your PC. Otherwise you will need to have a way of communicating with the UART.

>To access the prompt over USB-serial you need to use a terminal emulator program.

```
C:\>esptool.py -p COM4 erase_flash
esptool.py v1.3
Connecting....
Running Cesanta flasher stub...
Erasing flash (this may take a while)...
Erase took 11.2 seconds

C:\>esptool.py -p COM4 --baud 115200 write_flash --flash_size=detect -fm dio 0 esp8266-20170108-v1.8.7.bin
esptool.py v1.3
Connecting....
Auto-detected Flash size: 32m
Running Cesanta flasher stub...
Flash params set to 0x0240
Wrote 589824 bytes at 0x0 in 51.1 seconds (92.3 kbit/s)...
Leaving...
```
