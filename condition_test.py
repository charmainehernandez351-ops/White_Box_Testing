# this is 100% condition coverage because it tests the condition where year % 4 == 0 is true and year % 100 == 0 is true and year % 400 == 0 is false.
# its not 100% statement coverage and branch coverage because skips the return false statement 
def is_leap_year(year):
    condition1 = (year % 4 == 0)
    condition2 = (year % 100 != 0)
    condition3 = (year % 400 == 0)
    if condition1 and not condition2 and not condition3:
        return False
user_input = input("Enter year: ")
chosen_year = int(user_input)

if is_leap_year(chosen_year):
    print(f"{chosen_year} is a leap year.")
else:
    print(f"{chosen_year} is not a leap year.")