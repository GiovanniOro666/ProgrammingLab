class CSVFile ():
    def __init__(self, name):
        self.name = name
    def get_data(self):
        try:
            lista = []
            mio_file = open(self.name, 'r')
            if mio_file == []:
                return None
            for line in mio_file:
                elements = line.strip('\n').split(',')
                if elements[0] != 'Date':
                    lista.append(elements)
            print(lista)
            return lista
        except:
            print('Errore')

class numericalCSVFile (CSVFile):
    def super.get_data(self):
    float_list = get_data(self)
    for item in float_list:
        try:
            item[1] = float(item[1])
        except ValueError:
            print('errore di valore')
        except TypeError:
            print('errore di print')
        except 
csvfile = CSVFile('shampoo_sales.csv')
list = csvfile.get_data()
print(list)