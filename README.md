# Weights & Biases ML Experiments

This repository demonstrates how to use **Weights & Biases (W&B)** for experiment tracking in Python, starting from a simple *Hello World* example to a complete *machine learning workflow* using scikit-learn.


## Experiments Included

### 1 Hello World Experiment
A minimal example showing how to:
- Initialize a W&B run
- Log configurations
- Track simple metrics over time

**File:** `01_hello_world_wandb.py`

**What it logs:**
- A custom message
- Step-wise values
- Run metadata


### 2 Iris Classification (Machine Learning Experiment)
A complete ML pipeline using the Iris dataset and Random Forest.

**File:** `02_iris_demo.py`

**Features:**
- Loads Iris dataset
- Trains a RandomForestClassifier
- Evaluates accuracy
- Logs metrics to W&B
- Saves and versions the trained model using **W&B Artifacts**


## Experiment Tracking with W&B
For each run, W&B automatically tracks:
- Hyperparameters
- Metrics (accuracy, steps, etc.)
- Run history & summaries
- Model artifacts

*All experiments can be viewed on the W&B dashboard.*


## Technologies Used
- Python
- scikit-learn
- Weights & Biases (`wandb`)
- joblib



## Project Structure
wandb-ml-experiments/   
│  
├── .venv                     # virtual environment   
├── 01_hello_world_wandb.py   # Hello World W&B experiment  
├── 02_iris_demo.py           # Iris ML experiment with Random Forest  
├── 03_wandb_artifact.py      # file that save the model in artifact   
├── requirements.txt          # Project dependencies  
├── .gitignore                # Ignored files & folders  
└── README.md                 # Project documentation  



## Setup Instructions

### 1 Create Virtual Environment
```bash
python -m venv .venv
```  

### 2 Activate Virtual Environment
``` py
.venv\Scripts\Activate
```

### 3 Install Dependencies
``` py
pip install -r requirements.txt

``` 

### 4 Login to W&B
``` python
wandb login
```

## Run Experiments
### Hello World
```
python 01_hello_world_wandb.py
```
### Iris ML Experiment
```
python 02_iris_demo.py
```

## Model Artifacts

- Models are versioned and stored using W&B Artifacts
- This ensures clean repositories and reproducible experiments


## Learning Outcomes
This project demonstrates:
- Experiment tracking best practices
- ML metric logging
- Model versioning with W&B
- Clean ML project structure

<br>  

🧑‍💻 Author  
Hanseeka Dhingana


