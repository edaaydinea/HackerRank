test_cases = int(input().strip())
for test_case in range(test_cases):
    snake_count = int(input().strip())
    shortcuts = {}
    for snake in range(snake_count):
        src, dst = [int(item) - 1 for item in input().strip().split()]
        shortcuts[src] = dst
    ladder_count = int(input().strip())
    for ladder in range(ladder_count):
        src, dst = [int(item) - 1 for item in input().strip().split()]
        shortcuts[src] = dst

    board = [0] + [None] * 99
    dst = 0
    while dst < 99:
        dst += 1
        moves = board[dst]
        sources = [cell for cell in board[max(dst - 6, 0):dst] if cell is not None]
        if not sources:
            continue
        moves = min(sources) + 1
        new_dst = shortcuts.get(dst, dst)
        if board[new_dst] is None or moves < board[new_dst]:
            board[new_dst] = moves
            dst = min(dst, new_dst)

    print(board[-1] if board[-1] is not None else '-1')
