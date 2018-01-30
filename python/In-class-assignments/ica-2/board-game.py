h= int(input("Enter the height of the board: "))
w= int(input("Enter the width of the board: "))

def board_draw(h,w):
    for i in range(h):
        print('\n')
        for j in range(w):
            print('--- ', end='')
        print('\n')
        for h in range(w):
            print('|\t', end='')

board_draw(h,w)