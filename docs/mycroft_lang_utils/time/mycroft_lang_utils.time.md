
## Module mycroft_lang_utils.time

### default\_timezone

 ```
 def default_timezone()
 ```

Get the default timezone

default system value

Returns:

    (datetime.tzinfo): Definition of the default timezone 
    
### now\_local

 ```
 def now_local(tz=None)
 
 ```
 
Retrieve the current time

Args:

    tz (datetime.tzinfo, optional): Timezone, default to user's settings

Returns:

    (datetime): The current time 
    
### now\_utc
 ```
 def now_utc()
 ```
 
 Retrieve the current time in UTC


Returns:

    (datetime): The current time in Universal Time, aka GMT 
    
### to\_local
 ```
 def to_local(dt)
 ```
 
 Convert a datetime to the user's local timezone

Args:

    dt (datetime): A datetime (if no timezone, defaults to UTC)
    
Returns:

    (datetime): time converted to the local timezone 
    
### to\_utc
 ```
 def to_utc(dt)
 ```
 
 Convert a datetime with timezone info to a UTC datetime

Args:

    dt (datetime): A datetime (presumably in some local zone)
    
Returns:

    (datetime): time converted to UTC