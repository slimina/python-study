import matplotlib.pyplot as pyt
import random


def main():
    times = 100
    result_list1 = []
    result_list2 = []
    for i in range(0, times):
        result_list1.append(random.randint(1, times))
        result_list2.append(random.randint(1, times))
    print(result_list1)
    print(result_list2)
    x = range(1, times + 1)
    pyt.scatter(x, result_list1, c='red', alpha=0.5)
    pyt.scatter(x, result_list2, alpha=0.5)
    pyt.show()


if __name__ == '__main__':
    main()
