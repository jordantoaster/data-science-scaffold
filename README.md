# data-science-scaffold
data-science-scaffold

## Setup - To get the project running (does not real world usage pattern)

- `export AZURE_STORAGE_ACCESS_KEY="<blob_access_key>"`
    - In the terminal where the runtime code is executed.
- `mlflow server --default-artifact-root "wasbs://mlflow@kedrotest.blob.core.windows.net/artifacts"`
    - For backend artifact store, and local mlruns metric level information.