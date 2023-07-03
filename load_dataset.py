import pandas as pd

data = pd.read_csv('data/Crop_recommendation.csv')


# Separar las características (X) y la variable objetivo (y)
X = data.drop('label', axis=1)
y = data['label']