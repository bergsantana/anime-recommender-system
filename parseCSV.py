import pandas as pd

def format_anime_list(file1, file2, output_file):
    df1 = pd.read_csv(file1)
    df2 = pd.read_csv(file2)

    my_row = df1.loc[df1['MAL_ID'] == 43]
    
    df2['name'] = None

       
    print(df2.columns.tolist())
    print(df1.columns.tolist())

    acc = 1
    for row in df2.iterrows():
        # print(f"Linha do data frame")
        # print(row[1].values[1])
        try:

            anime_id = row[1].values[1]
        #     anime_id = row[2]
            name = df1[df1['MAL_ID'] == anime_id]
             
            # print(f"id - {anime_id}")
            # print(f"name - {name['Name']}")
            # print(type(name['Name']))
            # print(name['Name'].values[0])
        #     print(name['MAL_ID'])
        #     print(name['Name'].to_dict)
        #    #  row[6] = df1.loc[df1['MAL_ID'] == row[2]]
            df2.at[row[0], 'name'] = name['Name'].values[0]
        except Exception as e:
            print(f"ERROR")
            print(e)
        acc += 1
        if acc > 1222333:
            break
    df2.to_csv(output_file, index=False)


file1='anime.csv'
file2='rating_complete.csv'
output='updated-list.csv'

format_anime_list(file1, file2, output)
