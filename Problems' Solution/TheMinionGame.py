string = input()

vowels = ['A', 'E', 'I', 'O', 'U']

stuart, kevin = 0, 0

ln = len(string)

for i in range(ln):
    if string[i] in vowels:
        kevin += ln - i
    else:
        stuart += ln - i

if stuart > kevin:
    print('Stuart', stuart)

elif kevin > stuart:
    print('Kevin', kevin)

else:
    print('Draw')
