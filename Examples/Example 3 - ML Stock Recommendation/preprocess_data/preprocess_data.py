import json
import pandas as pd
import os
import argparse
from pathlib import Path

def _preprocess_data(args):

    df = pd.read_csv('data/data.csv')
    df.to_csv('{}/data_out.csv'.format(args.outputpath), index=False)  

if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()
    parser.add_argument('--outputpath', type=str)
    
    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    os.makedirs(args.outputpath, exist_ok=True)



    _preprocess_data(args)
    