
## Module mycroft_lang_utils.lang

### get\_active\_lang
 ```
 def get_active_lang()
 ```
 
 Get the active full language code (BCP-47)

Returns:

    str: A BCP-47 language code, e.g. ("en-us", or "pt-pt") 
    
### get\_full\_lang\_code
 ```
 def get_full_lang_code(lang=None)
 ```
 
 Get the full language code

Args:

    lang (str, optional): A BCP-47 language code, or None for default

Returns:

    str: A full language code, such as "en-us" or "de-de" 
    
### get\_primary\_lang\_code
 ```
 def get_primary_lang_code(lang=None)
 ```
 
 Get the primary language code

Args:

    lang (str, optional): A BCP-47 language code, or None for default

Returns:

    str: A primary language family, such as "en", "de" or "pt" 
    
### set\_active\_lang
 ```
 def set_active_lang(lang_code)
 ```
 
 Set the active BCP-47 language code to be used in formatting/parsing


Args:

    lang (str): BCP-47 language code, e.g. "en-us" or "es-mx"
    

## Module mycroft_lang_utils.lang.format_common

### convert\_to\_mixed\_fraction
 ```
 def convert_to_mixed_fraction(number, denominators)
 ```
 
 Convert floats to components of a mixed fraction representation

Returns the closest fractional representation using the
provided denominators.  For example, 4.500002 would become
the whole number 4, the numerator 1 and the denominator 2

Args:

    number (float): number for convert
    denominators (iter of ints): denominators to use, default [1 .. 20]
    
Returns:

    whole, numerator, denominator (int): Integers of the mixed fraction
    

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
 "
This function takes a list made by fraction & determines if a fraction.

Args:
    split_list (list): list created by splitting on '/'
Returns:
    (bool): False if not a fraction, otherwise True
