
## Module mycroft_lang_utils.lang.parse_en

### extract\_datetime\_en
 ```
 def extract_datetime_en(string, dateNow, default_time)
 ```
 Convert a human date reference into an exact datetime

Convert things like
    "today"
    "tomorrow afternoon"
    "next Tuesday at 4pm"
    "August 3rd"
into a datetime.  If a reference date is not provided, the current
local time is used.  Also consumes the words used to define the date
returning the remaining string.  For example, the string
   "what is Tuesday's weather forecast"
returns the date for the forthcoming Tuesday relative to the reference
date and the remainder string
   "what is weather forecast".

Args:
    string (str): string containing date words
    dateNow (datetime): A reference date/time for "tommorrow", etc
    default_time (time): Time to set if no time was found in the string

Returns:
    [datetime, str]: An array containing the datetime and the remaining
                     text not consumed in the parsing, or None if no
                     date or time related text was found. 
### extract\_duration\_en
 ```
 def extract_duration_en(text)
 ```
 Convert an english phrase into a number of seconds

Convert things like:
    "10 minute"
    "2 and a half hours"
    "3 days 8 hours 10 minutes and 49 seconds"
into an int, representing the total number of seconds.

The words used in the duration will be consumed, and
the remainder returned.

As an example, "set a timer for 5 minutes" would return
(300, "set a timer for").

Args:
    text (str): string containing a duration

Returns:
    (timedelta, str):
                A tuple containing the duration and the remaining text
                not consumed in the parsing. The first value will
                be None if no duration is found. The text returned
                will have whitespace stripped from the ends. 
### extract\_numbers\_en
 ```
 def extract_numbers_en(text, short_scale=True, ordinals=False)
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
### extractnumber\_en
 ```
 def extractnumber_en(text, short_scale=True, ordinals=False)
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
### isFractional\_en
 ```
 def isFractional_en(input_str, short_scale=True)
 ```
 This function takes the given text and checks if it is a fraction.

Args:
    input_str (str): the string to check if fractional
    short_scale (bool): use short scale if True, long scale if False
Returns:
    (bool) or (float): False if not a fraction, otherwise the fraction 
### normalize\_en
 ```
 def normalize_en(text, remove_articles)
 ```
 English string normalization 