import locale
from factory import StoneHouseFactory, WoodHouseFactory

def main():
    if locale.getlocale()[0] == 'ru_RU':
        factory = StoneHouseFactory()
    else:
        factory = WoodHouseFactory()
    
    factory.createWall().build()
    factory.createRoof().cover().waterprotect()
    factory.createWindow().install().open()



if __name__ == '__main__':
    main()