
import pandas as pd
import numpy as np
from nltk.tokenize import word_tokenize
from bs4 import BeautifulSoup
import unicodedata
import re
from nltk.corpus import stopwords
from nltk.corpus import wordnet
from nltk import pos_tag
from nltk import ne_chunk
from nltk.stem.porter import PorterStemmer
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.probability import FreqDist


def remove_html_tags_func(text):
    '''
    Removes HTML-Tags from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without HTML-Tags
    ''' 
    return BeautifulSoup(text, 'html.parser').get_text()


def remove_url_func(text):
    '''
    Removes URL addresses from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without URL addresses
    ''' 
    return re.sub(r'https?://\S+|www\.\S+', '', text)


def remove_accented_chars_func(text):
    '''
    Removes all accented characters from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without accented characters
    '''
    return unicodedata.normalize('NFKD', text).encode('ascii', 'ignore').decode('utf-8', 'ignore')


def remove_punctuation_func(text):
    '''
    Removes all punctuation from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without punctuations
    '''
    return re.sub(r'[^a-zA-Z0-9]', ' ', text)


def remove_irr_char_func(text):
    '''
    Removes all irrelevant characters (numbers and punctuation) from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without irrelevant characters
    '''
    return re.sub(r'[^a-zA-Z]', ' ', text)


def remove_extra_whitespaces_func(text):
    '''
    Removes extra whitespaces from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without extra whitespaces
    ''' 
    return re.sub(r'^\s*|\s\s*', ' ', text).strip()


def word_count_func(text):
    '''
    Counts words within a string
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Number of words within a string, integer
    ''' 
    return len(text.split())



from emo_dictonary import EMOTICONS

def emoticons_to_words_func(text):
    '''
    Convert Emoticons to Words
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string with converted Emoticons to Words
    ''' 
    for emot in EMOTICONS:
        emoticon_pattern = r'('+emot+')'
        # replace
        emoticon_words = EMOTICONS[emot]
        replace_text = emoticon_words.replace(",","")
        replace_text = replace_text.replace(":","")
        replace_text_list = replace_text.split()
        emoticon_name = '_'.join(replace_text_list)
        text = re.sub(emoticon_pattern, emoticon_name, text)
    return text



def chat_words_to_norm_words_func(text):
    '''
    Replaces common chat expressions with their spelled out form
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string with replaced chat expressions
    ''' 
    return re.sub(r'\S+', lambda m: chat_expressions_dict.get(m.group().upper(), m.group()) , text)



def sep_num_words_func(text):
    '''
    Separates numbers from words or other characters
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string with separated numbers from words or other characters
    ''' 
    return re.sub(r"([0-9]+(\.[0-9]+)?)",r" \1 ", text).strip() 


def num_to_words(text):
    '''
    Convert Numbers to Words
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string with converted Numbers to Words
    ''' 
    after_spliting = text.split()

    for index in range(len(after_spliting)):
        if after_spliting[index].isdigit():
            after_spliting[index] = num2words(after_spliting[index])
    numbers_to_words = ' '.join(after_spliting)
    return numbers_to_words



def remove_english_stopwords_func(text):
    '''
    Removes Stop Words (also capitalized) from a string, if present
    
    Args:
        text (str): String to which the function is to be applied, string
    
    Returns:
        Clean string without Stop Words
    ''' 
    # check in lowercase 
    t = [token for token in text if token.lower() not in stopwords.words("english")]
    text = ' '.join(t)    
    return text


def norm_stemming_func(text):
    '''
    Stemming tokens from string
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Use PorterStemmer() to stem the created tokens
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with stemmed words
    '''  
    words = word_tokenize(text)
    text = ' '.join([PorterStemmer().stem(word) for word in words])
    return text


def norm_lemm_func(text):
    '''
    Lemmatize tokens from string
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Use WordNetLemmatizer() to lemmatize the created tokens
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with lemmatized words
    '''  
    words = word_tokenize(text)
    text = ' '.join([WordNetLemmatizer().lemmatize(word) for word in words])
    return text


def norm_lemm_v_func(text):
    '''
    Lemmatize tokens from string 
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Use WordNetLemmatizer() to lemmatize the created tokens
            POS tag is set to 'v' for verb
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with lemmatized words
    '''  
    words = word_tokenize(text)
    text = ' '.join([WordNetLemmatizer().lemmatize(word, pos='v') for word in words])
    return text


def norm_lemm_a_func(text):
    '''
    Lemmatize tokens from string
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Use WordNetLemmatizer() to lemmatize the created tokens
            POS tag is set to 'a' for adjective
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with lemmatized words
    ''' 
    words = word_tokenize(text)
    text = ' '.join([WordNetLemmatizer().lemmatize(word, pos='a') for word in words])
    return text


def get_wordnet_pos_func(word):
    '''
    Maps the respective POS tag of a word to the format accepted by the lemmatizer of wordnet
    
    Args:
        word (str): Word to which the function is to be applied, string
    
    Returns:
        POS tag, readable for the lemmatizer of wordnet
    '''     
    tag = pos_tag([word])[0][1][0].upper()
    tag_dict = {"J": wordnet.ADJ,
                "N": wordnet.NOUN,
                "V": wordnet.VERB,
                "R": wordnet.ADV}

    return tag_dict.get(tag, wordnet.NOUN)


def norm_lemm_POS_tag_func(text):
    '''
    Lemmatize tokens from string
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Use WordNetLemmatizer() to lemmatize the created tokens
            POS tag is determined with the help of function get_wordnet_pos()
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with lemmatized words
    ''' 
    words = word_tokenize(text)
    text = ' '.join([WordNetLemmatizer().lemmatize(word, get_wordnet_pos_func(word)) for word in words])
    return text


def norm_lemm_v_a_func(text):
    '''
    Lemmatize tokens from string
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Use WordNetLemmatizer() with POS tag 'v' to lemmatize the created tokens
    Step 3: Use word_tokenize() to get tokens from generated string        
    Step 4: Use WordNetLemmatizer() with POS tag 'a' to lemmatize the created tokens
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with lemmatized words
    '''
    words1 = word_tokenize(text)
    text1 = ' '.join([WordNetLemmatizer().lemmatize(word, pos='v') for word in words1])
    words2 = word_tokenize(text1)
    text2 = ' '.join([WordNetLemmatizer().lemmatize(word, pos='a') for word in words2])
    return text2


def remove_single_char_func(text, threshold=1):
    '''
    Removes single characters from string, if present
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Removes words whose length falls below the threshold (by default = 1)
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        String with removed words whose length was below the threshold (by default = 1)
    ''' 
    threshold = threshold
    
    words = word_tokenize(text)
    text = ' '.join([word for word in words if len(word) > threshold])
    return text


def token_and_unique_word_count_func(text):
    '''
    Outputs the number of words and unique words
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Uses the FreqDist function to count unique words
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Prints:
        Number of existing tokens and number of unique words
    ''' 
    words = word_tokenize(text)
    fdist = FreqDist(words) 
    
    print('Number of tokens: ' + str(len(words))) 
    print('Number of unique words: ' + str(len(fdist)))


def most_common_word_func(text, n_words=25):
    '''
    Returns a DataFrame with the most commonly used words from a text with their frequencies
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Uses the FreqDist function to determine the word frequency
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        A DataFrame with the most commonly occurring words (by default = 25) with their frequencies
    ''' 
    words = word_tokenize(text)
    fdist = FreqDist(words) 
    
    n_words = n_words
    
    df_fdist = pd.DataFrame({'Word': fdist.keys(),
                             'Frequency': fdist.values()})
    df_fdist = df_fdist.sort_values(by='Frequency', ascending=False).head(n_words)
    
    return df_fdist


def least_common_word_func(text, n_words=25):
    '''
    Returns a DataFrame with the least commonly used words from a text with their frequencies
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Uses the FreqDist function to determine the word frequency
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        A DataFrame with the least commonly occurring words (by default = 25) with their frequencies
    ''' 
    words = word_tokenize(text)
    fdist = FreqDist(words) 
    
    n_words = n_words
    
    df_fdist = pd.DataFrame({'Word': fdist.keys(),
                             'Frequency': fdist.values()})
    df_fdist = df_fdist.sort_values(by='Frequency', ascending=False).tail(n_words)
    
    return df_fdist


def single_word_remove_func(text, word_2_remove):
    '''
    Removes a specific word from string, if present
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Removes the defined word from the created tokens
    
    Args:
        text (str): String to which the functions are to be applied, string
        word_2_remove (str): Word to be removed from the text, string
    
    Returns:
        String with removed words
    '''    
    word_to_remove = word_2_remove
    
    words = word_tokenize(text)
    text = ' '.join([word for word in words if word != word_to_remove])
    return text


def multiple_word_remove_func(text, words_2_remove_list):
    '''
    Removes certain words from string, if present
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Removes the defined words from the created tokens
    
    Args:
        text (str): String to which the functions are to be applied, string
        words_2_remove_list (list): Words to be removed from the text, list of strings
    
    Returns:
        String with removed words
    '''     
    words_to_remove_list = words_2_remove_list
    
    words = word_tokenize(text)
    text = ' '.join([word for word in words if word not in words_to_remove_list])
    return text


def most_freq_word_func(text, n_words=5):
    '''
    Returns the most frequently used words from a text
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Uses the FreqDist function to determine the word frequency
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        List of the most frequently occurring words (by default = 5)
    ''' 
    words = word_tokenize(text)
    fdist = FreqDist(words) 
    
    df_fdist = pd.DataFrame({'Word': fdist.keys(),
                             'Frequency': fdist.values()})
    df_fdist = df_fdist.sort_values(by='Frequency', ascending=False)
    
    n_words = n_words
    most_freq_words_list = list(df_fdist['Word'][0:n_words])
    
    return most_freq_words_list


def most_rare_word_func(text, n_words=5):
    '''
    Returns the most rarely used words from a text
    
    Step 1: Use word_tokenize() to get tokens from string
    Step 2: Uses the FreqDist function to determine the word frequency
    
    Args:
        text (str): String to which the functions are to be applied, string
    
    Returns:
        List of the most rarely occurring words (by default = 5)
    ''' 
    words = word_tokenize(text)
    fdist = FreqDist(words) 
    
    df_fdist = pd.DataFrame({'Word': fdist.keys(),
                             'Frequency': fdist.values()})
    df_fdist = df_fdist.sort_values(by='Frequency', ascending=False)
    
    n_words = n_words
    most_rare_words_list = list(df_fdist['Word'][-n_words:])
    
    return most_rare_words_list

