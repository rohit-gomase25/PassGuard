# Password Analyzer AI

A web app to analyze password strength and estimate time-to-crack using machine learning models.

## Project Structure

```
password-analyzer-ai/
├── frontend/
│   ├── public/
│   │   └── index.html
│   ├── src/
│   │   ├── components/
│   │   │   ├── PasswordInput.jsx
│   │   │   ├── StrengthMeter.jsx
│   │   │   ├── TimeDisplay.jsx
│   │   │   └── Results.jsx
│   │   ├── services/
│   │   │   └── api.js
│   │   ├── App.jsx
│   │   └── index.js
│   └── package.json
├── backend/
│   ├── app.py
│   ├── models/
│   │   ├── strength_model.pkl     # Your trained strength model
│   │   └── time_crack_model.pkl   # Your trained time-to-crack model
│   ├── utils/
│   │   ├── model_loader.py        # Load and use pkl files
│   │   └── helpers.py             # Helper functions
│   └── requirements.txt
└── README.md
``` 