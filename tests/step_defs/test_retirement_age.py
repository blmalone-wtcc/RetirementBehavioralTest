from pytest_bdd import scenario, given, when, then, parsers
from retirement_calculator import RetirementCalculator

EXTRA_TYPES = {'Number': int, 'String': str}
CONVERTERS = {'birth_year': int, 'years_old': int, 'months_old': int}


@scenario("retirement_age.feature", "The user enters a valid birth month", example_converters=CONVERTERS, features_base_dir="../features")
def test_nra():
    pass


@given("the user's birth year is <birth_year>", target_fixture="calc_nra")
def calc_nra(birth_year):
    assert isinstance(birth_year, int)
    return RetirementCalculator().getRetirementAge(year=int(birth_year))


@then("the user's full retirement age is <years_old>, <months_old>")
def validate_nra(calc_nra, years_old, months_old):
    assert calc_nra == (years_old, months_old)
