from pytest_bdd import scenario, given, then, parsers
from retirement_calculator import RetirementCalculator

EXTRA_TYPES = {'Number': int, 'String': str}
CONVERTERS = {'birth_year': int, 'retirement_year': int, 'retirement_month': int}


@scenario("retirement_date.feature", "The enters a birth year to calculate their expected retirement date", example_converters=CONVERTERS, features_base_dir="../features")
def test_retirement_date():
    pass


@given("the user birth month is November and birth year is <birth_year>", target_fixture="calc_date")
def calc_date(birth_year):
    assert isinstance(birth_year, int)
    return RetirementCalculator().getDateForFullBenefits(year=int(birth_year), month=11)


@then("the user retirement date will be <retirement_year>, <retirement_month>")
def validate_date(calc_date, retirement_year, retirement_month):
    assert calc_date == (retirement_year, retirement_month)
