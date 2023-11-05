import sys
import pandas as pd
import yaml
import os

def main():

    params = yaml.safe_load(open("params.yaml"))["featurize"]

    volume = params["volume"]

    df = pd.read_csv(params["input"])

    # Mock manipulate
    df.sample(volume)

    print(df.head())

    os.makedirs(params["output_directory"], exist_ok=True)
    df.to_csv(params["output_directory"] + params["output_filename"])

if __name__ == "__main__":
    main()