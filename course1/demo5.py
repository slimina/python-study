#!/usr/bin/env python3

# -*- coding: utf-8 -*-

import math

from datetime import datetime


'''
存入金额列表
'''
def save_money(week_add, week_count):
    amounts = []
    week_add = week_add
    week_amount = week_add
    week_count = week_count
    for i in range(week_count):
        amounts.append(week_amount)
        print("第{}周，存钱数为{},总共存钱:{}".format((i + 1), week_amount, math.fsum(amounts)))
        week_amount += week_add
    return amounts

def main():
    exit_status = True
    while exit_status:
        week_add = float(input("请输入每周递增金额:"))
        week_count = int(input("请输入存钱总周数:"))
        amounts = save_money(week_add, week_count)
        input_date_str = input('请输入日期(yyy-mm-dd):')
        input_date = datetime.strptime(input_date_str,'%Y-%m-%d')
        print(input_date.isocalendar())
        week_num = input_date.isocalendar()[1]
        print("第{}周存入金额:{}".format(week_num,amounts[week_num -1]))
        print()
        print("-----------------------------")
        print()
        exit_status = input("是否退出程序(y/n):") == 'n'

    print(range(10))
    print(list(range(10)))


if __name__ == '__main__':
    main()
