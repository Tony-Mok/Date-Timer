from solution import DateString

class TestDateSring:
    def test_lt(self):
        # all same
        date1 = DateString(2008, 10, 15)
        date2 = DateString(2008, 10, 15)
        is_less_than = date1 < date2
        assert is_less_than == False # they are equal

        # same year and month different day
        date1 = DateString(2008, 10, 15)
        date2 = DateString(2008, 10, 16)
        assert date1 < date2
        assert date2 > date1

        # same year same year and day but different month
        date1 = DateString(2008, 10, 15)
        date2 = DateString(2008, 11, 15)
        assert date1 < date2
        assert date2 > date1

        # all same, year diff
        date1 = DateString(2007, 10, 15)
        date2 = DateString(2008, 10, 15)
        assert date1 < date2
        assert date2 > date1

        # all same, year diff
        date1 = DateString(2007, 10, 15)
        date2 = DateString(2008, 3, 15)
        assert date1 < date2
        assert date2 > date1

    def test_more_than_a_month_apart(self):
        # same day
        date1 = DateString(2008, 10, 15)
        date2 = DateString(2008, 10, 15)
        assert DateString.more_than_a_month_apart(date1, date2) == False

        # 1 month apart
        date1 = DateString(2008, 10, 15)
        date2 = DateString(2008, 11, 15)
        assert DateString.more_than_a_month_apart(date1, date2) == False

        # 1 month + 1 day
        date1 = DateString(2008, 10, 15)
        date2 = DateString(2008, 11, 16)
        assert DateString.more_than_a_month_apart(date1, date2) == True

        # 1 month + 1 day (rev)
        date1 = DateString(2008, 11, 16)
        date2 = DateString(2008, 10, 15)
        assert DateString.more_than_a_month_apart(date1, date2) == True

        # boundary case
        date1 = DateString(2008, 12, 16)
        date2 = DateString(2009, 1, 16)
        assert DateString.more_than_a_month_apart(date1, date2) == False

        # boundary case
        date1 = DateString(2008, 12, 16)
        date2 = DateString(2009, 1, 17)
        assert DateString.more_than_a_month_apart(date1, date2) == True

        # boundary case (rev)
        date2 = DateString(2008, 12, 16)
        date1 = DateString(2009, 1, 17)
        assert DateString.more_than_a_month_apart(date1, date2) == True

        # diff year
        date2 = DateString(2008, 12, 16)
        date1 = DateString(2010, 1, 17)
        assert DateString.more_than_a_month_apart(date1, date2) == True
