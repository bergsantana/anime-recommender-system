import pandas as pd

def format_anime_list(file1  , output_file):
    df = pd.read_csv(file1)
    dfinal = pd.read_csv(output_file)

    print(dfinal.columns.to_list())

    data = {}

    size_columns =  dfinal.columns.to_list()[len(dfinal.columns.to_list()) -1]
    acc = 0
    for row in df.iterrows():
        # print(row[1].values) # linha
        index = row[1].values[0]
        user_id = row[1].values[1]
        anime_id = row[1].values[2]
        rating = row[1].values[3]
        
        # print(row[1].values[1])
        # print(row[1].values[2])
        # print(row[1].values[3])
        # print(row[1].values[4])
    
         

        if user_id not in data:
            # data[str(user_id)] = [None] * len(dfinal.columns.to_list())
            data[user_id] =  [None] * int( size_columns)
            data[user_id][anime_id] = rating
        else:
            data[user_id][anime_id] = rating
        
        # print(user_id)
        # print(data[user_id])
        print(f"acc - {acc}")
        #print(data[user_id])
        acc += 1
        # dfinal.at[index, 'user_id'] = user_id
        # dfinal.at[index, anime_id] = rating

   # dfinal.to_csv('teste-final.csv')

    return pd.DataFrame.from_dict(data, orient='index' ).to_csv('teste-final.csv')
        
    # columns = ['user_id']
    # data = []

    # all_anime = pd.read_csv('anime.csv')

    # for anime in all_anime.iterrows():
    #     print(anime[1].values[1])
    #     print(anime[1].values[0])
        
    #     columns.append(anime[1].values[0])



    # return pd.DataFrame(data=[], columns=columns).to_csv(output_file)
 


file1='./user-ratings.csv'
output='./user-ratings-final.csv'


format_anime_list(file1, output)
