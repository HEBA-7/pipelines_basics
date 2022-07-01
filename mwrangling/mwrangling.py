import pandas as pd

#Wrangling method

def wrangling(df, year):
    df_filtred = df[df["Year"] == year]
    return df_filtred