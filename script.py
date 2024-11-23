import reinkpy

device = reinkpy.Device.from_usb()  # Attempt to connect to the USB device
print(device.epson.reset_waste()) 