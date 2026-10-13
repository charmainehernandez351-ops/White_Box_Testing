# both true and false are executed in the if statement, so this is 100% branch coverage.
# not condition coverage because it does not test the condition where year % 4 == 0 is true and year % 100 == 0 is true and year % 400 == 0 is false.
from leap_year import is_leap_year
def test_branch():
    assert is_leap_year(2024) == True
    assert is_leap_year(1923) == False
if __name__ == "__main__":
    test_branch()
    print("All tests passed.")