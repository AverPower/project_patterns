from suppliers import CompanyA, CompanyB, windows, GenericSupplier
from windows import WoodFrameWindow


def main():
    creators = [CompanyA(), CompanyB(), GenericSupplier(WoodFrameWindow())]
    for creator in creators:
        creator.install().open()

    print("Установленные окна: ")
    for window in windows:
        print(window)


if __name__ == "__main__":
    main()
