from datetime import datetime

def get_dates():
    with open('shampoo_sales.csv', 'r') as my_file:
        date_list = []
        for line in my_file:
            elements = line.split(',')
            if(elements[0] != 'Date'):
                date = datetime.strptime(elements[0], '%d-%m-%Y')
                date_list.append(date)
        
        for date in date_list:
            print(date.strftime('%d-%m-%Y'))

get_dates()