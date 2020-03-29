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
    for item in str_digits:
        int_item = replacement_dict[item]
        int_item = int_item*10 + int_item
    return int_item

if __name__ == '_main_':
    print(my_int_convert('345'))




