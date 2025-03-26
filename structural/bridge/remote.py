from device import Device

class Remote:
    def __init__(self, device: Device):
        self.device = device  # Композиция вместо наследования

    def toggle_power(self):
        if self.device.is_on:
            self.device.turn_off()
        else:
            self.device.turn_on()

    def set_channel(self, channel):
        self.device.set_channel(channel)


class AdvancedRemote(Remote):
    def mute(self):
        print("Звук отключен")