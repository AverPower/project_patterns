from typing import override

from items import Documentation, House

class Builder:
    def reset(self):
        ...
    def prepare(self):
        ...
    def mainWork(self):
        ... 
    def addServiceLines(self):
        ...
    def finish(self):
        ...


class DocBuilder(Builder):

    doc: Documentation

    @override
    def reset(self):
        self.doc = Documentation()

    @override
    def prepare(self):
        print('Получение разрешения на строительство')
        self.doc.base = True
    
    @override
    def mainWork(self):
        print('Подготовка сметы')
        self.doc.building = True 
    
    @override
    def addServiceLines(self):
        print('Документы на подключение коммуникаций')
        self.doc.serviceLines = True 
    
    @override
    def finish(self):
        print('Акт ввода в эксплуатацию')
        self.doc.finish = True 

    def getResult(self):
        return self.doc
	

class HouseBuilder(Builder):

    house: House

    @override
    def reset(self):
        self.house = House()

    @override
    def prepare(self):
        print('Получение разрешения на строительство')
        self.house.base = True
    
    @override
    def mainWork(self):
        print('Подготовка сметы')
        self.house.building = True 
    
    @override
    def addServiceLines(self):
        print('Документы на подключение коммуникаций')
        self.house.serviceLines = True 
    
    @override
    def finish(self):
        print('Акт ввода в эксплуатацию')
        self.house.finish = True 

    def getResult(self):
        return self.house
	

class PriceBuilder(Builder):

    total: int

    @override
    def reset(self):
        self.total = 0

    @override
    def prepare(self):
        self.total += 500
    
    @override
    def mainWork(self):
        self.total += 1500
    
    @override
    def addServiceLines(self):
        self.total += 300
    
    @override
    def finish(self):
        self.total += 400

    def getResult(self):
        return self.total
	