
"""
current_datetime=datetime.datetime.now()

formatted_datetime = current_datetime.strftime("%d/%m/%Y %H:%M")


print(formatted_datetime)

print(current_datetime)
print(current_datetime.year)
print(current_datetime.month)
print(current_datetime.day)
print(current_datetime.date())
print(current_datetime.time())
print(current_datetime.weekday())
print(current_datetime.hour)
print(current_datetime.minute)
print(current_datetime.second)
print(current_datetime.microsecond)
"""

from datetime import datetime, timedelta

date1 = datetime(year=2024, month=9, day=1)
date2 = datetime(year=2023, month=9, day=1)

difference = date1 - date2
print(difference)

new_date = date1 + timedelta(days=10)
print(new_date)
