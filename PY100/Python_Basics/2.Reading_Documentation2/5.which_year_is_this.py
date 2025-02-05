# What is the difference between the year attribute and the isocalendar method?
from datetime import date

today = date.today()

today_year = today.year
iso_year = today.isocalendar()[0]
print(today.year)
print(today.isocalendar())

# Attribute `today` returns the local date
# Attribute `isocalendar` returns a tuple object wtih 3 componentws: year, week and weekday
