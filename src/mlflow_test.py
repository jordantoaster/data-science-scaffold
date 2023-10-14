import mlflow
import pandas as pd

# Assumes server running locally.
mlflow.set_tracking_uri("http://127.0.0.1:5000/")

exp_name = "exp1" 
mlflow.set_experiment(exp_name)

run_name = 'run1'
with mlflow.start_run(run_name=run_name):

    mlflow.log_metric("accuracy", 0.95)

    df = pd.DataFrame({'a': [1, 2, 3], 'b': [4, 5, 6]})
    df.to_csv('test.csv')

    # refers to local file.
    mlflow.log_artifact('test.csv', 'test_artifact_name.csv')
