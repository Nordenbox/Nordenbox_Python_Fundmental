class Abosolute:
    
    
    
    def output_absolute(self):
        while True:
            for i in range(4):
                value = int(input('input a value:\n'))
                if value >= 0:
                    print('绝对值为：'+str(value))
                else:
                    print('绝对值为：'+str(-1*value))
            
            res = input('continue? Y or N? \n')
            if res == 'Y':
                continue
            else:
                break
            
Abosolute_counting = Abosolute()

Abosolute_counting.output_absolute()