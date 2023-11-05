import sys
import pandas as pd
import yaml
import os

def main():

    params = yaml.safe_load(open("params.yaml"))["preprocess"]

    multiplier = params["multiplier"]

    df = pd.read_csv(params["input"])

    # Mock manipulate
    df[['a', 'b']] = df[['a', 'b']].multiply(multiplier)

    print(df.tail())

    os.makedirs(params["output_directory"], exist_ok=True)
    df.to_csv(params["output_directory"] + "preprocessed.csv")

if __name__ == "__main__":
    main()