"""
try
<some code>
except <SomeException> as <SomeVariable>
except:
<generic Error>
else:
<when no exception occurs>
finally:
<after all exception handling is processed or no 
error occurs>
"""

try:
    x = y/0
except ZeroDivisionError as zde:
    print("You divided by zero!")
    print(zde)
except Exception as e:
    print("Some other exception")
    print(e)
else:
    print("You did not create an exception")
finally:
    print("All done now!")
    
try:
    raise Exception("This is an exception")
except Exception as e:
    print(e)
    raise