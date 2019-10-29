# -*- coding: utf-8 -*-


def check_num(pwd_str):
    for s in pwd_str:
        if s.isnumeric():
            return True
    return False


def check_letter(pwd_str):
    for s in pwd_str:
        if s.isalpha():
            return True
    return False


def main():
    try_count = 5
    while try_count > 0:
        try_count -= 1
        pwd_str = input("请输入密码：")
        strength_level = 0
        if len(pwd_str) >= 8:
            strength_level += 1
        else:
            print("密码太短")
            continue

        if check_num(pwd_str):
            strength_level += 1
        else:
            print("密码需要包含数字")
            continue

        if check_letter(pwd_str):
            strength_level += 1
        else:
            print("密码需要包含字母")
            continue

        if strength_level >= 3:
            print("恭喜你！密码设置成功")
            break
        print()
    print("设置结束")


if __name__ == '__main__':
    main()
