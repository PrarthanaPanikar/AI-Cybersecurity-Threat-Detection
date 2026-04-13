import joblib
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import os

def train_and_evaluate_model(X_train, X_test, y_train, y_test, model_path="models/cybersecurity_model.pkl"):
    """
    Trains a Random Forest classifier to detect anomalies/attacks.
    Evaluates its performance and saves the model.
    """
    print("[*] Training Random Forest Classifier...")
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    
    print("[*] Generating predictions on test set...")
    y_pred = model.predict(X_test)
    
    print("--- Model Evaluation Metrics ---")
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Accuracy: {accuracy * 100:.2f}%\n")
    print(classification_report(y_test, y_pred, target_names=['Normal', 'Attack']))
    
    # Save Model
    os.makedirs(os.path.dirname(model_path), exist_ok=True)
    joblib.dump(model, model_path)
    print(f"[*] Model saved successfully at {model_path}")
    
    generate_confusion_matrix(y_test, y_pred)
    
    return model

def generate_confusion_matrix(y_test, y_pred, save_path="images/confusion_matrix.png"):
    """
    Generates and saves a confusion matrix visualization.
    """
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cm = confusion_matrix(y_test, y_pred)
    
    plt.figure(figsize=(6, 4))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=['Normal', 'Attack'], yticklabels=['Normal', 'Attack'])
    plt.xlabel("Predicted")
    plt.ylabel("Actual")
    plt.title("Cybersecurity Threat Detection - Confusion Matrix")
    plt.savefig(save_path)
    print(f"[*] Saved confusion matrix plot to {save_path}")

if __name__ == "__main__":
    from data_preprocessing import generate_dummy_data, load_and_preprocess_data
    filepath = generate_dummy_data()
    X_train, X_test, y_train, y_test, _ = load_and_preprocess_data(filepath)
    train_and_evaluate_model(X_train, X_test, y_train, y_test)
