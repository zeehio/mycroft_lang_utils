
## Module mycroft_lang_utils.lang.parse_sv

### extract\_datetime\_sv
 ```
 def extract_datetime_sv(string, currentDate, default_time)
 ```
 
### extractnumber\_sv
 ```
 def extractnumber_sv(text)
 ```
 This function prepares the given text for parsing by making
numbers consistent, getting rid of contractions, etc.
Args:
    text (str): the string to normalize
Returns:
    (int) or (float): The value of extracted number 
### is\_fractional\_sv
 ```
 def is_fractional_sv(input_str)
 ```
 This function takes the given text and checks if it is a fraction.

Args:
    input_str (str): the string to check if fractional
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### normalize\_sv
 ```
 def normalize_sv(text, remove_articles)
 ```
 English string normalization 