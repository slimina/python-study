# -*- coding: utf-8 -*-


def main():
    f = open("abc.txt", 'w')
    f.write("你好 hello ! \n")
    f.write("test hello ! \n")
    f.write("人人 hello ! \n")
    f.close()

    f = open("abc.txt", 'r')
    print(f.read())
    f.close()
    print("--------------")

    f = open("abc.txt", 'r')
    for s in f:
        print(s)
    f.close()

    print("--------------")

    f = open("abc.txt", 'r')
    for s in f.readlines():
        print(s)
    f.close()


if __name__ == '__main__':
    main()
