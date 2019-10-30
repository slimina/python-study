
class A:
    def f_a(self):
        print('-------a:A------')

    def f_b(self):
        print('-------b:A------')

    def f_c(self):
        print('-------c:A------')


class B:
    def f_a(self):
        print('-------a:B------')

    def f_b(self):
        print('-------b:B------')

    def f_c(self):
        print('-------c:B------')


class C(A, B):
    def f_a(self):
        print('-------a:C------')

    def f_b(self):
        # 直接使用super()方法会调用A类的f_a方法，因为它会默认多继承中从左到右的顺序来调用
        super().f_b()
        A.f_b(self)
        B.f_b(self)
        print('-------b:C------')

    def f_c(self):
        # 若果继承的不止两个类，如果要调用某个类方法，只要知道前一个类名就可以调用。
        super(C, self).f_c()
        super(A, self).f_c()
        print('-------c:C------')


def main():
    c = C()
    c.f_c()


if __name__ == '__main__':
    main()