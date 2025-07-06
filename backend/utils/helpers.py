# Placeholder for helper functions 

import math
import re
from collections import Counter

FEATURES = [
    'length', 'num_uppercase', 'num_lowercase', 'num_digits', 'num_special',
    'entropy', 'has_sequence', 'has_repeated', 'has_common_word',
    'has_leet', 'has_year', 'has_keyboard_adjacent'
]

COMMON_WORDS = ['password', '123456', 'qwerty', 'letmein', 'admin', 'welcome']
LEET_MAP = {'4': 'a', '3': 'e', '1': 'i', '0': 'o', '$': 's', '@': 'a', '!': 'i'}
KEYBOARD_SEQUENCES = ['qwerty', 'asdf', 'zxcv', '1234', 'qaz', 'wsx', 'edc', 'rfv', 'tgb', 'yhn', 'ujm']


def calculate_entropy(password):
    pool = 0
    if re.search(r'[a-z]', password):
        pool += 26
    if re.search(r'[A-Z]', password):
        pool += 26
    if re.search(r'\d', password):
        pool += 10
    if re.search(r'[^a-zA-Z\d]', password):
        pool += 32
    if pool == 0:
        return 0
    return round(len(password) * math.log2(pool), 2)

def has_sequence(password):
    for i in range(len(password) - 2):
        if ord(password[i+1]) == ord(password[i]) + 1 and ord(password[i+2]) == ord(password[i+1]) + 1:
            return 1
    return 0

def has_repeated(password):
    return 1 if len(set(password)) < len(password) else 0

def has_common_word(password):
    lower = password.lower()
    for word in COMMON_WORDS:
        if word in lower:
            return 1
    return 0

def has_leet(password):
    for k, v in LEET_MAP.items():
        if k in password:
            return 1
    return 0

def has_year(password):
    return 1 if re.search(r'(19|20)\d{2}', password) else 0

def has_keyboard_adjacent(password):
    lower = password.lower()
    for seq in KEYBOARD_SEQUENCES:
        if seq in lower:
            return 1
    return 0

def extract_features(password):
    features = {
        'length': len(password),
        'num_uppercase': sum(1 for c in password if c.isupper()),
        'num_lowercase': sum(1 for c in password if c.islower()),
        'num_digits': sum(1 for c in password if c.isdigit()),
        'num_special': sum(1 for c in password if not c.isalnum()),
        'entropy': calculate_entropy(password),
        'has_sequence': has_sequence(password),
        'has_repeated': has_repeated(password),
        'has_common_word': has_common_word(password),
        'has_leet': has_leet(password),
        'has_year': has_year(password),
        'has_keyboard_adjacent': has_keyboard_adjacent(password)
    }
    return [features[f] for f in FEATURES] 