# Branch and Condition Coverage Test is 100% coverage but not MC/DC
# 100% condtion covers all 3 condtions given 
# 100% branch covers both true and false in the if statement
#not MCDC because it requires each condtion to independanlty change the outcome of the decision. 
def is_leap_year(year):
    condition1 = year % 4 == 0
    condition2 = year % 100 == 0
    condition3 = year % 400 == 0
    if (condition1 and not condition2) or condition3:
        return True
    else:
        return False
def branch_condition():
    assert is_leap_year(2024) == True
    assert is_leap_year(1900) == False
    assert is_leap_year(3050) == False
    assert is_leap_year(2000) == True
if __name__ == "__main__":
    branch_condition()
    print("All tests passed.")


