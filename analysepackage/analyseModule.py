import pandas as pd
import numpy as np

ebp_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/electrification_by_province.csv'
ebp_df = pd.read_csv(ebp_url)

for col, row in ebp_df.iloc[:,1:].iteritems():
    ebp_df[col] = ebp_df[col].str.replace(',','').astype(int)

twitter_url = 'https://raw.githubusercontent.com/Explore-AI/Public-Data/master/Data/twitter_nov_2019.csv'
twitter_df = pd.read_csv(twitter_url)

# gauteng ebp data as a list
gauteng = ebp_df['Gauteng'].astype(float).to_list()

# dates for twitter tweets
dates = twitter_df['Date'].to_list()

# dictionary mapping official municipality twitter handles to the municipality name
mun_dict = {
    '@CityofCTAlerts' : 'Cape Town',
    '@CityPowerJhb' : 'Johannesburg',
    '@eThekwiniM' : 'eThekwini' ,
    '@EMMInfo' : 'Ekurhuleni',
    '@centlecutility' : 'Mangaung',
    '@NMBmunicipality' : 'Nelson Mandela Bay',
    '@CityTshwane' : 'Tshwane'
}

# dictionary of english stopwords
stop_words_dict = {
    'stopwords':[
        'where', 'done', 'if', 'before', 'll', 'very', 'keep', 'something', 'nothing', 'thereupon',
        'may', 'why', 'â€™s', 'therefore', 'you', 'with', 'towards', 'make', 'really', 'few', 'former',
        'during', 'mine', 'do', 'would', 'of', 'off', 'six', 'yourself', 'becoming', 'through',
        'seeming', 'hence', 'us', 'anywhere', 'regarding', 'whole', 'down', 'seem', 'whereas', 'to',
        'their', 'various', 'thereafter', 'â€˜d', 'above', 'put', 'sometime', 'moreover', 'whoever', 'although',
        'at', 'four', 'each', 'among', 'whatever', 'any', 'anyhow', 'herein', 'become', 'last', 'between', 'still',
        'was', 'almost', 'twelve', 'used', 'who', 'go', 'not', 'enough', 'well', 'â€™ve', 'might', 'see', 'whose',
        'everywhere', 'yourselves', 'across', 'myself', 'further', 'did', 'then', 'is', 'except', 'up', 'take',
        'became', 'however', 'many', 'thence', 'onto', 'â€˜m', 'my', 'own', 'must', 'wherein', 'elsewhere', 'behind',
        'becomes', 'alone', 'due', 'being', 'neither', 'a', 'over', 'beside', 'fifteen', 'meanwhile', 'upon', 'next',
        'forty', 'what', 'less', 'and', 'please', 'toward', 'about', 'below', 'hereafter', 'whether', 'yet', 'nor',
        'against', 'whereupon', 'top', 'first', 'three', 'show', 'per', 'five', 'two', 'ourselves', 'whenever',
        'get', 'thereby', 'noone', 'had', 'now', 'everyone', 'everything', 'nowhere', 'ca', 'though', 'least',
        'so', 'both', 'otherwise', 'whereby', 'unless', 'somewhere', 'give', 'formerly', 'â€™d', 'under',
        'while', 'empty', 'doing', 'besides', 'thus', 'this', 'anyone', 'its', 'after', 'bottom', 'call',
        'nâ€™t', 'name', 'even', 'eleven', 'by', 'from', 'when', 'or', 'anyway', 'how', 'the', 'all',
        'much', 'another', 'since', 'hundred', 'serious', 'â€˜ve', 'ever', 'out', 'full', 'themselves',
        'been', 'in', "'d", 'wherever', 'part', 'someone', 'therein', 'can', 'seemed', 'hereby', 'others',
        "'s", "'re", 'most', 'one', "n't", 'into', 'some', 'will', 'these', 'twenty', 'here', 'as', 'nobody',
        'also', 'along', 'than', 'anything', 'he', 'there', 'does', 'we', 'â€™ll', 'latterly', 'are', 'ten',
        'hers', 'should', 'they', 'â€˜s', 'either', 'am', 'be', 'perhaps', 'â€™re', 'only', 'namely', 'sixty',
        'made', "'m", 'always', 'those', 'have', 'again', 'her', 'once', 'ours', 'herself', 'else', 'has', 'nine',
        'more', 'sometimes', 'your', 'yours', 'that', 'around', 'his', 'indeed', 'mostly', 'cannot', 'â€˜ll', 'too',
        'seems', 'â€™m', 'himself', 'latter', 'whither', 'amount', 'other', 'nevertheless', 'whom', 'for', 'somehow',
        'beforehand', 'just', 'an', 'beyond', 'amongst', 'none', "'ve", 'say', 'via', 'but', 'often', 're', 'our',
        'because', 'rather', 'using', 'without', 'throughout', 'on', 'she', 'never', 'eight', 'no', 'hereupon',
        'them', 'whereafter', 'quite', 'which', 'move', 'thru', 'until', 'afterwards', 'fifty', 'i', 'itself', 'nâ€˜t',
        'him', 'could', 'front', 'within', 'â€˜re', 'back', 'such', 'already', 'several', 'side', 'whence', 'me',
        'same', 'were', 'it', 'every', 'third', 'together'
    ]
}


#Function 1
def dictionary_of_metrics(items):
    """ 
    Function that calculates the mean, median, variance, standard deviation
    minimum and maximum of of list of items.

    Args:
        items: which is a list of items.

    Returns: 
        It returns calculated measures of central tendency.
    """
    return{'mean': np.round(np.mean(np.array(items)),2),
         'median':np.median(np.array(items)),
         'var': np.round(np.var(np.array(items),ddof=1),2),
         'std': np.round(np.std(np.array(items),ddof=1),2),
         'min': min(np.array(items)),
         'max': max(np.array(items))}

#End of function 1 


#Function 2
def five_num_summ(items):
    '''
        This function takes in a list of integers and returns a dictionary
    '''
    return {'max': max(items),
          'median': np.median(items),
          'min': min(items),
          'q1': np.quantile(items, q= 0.25),
          'q3': np.quantile(items, q= 0.75)}
#End of function 2


#Function 3
def date_parser(dates):
    '''
    Creating a list of dates only wihout the time 

    Args:
        dates (string) : A list containing a string of dates that contain both the time and the date
    
    Returns:
        dates (string) : A list containing a string of dates without the time

    Example:
         >>>>>> dates=['2019-11-29 12:50:54',
         '2019-11-29 12:46:53']

         ['2019-11-29',2019-11-29]


    '''

    storage = [] #create an empty list to store the dates
    #iterate through the parameter in order to access dates
    for i in dates:
            stor_var = i.split()   #splits the string
            storage.append(stor_var[0])    #adds the date to storage list excluding time
    return storage  
#End of function 3


#Function 4
def extract_municipality_hashtags(df):

    """
    This function takes a dataframe of tweets consisting of two columns (Tweets and Dates respectively)
    and returns a dataframe with with two new columns added: municipality; hashtags.

    Args:
        df (dataframe): A pandas data frame consisting of two Columns (Tweets, Dates)
    Returns:
        pandas dataframe with two new columns
        municipality: this column contains the municipality mentioned in the tweet as per the supplied dictionary muni_dict.
        hashtags: this column contains the hashtags contained in the tweet.
    """
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
    Function calculates the number of tweets that were posted per  day

    Args:
        A pandas dataframe

    Returns:
        A  new dataframe grouped by Date with a Date column as well as number of tweets for that date/day
    '''

    df_copy = df.copy(deep = True)
    df_copy['Date'] = pd.to_datetime(df_copy['Date']).dt.date  #returns date only,cutting tweet time
    byDate_copy = df_copy.groupby('Date').count().copy(deep = True)

    return byDate_copy
#End of function 5


#Function 6
def word_splitter(df):
    '''
    This function splits a sentence into a list of the separate words, it takes in a dataframe and return a 
    data with a new column
    '''
    df['split tweets']=df['Tweets'].str.lower().str.split(" ")

    return df
#End function 6


#Function 7
def stop_words_remover(df):
    """
    Function that removes english stop words from a tweet.

    Args:
        dataframe: It takes in the dataframe that has column with tweets
        
    Returns:
        new dataframe:it returns dataframe with column that has tweets without the stop words.
    """
    def tweets(row):
        return [word for word in row.lower().split() if word not in stop_words_dict['stopwords']]
    df['Without Stop Words'] = df['Tweets'].apply(tweets)
    return df
#End of function 7
