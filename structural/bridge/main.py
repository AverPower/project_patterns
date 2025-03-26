from device import Radio, TV
from remote import Remote, AdvancedRemote

def main():

    tv = TV()
    remote = Remote(tv)
    remote.toggle_power()  # Телевизор включен
    remote.set_channel(5)  # Канал изменен на 5

    radio = Radio()
    advanced_remote = AdvancedRemote(radio)
    advanced_remote.toggle_power()  # Радио включено
    advanced_remote.mute()          # Звук отключен

if __name__ == '__main__':
    main()