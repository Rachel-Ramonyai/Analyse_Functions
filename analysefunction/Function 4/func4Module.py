#Function 1
def dictionary_of_metrics(items):
    """ 
    Write a function that calculates the mean, median, variance, standard deviation, 
    minimum and maximum of of list of items. You can assume the given list is contains 
    only numerical entries.
    """
    return{'mean': np.round(np.mean(np.array(items)),2),
         'median':np.median(np.array(items)),
         'var': np.round(np.var(np.array(items),ddof=1),2),
         'std': np.round(np.std(np.array(items),ddof=1),2),
         'min': min(np.array(items)),
         'max': max(np.array(items))}

#End of function 1 


#Function 2

'''
This function takes in a list of integers and returns a dictionary
'''
def five_num_summ(items):

    return {'max': max(items),
          'median': np.median(items),
          'min': min(items),
          'q1': np.quantile(items, q= 0.25),
          'q3': np.quantile(items, q= 0.75)}
#End of function 2


#Function 3
def date_parser(dates):

    storage = [] #create an empty list to store the dates
    #iterate through the parameter in order to access dates
    for i in dates:
            stor_var = i.split()   #splits the string 
            storage.append(stor_var[0])    #adds the date to storage list excluding time
    return storage  
#End of function 3


#Function 4
def extract_municipality_hashtags(df):

    '''
    This function takes a dataframe of tweets consisting of two columns (Tweets and Dates respectively)
    and returns a dataframe with with two new columns added: municipality; hashtags.

    municipality: this column contains the municipality mentioned in the tweet as per the supplied dictionary muni_dict.
    hashtags: this column contains the hashtags contained in the tweet.
    '''
    df_working = df.copy(deep = True)
    finder_keys = list(mun_dict.keys())
    finder_values = list(mun_dict.values())
    finder = '|'.join(finder_keys +finder_values)
    df_working.insert(2, 'municipality', df.Tweets.str.contains(finder).replace((True,False),('', np.nan))) #creates a column entry containing an empty string where a municipality (as defined by muni_dict) is present in the tweet. Otherwise returns NaN value.
    df_working.insert(3, 'hashtags', df.Tweets.str.contains('#').replace((True, False),('', np.nan)))   #creates a column entry containing an empty string if hashtags are present in the tweet. Otherwise returns NaN value. 
    finder_municipality = df_working[df.Tweets.str.contains(finder) == True].index.to_list()    #creates a list of indexes where municipalities have been indetified as per muni_dict
    finder_tags = df_working[df.Tweets.str.contains('#') == True].index.to_list()   #creates a list of indexes where hashtags are present in the tweet
    
    for index in finder_tags:   #stores the hashtags identified in a tweet as a list (tempy) and assigns that value to the hashtags column for that tweets's row index
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
    for index in finder_municipality:   #identifies the municipality identified in the tweet and either returns the muni_dict dictionary value at that key in the dictionary or directly assigns the value to the municipality column at that tweet's row index 
        magic = df_working.at[index, 'Tweets'].split()
        for items in magic:
            if items in finder_keys:
                df_working.at[index, 'municipality'] = mun_dict[items]
            elif items in finder_values:
                df_working.at[index, 'municipality'] = items
            elif items[-1]  == ':' : #helps properly identify a dictionary key/value if the last entry in that items string is ':'
                finder_2 = items[:-1]
                if finder_2 in finder_keys:
                    df_working.at[index, 'municipality'] = mun_dict[finder_2]
                elif finder_2 in finder_values:
                    df_working.at[index, 'municipality'] = finder_2
                    
    return df_working
#End of function 4


#Function 5
def number_of_tweets_per_day(df):

    '''
    Function groups tweets by date and counts the number of tweets for that day/date
    '''

    df_copy = df.copy(deep = True)
    df_copy['Date'] = pd.to_datetime(df_copy['Date']).dt.date  #returns date only,cutting tweet time
    byDate_copy = df_copy.groupby('Date').count().copy(deep = True)

    return byDate_copy

#End of function 5


#Function 6
def word_splitter(df):
'''
This function splits a sentence into a list of the separate words, it takes in a dataframe and return a data with a new column
'''
    df['split tweets']=df['Tweets'].str.lower().str.split(" ")

    return df
#End function 6


#Function 7
def stop_words_remover(df):
    """
    function which removes english stop words from a tweet.
    """
    
    def tweets(row):
        return [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
    df['Without Stop Words'] = df['Tweets'].apply(tweets)
    return df
#End of function 7
