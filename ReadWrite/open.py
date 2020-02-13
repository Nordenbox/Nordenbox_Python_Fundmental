file1=open('test/Scores.txt','r')
file_nonlines= file1.read()
file1.close()
file1=open('test/Scores.txt','r')
file_lines=file1.readlines()
file1.close()
print(file_nonlines)
print('-----------')
print(file_lines)
print('----------------')
Final_scores = []
for items in file_lines:
    data=items.split()
    print(data)
    sum = 0
    for score in data[1:]:
        sum=sum+int(score)
    result = data[0]+str(sum)+'\n'
    print(result)
    Final_scores.append(result)
winner = open('test/Scores_output.txt','w',encoding='utf-8')
winner.writelines(Final_scores)
winner.close()
winneropen = open('test/Score_output.txt','r',encoding='utf-8')
winner_diplay=winneropen.read()
print(winner_diplay)