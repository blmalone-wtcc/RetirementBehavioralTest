Feature: I want to determine the date I will retire based on the year and month I was born.

  Scenario Outline: The enters a birth year to calculate their expected retirement date
    Given the user birth month is November and birth year is <birth_year>
    Then the user retirement date will be <retirement_year>, <retirement_month>

    Examples:
      | birth_year | retirement_year | retirement_month |
      | 1900       | 1965            | 11               |
      | 1937       | 2002            | 11               |
      | 1938       | 2004            | 1                |
      | 1939       | 2005            | 3                |
      | 1940       | 2006            | 5                |
      | 1941       | 2007            | 7                |
      | 1942       | 2008            | 9                |
      | 1943       | 2009            | 11               |
      | 1954       | 2020            | 11               |
      | 1955       | 2022            | 1                |
      | 1956       | 2023            | 3                |
      | 1957       | 2024            | 5                |
      | 1958       | 2025            | 7                |
      | 1959       | 2026            | 9                |
      | 1960       | 2027            | 11               |
      | 2020       | 2087            | 11               |
      | 2021       | -1              | -1               |
      | 1899       | -1              | -1               |


