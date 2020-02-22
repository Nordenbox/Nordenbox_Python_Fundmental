import time
import random


class BrutalForce_Decoding:
    def generat_random_password_all(self, pass_length):
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

    def generat_random_password_alldigitals(self, pass_length):
        random_str = ""
        # base_str_complicate = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        base_str_digital = "0123456789"
        # base_str_lowcharacter = 'abcdefghijklmnopqrstuvwxyz'

        length = len(base_str_digital) - 1
        for i in range(pass_length):
            random_str = random_str + base_str_digital[random.randint(0, length)]
        return random_str

    def generat_random_password_allchracters(self, psss_length):
        """
        生成一个指定长度的全小写字母随机字符串
        """
        random_str = ""
        # base_str_complicate = 'ABCDEFGHIGKLMNOPQRSTUVWXYZabcdefghigklmnopqrstuvwxyz0123456789'
        # base_str_digital = '0123456789'
        base_str_lowcharacter = "abcdefghijklmnopqrstuvwxyz"

        length = len(base_str_lowcharacter) - 1
        for i in range(psss_length):
            random_str = random_str + base_str_lowcharacter[random.randint(0, length)]
        return random_str

    def dispatch_to_generat(self, pass_given):
        pass_length = len(pass_given)
        if str.isdigit(pass_given) is True:
            self.generat_random_password_alldigitals(pass_length)
        elif str.islower(pass_given) is True:
            self.generat_random_password_allchracters(pass_length)
        else:
            self.generat_random_password_all(pass_length)

        

    def decoding_output(self,random_str):
        decoded_str = ""

        while decoded_str != pass_given:

            decoded_str = self.dispatch_to_generat(pass_given)
            print(decoded_str, end=",")

        else:

            print("密码为 ", decoded_str, "\n")


pass_given = input("请输入您的密码，等待解码： ")
use = BrutalForce_Decoding()
temp = use.dispatch_to_generat(pass_given)
use.decoding_output(temp)

