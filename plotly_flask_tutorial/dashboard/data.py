"""Prepare data for Plotly Dash."""
import numpy as np
import pandas as pd
from pandas import DataFrame
import json

def create_dataframe() -> DataFrame:
    with open("/app/data/jayden.json") as f:
        data = json.load(f)

    splits = len(data['statistics']['splits'])
    stats = len(data['statistics']['splits'][0]['stats'])

    df = pd.DataFrame([[float(data['statistics']['splits'][x]['stats'][y].replace(',', '')) for x in range(splits)] for y in range(stats)], 
                      index=[data['statistics']['names']], 
                      columns=[data['statistics']['splits'][y]['displayName'] for y in range(splits)])

    return df


'''
def create_dataframe() -> DataFrame:
    """Create Pandas DataFrame from local CSV."""
    df = pd.read_csv("data/calls.csv", parse_dates=["created"])
    df["created"] = df["created"].dt.date
    df.drop(columns=["incident_zip"], inplace=True)
    num_complaints = df["complaint_type"].value_counts()
    to_remove = num_complaints[num_complaints <= 30].index
    df.replace(to_remove, np.nan, inplace=True)
    return df
'''