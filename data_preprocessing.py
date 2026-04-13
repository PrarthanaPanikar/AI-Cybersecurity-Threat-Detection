import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

def generate_dummy_data(samples=1000, save_path="data/dataset.csv"):
    """
    Generates dummy network traffic data for simulation purposes
    since the user may not have downloaded the CICIDS dataset yet.
    """
    np.random.seed(42)
    data = {
        'packet_size': np.random.normal(500, 200, samples),
        'failed_logins': np.random.poisson(0.5, samples),
        'request_frequency': np.random.normal(50, 20, samples),
        'connection_duration': np.random.exponential(10, samples),
    }
    
    # Intentionally introducing anomalies (Threats)
    # Let's say 5% of data is anomalous
    num_anomalies = int(samples * 0.05)
    data['packet_size'][:num_anomalies] = np.random.normal(5000, 1000, num_anomalies)  # Large packets
    data['failed_logins'][:num_anomalies] = np.random.poisson(10, num_anomalies)     # Brute force
    data['request_frequency'][:num_anomalies] = np.random.normal(500, 100, num_anomalies) # DDoS representation
    
    df = pd.DataFrame(data)
    
    # 1 indicates Attack, 0 indicates Normal
    labels = np.zeros(samples)
    labels[:num_anomalies] = 1
    df['Attack_Label'] = labels
    
    # Save the generated dataset
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    df.to_csv(save_path, index=False)
    print(f"[*] Generated simulated dataset at {save_path}")
    return save_path

def load_and_preprocess_data(filepath):
    """
    Loads network dataset, scales features and returns splits.
    """
    print(f"[*] Loading dataset from {filepath}")
    df = pd.read_csv(filepath)
    
    # Separate Features and Labels
    X = df.drop("Attack_Label", axis=1)
    y = df["Attack_Label"]
    
    # Feature Scaling (Normalization)
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    
    # Splitting into training and test datasets
    X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)
    
    print(f"[*] Data Preprocessing Completed.")
    print(f"    Training samples: {X_train.shape[0]}, Testing samples: {X_test.shape[0]}")
    
    return X_train, X_test, y_train, y_test, scaler

if __name__ == "__main__":
    filepath = generate_dummy_data()
    load_and_preprocess_data(filepath)
