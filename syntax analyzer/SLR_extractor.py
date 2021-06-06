import pandas as pd
import numpy as np

df = pd.read_csv('SLR.csv')

for k in range(len(df)):
    print("{", end="")
    for index, value in df.loc[k].items():
        if str(value) != 'nan':
            if type(value) == str:
                print("'"+index+"'"+":", "'"+value.upper()+"'", end=", ")
            else :
                print("'"+index+"'"+":", int(value), end=", ")
    print("},")
