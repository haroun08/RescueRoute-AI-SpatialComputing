from flask import Flask, request, jsonify
from flask_cors import CORS
import googlemaps

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Initialize Google Maps API client (hardcoded API key for testing)
gmaps = googlemaps.Client(key='****')

@app.route('/directions', methods=['GET'])
def get_directions():
    origin = request.args.get('origin')
    destination = request.args.get('destination')

    if not origin or not destination:
        return jsonify({'error': 'Both origin and destination are required'}), 400

    try:
        # Request directions from Google Maps
        directions_result = gmaps.directions(
            origin,
            destination,
            mode="driving",
            departure_time="now",  # Real-time traffic
            traffic_model="best_guess",  # Optimize for current traffic conditions
            alternatives=True  # Provide alternative routes
        )
        return jsonify(directions_result)

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)