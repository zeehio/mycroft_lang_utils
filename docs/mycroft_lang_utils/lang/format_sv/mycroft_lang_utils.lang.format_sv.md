
## Module mycroft_lang_utils.lang.format_sv

### nice\_number\_sv
 ```
 def nice_number_sv(number, speech, denominators)
 ```
 Swedish helper for nice_number

This function formats a float to human understandable functions. Like
4.5 becomes "4 och en halv" for speech and "4 1/2" for text

Args:
    number (int or float): the float to format
    speech (bool): format for speech (True) or display (False)
    denominators (iter of ints): denominators to use, default [1 .. 20]
Returns:
    (str): The formatted string.