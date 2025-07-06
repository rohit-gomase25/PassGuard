from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.model_loader import load_strength_model, load_time_crack_model
from utils.helpers import extract_features

app = Flask(__name__)
CORS(app)

strength_model = load_strength_model()
time_crack_model = load_time_crack_model()

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')
    features = extract_features(password)
    strength = strength_model.predict([features])[0]
    time_to_crack = time_crack_model.predict([features])[0]
    return jsonify({
        'strength': strength,
        'time_to_crack': float(time_to_crack)
    })

if __name__ == '__main__':
    app.run(debug=True) 