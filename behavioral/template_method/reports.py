from abc import abstractmethod, ABC

class ReportGenerator(ABC):
    # Шаблонный метод
    def generate_report(self):
        self.create_header()
        self.fill_content()
        self.create_footer()
        self.format_report()

    @abstractmethod
    def create_header(self):
        pass

    @abstractmethod
    def fill_content(self):
        pass

    @abstractmethod
    def create_footer(self):
        pass

    # Общий шаг
    def format_report(self):
        print("Форматируем отчет...")


class HTMLReport(ReportGenerator):
    def create_header(self):
        print("<header>Отчет</header>")

    def fill_content(self):
        print("<main>Данные отчета</main>")

    def create_footer(self):
        print("<footer>2023</footer>")

class PDFReport(ReportGenerator):
    def create_header(self):
        print("PDF Header: Отчет")

    def fill_content(self):
        print("PDF Content: Данные отчета")

    def create_footer(self):
        print("PDF Footer: Страница 1")