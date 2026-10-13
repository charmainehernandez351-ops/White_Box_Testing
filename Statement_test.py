# this tests 100% statement coverage by entering both a leap year and a non-leap year but does not pass condiotn coverage 
# because it does not test the condition where year % 4 == 0 is true and year % 100 == 0 is true and year % 400 == 0 is false.
from leap_year import is_leap_year
def test_statment():
    assert is_leap_year(2020) == True
    assert is_leap_year(3050) == False
if __name__ == "__main__":
    test_statment()
    print("All tests passed.")