import os
import time
from src.data_preprocessing import generate_dummy_data, load_and_preprocess_data
from src.model_training import train_and_evaluate_model

def run_pipeline():
    print("==================================================")
    print("   AI-Powered Cybersecurity Threat Detection API")
    print("==================================================")
    print("\n[Stage 1] Checking Dataset...")
    
    data_path = os.path.join("data", "dataset.csv")
    if not os.path.exists(data_path):
        print("[*] Dataset not found. Simulating dummy network data...")
        generate_dummy_data(samples=2000, save_path=data_path)
    else:
        print("[*] Found existing dataset.")

    print("\n[Stage 2] Preprocessing Data...")
    X_train, X_test, y_train, y_test, scaler = load_and_preprocess_data(data_path)
    
    print("\n[Stage 3] Training ML Model (Random Forest)...")
    # Training the model and saving it
    model_path = os.path.join("models", "cybersecurity_model.pkl")
    model = train_and_evaluate_model(X_train, X_test, y_train, y_test, model_path=model_path)
    
    print("\n==================================================")
    print(" Pipeline Completed Successfully!")
    print(f" Model Output saved at: {model_path}")
    print(" Next Steps:")
    print(" 1. Run 'python src/predict.py' to start the Web API")
    print(" 2. Run 'python src/simulation.py' to simulate real-time attacks")
    print("==================================================")

if __name__ == "__main__":
    run_pipeline()
