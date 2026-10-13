# this tests 100% statement coverage by entering both a leap year and a non-leap year but does not pass condiotn coverage 
# because it does not test the condition where year % 4 == 0 is true and year % 100 == 0 is true and year % 400 == 0 is false.
def is_leap_year(year):
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False
user_input = input("Enter year: ")
chosen_year = int(user_input)

if is_leap_year(chosen_year):
    print(f"{chosen_year} is a leap year.")
else:
    print(f"{chosen_year} is not a leap year.")