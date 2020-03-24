import numpy as np
import random


class DiceThrow:
    def __init__(self, dices_throw_times, dices_numbers):
        self.dices_throw_times = dices_throw_times

        self.dices_numbers = dices_numbers

    def throwing(self):

        origin_list = []

        def throw_once():
            for s in range(self.dices_numbers):
                origin_list.append([random.randint(1, 6)
                                    for i in range(1, self.dices_throw_times + 1)])
            return origin_list

        res = throw_once()
        print(res)
        les_array = np.array(res)
        print('每一行是一个骰子的所有掷出情况。\n', les_array)
        print('ranks or axises of this array is ',les_array.ndim)


numbers = int(input('how many dices do you want throw: '))
throw_times = int(input('how many times do you want throw on each dice: '))

dice_throwing = DiceThrow(throw_times, numbers)
dice_throwing.throwing()
