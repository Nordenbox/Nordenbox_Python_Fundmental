test = input('input a string: ')


def is_isogram(string):
    n = 0

    for i in string:
        if string.count(i) > 1:

            print('False')
            break
        else:
            n = n + 1

            continue
    if n > 0:
        print("True")


is_isogram(test)
