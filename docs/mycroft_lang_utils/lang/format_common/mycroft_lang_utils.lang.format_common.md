
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