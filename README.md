# data-science-scaffold
data-science-scaffold

## Setup - To get the project running (does not real world usage pattern)

- `export AZURE_STORAGE_ACCESS_KEY="<blob_access_key>"`
    - In the terminal where the runtime code is executed.
- `mlflow server --default-artifact-root "wasbs://mlflow@kedrotest.blob.core.windows.net/artifacts"`
    - For backend artifact store, and local mlruns metric level information.
- `mlflow server --backend-store-uri 'postgresql://jordan:<PASSWORD>!@jmcd-mlflow-server.postgres.database.azure.com:5432/mlflowdb' --default-artifact-root 'wasbs://mlflow@kedrotest.blob.core.windows.net/artifacts'`
    - Azure Database for PostgreSQL flexible server, added my own IP address to firewall rules.
    - once MLFlow is pointed to DB, it setsup the tables for you.
- python src/mlflow_test.py