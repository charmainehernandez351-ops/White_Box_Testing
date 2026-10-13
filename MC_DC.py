#Mc/DC test is 100% coverage because it tests all the conditions and branches in the if statement.
# its not MCC because it needs to test all 8 combinations of the 3 conditions in the if statement.
from Barnch_test import is_leap_year
def test_mcdc():
    assert is_leap_year(2024) == True  # Tests condition1 = True, condition2 = False, condition3 = False
    assert is_leap_year(1900) == False  # Tests condition1 = True, condition2 = True, condition3 = False
    assert is_leap_year(3052) == True  # Tests condition1 = True, condition2 = False, condition3 = False
    assert is_leap_year(1850) == False  # Tests condition1 = False, condition2 = False, condition3 = False
if __name__ == "__main__":
    test_mcdc()
    print("All tests passed.")