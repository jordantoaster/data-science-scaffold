# data-science-scaffold
data-science-scaffold

## Setup - To get the project running (does not real world usage pattern)

- `dvc init` (if from scratch)

- Pending

## Workflow

### Setup

- `dvc add data/0_raw/raw.csv` - ensure file not already git ignored or a error will occur.

- `dvc remote add -d myremote C:\Users\jorda\Desktop\data-science-scaffold\temp_remote` - temp remote, windows.

- `dvc push` to add files to the remote.

- `dvc pull` to get data fresh from the remote (IE for a user doing a fresh clone)

### if the data changes

- `dvc add ...` - add the change file.

- `dvc push` - usually with a git commit to make sure the change is commented upon in git.

### Checking out a specific version of the data in current branch - If you want to roll back a dataset.

- `git checkout HEAD~1 data/data.xml.dvc`
- `dvc checkout`
- `git commit data/data.xml.dvc -m "Revert dataset updates"`

To change versions of data, you change the dvc files in a branch, keeping synced with Git.

### Experiment Tracking - repeatable end to end.

#### Setup a working pipeline

Example - DVC uses the pipeline definition to automatically track the data used and produced by any stage, so there's no need to manually run dvc add for data/prepared 
```
stages:
  preprocess:
    cmd: python src/preprocess.py data/01_raw/raw.csv
    deps:
    - data/01_raw/raw.csv
    - src/preprocess.py
    params:
    - preprocess.multiplier = 10
    outs:
    - data/1_preprocessed
```
Notice that the source code itself is marked as a dependency as well. If any of these files change, DVC will know that this stage needs to be reproduced when the pipeline is executed.

- `dvc repro`

#### Track experiments


