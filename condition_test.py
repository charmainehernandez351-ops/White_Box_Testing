# this is 100% condition coverage because it tests the condition where year % 4 == 0 is true and year % 100 == 0 is true and year % 400 == 0 is false.
# its not 100% statement coverage and branch coverage because skips the return false statement 
from leap_year import is_leap_year
def test_condition():
    assert is_leap_year(2024) == True  # Tests condition1 = True, condition2 = True, condition3 = False
   
    assert is_leap_year(2000) == True  # Tests condition1 = True, condition2 = True, condition3 = True
   
if __name__ == "__main__":
    test_condition()
    print("All tests passed.")