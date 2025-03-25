class Documentation:

    def __init__(self):
        self._base = False
        self._building = False
        self._serviceLines = False
        self._finish = False

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, building):
        self._building = building

    @property
    def serviceLines(self):
        return self._serviceLines

    @serviceLines.setter
    def serviceLines(self, service_lines):
        self._serviceLines = service_lines

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, finish):
        self._finish = finish

    def yes_no(self, r):
        return 'Получено' if r else 'Нет'
	
    def __repr__(self):
        sb = ''
        sb += f"\tРазрешение на строительство: {self.yes_no(self.base)}\n"
        sb += f"\tУтверждение сметы: {self.yes_no(self.building)}\n"
        sb += f"\tРазрешение на подключение коммуникаций: {self.yes_no(self.serviceLines)}\n"
        sb += f"\tВвод в эксплуатацию: {self.yes_no(self.finish)}\n"
        return sb




class House:

    def __init__(self):
        self._base = False
        self._building = False
        self._serviceLines = False
        self._finish = False

    @property
    def base(self):
        return self._base

    @base.setter
    def base(self, base):
        self._base = base

    @property
    def building(self):
        return self._building

    @building.setter
    def building(self, building):
        self._building = building

    @property
    def serviceLines(self):
        return self._serviceLines

    @serviceLines.setter
    def serviceLines(self, service_lines):
        self._serviceLines = service_lines

    @property
    def finish(self):
        return self._finish

    @finish.setter
    def finish(self, finish):
        self._finish = finish

    def yes_no(self, r):
        return 'Получено' if r else 'Нет'
	
    def __repr__(self):
        sb = ''
        sb += f"\tФундамент: {self.yes_no(self.base)}\n"
        sb += f"\tСтроение: {self.yes_no(self.building)}\n"
        sb += f"\tКоммуникации: {self.yes_no(self.serviceLines)}\n"
        sb += f"\tОтделка: {self.yes_no(self.finish)}\n"
        return sb
