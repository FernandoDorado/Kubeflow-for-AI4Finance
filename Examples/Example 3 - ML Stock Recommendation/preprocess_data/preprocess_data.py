import json
import pandas as pd
import os
import argparse
from pathlib import Path
import pickle


def _preprocess_data(args):
    

    # Load funtamental table
    inputfile_fundamental = args.fundamental_input
    fundamental_total = pd.read_excel(inputfile_fundamental)
    fundamental_total = fundamental_total[fundamental_total['tradedate'] < 20170901]
    
    # Get all unique quarterly date
    unique_datetime = sorted(fundamental_total.tradedate.unique())

    # Load sector data
    inputfile_sector = args.sector_input
    sector_data=pd.read_excel(inputfile_sector)
    # Get sector unique ticker
    unique_ticker=sorted(sector_data.tic.unique())



    # Set rolling window
        # train: 4 years = 16 quarters
        # test: 1 year = 4 quarters
        # so first trade date = #20 quarter
        #first trade date is 1995-06-01

    first_trade_date_index = args.first_trade_index


    # Testing window
    testing_windows = args.testing_window

    # Get all backtesting period trade dates
    trade_date=unique_datetime[first_trade_date_index:]
    
    #variable column name
    label_column = args.label_column
    date_column = args.date_column
    tic_column = args.tic_column
    
    # features column: different base on sectors
    no_feature_column_names = args.no_feature_column_names
    features_column = [x for x in sector_data.columns.values if x not in no_feature_column_names]
    
    #sector name
    sector_name = args.sector_name_input


    # Save data
    output_path = args.outputpath

    fundamental_total.to_csv(f'{output_path}/fundamental_total.csv', index = False)
    sector_data.to_csv(f'{output_path}/sector_data.csv', index = False)



if __name__ == '__main__':
    
    # This component does not receive any input
    # it only outpus one artifact which is `data`.
    parser = argparse.ArgumentParser()

    # Inputs

    # Sector name
    parser.add_argument('-sector_name','--sector_name_input', type=str,  required=True,help='sector name: i.e. sector10')

    # Filename
    parser.add_argument('-fundamental','--fundamental_input', type=str,  required=True,help='inputfile name for fundamental table')
    parser.add_argument('-sector','--sector_input', type=str,  required=True,help='inputfile name for individual sector')

    # Rolling windows variables
    # Sector name
    parser.add_argument("-first_trade_index", default=20, type=int)
    parser.add_argument("-testing_window", default=4, type=int)

    # Column name
    parser.add_argument("-label_column", default='y_return', type=str)
    parser.add_argument("-date_column", default='tradedate', type=str)
    parser.add_argument("-tic_column", default='tic', type=str)
    parser.add_argument("-no_feature_column_names", default = ['gvkey', 'tic', 'datadate', 'rdq', 'tradedate', 'fyearq', 'fqtr',
       'conm', 'datacqtr', 'datafqtr', 'gsector','y_return'], type=list,help='column names that are not fundamental features')


    # Outputs
    parser.add_argument('-outputpath', type=str)

    args = parser.parse_args()
    
    # Creating the directory where the output file will be created 
    # (the directory may or may not exist).
    os.makedirs(args.outputpath, exist_ok=True)



    _preprocess_data(args)
    