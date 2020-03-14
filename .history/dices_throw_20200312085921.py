"""n 个骰子都扔出某一面的概率计算"""
import random


class ThrowDices:

    def __init__(self, dices_numbers, face_want, throw_times):
        self.dices_numbers = dices_numbers
        self.face_want = face_want
        self.throw_times = throw_times

    def get_probabilities(self):

        list_calculate = self.create_dices_throwing()

        # print(dices_log)
        n = 0

        for i in list_calculate:
            if self.face_want in i:
                n += 1
        print('{}次以后，{}个骰子至少能够掷出{}点面的次数为{}（一个骰子不管掷中几次只算一次）,占比为{}%'.format(self.throw_times,
                                                    self.dices_numbers, face_want, n, 100*n/(dices_numbers)))

    def create_dices_throwing(self):
        dices_throwing_final= []
        for i in range(dices_numbers):
            dices_throwing = []
            for s in range(throw_times):

                dices_throwing.append(random.randint(1, 6))

            #print(dices_throwing, '\n')
            dices_throwing_final.append(dices_throwing)
        print(dices_throwing_final,len(dices_throwing_final))
        return dices_throwing_final


dices_numbers = int(input('你要几个骰子: '))
throw_times = int(input('你要投掷几次: '))
face_want = int(input('你要哪个点数（1-6）: '))

task1 = ThrowDices(dices_numbers, face_want, throw_times)

task1.get_probabilities()
