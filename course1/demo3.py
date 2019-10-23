"""
数据类型，异常
"""


def main():
    while input("是否退出程序(y/n) ? ") != 'y':
        data_str = input("请输入性别(男 or 女)，体重（KG），身高（CM），年龄（空格分割）：")
        try:
            data = data_str.split(" ");
            sex = data[0]
            weight = float(data[1])
            height = float(data[2])
            age = int(data[3])
            bmr = -1
            if sex == '男':
                bmr = 13.7*weight+5.0*height-6.8*age+66
            elif sex == '女':
                bmr = 9.6 * weight + 1.8 * height - 4.7 * age + 655
            if bmr != -1:
                print("您的输入的身高:{2},体重:{0},年龄:{1}".format(weight,age, height))
                print("您的BMR值为: {}".format(bmr))
            else:
                print("暂不支持该性别")
        except ValueError:
            print("数据信息输入错误")
        except IndexError:
            print("格式输入错误")
        except :
            print("程序错误")
        print()
        print("***************华丽的外衣*****************")
        print()


if __name__ == "__main__":
    main()
