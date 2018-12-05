def permute(n):
    if n < 1:
        return None
    outcomes = []
    board = [0,0,0]
    possibilities = 3
    for i in range(1, possibilities ** n + 1):
        if ~(1 << (possibilities - 1))  & i :
            board = [0,0,0]
            board[i % 3] = 1
            print (i % 3)
        outcomes.append(board)
    print(outcomes)
    return outcomes

permute(2)
