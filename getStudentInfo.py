from html.parser import HTMLParser
import requests
import openpyxl


class TableParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.inside_table = False
        self.inside_row = False
        self.inside_cell = False
        self.current_row = []
        self.table_data = []

    def handle_starttag(self, tag, attrs):
        if tag == 'table':
            self.inside_table = True
        elif tag == 'tr':
            self.inside_row = True
            self.current_row = []
        elif tag == 'td':
            self.inside_cell = True

    def handle_endtag(self, tag):
        if tag == 'table':
            self.inside_table = False
        elif tag == 'tr':
            self.inside_row = False
            self.table_data.append(self.current_row)
        elif tag == 'td':
            self.inside_cell = False

    def handle_data(self, data):
        if self.inside_cell:
            self.current_row.append(data.strip())


# Create a new workbook and select the active worksheet
workbook = openpyxl.Workbook()
worksheet = workbook.active

for i in range(0, 1001, 50):
    url = f"http://114.55.147.180/ranklist.php?start={i}&prefix=2022&scope="
    response = requests.get(url)
    parser = TableParser()
    parser.feed(response.text)
    namelist = parser.table_data
    del namelist[1], namelist[0]
    print(namelist)
    for row in namelist:
        worksheet.append(row)

workbook.save('studentlist.xlsx')
