import random       #for spawn blocks
import os           #for clear console

#make table 4x4
table = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

# function for spawn number in random place
def spawn_number():
    while True:
        y = random.randrange(0,4)
        x = random.randrange(0,4)
        if table[y][x] == 0:
            table[y][x] = 2
            break
        else:
            continue

# function for detection lose
def defeat():
    full_rows = 0
    for i in range(4):
        try:
            table[i].index(0)
        except:
            full_rows += 1
    if full_rows == 4:
        return(1)

# repair input eror
def set_array():
    while True:
        array = input()
        if array != '':
            break
    return(array)

# function for adding numbers
def sums_numbers(list, array):
    option = len(list)
    if array == '+':
        if option == 1:
            return
        elif option == 2:
            if list[0] == list[1]:
                list[0] = list[0] * 2
                list[1] = 0
        elif option == 3:
            if list[0] == list [1]:
                list[0] = list[0] * 2
                list[1] = list[2]
                list[2] = 0
            elif list[1] == list[2]:
                list[1] = list[1] * 2
                list[2] = 0
        elif option == 4:
            if list[0] == list[1] and list[2] == list[3]:
                list[0] = list[0] * 2
                list[1] = list[2] * 2
                list[2],list[3] = 0,0
            elif list[0] == list [1]:
                list[0] = list[0] * 2
                list[1] = list[2]
                list[2] = list[3]
                list[3] = 0
            elif list[1] == list[2]:
                list[1] = list[1] * 2
                list[2] = list[3]
                list[3] = 0
            elif list[2] == list[3]:
                list[2] = list[2] * 2
                list[3] = 0

    elif array == '-':
        list.reverse()
        if option == 1:
            return
        if option == 2:
            if list[1] == list[0]:
                list[1] = list[1] * 2
                list[0] = 0
        if option == 3:
            if list[2] == list[1]:
                list[2] = list[2] * 2
                list[1] = list[0]
                list[0] = 0
            elif list [1] == list[0]:
                list[1] = list[1] * 2
                list[0] = 0
        if option == 4:
            if list[3] == list[2] and list[1] == list[0]:
                list[3] = list[3] * 2
                list[2] = list[1] * 2
                list[1],list[0] = 0,0
            elif list[3] == list[2]:
                list[3] = list[3] * 2
                list[2] = list[1]
                list[1] = list[0]
                list[0] = 0
            elif list[2] == list[1]:
                list[2] = list[2] * 2
                list[1] = list[0]
                list[0] = 0
            elif list [1] == list[0]:
                list[1] = list[1] * 2
                list[0] = 0
# function for add ziros and extend string
def add_zero(list, array):
    if len(list) != 4:
        append_zero = 4 - len(list)
        for zero in range(append_zero):
            if array == '+':
                list.append(0)
            elif array == '-':
                list.insert(0,0)

#loop for drawing a table
while True:
    if defeat() == 1:
        print('you a lose')
        input()
        break

    spawn_number()
    for i in table:
        print(i)

    inp = set_array()
    new_row = []

    if inp[0] == '4':
        for i in range(0,4):
            for j in range(0,4):
                if table[i][j] != 0:
                    new_row.append(table[i][j])
            sums_numbers(new_row, '+')
            add_zero(new_row, '+')
            for k in range(0,4):
                table[i][k] = new_row[k]
            new_row = []

    if inp[0] == '8':
        for j in range(0,4):
            for i in range(0,4):
                if table[i][j] != 0:
                    new_row.append(table[i][j])
            sums_numbers(new_row, '+')
            add_zero(new_row, '+')
            for k in range (0,4):
                table[k][j] = new_row[k]
            new_row = []

    if inp[0] == '6':
        for i in range(0,4):
            for j in range(3,-1,-1):
                if table[i][j] != 0:
                    new_row.append(table[i][j])
            sums_numbers(new_row, '-')
            add_zero(new_row, '-')
            for k in range(3,-1,-1):
                table[i][k] = new_row[k]
            new_row = []

    if inp[0] == '2':
        for j in range(0,4):
            for i in range(3,-1,-1):
                if table[i][j] != 0:
                    new_row.append(table[i][j])
            sums_numbers(new_row, '-')
            add_zero(new_row, '-')
            for k in range(3,-1,-1):
                table[k][j] = new_row[k]
            new_row = []






    os.system('cls')


