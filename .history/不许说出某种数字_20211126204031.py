number = [int(x) for x in range(1000)]
game_number = int(input('game number is '))
for i in number:
    if i % game_number == 0 or i % 10 == game_number:
        print(i)