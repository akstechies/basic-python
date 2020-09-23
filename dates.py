#datetime

import datetime

x = datetime.datetime.now()
print(x)
print(x.year)
print(x.strftime("%A"))
print(x.strftime('%B'))

y = datetime.datetime(2018, 5, 2)
print(y)
print(y.strftime('%B'))