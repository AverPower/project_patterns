from builder import PriceBuilder, HouseBuilder, DocBuilder
from director import Director


def main():
    priceBuilder = PriceBuilder()
    houseBuilder = HouseBuilder()
    docBuilder = DocBuilder()

    salesman = Director(priceBuilder)
    manager = Director(docBuilder)
    foreman = Director(houseBuilder)
    
    salesman.make(True)
    price = priceBuilder.getResult()
    print(f'Результат работы продавца - цена:\n{price}\n\n')

    foreman.make(True)
    house = houseBuilder.getResult()
    print(f'Результат работы прораба - дом:\n{house}\n\n')

    manager.make(True)
    doc = docBuilder.getResult()
    print(f'Результат работы менеджера - пакет документов:\n{doc}\n\n')

if __name__ == '__main__':
    main()