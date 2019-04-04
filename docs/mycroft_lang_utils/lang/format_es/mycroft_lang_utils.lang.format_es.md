
## Module mycroft_lang_utils.lang.format_es


Format functions for castillian (es-es)


### nice\_number\_es
 ```
 def nice_number_es(number, speech, denominators)
 ```
 Spanish helper for nice_number

This function formats a float to human understandable functions. Like
4.5 becomes "4 y medio" for speech and "4 1/2" for text

Args:
    number (int or float): the float to format
    speech (bool): format for speech (True) or display (False)
    denominators (iter of ints): denominators to use, default [1 .. 20]
Returns:
    (str): The formatted string. 
### nice\_time\_es
 ```
 def nice_time_es(dt, speech=True, use_24hour=False, use_ampm=False)
 ```
 Format a time to a comfortable human format

For example, generate 'cinco treinta' for speech or '5:30' for
text display.

Args:
    dt (datetime): date to format (assumes already in local timezone)
    speech (bool): format for speech (default/True) or display (False)=Fal
    use_24hour (bool): output in 24-hour/military or 12-hour format
    use_ampm (bool): include the am/pm for 12-hour format
Returns:
    (str): The formatted time string 
### pronounce\_number\_es
 ```
 def pronounce_number_es(num, places=2)
 ```
 Convert a number to it's spoken equivalent

For example, '5.2' would return 'cinco coma dos'

Args:
    num(float or int): the number to pronounce (under 100)
    places(int): maximum decimal places to speak
Returns:
    (str): The pronounced number