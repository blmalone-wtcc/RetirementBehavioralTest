class RetirementCalculator:

    def getRetirementAge(self, year):
        birth_year = 0
        birth_month = 0

        if year < 1937:
            if year >= 1900:
                birth_year = 65
            else:
                birth_year = -1
                birth_month = -1
        elif 1937 <= year & year < 1943:
            birth_year = 65
            birth_month = (year - 1937) * 2
        elif 1943 <= year & year < 1954:
            birth_year = 66
        elif 1954 <= year & year < 1960:
            birth_year = 66
            birth_month = (year - 1954) * 2
        elif year >= 1960:
            if year <= 2020:
                birth_year = 67
            else:
                birth_year = -1
                birth_month = -1
        else:
            birth_year = -1
            birth_month = -1

        return birth_year, birth_month

    def getDateForFullBenefits(self, year, month):
        retire_year = 0
        retire_month = 0

        ret_year, ret_month = self.getRetirementAge(year)
        if ret_year < 0:
            retire_year = -1
            retire_month = -1
            return retire_year, retire_month
        else:
            retire_month = month + ret_month

            while retire_month > 12:
                retire_month -= 12
                ret_year += 1

        retire_year = year + ret_year

        return retire_year, retire_month
