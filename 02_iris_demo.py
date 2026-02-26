import wandb, joblib
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Initialize a new W&B run
wandb.init(project="sklearn-iris", config={"model":"RandomForestClassifier", "n_estimators": 100, "test_size":0.2})

# Load the Iris dataset
x, y = load_iris(return_X_y=True)

X_train, X_test, Y_train, Y_test = train_test_split(x, y, test_size=wandb.config.test_size, random_state=42)

# Train a Random Forest Classifier
model = RandomForestClassifier(n_estimators=wandb.config.n_estimators, random_state=42)
model.fit(X_train, Y_train)

# Make predictions and evaluate the model
predictions = model.predict(X_test)
accuracy = accuracy_score(Y_test, predictions)

# Log the accuracy to W&B
wandb.log({"accuracy": accuracy})

# Save the model using joblib and log it as an artifact
model_path = "random_forest_iris.pkl"
joblib.dump(model, model_path)

artifact = wandb.Artifact("random_forest_iris_model", type="model")
artifact.add_file(model_path)

wandb.log_artifact(artifact)

# Finish run
wandb.finish()