import random

number_optional = [i for i in range(1, 10)]


def equation_rendering():
    while True:
        a = random.choice(number_optional)
        b = random.choice(number_optional)
        c = random.choice(number_optional)
        d = random.choice(number_optional)
        list_temp = [a, b, c, d]

        if a + b - c == d and len(list_temp) == len(set(list_temp)):
            print('{}+{}-{}={}'.format(a, b, c, d))
            break


loop_command = input('训练开始,回车：')
while True:

    equation_rendering()
    loop_judge = input('是否继续？回车继续，输入 n 即结束： ')
    if loop_judge == 'n':
        print('训练结束。')
        break
    else:
        continue

