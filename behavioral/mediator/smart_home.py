class SmartHomeMediator:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def notify(self, sender, event):
        for device in self._devices:
            if device != sender:
                device.handle_event(event)

class Device:
    def __init__(self, name, mediator):
        self._name = name
        self._mediator = mediator

    def trigger_event(self, event):
        print(f"{self._name} инициирует событие: {event}")
        self._mediator.notify(self, event)

    def handle_event(self, event):
        print(f"{self._name} реагирует на событие: {event}")

# Устройства
mediator = SmartHomeMediator()
light = Device("Свет", mediator)
thermostat = Device("Термостат", mediator)
speaker = Device("Колонка", mediator)

mediator.add_device(light)
mediator.add_device(thermostat)
mediator.add_device(speaker)

# Симуляция события
light.trigger_event("включение")