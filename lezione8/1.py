class Model ():
    def fit(self, dati):
        raise NotImplementedError('Metodo non implementato')

    def predict(self, dati):
        raise NotImplementedError('Metodo non implementato')

class incrementModel(Model):
    def predict(self, dati):
        prev_value = 0;
        value = []
        for item in dati:
            if item != prev_value:
                increment = item - prev_value
                value.append(increment)
                prev_value = item
            
        prediction =  (sum(value)/len(dati)) + prev_value
        return prediction

dati = [50, 52, 60]
pred = incrementModel()
print("Valore prossimo:{}".format(pred.predict(dati)))