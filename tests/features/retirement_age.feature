Feature: I want to determine the age I will retire based on my birth year and birth month

@validYear
Scenario Outline: The user enters a valid birth month
	Given the user's birth year is <birth_year>
	Then the user's full retirement age is <years_old>, <months_old>

	Examples: Years
		| birth_year | years_old | months_old |
		| 1900	     | 65        | 0          |
		| 1937	     | 65        | 0          |
		| 1938	     | 65        | 2          |
		| 1939	     | 65        | 4          |
		| 1940	     | 65        | 6          |
		| 1941	     | 65        | 8          |
		| 1942	     | 65        | 10         |
		| 1943	     | 66        | 0          |
		| 1954	     | 66        | 0          |
		| 1955	     | 66        | 2          |
		| 1956	     | 66        | 4          |
		| 1957	     | 66        | 6          |
		| 1958	     | 66        | 8          |
		| 1959	     | 66        | 10         |
		| 1960	     | 67        | 0          |
		| 2020	     | 67        | 0          |
	    | 2021       | -1        | -1         |
	    | 1800       | -1        | -1         |


