from datetime import datetime

class CSVFile:    
    def __init__(self, name):
        self.name = name

    def get_data(self):
        with open(self.name, 'r') as my_file:
            big_list = []
            for line in my_file:
                elements = line.split(',')
                if(elements[0] != 'Date'):
                    date = elements[0]
                    sale = elements[1].strip('\n')
                    small_list = [date, sale]
                    big_list.append(small_list)
            
            return big_list

    def get_date_vendite(self):
        with open(self.name, 'r') as my_file:
            date_list = []
            for line in my_file:
                elements = line.split(',')
                if(elements[0] != 'Date'):
                    date = datetime.strptime(elements[0], '%d-%m-%Y')
                    date_list.append(date)

            return date_list

    def __str__(self):
        with open(self.name, 'r') as my_file:
            for line in my_file:
                head = line.strip('\n')
                return head