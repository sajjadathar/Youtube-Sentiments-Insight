from mlflow.tracking import MlflowClient
import mlflow

mlflow.set_tracking_uri("http://ec2-3-133-149-243.us-east-2.compute.amazonaws.com:5000/")
client = MlflowClient()

print([m.name for m in client.search_registered_models()])