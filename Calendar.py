from datetime import datetime
import calendar

dt = datetime.today()
dn = dt.weekday()

print("Today is day number: {0}".format(dn))
print("Today is a {0}".format(calendar.day_name[dn]))