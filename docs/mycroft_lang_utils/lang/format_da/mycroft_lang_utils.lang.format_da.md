
## Module mycroft_lang_utils.lang.format_da

### nice\_number\_da
 ```
 def nice_number_da(number, speech, denominators)
 ```
 Danish helper for nice_number
This function formats a float to human understandable functions. Like
4.5 becomes "4 einhalb" for speech and "4 1/2" for text
Args:
    number (int or float): the float to format
    speech (bool): format for speech (True) or display (False)
    denominators (iter of ints): denominators to use, default [1 .. 20]
Returns:
    (str): The formatted string. 
### nice\_ordinal\_da
 ```
 def nice_ordinal_da(text)
 ```
 
### nice\_response\_da
 ```
 def nice_response_da(text)
 ```
 
### nice\_time\_da
 ```
 def nice_time_da(dt, speech=True, use_24hour=False, use_ampm=False)
 ```
 Format a time to a comfortable human format

For example, generate 'five thirty' for speech or '5:30' for
text display.

Args:
    dt (datetime): date to format (assumes already in local timezone)
    speech (bool): format for speech (default/True) or display (False)=Fal
    use_24hour (bool): output in 24-hour/military or 12-hour format
    use_ampm (bool): include the am/pm for 12-hour format
Returns:
    (str): The formatted time string 
### pronounce\_number\_da
 ```
 def pronounce_number_da(num, places=2)
 ```
 Convert a number to its spoken equivalent
For example, '5.2' would return 'five point two'
Args:
    num(float or int): the number to pronounce (set limit below)
    places(int): maximum decimal places to speak
Returns:
    (str): The pronounced number 
### pronounce\_ordinal\_da
 ```
 def pronounce_ordinal_da(num)
 ```
