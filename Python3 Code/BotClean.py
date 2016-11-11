# Solution to Hackerrank Problem at:
# https://www.hackerrank.com/challenges/botclean

class Cell:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def dist_diff(self,target_dist):
        return abs(target_dist.x - self.x) + abs(target_dist.y - self.y)

# Head ends here
def next_move(posr, posc, board):
    current_cell = Cell(posc, posr)
    dirty_cell = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == "d":
                dirty_cell.append(Cell(j,i))

    nearest_cell = None
    for cell in dirty_cell:
        if nearest_cell is None or cell.dist_diff(current_cell) < nearest_cell.dist_diff(current_cell):
            nearest_cell = cell

    if nearest_cell is not None:
        print_move(nearest_cell.x - current_cell.x, nearest_cell.y - current_cell.y)


def print_move(delta_x, delta_y):
    if delta_x < 0 :
        print('LEFT')
    elif delta_x > 0 :
        print ('RIGHT')
    elif delta_y < 0 :
        print('UP')
    elif delta_y > 0 :
        print('DOWN')
    else:
        print('CLEAN')


# Tail starts here
if __name__ == "__main__":
    pos = [int(i) for i in input().strip().split()]
    board = [[j for j in input().strip()] for i in range(5)]
    next_move(pos[0], pos[1], board)
