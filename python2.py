import datetime
vandaag = datetime.datetime.today().weekday()

from datetime import date
import calendar
my_date = date.today()
dag = calendar.day_name[my_date.weekday()]
print("Het is vandaag " + dag + " en we eten:")

if dag == "Monday":
    print("pizza")
elif dag == "Tuesday":
    print("brocoli")
elif dag == "Wednesday":
    print("naasie")
elif dag == "Thursday":
    print("bami")
else:
    print("don't care")
