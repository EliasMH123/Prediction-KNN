from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report
from load_dataset import X,y

# Entrenar el modelo
knn_classifier = KNeighborsClassifier()
knn_classifier.fit(X, y)

# Obtener los valores de los parámetros desde el usuario

# Realizar la predicción utilizando los valores de los parámetros ingresados

report = classification_report(y, knn_classifier.predict(X))


def make_prediccion(N,P,K,temperature,humidity,ph,rainfall):
    datos_prediccion = [[N, P, K, temperature, humidity, ph, rainfall]]
    resultado_prediccion = knn_classifier.predict(datos_prediccion)
    return {
    'Nitrógeno en el suelo': [N],
    'Fósforo en el suelo': [P],
    'Potasio en el suelo': [K],
    'Temperatura': [temperature],
    'Humedad relativa': [humidity],
    'Valor pH del suelo': [ph],
    'Precipitación': [rainfall],
    'Predicción': resultado_prediccion.tolist()
}

# Obtener la precisión del modelo
precision = knn_classifier.score(X, y)