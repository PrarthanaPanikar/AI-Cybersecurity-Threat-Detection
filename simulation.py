import requests
import time
import random
import json

API_URL = "http://127.0.0.1:5000/predict"

def generate_traffic(is_attack=False):
    """
    Generates dummy traffic stats mimicking real queries.
    """
    if is_attack:
        return {
            "packet_size": random.randint(1500, 8000),      # Abnormally large packets
            "failed_logins": random.randint(5, 20),         # Repeated failed logins
            "request_frequency": random.randint(150, 600),  # High frequency
            "connection_duration": random.uniform(1.0, 50.0) # Variable durations
        }
    else:
        return {
            "packet_size": random.randint(100, 600),        # Normal operations
            "failed_logins": random.randint(0, 1),          # Standard user misclicks
            "request_frequency": random.randint(10, 50),    # Smooth web traffic
            "connection_duration": random.uniform(10.0, 100.0) # Typical durations
        }

def simulate_real_time_monitoring(duration_seconds=10):
    print("======================================================")
    print("   Cybersecurity SOC - Real-Time Threat Simulation")
    print("======================================================")
    print(f"Target API: {API_URL}")
    print(f"Simulating traffic for {duration_seconds} seconds...\n")
    
    start_time = time.time()
    traffic_count = 0
    threats_count = 0
    
    while time.time() - start_time < duration_seconds:
        traffic_count += 1
        
        # 20% Probability of generating attack traffic
        is_attack = random.random() < 0.2
        
        payload = generate_traffic(is_attack)
        
        try:
            response = requests.post(API_URL, json=payload)
            result = response.json()
            
            if response.status_code == 200:
                threat_detected = result.get("Threat_Detected", False)
                if threat_detected:
                    threats_count += 1
                    print(f"[!] ALERT: Suspicious Activity! Event {traffic_count} -> {payload}")
                else:
                    print(f"[-] Traffic Normal Event {traffic_count}.")
            else:
                print(f"[Error] API returned status {response.status_code} - {response.text}")
                
        except requests.exceptions.ConnectionError:
            print("[X] Connection Refused. Ensure predict.py (Flask API) is running!")
            break
        
        # Wait a bit before next traffic ping
        time.sleep(random.uniform(0.5, 1.5))
        
    print("\n======================================================")
    print("   Simulation Completed!")
    print(f"Total Traffic Events    : {traffic_count}")
    print(f"Total Threats Blocked   : {threats_count}")
    print("======================================================")

if __name__ == "__main__":
    simulate_real_time_monitoring(15)
