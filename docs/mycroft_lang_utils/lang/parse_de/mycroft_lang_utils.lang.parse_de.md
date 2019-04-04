
## Module mycroft_lang_utils.lang.parse_de

### extract\_datetime\_de
 ```
 def extract_datetime_de(string, currentDate, default_time)
 ```
 
### extract\_numbers\_de
 ```
 def extract_numbers_de(text, short_scale=True, ordinals=False)
 ```
     Takes in a string and extracts a list of numbers.

Args:
    text (str): the string to extract a number from
    short_scale (bool): Use "short scale" or "long scale" for large
        numbers -- over a million.  The default is short scale, which
        is now common in most English speaking countries.
        See https://en.wikipedia.org/wiki/Names_of_large_numbers
    ordinals (bool): consider ordinal numbers, e.g. third=3 instead of 1/3
Returns:
    list: list of extracted numbers as floats 
### extractnumber\_de
 ```
 def extractnumber_de(text)
 ```
 This function prepares the given text for parsing by making
numbers consistent, getting rid of contractions, etc.
Args:
    text (str): the string to normalize
Returns:
    (int) or (float): The value of extracted number


undefined articles cannot be suppressed in German:
'ein Pferd' means 'one horse' and 'a horse' 
### isFractional\_de
 ```
 def isFractional_de(input_str)
 ```
 This function takes the given text and checks if it is a fraction.

Args:
    input_str (str): the string to check if fractional
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### isOrdinal\_de
 ```
 def isOrdinal_de(input_str)
 ```
 This function takes the given text and checks if it is an ordinal number.

Args:
    input_str (str): the string to check if ordinal
Returns:
    (bool) or (float): False if not an ordinal, otherwise the number
    corresponding to the ordinal

ordinals for 1, 3, 7 and 8 are irregular

only works for ordinals corresponding to the numbers in de_numbers 
### normalize\_de
 ```
 def normalize_de(text, remove_articles)
 ```
 German string normalization 