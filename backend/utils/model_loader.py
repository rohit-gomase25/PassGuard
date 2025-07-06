# Placeholder for model loading logic

import joblib
import os

MODELS_DIR = os.path.join(os.path.dirname(__file__), '..', 'models')

_strength_model = None
_time_crack_model = None

def load_strength_model():
    global _strength_model
    if _strength_model is None:
        _strength_model = joblib.load(os.path.join(MODELS_DIR, 'password_strength_model.pkl'))
    return _strength_model

def load_time_crack_model():
    global _time_crack_model
    if _time_crack_model is None:
        _time_crack_model = joblib.load(os.path.join(MODELS_DIR, 'time_to_crack_model.pkl'))
    return _time_crack_model 