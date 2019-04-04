
## Module mycroft_lang_utils.lang.parse_it


    Parse functions for Italian (IT-IT)


### extract\_datetime\_it
 ```
 def extract_datetime_it(string, dateNow, default_time)
 ```
 
### extract\_numbers\_it
 ```
 def extract_numbers_it(text, short_scale=False, ordinals=False)
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
### extractnumber\_it
 ```
 def extractnumber_it(text, short_scale=False, ordinals=False)
 ```
 This function extracts a number from a text string,
handles pronunciations in long scale and short scale

https://en.wikipedia.org/wiki/Names_of_large_numbers

Args:
    text (str): the string to normalize
    short_scale (bool): use short scale if True, long scale if False
    ordinals (bool): consider ordinal numbers, third=3 instead of 1/3
Returns:
    (int) or (float) or False: The extracted number or False if no number
                               was found 
### extractnumber\_long\_it
 ```
 def extractnumber_long_it(word)
 ```
  This function converts a long textual number like
 milleventisette -> 1027 diecimila -> 10041 in
 integer value, covers from  0 to 999999999999999
 for now limited to 999_e21 but ready for 999_e63
 example:
    milleventisette -> 1027
    diecimilaquarantuno-> 10041
    centottomiladuecentotredici -> 108213
Args:
     word (str): the word to convert in number
Returns:
     (bool) or (int): The extracted number or False if no number
                               was found 
### get\_gender\_it
 ```
 def get_gender_it(word, raw_string='')
 ```
 In Italian to define the grammatical gender of a word is necessary
analyze the article that precedes the word and not only the last
letter of the word.

TODO: check if useful 
### isFractional\_it
 ```
 def isFractional_it(input_str, short_scale=False)
 ```
 This function takes the given text and checks if it is a fraction.
Updated to italian from en version 18.8.9

Args:
    input_str (str): the string to check if fractional
    short_scale (bool): use short scale if True, long scale if False
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### normalize\_it
 ```
 def normalize_it(text, remove_articles)
 ```
 IT string normalization 