class ExamException(Exception):        #eccezioni dedicate all'esame
    pass


class CSVFile:
    def __init__(self, name):
        self.name = name
        
    
    def get_data():
        pass


class CSVTimeSeriesFile(CSVFile):
    def __init__(self, name):
        super().__init__(name)        # richiamo al metodo della classe superiore
        
   
    def get_data(self):
        time_series = []

        try:
            data = open(self.name, 'r')
            if data.read() == '':        # legge il file e controlla se è vuoto
                raise ExamException('Errore: file vuoto quindi inutilizzabile')
            data.close()        # lo chiudo e poi lo riapro perché ho usato read()
        except:
            raise ExamException('Errore, impossibile aprire il file')        # test per vedere se si apre il file

        data = open(self.name, 'r')        # riapro il file
        for line in data:
            if line == '\n':        # riga vuota saltata
                continue
            split_line = line.strip('\n').split(',')
            if split_line[0] != 'epoch':
                try:
                    timestamp = split_line[0]
                    temperature = split_line[1]
                    float(temperature)
                    time_series.append([int(timestamp), float(temperature)])
                except:
                    continue
        if time_series == []:
            raise ExamException('Errore: la time series è vuota')
            
        data.close()
        return time_series

        
def check_time_series(time_series):
    prev_timestamp = None        # tempo precedente
    seen_timestamps = set()        # creo un insieme disordinato così salvo i tempi già visti
    for timestamp, _ in time_series:
        # se il precedente non è nullo e se è maggiore dell'attuale elemento iterato
        if prev_timestamp is not None and timestamp < prev_timestamp:        
            raise ExamException("Errore: la time series non è in ordine")
        prev_timestamp = timestamp
        
        if timestamp in seen_timestamps:        # se è già stato visto
            raise ExamException("Errore: la timeseries contiene duplicati")
        seen_timestamps.add(timestamp)        # add perché è un set e non una lista


def compute_daily_max_difference(time_series):
    temperature_ranges = []        # raccoglitore delle diverse escursioni termiche
    i = 0
    while i < len(time_series):
        day_start = time_series[i][0] - (time_series[i][0] % 86400)        # mezzanotte
        day_end = day_start + 86400        # (inizio giorno + 24h)
        day_temperatures = [time_series[i][1]]        # riga i colonna numero 2(1)
        i += 1
        while i < len(time_series) and time_series[i][0] < day_end:        # logica interna al giorno
            day_temperatures.append(time_series[i][1])        #fissa i valori di temperatura in day_temperature
            i += 1
        if len(day_temperatures) == 1:        # caso in cui c'è una misurazione per il giorno
            temperature_ranges.append(None)
        else:
            temperature_ranges.append(max(day_temperatures) - min(day_temperatures))        #fisso le variazioni di temperatura in temperature_ranges
    return temperature_ranges


#time_series_file = CSVTimeSeriesFile(name='data.csv')
#time_series = time_series_file.get_data()
#check_time_series(time_series)
#result = compute_daily_max_difference(time_series)
#print(*result, sep = '\n') 