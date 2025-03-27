from reports import HTMLReport, PDFReport


html_report = HTMLReport()
print("Генерация HTML-отчета:")
html_report.generate_report()

print("\nГенерация PDF-отчета:")
pdf_report = PDFReport()
pdf_report.generate_report()