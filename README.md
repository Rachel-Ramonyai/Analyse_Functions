# Analyse Predict

This module was created to work with:  
    1) a Pandas dataframe containing tweets  
    2) a Pandas dataframe containing Eskom data  
The aim of this module is two extract insights from Eskom data/variables.The module itself is composed of seven different functions. The use of these functions is detailed below.

### Modules needed
- Numpy
- Pandas

# Function Components

### Default Data
The following data is available in this module in order to be used to illustrate the outputs one can expect from the functions therein: 
    - Twitter data dataframe: twitter_df
    - Dictionary of english stopwords: stop_words_dict
    - Dates for twitter tweets: dates
    - Metrics function testing string: gauteng

## Function 1: Metric Dictionary
    dictionary_of_metrics(items)

Function that calculates the mean, median, variance, standard deviation, minimum and maximum of a list of items. The functon itself takes in a list of items and returns calculated measures of central tendency. These metrics are returned in a dictionary containing: mean , median, standard deviation, variance , minimum value and maximum value.

**Function Specifications:**  
Args:  
    items(list): a list containing data across which the metrics will be calculated.  
Returns:  
    A dictionary containing the following metrics: mean (mean), median (median), variance (var), standard deviation (std), minimum value (min), maximum value (max).


## Function 2: Five Number Summary
    five_num_summ(items)

 This function also takes in a list of integers and calculates a five number summary. The function returns a dictionary containing the following metrics: maximum, median, minimum value, quartile 1 value and quartile 3 value

**Function Specifications:**  
Args:  
    items(list): a list containing data across which the metrics will be calculated.  
Returns:  
    A dictionary of the following metrics: maximum value (max), median (median), minimum value (min), quartile 1 (q1), quartile 3 (q3).


## Function 3: Date Parser
    date_parser(dates)

This function takes in a list of dates represented as strings containing the date in the `'yyyy-mm-dd'` format, as well as time in the `hh:mm:ss` formamt. The function then returns these datetime strings as dates in the `'yyyy-mm-dd'` format.

**Function Specifications:**  
Args:  
    dates (list of strings) : A list containing a string of dates that contain both the time and the date  
    
Returns:  
    storage (list of strings) : A list containing a string of dates without the time.


## Function 4: Municipality & Hashtag Detector
    extract_municipality_hashtags(df)

This function takes a dataframe of tweets consisting of two columns (Tweets and Dates respectively) and returns a modified dataframe that includes two new columns that contain information about the municipality and hashtag of the tweet. These columns are named 'municipality' and 'hashtags' in the modified dataframe. The municipalities in the tweets are identified as per the dictionary muni_dict.

**Function Specifications:**  
Args:  
    df (dataframe): A pandas dataframe consisting of two Columns (Tweets, Dates)  
Returns:  
    pandas dataframe with two new columns  
    municipality: this column contains the municipality mentioned in the tweet as per the supplied dictionary muni_dict.  
    hashtags: this column contains the hashtags contained in the tweet.


## Function 5: Number of Tweets per Day
    number_of_tweets_per_day(df)

This function calculates the number of tweets that were posted per day. The date returned is given in the format 'yyyy-mm-dd` as a datetime object.

**Function Specifications:**  
Args:  
    df(dataframe): A pandas dataframe dataframe consisting of two Columns (Tweets, Dates)  
Returns:  
    by_Date_copy(dataframe): A new dataframe grouped by Date with a Date column as well as number of tweets for that date/day


## Function 6: Word Splitter
    word_splitter(df)
    
This function splits tweets in the 'Tweets' column of the dataframe into a list of the separate words. The function then returns a modified dataframe with a new column `'Split Tweets'` containing the split tweets.

**Function Specifications:**  
Args:  
    df(dataframe): A dataframe consisting of two columns (Tweets, Date)  
Returns:  
    The function returns a modified dataframe with a new column ('Split Tweets'). This column contains the tokenized tweets from the 'Tweets' column.

## Function 7: Stop Words
    stop_words_remover(df)

This function removes english stop words from a tweets. The function returns a modified dataframe with a new column ('Without Stop Words) containing the split tweets from the 'Tweets' column without the stop words contained in the dictionary 'stop_words_dict'.

**Function Specifications:**  
Args:  
    df(dataframe): A pandas dataframe consisting of two columns (Tweets, Date)  
Returns:  
    The function returns a modified version of the dataframe with a new column ('Without Stop Words'). This column contains the tweets from the 'Tweets' column as a list without the stop words definned in 'stop_words_dict'.

# How To Use

## Installation
The module can be installed via: 
pip install git+https://github.com/londzy/Analyse_Functions.git

## Module Import
Module can be imported using:
from analysepackage import analyseModule

## Calling methods
The functions in the module can be called as follows:
analyseModule.five_num_summ()

## Using Default Data
The default data sets can be passed to the functons by calling them from analyseModule as follows:
analyseModule.five_num_summ(analyseModule.gauteng)

