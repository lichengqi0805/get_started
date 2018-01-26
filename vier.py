grid = [['.', '.', '.', '.', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['0', '0', '0', '0', '0', '.'],
        ['.', '0', '0', '0', '0', '0'],
        ['0', '0', '0', '0', '0', '.'],
        ['0', '0', '0', '0', '.', '.'],
        ['.', '0', '0', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]
'''
str1=''
for i in range(0,9):                                 
        str1 = str1 + grid[i][0]
print(str1)
str2=''
for i in range(0,9):
        str2 = str2 + grid[i][1]
print(str2)
str3=''
for i in range(0,9):
        str3 = str3 + grid[i][2]
print(str3)
str4=''
for i in range(0,9):
        str4 = str4 + grid[i][3]
print(str4)
str5=''
for i in range(0,9):
        str5 = str5 + grid[i][4]
print(str5)
str6=''
for i in range(0,9):
        str6 = str6 + grid[i][5]
print(str6)
'''
for j in range(0, 6):
    for i in range(0, 9):
        print(grid[i][j],end='')
    print('')


