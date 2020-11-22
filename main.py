import retirement_calculator as _calc
import calendar

retirement_calculator = _calc.RetirementCalculator()

print("Social Security Full Retirement Age Calculator")

prompt_for_input = True
while prompt_for_input:
    print("")
    year = str(input("Enter the year of birth or to exit ")).strip()

    while int(year) < 1900 or int(year) > 2999:
        print("Invalid year.")
        year = str(input("Enter the year of birth or to exit ")).strip()
    print("")

    prompt_for_month = (year != "")
    if prompt_for_month:

        month = str(input("Enter the month of birth ")).strip()
        while month not in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12']:
            print("Invalid month.")
            month = str(input("Enter the month of birth ")).strip()
        print("")

        retYear, retMonth = retirement_calculator.getRetirementAge(int(year))
        print("your full retirement age is", retYear, "and", retMonth, "months")
        print("")

        retireYear, retireMonth = retirement_calculator.getDateForFullBenefits(int(year), int(month))
        display_month = calendar.month_name[retireMonth]
        print("this will be in", display_month, "of", retireYear)
        print("")
