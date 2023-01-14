# function gets board (2D list) and print it
def print_board(board):

    for row in board:   # for loop runs until every row is printed
        print(row)
    print("#########")


# function gets board (2D list) and return if it full
def is_board_full(board):

    for raw in board:  # for loop runs for num of rows
        for col in raw:  # for loop runs for num of cols
            if col == ".":  # condition checks if empty, return false, otherway return true in the end
                return False

    return True


# function cheks for victory
def victory_check(board):

    # x victory
    if board[0][0] == board[0][1] == board[0][2] == "x":  # checks first row for x
        print("x win!!!")
        return True
    if board[1][0] == board[1][1] == board[1][2] == "x":  # checks midlle row for x
        print("x win!!!")
        return True
    if board[2][0] == board[2][1] == board[2][2] == "x":  # checks last row for x
        print("x win!!!")
        return True
    if board[0][0] == board[1][1] == board[2][2] == "x":  # checks / for x
        print("x win!!!")
        return True
    if board[0][2] == board[1][1] == board[2][0] == "x":  # checks \ for x
        print("x win!!!")
        return True
    if board[0][0] == board[1][0] == board[2][0] == "x":  # checks first col for x
        print("x win!!!")
        return True
    if board[1][0] == board[1][1] == board[1][2] == "x":  # checks secend col for x
        print("x win!!!")
        return True
    if board[2][0] == board[2][1] == board[2][2] == "x":  # checks last col for x
        print("x win!!!")
        return True

    # o victory
    if board[0][0] == board[0][1] == board[0][2] == "o":  # checks first row for o
        print("o win!!!")
        return True
    if board[1][0] == board[1][1] == board[1][2] == "o":  # checks midlle row for o
        print("o win!!!")
        return True
    if board[2][0] == board[2][1] == board[2][2] == "o":  # checks last row for o
        print("o win!!!")
        return True
    if board[0][0] == board[1][1] == board[2][2] == "o":  # checks / for o
        print("0 win!!!")
        return True
    if board[0][2] == board[1][1] == board[2][0] == "o":  # checks \ for o
        print("o win!!!")
        return True
    if board[0][0] == board[1][0] == board[2][0] == "o":  # checks first col for o
        print("o win!!!")
        return True
    if board[1][0] == board[1][1] == board[1][2] == "o":  # checks secend col for o
        print("0 win!!!")
        return True
    if board[2][0] == board[2][1] == board[2][2] == "o":  # checks last col for o
        print("o win!!!")
        return True

    return False


# main function , runs the game
def ixs_igul():
    board = [
        [".", ".", "."],
        [".", ".", "."],
        [".", ".", "."]
    ]

    # while loop , runs until board is full
    while (is_board_full(board) != True) and (victory_check(board) == False):
        # x turn
        x_turn = input(print("X is your turn: write num1,num2"))
        x_raw = int(x_turn[0])
        x_col = int(x_turn[2])
        if board[x_raw][x_col] == '.':
            board[x_raw][x_col] = "x"
        print_board(board)

        is_board_full(board)
        victory_check(board)

        # o turn
        o_turn = input(print("Y is your turn: write num1,num2"))
        o_raw = int(o_turn[0])
        o_col = int(o_turn[2])
        if board[o_raw][o_col] == ".":
            board[o_raw][o_col] = "O"
        print_board(board)


ixs_igul()

