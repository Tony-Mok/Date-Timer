class DateString:
    ''' A class containing year, month and day of a date
    '''
    def __init__(self, year: int, month: int, day: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    def __lt__(self, other):
        if self.year != other.year:
            # different year, then compare the year
            return self.year < other.year
        elif self.month != other.month:
            # the year is the same but month is different
            return self.month < other.month
        else:
            # year and month are the same, but the day might different
            return self.day < other.day

    @staticmethod
    def more_than_a_month_apart(date_str1, date_str2):
        ''' definition: A month is from some day to the same day in the following month,
        regardless of the number of days.  So, Jan 3rd to Feb 3rd is exactly one month.
        Jan 3rd to Feb 4th is more than a month.

        observation 1: only the edge cases is important, omit year diff >= 2
        observation 2: when the year diff == 1, the only case to be False will be Dec and next Jan
        '''

        # to make sure the ordering
        if date_str1 < date_str2:
            earlier_date, later_date = date_str1, date_str2
        else:
            earlier_date, later_date = date_str2, date_str1

        # case 1: year different > 1
        year_diff = later_date.year - earlier_date.year
        if year_diff >= 2:
            return True

        # case 2: year different == 0 or year different == 1
        # then we can simply convert the extra year to 13 .. 24 (next year Jan - next year Dec)
        earlier_month = earlier_date.month
        later_month = 12 * year_diff + later_date.month
        month_diff = later_month - earlier_month

        if month_diff == 0:
            # within the same month
            return False
        elif month_diff > 1:
            # difference more than one month
            return True
        else:
            # only one month apart, so need to check the day value for comparison
            return later_date.day > earlier_date.day
