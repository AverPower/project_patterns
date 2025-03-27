from objs import Light
from initiator import RemoteControl
from commands import LightOnCommand

light = Light()
remote = RemoteControl()

remote.press_button(LightOnCommand(light))  # Включаем свет
remote.undo_last()                          # Выключаем (отмена)