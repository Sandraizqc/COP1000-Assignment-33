# Function:     This program determines if a date entered by the user is valid.  
# Input:        Interactive
# Output:       Valid date is printed or user is alerted that an invalid date was entered.

validDate = True
MIN_YEAR = 0
MIN_MONTH = 1
MAX_MONTH = 12
MIN_DAY = 1
MAX_DAY = 31

year = None
month = None
day = None

# Get the year, then the month, then the day
# housekeeping()
print("Hello!! Let's see if your date is valid.")

year = int(input("First enter the year please: "))
month = int(input("Now enter the month: "))
day = int(input("Finally enter the day please: "))

# Check to be sure date is valid

if int(year) <= MIN_YEAR: # invalid year
    validDate = False
elif int(month) < MIN_MONTH or int(month) > MAX_MONTH: # invalid month
    validDate = False
elif int(day) < MIN_DAY or int(day) > MAX_DAY: # invalid day
    validDate = False

# Test to see if date is valid and output date and whether it is valid or not
else:
    if month in [4, 6, 9, 11] and day > 30:
        validDate = False
# endOfJob()
if validDate == True:
    # Output statement
     print(f"{month}/{day}/{year} is a valid date")
else:
    # Output statement
    print(f"{month}/{day}/{year} is an invalid date")
