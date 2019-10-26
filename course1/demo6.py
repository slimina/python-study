from datetime import datetime

# -*- coding: utf-8 -*-


def is_leap(year):
    if year % 400 == 0:
        return True
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False


def main():
    input_date_str = input('请输入日期(yyyy-mm-dd):')
    input_date = datetime.strptime(input_date_str, '%Y-%m-%d')
    year = input_date.year
    month = input_date.month
    day = input_date.day
    days_by_month = (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    days = day
    days += sum(days_by_month[:month-1])
    if is_leap(year) and month > 2:
        days += 1
    print("这是{}年的第{}天".format(year, days))

    days_by_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if is_leap(year):
        days_by_month[1] = 29
    print("这是{}年的第{}天".format(year, sum(days_by_month[:month-1])+day))

    _30_month = {4, 6, 9, 11}
    _31_month = {1, 3, 5, 7, 8, 10, 12}
    days = day
    for i in range(1, month):
        if i in _30_month:
            days += 30
        elif i in _31_month:
            days += 31
        else:
            days += 28
    if is_leap(year) and month > 2:
        days += 1
    print("这是{}年的第{}天".format(year, days))

    dd = {1: 31,
          2: 28,
          3: 31,
          4: 30,
          5: 31,
          6: 30,
          7: 31,
          8: 31,
          9: 30,
          10: 31,
          11: 30,
          12: 31}
    if is_leap(year):
        dd[2] = 29
    days = day
    for i in range(1, month):
        days += dd[i]
    print("这是{}年的第{}天".format(year, days))


if __name__ == '__main__':
    main()



