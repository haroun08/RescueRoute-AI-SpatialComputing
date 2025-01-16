import pandas as pd
from sklearn.preprocessing import StandardScaler

def preprocess_traffic_data(data):
    # Normalize traffic data
    scaler = StandardScaler()
    data['traffic_level'] = scaler.fit_transform(data[['traffic_level']])
    return data

def preprocess_weather_data(data):
    # One-hot encode weather conditions
    data = pd.get_dummies(data, columns=['weather_condition'])
    return data