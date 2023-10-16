import datetime

today_date = datetime.date.today()

print("🌟 Event Countdown Timer 🌟")
print()

event_name = input("What is the name of the event: ")
print()

year = int(input("Input the year: "))
month = int(input("What is the month: "))
day = int(input("What is the day: "))

event_date = datetime.date(year, month, day)

if event_date == today_date:
    print("Hurray! It's Today")
elif event_date > today_date:
    print("Coming in the future!")
else:
    print("Sad bruv, the day has gone")
