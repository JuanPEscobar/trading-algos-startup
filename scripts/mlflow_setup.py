import mlflow
from mlflow.exceptions import MlflowException

# Servidor remoto compartido
mlflow.set_tracking_uri("https://8a1eecce0e44.ngrok-free.app")

experiment_name = "experiment_escobar"

try:
    # Intenta crear nuevo experimento
    experiment_id = mlflow.create_experiment(experiment_name)
    print(f"Experiment created with ID: {experiment_id}")
except MlflowException:
    # Ya existe, solo lo usamos
    experiment = mlflow.get_experiment_by_name(experiment_name)
    print(f"Using existing experiment with ID: {experiment.experiment_id}")