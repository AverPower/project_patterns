class Device:
    is_on = False
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_channel(self, channel):
        pass

class TV(Device):
    def turn_on(self):
        print("Телевизор включен")
        self.is_on = True

    def turn_off(self):
        print("Телевизор выключен")
        self.is_on = False

    def set_channel(self, channel):
        print(f"Канал изменен на {channel}")

class Radio(Device):
    def turn_on(self):
        print("Радио включено")
        self.is_on = True

    def turn_off(self):
        print("Радио выключено")
        self.is_on = False

    def set_channel(self, frequency):
        print(f"Частота изменена на {frequency} МГц")