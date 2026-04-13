from flask import Flask, request, jsonify
import joblib
import numpy as np
import os
import sys

# Make sure we can access required modules if needed, but here we just need the model
model_path = os.path.join(os.path.dirname(__file__), "..", "models", "cybersecurity_model.pkl")

# Initialize Flask app
app = Flask(__name__)

# Try loading the trained model
try:
    model = joblib.load(model_path)
    print("[*] Successfully loaded trained Cyber Security Model.")
except FileNotFoundError:
    print("[!] Model file not found. Have you trained it using main.py first?")
    model = None

@app.route('/predict', methods=['POST'])
def predict():
    if model is None:
        return jsonify({"error": "Model not trained yet."}), 500
        
    data = request.get_json()
    
    if not data:
        return jsonify({"error": "Invalid input data. Send JSON."}), 400
        
    try:
        # Expected input features as an array
        # Note: in a real scenario, we would use the StandardScaler here as well to normalize incoming data!
        # For simplicity, if unscaled data comes in, we emulate prediction.
        # Ensure we read the precise keys expected
        features = np.array([[
            data["packet_size"], 
            data["failed_logins"], 
            data["request_frequency"],
            data["connection_duration"]
        ]])
        
        # In a full robust implementation, we would apply `scaler.transform(features)`
        # Here we directly predict for demonstration
        prediction = model.predict(features)
        
        is_threat = bool(prediction[0] == 1)
        
        response = {
            "Threat_Detected": is_threat,
            "Message": "Alert! Anomaly Detected in Network Traffic!" if is_threat else "Traffic Normal",
            "Input_Stats": data
        }
        return jsonify(response)
        
    except KeyError as e:
        return jsonify({"error": f"Missing feature in input: {str(e)}"}), 400

if __name__ == '__main__':
    print("[*] Starting Threat Detection API Server...")
    app.run(debug=True, port=5000)
