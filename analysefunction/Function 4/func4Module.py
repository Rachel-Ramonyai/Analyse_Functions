#function 1
def dictionary_of_metrics(items):
  ### Code Here
    return{'mean': np.round(np.mean(np.array(items)),2),
         'median':np.median(np.array(items)),
         'variance' : np.round(np.var(np.array(items),ddof=1),2),
         'standard deviation': np.round(np.std(np.array(items),ddof=1),2),
         'min': min(np.array(items)),
         'max': max(np.array(items))}
#end of function 1 

#function 2
def five_num_summ(items):
  ### Code Here 
    return {'max': max(items),
            'median': np.median(items),
            'min': min(items),
            'q1': np.quantile(items, q= 0.25),
            'q3': np.quantile(items, q= 0.75)}
#End of function 2


#function 3
def date_parser(dates):
  ### Code Here
    storage = []
    for i in dates:
        stor_var = i.split()
        storage.append(stor_var[0])
    return storage  
#end of function 3

#function 4
### START FUNCTION
def extract_municipality_hashtags(df):

    municipality_dict ={ '@CityofCTAlerts' : 'Cape Town',
                '@CityPowerJhb' : 'Johannesburg',
                '@eThekwiniM' : 'eThekwini' ,
                '@EMMInfo' : 'Ekurhuleni',
                '@centlecutility' : 'Mangaung',
                '@NMBmunicipality' : 'Nelson Mandela Bay',
                '@CityTshwane' : 'Tshwane'}
    df_working = df.copy(deep = True)
    finder_keys = list(municipality_dict.keys())
    finder_values = list(municipality_dict.values())
    finder = '|'.join(finder_keys +finder_values) 
    
    df_working = df.copy(deep = True)
    finder_keys = list(mun_dict.keys())
    finder_values = list(mun_dict.values())
    finder = '|'.join(finder_keys +finder_values)
    df_working.insert(2, 'municipality', df.Tweets.str.contains(finder).replace((True,False),('', np.nan)))
    df_working.insert(3, 'hashtags', df.Tweets.str.contains('#').replace((True, False),('', np.nan)))
    finder_municipality = df_working[df.Tweets.str.contains(finder) == True].index.to_list()
    finder_tags = df_working[df.Tweets.str.contains('#') == True].index.to_list()
    
    for index in finder_tags:
        tempy = []
        magic = df_working.at[index, 'Tweets'].lower().split()
        for items in magic:
            if items[0] == '#':
                tempy.append(items)
                df_working.at[index, 'hashtags'] = tempy
            elif '#' in items:
                stop=1
                while stop !=-1:
                    if items[stop] == '#':
                        tempy.append(items[stop:])
                        df_working.at[index, 'hashtags'] = tempy
                        stop =-1
                    else: stop+=1
    for index in finder_municipality:
        magic = df_working.at[index, 'Tweets'].split()
        for items in magic:
            if items in finder_keys:
                df_working.at[index, 'municipality'] = mun_dict[items]
            elif items in finder_values:
                df_working.at[index, 'municipality'] = items
            elif items[-1]  == ':' :
                finder_2 = items[:-1]
                if finder_2 in finder_keys:
                    df_working.at[index, 'municipality'] = mun_dict[finder_2]
                elif finder_2 in finder_values:
                    df_working.at[index, 'municipality'] = finder_2
    return df_working
#End of function 4


#Function 5
def number_of_tweets_per_day(df):

    df_copy = df.copy(deep = True)
    df_copy['Date'] = pd.to_datetime(df_copy['Date']).dt.date
    byDate_copy = df_copy.groupby('Date').count().copy(deep = True)
    return byDate_copy
#End of function 5

#start function 6
def word_spliter(df):
    df['Split Tweets']=df['Tweets'].str.lower().str.split(" ")
    return df
#End function 6

#function 7
def stop_words_remover(df):
   
    # your code here
    def tweets(row):
        return [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
    df['Without Stop Words'] = df['Tweets'].apply(tweets)
    return df
#end if function 7 