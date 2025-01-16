from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Load the API key from the file
with open('api.txt', 'r') as file:
    MAP_API_KEY = file.read().strip()
# Define the Google Maps Directions API endpoint
DIRECTIONS_API_URL = "https://maps.googleapis.com/maps/api/directions/json"

@app.route('/directions', methods=['GET'])
def get_directions():
    # Get origin and destination from query parameters
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    if not origin or not destination:
        return jsonify({"error": "Origin and destination parameters are required"}), 400

    # Prepare the request parameters
    params = {
        'origin': origin,
        'destination': destination,
        'key': MAP_API_KEY
    }

    # Make the request to the Google Maps Directions API
    response = requests.get(DIRECTIONS_API_URL, params=params)

    # Check if the request was successful
    if response.status_code == 200:
        return jsonify(response.json())
    else:
        return jsonify({"error": "Failed to fetch directions"}), response.status_code

if __name__ == '__main__':
    app.run(debug=True)