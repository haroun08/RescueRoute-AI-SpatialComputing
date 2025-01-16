import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import LSTM, Dense
import numpy as np

def build_lstm_model(input_shape):
    model = Sequential([
        LSTM(50, return_sequences=True, input_shape=input_shape),
        LSTM(50),
        Dense(1)
    ])
    model.compile(optimizer='adam', loss='mse')
    return model

def train_traffic_model(data):
    # Preprocess data (e.g., normalize, split into sequences)
    X, y = preprocess_data(data)
    
    # Build and train the model
    model = build_lstm_model((X.shape[1], X.shape[2]))
    model.fit(X, y, epochs=20, batch_size=32)
    
    # Save the model
    model.save('models/traffic_lstm.h5')

def predict_traffic(model, new_data):
    # Preprocess new data
    X_new = preprocess_new_data(new_data)
    
    # Make predictions
    predictions = model.predict(X_new)
    return predictions