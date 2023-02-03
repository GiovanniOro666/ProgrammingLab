#Scrivete uno script che sommi tutti i valori delle vendite degli shampoo del file “shampoo_sales.csv” Poi, committate il file in cui l’avete scritto.

def sommashampoo(file_name):
    values = []
    myfile = open(file_name, 'r')
    for line in myfile:
        elements = line.split(',')
        if elements[0] != 'Date':
            date = elements[0]
            value = float(elements[1])
            values.append(float(value))
    sum = 0
    for item in values:
        sum = sum + item
    myfile.close()
    return sum

print('la somma dei valori è {}'.format(sommashampoo('shampoo_sales.csv')))