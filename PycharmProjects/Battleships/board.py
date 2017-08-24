
def generate(board_max):
    board_f = []
    for i in range(board_max + 1):
        nextrow = []
        if i == 0:
            toprow = []
            for j in range(board_max + 1):
                if j == 0:
                    toprow.append(" ")
                else:
                    toprow.append(str(j))
            board_f.append(toprow)
        else:
            nextrow.append(str(i))
            for j in range(2, board_max + 2):
                nextrow.append("-")
            board_f.append(nextrow)
    return board_f


def display(board_f):
    for row in board_f:
        print(" ".join(row))


def update(update_coordinates, board_x, value):
    board_x[update_coordinates["row"]][update_coordinates["col"]] = value
    return board_x

