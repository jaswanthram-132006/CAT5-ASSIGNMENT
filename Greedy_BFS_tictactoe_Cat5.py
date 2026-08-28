import heapq

def heuristic(board):
    score = 0
    for line in [(0,1,2),(3,4,5),(6,7,8),
                 (0,3,6),(1,4,7),(2,5,8),
                 (0,4,8),(2,4,6)]:
        a,b,c = line
        if board[a] == board[b] == board[c] != ' ':
            score += 10 if board[a] == 'X' else -10
    return -score

def greedy_best_first(board):
    moves = []
    for i in range(9):
        if board[i] == ' ':
            new_board = board[:]
            new_board[i] = 'X'
            h = heuristic(new_board)
            heapq.heappush(moves, (h, new_board, i))

    if moves:
        return heapq.heappop(moves)[2]
    return -1

board = ['X','O','X',
         ' ','O',' ',
         ' ',' ',' ']

move = greedy_best_first(board)
print("Best Move:", move)