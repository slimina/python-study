import random


def roll_dice():
    return random.randint(1, 6)


def main():
    total_time = 100000
    result_list = [0]*6
    for i in range(total_time):
        roll = roll_dice()
        for j, v in enumerate(result_list):
            if j == (roll - 1):
                result_list[j] += 1
    for i, v in enumerate(result_list):
        print("点数{}的总次数{},概率:{}".format(i+1, v, v/total_time))

    print()
    print()
    result_list = [0] * 11
    roll_list = list(range(2, 13))
    roll_dict = dict(zip(roll_list, result_list))
    for i in range(total_time):
        roll1 = roll_dice()
        roll2 = roll_dice()
        for j in range(2, 13):
            if j == (roll1 + roll2):
                roll_dict[j] += 1
    for k, v in roll_dict.items():
        print("点数{}的总次数{},概率:{}".format(k, v, v/total_time))


if __name__ == '__main__':
    main()
