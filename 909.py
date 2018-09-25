# bfs

import collections

def snakesAndLadders(board):
    """
    :type board: List[List[int]]
    :rtype: int
    """
    N = len(board)
    def get_destination (s):
        a, b = divmod(s-1, N)
        r = N - 1 - a
        c = b if a%2 == 0 else N - 1 - b
        return r, c

    queue = collections.deque([1])
    dist = {1: 0}
    while queue:
        s = queue.popleft()
        if s == N*N:
            return dist[s]
        for s_to in range(s+1, min(s+6, N*N)+1):
            r, c = get_destination(s_to)
            if board[r][c] != -1:
                s_to = board[r][c]
            if s_to not in dist:
                dist[s_to] = dist[s] + 1
                queue.append(s_to)

    return -1

a = [
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,-1,-1,-1,-1,-1],
[-1,35,-1,-1,13,-1],
[-1,-1,-1,-1,-1,-1],
[-1,15,-1,-1,-1,-1]]

print(snakesAndLadders(a))
