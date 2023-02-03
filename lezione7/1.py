def somma(file_in_entrata):
    values = []
    tabella = open(file_in_entrata, 'r')

    for line in tabella:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = elements[1]
            values.append(float(value))
    sum = 0
    for item in values:
        sum = sum + item
    
    tabella.close()
    return sum

class CSVFile:
    def __init__(self, name):
        self.name = name

    def get_data(self):
        try:
            file = open(self.name, 'r')
            file_content = []

            for line in file:
                elements = line.split(',')
                elements[1] = elements[1].strip('\n')
                if elements[0] != 'Date':
                    date = elements[0]
                    value = elements[1]
                    elements[1] = elements[1].strip('\n')
                    file_content.append([date, value])

            file.close()
            return file_content

        except:
            print('Errore')


class NumericalCSVFile(CSVFile):
    def get_data(self):
        string_data = super().getdata()
        numerical_values = []
        for line in string_data:
            numerical_string = []
            element[1] = float(element[1])
            numerical_string.append(element[1])
            numerical_values.append(numerical_string)






list = CSVFile('shampoo_sales.csv')
print("{}".format(list.get_data()))







#result = somma('shampoo_sales.csv')
#print('{}'.format(result))
