
## Module mycroft_lang_utils.lang.parse_common

### extract\_numbers\_generic
 ```
 def extract_numbers_generic(text, pronounce_handler, extract_handler, short_scale=True, ordinals=False)
 ```

Takes in a string and extracts a list of numbers.
Language agnostic, per language parsers need to be provided

Args:

    text (str): the string to extract a number from
    pronounce_handler (function): function that pronounces a number
    extract_handler (function): function that extracts the last number
    present in a string
    short_scale (bool): Use "short scale" or "long scale" for large
        numbers -- over a million.  The default is short scale, which
        is now common in most English speaking countries.
        See https://en.wikipedia.org/wiki/Names_of_large_numbers
    ordinals (bool): consider ordinal numbers, e.g. third=3 instead of 1/3
    
Returns:

    list: list of extracted numbers as floats 
    
### is\_numeric
 ```
 def is_numeric(input_str)
 ```
 
 Takes in a string and tests to see if it is a number.
 
Args:

    text (str): string to test if a number
    
Returns:

    (bool): True if a number, else False 
    
### look\_for\_fractions
 ```
 def look_for_fractions(split_list)
 ```


This function takes a list made by fraction & determines if a fraction.

Args:

    split_list (list): list created by splitting on '/'
    
Returns:

    (bool): False if not a fraction, otherwise True
   