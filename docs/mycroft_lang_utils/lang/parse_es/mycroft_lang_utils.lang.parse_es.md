
## Module mycroft_lang_utils.lang.parse_es


    Parse functions for spanish (es)
    TODO: numbers greater than 999999

### es\_number\_parse
 ```
 def es_number_parse(words, i)
 ```
 
### extract\_datetime\_es
 ```
 def extract_datetime_es(input_str, currentDate=None, default_time=None)
 ```
 
### extractnumber\_es
 ```
 def extractnumber_es(text)
 ```
 This function prepares the given text for parsing by making
numbers consistent, getting rid of contractions, etc.
Args:
    text (str): the string to normalize
Returns:
    (int) or (float): The value of extracted number 
### get\_gender\_es
 ```
 def get_gender_es(word, raw_string='')
 ```
 
### isFractional\_es
 ```
 def isFractional_es(input_str)
 ```
 This function takes the given text and checks if it is a fraction.

Args:
    text (str): the string to check if fractional
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### normalize\_es
 ```
 def normalize_es(text, remove_articles)
 ```
 Spanish string normalization 