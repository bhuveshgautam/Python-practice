"""
Author: Chang Li
Function signatures given: nestEggFixed, nestEggVariable, postRetirement, findMaxExpenses
All test functions given; additional tests written
"""

import pydoc

def nestEggFixed(salary, save, growthRate, years):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: the annual percent increase in your investment account (an
      integer between 0 and 100).
    - years: the number of years to work.
    - return: a list whose values are the size of your retirement account at
      the end of each year.
    """
    # TODO: Your code here.
    # using recursion would be great, but I can't see how to pass both F and counter without modifying the parameters without using another function
    F = [0] * years
    for x in range(0, years):  # since one value was precalculated before the loop, must take last year off. Otherwise, a pop() would work too.
        savings = F[x - 1] * (1 + 0.01 * growthRate) + (salary * save * 0.01)
        F[x] = savings


    return F



def testNestEggFixed():
    salary     = 10000
    save       = 10
    growthRate = 15
    years      = 5
    savingsRecord = nestEggFixed(salary, save, growthRate, years)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2150.0, 3472.5, 4993.375, 6742.3812499999995]

    # TODO: Add more test cases here.
    savingsRecord = nestEggFixed(salary = 10000, save = 1, growthRate = 10, years = 5)  # multiline for each modified parameter like sample code is a pain
    print(savingsRecord)

    savingsRecord = nestEggFixed(salary = 10000, save = 1, growthRate = 20, years = 5)
    print(savingsRecord)

    savingsRecord = nestEggFixed(salary = 10000, save = 1, growthRate = 30, years = 5)
    print(savingsRecord)

    savingsRecord = nestEggFixed(salary = 10000, save = 1, growthRate = 40, years = 5)
    print(savingsRecord)

    # save gains are real
    savingsRecord = nestEggFixed(salary = 10000, save = 2, growthRate = 5, years = 5)
    print(savingsRecord)


#
# Problem 2
#

def nestEggVariable(salary, save, growthRates):
    # TODO: Your code here.
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - growthRate: a list of the annual percent increases in your investment
      account (integers between 0 and 100).
    - return: a list of your retirement account value at the end of each year.
    """

    F = [0] * len(growthRates)  # I forgot this was allowed in Python. Python why are you so great?
    for x in range(0, len(growthRates)):
        savings = F[x-1] * (1 + 0.01 * growthRates[x]) + (salary * save * 0.01)  # [1] Why specifically adding a case for the first year isn't necessary
        F[x] = savings

    return F

def testNestEggVariable():
    salary      = 10000
    save        = 10
    growthRates = [3, 4, 5, 0, 3]
    savingsRecord = nestEggVariable(salary, save, growthRates)
    print(savingsRecord)
    # Output should have values close to:
    # [1000.0, 2040.0, 3142.0, 4142.0, 5266.2600000000002]

    # TODO: Add more test cases here.

#
# Problem 3
#

def postRetirement(savings, growthRates, expenses):
    """
    - savings: the initial amount of money in your savings account.
    - growthRate: a list of the annual percent increases in your investment
      account (an integer between 0 and 100).
    - expenses: the amount of money you plan to spend each year during
      retirement.
    - return: a list of your retirement account value at the end of each year.
    """
    # TODO: Your code here.
    F = [savings * (1 + 0.01 * growthRates[0]) - expenses]
    for x in range(0, len(growthRates) - 1):
        # since growthRates is off by 1 compared to index, need to +1 within the function to offset the range. 
        # range must use len(growthRates)-1 or x has index error
        rem_balance = F[x] * (1 + 0.01 * growthRates[x + 1]) - expenses
        F.append(rem_balance)
    return F

def testPostRetirement():
    savings     = 100000
    growthRates = [10, 5, 0, 5, 1]
    expenses    = 30000
    savingsRecord = postRetirement(savings, growthRates, expenses)
    print(savingsRecord)
    # Output should have values close to:
    # [80000.000000000015, 54000.000000000015, 24000.000000000015,
    # -4799.9999999999854, -34847.999999999985]

    # TODO: Add more test cases here.
    growthRates = [5, 6, 7, 8, 9]

    savingsRecord = postRetirement(savings = 100000, growthRates = growthRates, expenses = 15000)
    print(savingsRecord)

    growthRates = [9, 8, 7, 6, 5]
    savingsRecord = postRetirement(savings = 100000, growthRates = growthRates, expenses = 15000)
    print(savingsRecord)

    growthRates = [5, 5, 5, 5, 5]
    savingsRecord = postRetirement(savings = 100000, growthRates = growthRates, expenses = 15000)
    print(savingsRecord)


#
# Problem 4
#

def findMaxExpenses(salary, save, preRetireGrowthRates, postRetireGrowthRates,
                    epsilon):
    """
    - salary: the amount of money you make each year.
    - save: the percent of your salary to save in the investment account each
      year (an integer between 0 and 100).
    - preRetireGrowthRates: a list of annual growth percentages on investments
      while you are still working.
    - postRetireGrowthRates: a list of annual growth percentages on investments
      while you are retired.
    - epsilon: an upper bound on the absolute value of the amount remaining in
      the investment fund at the end of retirement.
    """
    # the expenses only apply AFTER retirement, none while still working
    working_cashflow = nestEggVariable(salary, save, preRetireGrowthRates)
    retire_start_bal = working_cashflow[-1]
    low, high = 0, retire_start_bal
    est_expense = (low + high)/2  # start estimate right at the middle
    retire_cashflow = postRetirement(retire_start_bal, postRetireGrowthRates, est_expense)
    final_bal = retire_cashflow[-1]
    #print(retire_cashflow)
    #print("Estimated expense:", est_expense)
    while abs(final_bal) > epsilon:
        if final_bal > 0:  # positive balance remaining, make expenses higher
            low = est_expense
        else:  # negative balance, make expenses lower
            high = est_expense
        est_expense = (low + high)/2
        retire_cashflow = postRetirement(retire_start_bal, postRetireGrowthRates, est_expense)
        final_bal = retire_cashflow[-1]
        #print(retire_cashflow)
        #print("Estimated expense:", est_expense)

    return est_expense





def testFindMaxExpenses():
    salary                = 10000
    save                  = 10
    preRetireGrowthRates  = [3, 4, 5, 0, 3]
    postRetireGrowthRates = [10, 5, 0, 5, 1]
    epsilon               = .01
    expenses = findMaxExpenses(salary, save, preRetireGrowthRates,
                               postRetireGrowthRates, epsilon)
    print(expenses)
    # Output should have a value close to:
    # 1229.95548986
    preRetireGrowthRates  = [5, 4, 3, 2, 1]
    postRetireGrowthRates = [0, 0, 0, 0, 0]
    expenses = findMaxExpenses(salary = 10000, save = 10, preRetireGrowthRates = preRetireGrowthRates, postRetireGrowthRates = postRetireGrowthRates, epsilon = epsilon)
    print(expenses)
    
    preRetireGrowthRates  = [5, 4, 3, 2, 1]
    postRetireGrowthRates = [10, 10, 10, 10, 10]
    expenses = findMaxExpenses(salary = 10000, save = 10, preRetireGrowthRates = preRetireGrowthRates, postRetireGrowthRates = postRetireGrowthRates, epsilon = epsilon)
    print(expenses)
    
    
    preRetireGrowthRates  = [5, 4, 3, 2, 1]
    postRetireGrowthRates = [10, 10, 10, 10, 10]
    expenses = findMaxExpenses(salary = 10000, save = 5, preRetireGrowthRates = preRetireGrowthRates, postRetireGrowthRates = postRetireGrowthRates, epsilon = epsilon)
    print(expenses)
    


if __name__ == '__main__':
    testFindMaxExpenses()

"""
[1] Hilariously enough, since F[-1] is a valid index AND it contains 0, using F[x-1] for everything works.
If F were initialized with any other number, this would not have worked.
"""