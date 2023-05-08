import imp
import pandas as pd 
import datatable as dt 
from dask import dataframe as dd 

file = "df.csv"

##CSV

df = pd.read_csv(file)


##datatable 
dsk_df = dt.fread(file)
dsk_df = dsk_df.to_pandas()

##Dask
dt_df = dd.read_csv(file)
dt_df = dt_df.compute()

