def my_int_convert(str_digits):
    """a function convert str(digits) to int digits

    Arguments:
        str_digits {[str} -- [user input]
    """


    replacement_dict = {
    '0': 0,
    '1': 1,
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
}
    int_res = 0
    for item in str_digits:
        int_item = replacement_dict[item]
        int_res = int_res*10 + int_item
    return int_res

if __name__ == '__main__':

    print(my_int_convert('345'))




