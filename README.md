# data-science-scaffold
data-science-scaffold

This is an inplace, realised variant of a setup scaffold, the setup process will vary off the starting Kedro Template (TBD).
IE you need a setup foundation, which manifests as the contents of this repo.

repo intended to prove use of Kedro on Azure for versioned storage and ability to call out to mlflow.
- Kedro data blob
- ML flow artifact blob
- postgres sql db

Ideally using mlflow backend in a shared, cross project manner.

## TODO

- In a compose app, run MLFLOW service as a service locally and dev environment as a service locally.

- Instructions for each project to create kedro scaffold, against a custom cookie cutter and play nice with Docker.
    - IE Kedro project is instantiated from scracth on each new fork of the project.

- Can you put the stuff outside the kedro folder inside it by modifying the cookie cutter template?

- Install kedro reqs from a bash script, all install a bash script? checks user install of kedro etc.

- pip install kedro-viz

- No need for a virtual env if in docker.

- How to make Kedro play nice with pipenv?

- multiple pipeline example, best practice on testing.

- https://docs.kedro.org/en/stable/kedro_project_setup/starters.html
    - add additional files needed, rmeove boilerplate.

- Kedro switch between local and remote data persistence easily?
    https://docs.kedro.org/en/stable/data/data_catalog.html#use-the-data-catalog-within-kedro-configuration
    kedro run --env=<env_name>

- How to automate some of the project specific stuff? project name when inserting into MLflow DB etc?

- debugging

- dep manage: https://docs.kedro.org/en/stable/kedro_project_setup/dependencies.html

- inject session store for experiment tracking in session.py with env vars.

- inject bucket etc to file paths in catalogs?

- Retention and backups for blob?
    - Some infra as code to spin it up in a standard way?

- Need for a core starter variant, then half aws or azure versions or starter than is fine on both of docs on both.

- Use Sphinx correctly.

## Setup - To get the project running (does not real world usage pattern)

- `source setup.sh`

- `cd iris-test`

- `pip install -r src/requirements.txt`

- From kedro root, `kedro run` or `kedro viz` or `pytest`

- Kedro vis, tracking.
- `export ACCOUNT_NAME=""` 
- `export ACCOUNT_KEY=""`