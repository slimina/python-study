import numpy as np


def main():
  # 创建随机数组,3行4列，[1,10)随机数数列
  arr = np.random.randint(1, 10, (3, 4))
  print(arr)


if __name__ == '__main__':
    main()
