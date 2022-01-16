import json
import pandas as pd

import argparse
from pathlib import Path

def _load_data(args):

    df = pd.read_csv('data/data.csv')


    df.to_csv('data/df_out.csv', index=False)  

if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--data', type=str)
    
    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    Path(args.data).parent.mkdir(parents=True, exist_ok=True)

    _load_data(args)
    