
## Module mycroft_lang_utils.format

### nice\_date
 ```
 def nice_date(dt, lang=None, now=None)
 ```
 
 Format a datetime to a pronounceable date

For example, generates 'tuesday, june the fifth, 2018'

Args:

    dt (datetime): date to format (assumes already in local timezone)
    lang (string): the language to use, use Mycroft default language if not
        provided
    now (datetime): Current date. If provided, the returned date for speech
        will be shortened accordingly: No year is returned if now is in the
        same year as td, no month is returned if now is in the same month
        as td. If now and td is the same day, 'today' is returned.
        
Returns:

    (str): The formatted date string 
    
### nice\_date\_time
 ```
 def nice_date_time(dt, lang=None, now=None, use_24hour=False, use_ampm=False)
 ```
 
 Format a datetime to a pronounceable date and time

For example, generate 'tuesday, june the fifth, 2018 at five thirty'

Args:

    dt (datetime): date to format (assumes already in local timezone)
    lang (string): the language to use, use Mycroft default language if
        not provided
    now (datetime): Current date. If provided, the returned date for
        speech will be shortened accordingly: No year is returned if
        now is in the same year as td, no month is returned if now is
        in the same month as td. If now and td is the same day, 'today'
        is returned.
    use_24hour (bool): output in 24-hour/military or 12-hour format
    use_ampm (bool): include the am/pm for 12-hour format
    
Returns:

    (str): The formatted date time string 
    
### nice\_duration
 ```
 def nice_duration(duration, lang=None, speech=True)
 ```
 
 Convert duration in seconds to a nice spoken timespan

Examples:

   duration = 60  ->  "1:00" or "one minute"
   duration = 163  ->  "2:43" or "two minutes forty three seconds"

Args:

    duration: time, in seconds
    lang (str, optional): a BCP-47 language code, None for default
    speech (bool): format for speech (True) or display (False)
    
Returns:

    str: timespan as a string 
    
### nice\_number
 ```
 def nice_number(number, lang=None, speech=True, denominators=None)
 ```
 
 Format a float to human readable functions

This function formats a float to human understandable functions. Like
4.5 becomes 4 and a half for speech and 4 1/2 for text

Args:

    number (int or float): the float to format
    lang (str): code for the language to use
    speech (bool): format for speech (True) or display (False)
    denominators (iter of ints): denominators to use, default [1 .. 20]
    
Returns:

    (str): The formatted string. 
    
### nice\_time
 ```
 def nice_time(dt, lang=None, speech=True, use_24hour=False, use_ampm=False)
 ```
 
 Format a time to a comfortable human format

For example, generate 'five thirty' for speech or '5:30' for
text display.

Args:

    dt (datetime): date to format (assumes already in local timezone)
    lang (str): code for the language to use
    speech (bool): format for speech (default/True) or display (False)
    use_24hour (bool): output in 24-hour/military or 12-hour format
    use_ampm (bool): include the am/pm for 12-hour format
    
Returns:

    (str): The formatted time string 
    
### nice\_year
 ```
 def nice_year(dt, lang=None, bc=False)
 ```
 
 Format a datetime to a pronounceable year

For example, generate 'nineteen-hundred and eighty-four' for year 1984

Args:

    dt (datetime): date to format (assumes already in local timezone)
    lang (string): the language to use, use Mycroft default language if
    not provided
    bc (bool) pust B.C. after the year (python does not support dates
        B.C. in datetime)
        
Returns:

    (str): The formatted year string 
    
### pronounce\_number
 ```
 def pronounce_number(number, lang=None, places=2, short_scale=True, scientific=False)
 ```
 
 Convert a number to it's spoken equivalent

For example, '5' would be 'five'

Args:

    number: the number to pronounce
    short_scale (bool) : use short (True) or long scale (False)
        https://en.wikipedia.org/wiki/Names_of_large_numbers
    scientific (bool) : convert and pronounce in scientific notation
    
Returns:

    (str): The pronounced number
### expand\_options
 ```
 def expand_options(parentheses_line:str) -> list
 ```
 
 Convert 'test (a|b)' -> ['test a', 'test b']
 
Args:

    parentheses_line: Input line to expand
    
Returns:

    List of expanded possibilities 
    
### expand\_parentheses

 ```
 def expand_parentheses(sent)
 ```
 
['1', '(', '2', '|', '3, ')'] -> [['1', '2'], ['1', '3']]
 
For example:

Will it (rain|pour) (today|tomorrow|)?
---->
Will it rain today?
Will it rain tomorrow?
Will it rain?
Will it pour today?
Will it pour tomorrow?
Will it pour?

Args:

    sent (list<str>): List of tokens in sentence
    
Returns:

    list<list<str>>: Multiple possible sentences from original 
    
### join\_list
 ```
 def join_list(items, connector, sep=None, lang=None)
 ```
 
 Join a list into a phrase using the given connector word

Examples:
    join_list([1,2,3], "and") ->  "1, 2 and 3"
    join_list([1,2,3], "and", ";") ->  "1; 2 and 3"

Args:

    items(array): items to be joined
    connector(str): connecting word (resource name), like "and" or "or"
    sep(str, optional): separator character, default = ","
    
Returns:

    str: the connected list phrase 
    
