import random


# return 5X5 array with random values of 1, 0
def random_array_5_5():
    arr = []
    rows, cols = 5, 5
    for i in range(rows):
        col = []
        for j in range(cols):
            col.append(random.randint(0, 1))
        print(col)
        arr.append(col)

    return arr


# return true if all dead (o)
def is_all_dead0(array, range1):
    question = True
    for i in range(range1):
        for j in range(range1):
            if array[i][j] == 1:
                question = False
                return question

    return question


# return number of friends
def count_friends(array, x, y):
    friends_num = 0
    if array[x - 1][y - 1] == 1 and (x - 1) >= 0 and (y - 1) >= 0:
        friends_num = friends_num + 1
    if array[x - 1][y] == 1 and (x - 1) >= 0 and y >= 0:
        friends_num = friends_num + 1
    if array[x - 1][y + 1] == 1 and (x - 1) >= 0 and (y + 1) <= 4:
        friends_num = friends_num + 1
    if array[x + 1][y] == 1 and (x + 1) <= 4 and y >= 0:
        friends_num = friends_num + 1
    if array[x + 1][y - 1] == 1 and (x + 1) <= 4 and (y - 1) >= 0:
        friends_num = friends_num + 1
    if array[x + 1][y + 1] == 1 and (x + 1) <= 4 and (y + 1) <= 4:
        friends_num = friends_num + 1
    if array[x][y - 1] == 1 and x >= 0 and (y - 1) >= 0:
        friends_num = friends_num + 1
    if array[x][y + 1] == 1 and x >= 0 and (y + 1) <= 4:
        friends_num = friends_num + 1
    return friends_num


def print_matrix(array):
    for r in array:
        for c in r:
            print(c, end=" ")
        print()
    print("#############")


# main function
def game_of_my_life():

    arr1 = random_array_5_5()

    while is_all_dead0(arr1 ,4 ) != True:
        for x in range(4):
            for y in range(4):
                if count_friends(arr1, x, y) == 3:
                    arr1[x][y] = 1
                if count_friends(arr1, x, y) > 3:
                    arr1[x][y] = 0
                if count_friends(arr1, x, y) <= 1:
                    arr1[x][y] = 0
        print_matrix(arr1)


game_of_my_life()

