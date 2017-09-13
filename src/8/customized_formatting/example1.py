_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d=self)


def test_datetime_date():
    from datetime import date
    d = date(2012, 12, 21)
    print(format(d))
    print(format(d, '%A, %B %d, %Y'))
    print('The end is {:%d %b %Y}. Goodbye'.format(d))


if __name__ == '__main__':
    d = Date(2012, 12, 21)
    print(format(d))
    print(format(d, 'mdy'))
    print('The date is {:ymd}'.format(d))
    print('The date is {:mdy}'.format(d))
    print("---test_datetime_date ---")
    test_datetime_date()
