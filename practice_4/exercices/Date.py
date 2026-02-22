from datetime import datetime, timedelta

today = datetime.now()

yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print(today - timedelta(days=5))
print(f"Yesterday was: {yesterday.date()}")
print(f"Today is: {today.date()}")
print(f"Tomorrow will be: {tomorrow.date()}")
print(f"Current microseconds: {today.microsecond}")

# Input format example: 2026-02-18 14:30:00
date1_str = input("Enter first date (YYYY-MM-DD HH:MM:SS): ")
date2_str = input("Enter second date (YYYY-MM-DD HH:MM:SS): ")

# Convert strings to datetime objects
date1 = datetime.strptime(date1_str, "%Y-%m-%d %H:%M:%S")
date2 = datetime.strptime(date2_str, "%Y-%m-%d %H:%M:%S")

# Calculate difference
difference = abs((date2 - date1).total_seconds())

print(int(difference))
