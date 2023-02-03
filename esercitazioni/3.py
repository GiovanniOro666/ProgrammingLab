from CSVFile import CSVFile

csv_file = CSVFile('shampoo_sales.csv')
        #list_of_dates = csv_file.get_date_vendite()        #list_of_all = csv_file.get_data()
        #print(list_of_dates)        #print(list_of_all)
list_of_header =csv_file.__str__()
print(csv_file)