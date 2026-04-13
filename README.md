# AI-Powered Cybersecurity Threat Detection System - Complete Guide

This project acts as proof of work on GitHub. It uses Datasets and Virtual Simulation of cyber threats to provide a hands-on, beginner-friendly insight into cybersecurity event monitoring and anomaly detection. 

---

## A. Project Explanation

**What is AI-Powered Cybersecurity Threat Detection?**
Traditional enterprise security systems rely on rigid, static rules. For instance, "Block any user who fails login 5 times." The problem? Hackers have evolved. They can fail login 4 times, stop, switch IPs, and try again. AI-powered detection fixes this by looking at **behavioral patterns**. It learns what "Normal" network traffic looks like (e.g., standard packet sizes, connection durations) and flags "Anomalous" activity—such as an unusually large packet volume suddenly querying a database—as a potential threat. 

**What problems does it solve?**
* **Zero-day Attacks:** It can detect entirely new forms of malware where no pre-existing signature or rule exists. 
* **Alert Fatigue:** Traditional firewalls generate thousands of false alarms. ML models drastically minimize false positives.
* **Speed:** Threats are detected in real-time, preventing large-scale data breaches.

**Industry Use Cases:**
* Banks use it for **Fraud Detection** (Unusual transaction patterns).
* IT Companies use it for **Network Security Monitoring** (DDoS attack forecasting).
* Product companies use it for **Intrusion Detection** (Detecting unauthorized employee dataset access).

**Complete Workflow:**
1. **Data Collection:** Collect network logs (e.g., NSL-KDD, CICIDS2017 datasets).
2. **Preprocessing:** Clean missing values, normalize large numbers.
3. **Feature Engineering:** Select only the most crucial data fields (e.g., Packet Size, Requests).
4. **Model Training:** Train an AI Model (like Random Forest) to classify "Normal" vs. "Attack".
5. **Prediction & Alert Generation:** Deploy the model behind an API. As real traffic arrives, the model instantly predicts if it's an attack and generates alerts via dashboards.

---

## B. Tech Stack Options

**Option A: Easiest Version (Beginner)**
* **Tools:** Python, Pandas, Scikit-learn, Matplotlib
* **Dataset:** Small CSV files with limited features.
* **Algorithm:** Logistic Regression / Decision Tree.
* **Output:** A static Python script that prints "Accuracy: 95%". No GPU needed.

**Option B: Intermediate Version (Recommended)**
* **Tools:** Python, Scikit-Learn, Seaborn, Flask (API Server)
* **Dataset:** CICIDS Data subsets containing typical TCP/IP stats.
* **Algorithm:** Random Forest Classifier.
* **Output:** A working API where you can "ping" fake network requests and get Real-Time Alert popups in terminal. No GPU needed.

**Option C: Advanced Version (Pro/Research Level)**
* **Tools:** PyTorch/TensorFlow, Kafka, ElasticSearch/Kibana
* **Dataset:** Live PCAP files traversing a real mock network.
* **Algorithm:** Deep Neural Networks / Autoencoders.
* **Output:** Requires High GPU power, real-time dashboards mapping attacks by geography.

---

## C. Selected Approach

We will build **Option B (Intermediate Version)**.
It provides a **Strong GitHub Proof** because it demonstrates a full pipeline—not just a static Jupyter Notebook, but a deployed Flask API and a realistic simulated testing module—which recruiters love!

---

## D. Architecture

**Data Flow Block Diagram:**
```text
[ Raw Network Data (Dataframe) ] 
       |
       v
[ Preprocessing Module (StandardScaler) ]
       |
       v
[ Random Forest AI Model (Training) ] ---> [ Save as cybersecurity_model.pkl ]
       |
       v
[ Flask Backend API (Prediction Server) ]
       |
       ^  (JSON Payload: Traffic Stats)
       |
[ Virtual Simulation Script (Generates mock attacks/traffic) ] ---> [ ALERT GENERATED ]
```
The incoming network traffic stats are preprocessed. The Model analyzes them, and if classified as "Attack (1)", the prediction is passed to the Flask backend, which triggers a JSON Warning Payload.

---

## E. Folder Structure

```
AI-Cybersecurity-Threat-Detection/
│
├── data/                  # Stores CSV datasets (e.g. CICIDS2017 subset)
├── notebooks/             # (Optional) Jupyter notebooks for EDA and trial runs
├── src/                   # Main Source Code
│   ├── data_preprocessing.py  # Cleans, Scales data and generates simulated dataset
│   ├── model_training.py      # Trains the Random Forest and Evaluation metrics
│   ├── predict.py             # Flask API Server that hosts the deployed model
│   └── simulation.py          # Real-time mock ping simulator to trigger alerts
├── models/                # Saved trained Scikit-learn models (.pkl files)
├── images/                # Stored Output Graphs (Confusion Matrix)
├── outputs/               # Real-time logs and results
├── requirements.txt       # Dependencies
├── .gitignore             # Do not upload .pkl or massive data files
└── main.py                # Wrapper script to execute full training pipeline
```

---

## F. Installation & Environment Setup

**Prerequisites:** Python 3.8+ installed.

1. **Open Terminal / Command Prompt**
2. **Setup Virtual Environment:**
   *(Windows)* `python -m venv venv` 
   *(Mac/Linux)* `python3 -m venv venv`
3. **Activate Environment:**
   *(Windows)* `venv\Scripts\activate`
   *(Mac/Linux)* `source venv/bin/activate`
4. **Install Dependencies:**
   `pip install -r requirements.txt`

*(requirements.txt contains: pandas, numpy, scikit-learn, matplotlib, seaborn, flask, joblib)*

---

## G. Complete Working Code

All modular code is successfully initialized in your project workspace under `src/` and the root folder `main.py`. These files are already fully connected. 

---

## H. Virtual Simulation of Cyber Threats

Because we cannot risk hooking directly into a live router to capture real cyberattacks on a corporate level, we **Virtualize** it.

**How we do it:**
* We use a Python script (`src/simulation.py`) to generate infinite JSON payloads resembling HTTP Requests!
* **Normal Traffic Scenario:** Packet size is around 500 bytes. Login attempts = 0.
* **Threat Simulation Scenario:** Every few seconds, the loop forcefully generates a 5000-byte packet with 20 login failures (simulating a Brute-force + DDoS attack).
* This hits our `Flask` API. The AI evaluates the JSON numbers and physically prints `[!] ALERT: Suspicious Activity Detected!` in your server Terminal.

---

## I. Execution Steps (How to Run)

1. **Train Model First:**
   Run `python main.py`
   *(You will see the Data Loading, Model Training, Accuracy Output ~99%, and a Graph saved)*
2. **Start the API Server:**
   Run `python src/predict.py`
   *(This starts an active listener on port 5000)*
3. **Trigger Real-Time Threat Simulation:**
   Open a *New* separate terminal. Activate environment. 
   Run `python src/simulation.py`
   *(Watch the simulated network requests fly across the screen and the AI detect the anomalies automatically!)*

---

## J. GitHub Upload Strategy

To land internships, your Git history must look professional.

1. `git init` inside the project folder.
2. Initialize `.gitignore` restricting `venv/`, `__pycache__/`, and `*.pkl` to avoid heavy file bloat.
3. Take screenshots of your Confusion Matrix, your Terminal Output simulating threats, and place them in the `images/` directory.
4. Name your repo: **AI-Powered-Cybersecurity-Threat-Detection**. Add Topics: `#Cybersecurity, #MachineLearning, #Python, #DataScience`.

---

## L. Daily Commit Plan

* **Day 1:** Initial setup, requirements and dummy dataset pipeline. *(commit: "Setup env and Data gen engine")*
* **Day 2:** Data Cleaning and preprocessing implementation. *(commit: "Implemented StandardScaler data pipeline")*
* **Day 3:** Build Random Forest Classifier & Metrics. *(commit: "Integrated RF ML Model & Confusion Matrix Graph")*
* **Day 4:** API Deployment using Flask. *(commit: "Built Prediction API server")*
* **Day 5:** Cybersecurity Virtual simulation script. *(commit: "Added Real-Time Simulation logic for SOC alerts")*

---

## M. Proof Checklist for GitHub

| Item | Status | Action |
| --- | --- | --- |
| Confusion Matrix Plot | Required | Upload `images/confusion_matrix.png` to Readme. |
| Simulation Video (GIF) | Highly Recommended | Use a screen recorder showing your Flask Terminal reacting to `simulation.py`. |
| Evaluation Metrics | Required | Post "Accuracy: 99%" clearly inside the repository overview. |
