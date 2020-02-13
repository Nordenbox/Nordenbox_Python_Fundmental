alphabeta = 'abcdefghijklmnopqrstuvwxyz'

text = input('input a sentence:\n')

for s in range(0, len(text)):
    print(text[s])
    num = alphabeta.find('text[s]') + 1
    print(num)
    text.replace('text[s]', 'alphabeta[num]')
    print(text)