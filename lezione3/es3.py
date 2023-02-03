class CSVFile ():
    def __init__(self, name):
        self.name = name
    def get_data(self):
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

#csvfile = CSVFile('shampoo_sales.csv')
#list = csvfile.get_data()
#print(list)