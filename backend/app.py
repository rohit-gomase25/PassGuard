from flask import Flask, request, jsonify
from flask_cors import CORS
from utils.model_loader import load_strength_model, load_time_crack_model
from utils.helpers import extract_features
import requests

app = Flask(__name__)
CORS(app)

strength_model = load_strength_model()
time_crack_model = load_time_crack_model()

GEMINI_API_KEY = "AIzaSyAvCIpACbRheH_a0_Mr59CqzCX5y7K9Fls"
GEMINI_API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key=" + GEMINI_API_KEY

def get_password_suggestion(password):
    prompt = f"Suggest a very strong password for a user who entered: '{password}'. Only suggest if the password is not very strong."
    data = {
        "contents": [
            {"parts": [{"text": prompt}]}
        ]
    }
    try:
        response = requests.post(GEMINI_API_URL, json=data)
        if response.status_code == 200:
            result = response.json()
            suggestion = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "")
            return suggestion
        else:
            return ""
    except Exception as e:
        return ""

@app.route('/api/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    password = data.get('password', '')
    features = extract_features(password)
    strength = strength_model.predict([features])[0]
    time_to_crack = time_crack_model.predict([features])[0]
    suggestion = get_password_suggestion(password)
    explanation = f"Your password '{password}' is rated as '{strength}'. Weak passwords are usually short, use common patterns (like '12345'), or lack a mix of uppercase, lowercase, numbers, and special characters. Consider using a longer password with more complexity."
    return jsonify({
        'strength': strength,
        'time_to_crack': float(time_to_crack),
        'suggestion': suggestion,
        'explanation': explanation
    })

if __name__ == '__main__':
    app.run(debug=True) 



