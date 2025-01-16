from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
import joblib

def train_weather_model(data):
    # Preprocess data
    X = data.drop('impact', axis=1)
    y = data['impact']
    
    # Split data into training and testing sets
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Train the model
    model = RandomForestClassifier(n_estimators=100)
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f'Model accuracy: {accuracy}')
    
    # Save the model
    joblib.dump(model, 'models/weather_rf.pkl')

def predict_weather_impact(model, new_data):
    # Preprocess new data
    X_new = preprocess_new_data(new_data)
    
    # Make predictions
    predictions = model.predict(X_new)
    return predictions