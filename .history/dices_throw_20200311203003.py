"""n 个骰子都扔出某一面的概率计算"""
import random


class ThrowDices:

    def __init__(self, dices_numbers, face_want, throw_times):
        self.dices_numbers = dices_numbers
        self.face_want = face_want
        self.throw_times = throw_times

    def get_probabilities(self):

        list_calculate = self.create_dices_throwing()
        faces_final_get = list_calculate.values()
        dices_log = list_calculate.keys()
        print(faces_final_get, len(faces_final_get))
        #print(dices_log)


    def create_dices_throwing(self):
        dices_throwing = {}
        for i in range(self.dices_numbers):
            for s in range(self.throw_times):
                dices_throws_each = '{}号骰子扔第{}次'.format(i+1, s)
                face_get = random.randint(1, 6)
                dices_throwing[dices_throws_each] = face_get

        print(dices_throwing)
        return dices_throwing


dices_numbers = int(input('how many dices: '))
face_want = int(input('which face you want: '))
throw_times = int(input('how many times you throw: '))
task1 = ThrowDices(dices_numbers, face_want, throw_times)

task1.get_probabilities()
