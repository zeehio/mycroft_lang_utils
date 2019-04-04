
## Module mycroft_lang_utils.lang.format_it

### nice\_number\_it
 ```
 def nice_number_it(number, speech, denominators)
 ```
 Italian helper for nice_number

This function formats a float to human understandable functions. Like
4.5 becomes "4 e un mezz" for speech and "4 1/2" for text

Args:
    number (int or float): the float to format
    speech (bool): format for speech (True) or display (False)
    denominators (iter of ints): denominators to use, default [1 .. 20]
Returns:
    (str): The formatted string. 
### nice\_time\_it
 ```
 def nice_time_it(dt, speech=True, use_24hour=False, use_ampm=False)
 ```
 Format a time to a comfortable human format
adapted to italian fron en version

For example, generate 'cinque e trenta' for speech or '5:30' for
text display.

Args:
    dt (datetime): date to format (assumes already in local timezone)
    speech (bool): format for speech (default/True) or display (False)=Fal
    use_24hour (bool): output in 24-hour/military or 12-hour format
    use_ampm (bool): include the am/pm for 12-hour format
Returns:
    (str): The formatted time string 
### pronounce\_number\_it
 ```
 def pronounce_number_it(num, places=2, short_scale=False, scientific=False)
 ```
 Convert a number to it's spoken equivalent
adapted to italian fron en version

For example, '5.2' would return 'cinque virgola due'

Args:
    num(float or int): the number to pronounce (under 100)
    places(int): maximum decimal places to speak
    short_scale (bool) : use short (True) or long scale (False)
        https://en.wikipedia.org/wiki/Names_of_large_numbers
    scientific (bool): pronounce in scientific notation
Returns:
    (str): The pronounced number