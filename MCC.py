#This is 100% modified condition coverage because it tests all the conditions in the if statement.

from MC_DC import is_leap_year

class TestMCC:

    def TestMcc(self):
        assert is_leap_year(2011) == False  # Tests condition1 = True, condition2 = False, condition3 = False
        assert is_leap_year(1900) == False  # Tests condition1 = True, condition2 = True, condition3 = False
        assert is_leap_year(3052) == True  # Tests condition1 = True, condition2 = False, condition3 = False
        assert is_leap_year(2100) == False  # Tests condition1 = True, condition2 = True, condition3 = False
        assert is_leap_year(3200) == True  # Tests condition1 = True, condition2 = True, condition3 = False

test = TestMCC()
test.TestMcc()
print("All tests passed.")