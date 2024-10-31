import pandas as pd 

df = pd.read_csv('anime.csv', nrows=7421)

df.to_csv('anime.csv')