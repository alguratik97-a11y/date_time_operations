# Importing the datetime module
import datetime

# 1. Get the current date and time
current_time = datetime.datetime.now()
print("Current Date and Time:", current_time)

# 2. Extracting specific components (Year, Month, Day, Hour, Minute)
print("Year:", current_time.year)
print("Month:", current_time.month)
print("Day:", current_time.day)

# 3. Getting just the current date
current_date = datetime.date.today()
print("Current Date:", current_date)

# 4. Formatting dates using strftime()
# Format: Day-Month-Year Hour:Minute:Second
formatted_date = current_time.strftime("%d-%m-%Y %H:%M:%S")
print("Formatted Date & Time:", formatted_date)

# 5. Creating a custom date
custom_date = datetime.date(2026, 12, 25)
print("Custom Date:", custom_date)

# 6. Date arithmetic (Adding or subtracting days using timedelta)
future_date = current_date + datetime.timedelta(days=7)
print("Date after 7 days:", future_date)
