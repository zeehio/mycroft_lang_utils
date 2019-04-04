
## Module mycroft_lang_utils.lang.parse_pt


    Parse functions for Portuguese (PT-PT)

    TODO: numbers greater than 999999
    TODO: date time pt

### extract\_datetime\_pt
 ```
 def extract_datetime_pt(input_str, currentDate, default_time)
 ```
 
### extractnumber\_pt
 ```
 def extractnumber_pt(text)
 ```
 This function prepares the given text for parsing by making
numbers consistent, getting rid of contractions, etc.
Args:
    text (str): the string to normalize
Returns:
    (int) or (float): The value of extracted number 
### get\_gender\_pt
 ```
 def get_gender_pt(word, raw_string='')
 ```
 
### isFractional\_pt
 ```
 def isFractional_pt(input_str)
 ```
 This function takes the given text and checks if it is a fraction.

Args:
    text (str): the string to check if fractional
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### normalize\_pt
 ```
 def normalize_pt(text, remove_articles)
 ```
 PT string normalization  
### pt\_number\_parse
 ```
 def pt_number_parse(words, i)
 ```
 
### pt\_pruning
 ```
 def pt_pruning(text, symbols=True, accents=True, agressive=True)
 ```
