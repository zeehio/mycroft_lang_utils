
## Module mycroft_lang_utils.lang.parse_fr

 Parse functions for french (fr)

    Todo:
        * extractnumber_fr: ordinal numbers ("cinquième")
        * extractnumber_fr: numbers greater than 999 999 ("cinq millions")
        * extract_datetime_fr: "quatrième lundi de janvier"
        * get_gender_fr

### extract\_datetime\_fr
 ```
 def extract_datetime_fr(string, currentDate, default_time)
 ```
 
### extract\_numbers\_fr
 ```
 def extract_numbers_fr(text, short_scale=True, ordinals=False)
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
### extractnumber\_fr
 ```
 def extractnumber_fr(text)
 ```
 Takes in a string and extracts a number.
Args:
    text (str): the string to extract a number from
Returns:
    (str): The number extracted or the original text. 
### getOrdinal\_fr
 ```
 def getOrdinal_fr(word)
 ```
 Get the ordinal number
Takes in a word (string without whitespace) and
extracts the ordinal number.
Args:
    word (string): the word to extract the number from
Returns:
    number (int)

    Returns None if no ordinal number was found. 
### isFractional\_fr
 ```
 def isFractional_fr(input_str)
 ```
 This function takes the given text and checks if it is a fraction.
Args:
    input_str (str): the string to check if fractional
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### normalize\_fr
 ```
 def normalize_fr(text, remove_articles)
 ```
 French string normalization  
### number\_ordinal\_fr
 ```
 def number_ordinal_fr(words, i)
 ```
 Find an ordinal number in a list of words
Takes in a list of words (strings without whitespace) and
extracts an ordinal number that starts at the given index.
Args:
    words (array): the list to extract a number from
    i (int): the index in words where to look for the ordinal number
Returns:
    tuple with ordinal number (str),
    index of next word after the number (int).

    Returns None if no ordinal number was found. 
### number\_parse\_fr
 ```
 def number_parse_fr(words, i)
 ```
 Parses a list of words to find a number
Takes in a list of words (strings without whitespace) and
extracts a number that starts at the given index.
Args:
    words (array): the list to extract a number from
    i (int): the index in words where to look for the number
Returns:
    tuple with number, index of next word after the number.

    Returns None if no number was found.