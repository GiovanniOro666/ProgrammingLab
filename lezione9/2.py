def increment(data):
    prev_value = None
    for item in data:
        if prev_value != None:
            increment += item - prev_value
            increment = item
    return increment / len(data)
        

class Model():

    def fit(self, data):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):
        raise NotImplementedError('Metodo non implementato')


class IncrementModel(Model):

    def predict(self, data):
        prev_value = None

        somma_inc = 0
        i = 0
        for item in data:
            if i > 0:
                somma_inc += data[i] - data[i - 1]
            i += 1

        if i <= 1:
            return None

        som_med = somma_inc / (i - 1)
        prediction = data[-1] + som_med
        return prediction


class FitIncrementModel(IncrementModel):
    def __init__(self, global_avg_increment):
        self.global_avg_increment = global_avg_increment 

    first_number = [8, 19, 31, 41]
    last_number = [50, 52, 60]
    first_predict = first_number.predict()
    last_predict = last_number.predict()
    
    def fit(self, data):
        super().fit(data)
        return self.global_avg_increment


data = [50, 52, 60]
m = IncrementModel()
print(m.predict(data))
