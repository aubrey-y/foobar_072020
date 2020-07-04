def calculate_dest(curr, path):
    return curr[0] + path[0], curr[1] + path[1]


def curr_is_valid(curr):
    return 0 <= curr[0] <= 7 and 0 <= curr[1] <= 7


def get_next_points(curr, traveled):
    return [(calculate_dest(curr, p), traveled) for p in [(2, 1),
                                                          (2, -1),
                                                          (-2, 1),
                                                          (-2, -1),
                                                          (1, 2),
                                                          (1, -2),
                                                          (-1, -2),
                                                          (-1, 2)]]


def solution(src, dest):
    board = [list(range(x, x + 8)) for x in range(0, 64, 8)]
    curr = [(ix, iy) for ix, row in enumerate(board) for iy, i in enumerate(row) if i == src][0]
    dest = [(ix, iy) for ix, row in enumerate(board) for iy, i in enumerate(row) if i == dest][0]
    q = get_next_points(curr, 1) if curr != dest else []

    while q:
        if curr_is_valid(q[0][0]):
            if q[0][0] == dest:
                return q[0][1]
            else:
                q += get_next_points(q[0][0], q[0][1] + 1)
        del q[0]
    return 0
