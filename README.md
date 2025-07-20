# Password Analyzer

Password Analyzer is a project that evaluates the strength of user passwords using two machine learning models: a strength model and a time-to-crack model. It also integrates with the Gemini API to provide suggestions for stronger passwords.

## Features

- **Strength Model:** Predicts the overall strength rating of a password.
- **Time to Crack Model:** Estimates the time it would take to crack the password.
- **Gemini API Integration:** Suggests a very strong password if the entered password is weak.
- **Explanation:** Provides information on why a password is considered weak, helping users understand how to improve their password security.

## How It Works

1. The user submits a password to the API.
2. Features are extracted from the password.
3. The strength model predicts the password's strength rating.
4. The time-to-crack model estimates how long it would take to crack the password.
5. If the password is not very strong, the Gemini API suggests a stronger alternative.
6. The API returns the strength rating, estimated time to crack, a suggested stronger password (if applicable), and an explanation of why the password might be weak.

## Why Was My Password Weak?

Passwords are considered weak if they:

- Are too short.
- Use common patterns such as "12345" or repeated characters.
- Lack a mix of uppercase letters, lowercase letters, numbers, and special characters.
- Are easily guessable or found in common password lists.

To improve your password strength, use longer passwords with a combination of different character types and avoid common patterns.

## Technologies Used

- Python Flask for the backend API.
- Machine learning models for password strength and time-to-crack prediction.
- Gemini API for generating strong password suggestions.

## Getting Started

To run the project locally:

1. Install the required dependencies listed in `backend/requirements.txt`.
2. Run the Flask app in `backend/app.py`.
3. Use the frontend interface to input passwords and view analysis results.

## License

This project is licensed under the MIT License.
