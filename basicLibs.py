#
#
# Python libraries basic exercise code
#
# Have fun!

# import date/time libs
from datetime import date
from datetime import  datetime
from datetime import timedelta

import calendar

def main():
    print("This is the main function\n")

    # Get today's date & time
    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    today = datetime.now()
    print("Today's date/time is:\n"
          + str(today.day) + "-" + str(today.month) + "-" + str(today.year)
          + "\n" + str(today.time()) + "\n" + str(weekdays[today.weekday()]))

    # Formatted printing %x locale's date, %X locale's time
    print("\nToday's date/time - formatted")
    print(today.strftime("%x") + "  " + today.strftime("%X"))

    # Printing a time delta
    print("\nA random time delta")
    print(timedelta(days=30, hours=12, minutes=15, seconds=24))

    # Printing today's date 100 years from now
    print("\nToday's date 100 years from now")
    print(str(today +  timedelta(days=30, hours=12, minutes=15, seconds=24)))

    # Comparing dates
    ams_reunion = date(today.year, 3, 30)
    if (date.today() > ams_reunion):
        print("You missed the reunion!." + "Today's date is: " + str(today.strftime("%x")))
        days_remaining_next = ams_reunion.replace(year=today.year + 1) - date.today()
        print(str(days_remaining_next.days) + " days to next year's reunion")
    elif (date.today() < ams_reunion):
        days_remaining = ams_reunion - date.today()
        print("Still time for the reunion. Days remaining: " + str(days_remaining.days))
    else:
        print("Today is the reunion day!")

    # Creating a calendar
    myCalendar = calendar.LocaleTextCalendar(calendar.MONDAY)
    print("\n")
    print(myCalendar.formatmonth(today.year, today.month))

if __name__ == '__main__':
    main()
