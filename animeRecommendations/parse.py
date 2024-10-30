import pandas as pd

def selectFirstLines():
    df1 = pd.read_csv('updated-list.csv', nrows=300000)

    df1.to_csv('user-ratings.csv')

    print('END')



