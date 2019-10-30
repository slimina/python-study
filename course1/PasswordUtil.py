# -*- coding: utf-8 -*-


"""
检查密码强度
"""


class PasswordUtil:
    def __init__(self, password):
        self.password = password
        self.strength_level = 0

    def check_num(self):
        for s in self.password:
            if s.isnumeric():
                return True
        return False

    def check_letter(self):
        for s in self.password:
            if s.isalpha():
                return True
        return False

    def check(self):
        if len(self.password) >= 8:
            self.strength_level += 1
        if self.check_num():
            self.strength_level += 1
        if self.check_letter():
            self.strength_level += 1


def main():
    try_count = 5
    while try_count > 0:
        try_count -= 1
        pwd_str = input("请输入密码：")
        password_util = PasswordUtil(pwd_str)
        password_util.check()
        if password_util.strength_level >= 3:
            print("恭喜你！密码设置成功")
            break
        print()
    print("程序退出.....")


if __name__ == '__main__':
    main()
