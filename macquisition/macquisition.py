import pandas as pd

#Acquisition method

def acquisition(path):
    df = pd.read_csv(path)
    return df