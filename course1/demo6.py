from datetime import datetime

# -*- coding: utf-8 -*-


def main():
    input_date_str = input('请输入日期(yyyy-mm-dd):')
    input_date = datetime.strptime(input_date_str,'%Y-%m-%d')


if __name__ == '__main__':
    main()



