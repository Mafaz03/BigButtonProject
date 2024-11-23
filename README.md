ReInkPy
=======
Waste ink counter resetter for some (EPSON) printers.

Free and open. [Python](https://python.org) code.


# Getting started

```
pip install -e git+https://codeberg.org/atufi/reinkpy#egg=reinkpy[ui,usb,net]
```

`python -m reinkpy.ui` launches a GUI.


Python API examples:

```
import reinkpy

for p in reinkpy.Device.find():
	print(p)
    print(p.info)

# Get a specific device
d = Device.from_file('/dev/usb/lp0')
d = Device.from_usb(manufacturer='EPSON')
d = Device.from_ip('192.168.0.255')

e = d.epson # Epson driver
assert e.specs.model # model is known

print(e.read_eeprom())
# e.reset_waste()
# e.write_eeprom((address, value), …)
```

CLI one-liners:

`python -c 'import reinkpy;print(reinkpy.Device.from_usb().epson.read_eeprom(*range(256)))'`

`python -c 'import reinkpy;reinkpy.Device.from_ip("1.2.3.4").epson.reset_waste()'`


# Warning

This is software. It won't actually replace pads.


# Similar projects

This was started as a port of [ReInk](https://github.com/lion-simba/reink/).
See also [epson_print_conf](https://github.com/Ircama/epson_print_conf).
