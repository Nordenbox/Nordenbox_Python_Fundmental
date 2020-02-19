import random
import time

passGiven = input("pass:")
pass_length = len(passGiven)


def generate_random_str_complicate(pass_length):
    """
    生成一个指定长度的大小写字母数字随机字符串
    """
    random_str = ""
    base_str_complicate = (
        "ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789"
    )
    # base_str_digital = '0123456789'
    # base_str_lowcharacter = 'abcdefghijklmnopqrstuvwxyz'

    length = len(base_str_complicate) - 1
    for i in range(pass_length):
        random_str = random_str + base_str_complicate[random.randint(0, length)]
    return random_str


def generate_random_str_digital(pass_length):
    """
    生成一个指定长度的全数字随机字符串
    """
    random_str = ""
    # base_str_complicate = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    base_str_digital = "0123456789"
    # base_str_lowcharacter = 'abcdefghijklmnopqrstuvwxyz'

    length = len(base_str_digital) - 1
    for i in range(pass_length):
        random_str = random_str + base_str_digital[random.randint(0, length)]
    return random_str


def generate_random_str_lowcharacter(pass_length):
    """
    生成一个指定长度的全小写字母随机字符串
    """
    random_str = ""
    # base_str_complicate = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
    # base_str_digital = '0123456789'
    base_str_lowcharacter = "abcdefghijklmnopqrstuvwxyz"

    length = len(base_str_lowcharacter) - 1
    for i in range(pass_length):
        random_str = random_str + base_str_lowcharacter[random.randint(0, length)]
    return random_str





decoded_str = ""
loops = 0
time_start = time.time()

if str.isdigit(passGiven) is True:

    while decoded_str != passGiven:

        decoded_str = generate_random_str_digital(pass_length)
        #print(decoded_str, end=",")

        loops = loops + 1
    else:
        time_end = time.time()

        print("\n")
        print(
            "消耗时间",
            (time_end - time_start),
            "秒。",
            "循环了 %d 次 = 生成和比对次数 %d X 随机数长度 %d"
            % (loops * pass_length, loops, pass_length),
        )

        print(
            "密码为 ",
            decoded_str,
            "\n",
            "随机生成%d位纯数字密码的复杂度为10的%d次方= %d。"
            % (pass_length, pass_length, 10 ** pass_length),
            "我的人品系数为百分之%f" % (100 * (1 - (loops / (10 ** pass_length)))),
        )
        print("复杂度列表：")
        for i in range(1, pass_length + 1):
            print("%d 位的复杂度为%d" % (i, 10 ** i))
else:
    if str.islower(passGiven) is True:
        while decoded_str != passGiven:

            decoded_str = generate_random_str_lowcharacter(pass_length)
            #print(decoded_str, end=",")

            loops = loops + 1
        else:
            time_end = time.time()

            print("\n")
            print(
                "消耗时间",
                (time_end - time_start),
                "秒。",
                "循环了 %d 次 = 生成和比对次数 %d X 随机数长度 %d"
                % (loops * pass_length, loops, pass_length),
            )

            print(
                "密码为 ",
                decoded_str,
                "\n",
                "随机生成%d位全小写字母密码的复杂度为62的%d次方= %d。"
                % (pass_length, pass_length, 26 ** pass_length),
                "我的人品系数为百分之%f" % (100 * (1 - (loops / (26 ** pass_length)))),
            )
            print("复杂度列表：")
            for i in range(1, pass_length + 1):
                print("%d 位的复杂度为%d" % (i, 26 ** i))

    else:
        while decoded_str != passGiven:

            decoded_str = generate_random_str_complicate(pass_length)
            #print(decoded_str, end=",")

            loops = loops + 1
        else:
            time_end = time.time()

            print("\n")
            print(
                "消耗时间",
                (time_end - time_start),
                "秒。",
                "循环了 %d 次 = 生成和比对次数 %d X 随机数长度 %d"
                % (loops * pass_length, loops, pass_length),
            )

            print(
                "密码为 ",
                decoded_str,
                "\n",
                "随机生成%d位大小写字母与数字混合密码的复杂度为62的%d次方= %d。"
                % (pass_length, pass_length, 62 ** pass_length),
                "我的人品系数为百分之%f" % (100 * (1 - (loops / (62 ** pass_length)))),
            )
            print("复杂度列表：")
            for i in range(1, pass_length + 1):
                print("%d 位的复杂度为%d" % (i, 62 ** i))

