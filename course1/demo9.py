class Human:
    def __init__(self,name):
        self.name = name

    def say(self):
        print("我是{}".format(self.name))

    def __test(self):
        print("test")


class Chinese(Human):
    def say(self):
        super().say()
        print("Chinese say")


def main():
    chinese = Chinese('abc123')
    chinese.say()


if __name__ == '__main__':
    main()