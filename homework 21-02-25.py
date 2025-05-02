from collections import deque
def f(n, dislikes):
    graph = [[] for _ in range(n + 1)]
    for a, b in dislikes:
        graph[a].append(b)
        graph[b].append(a)
    color = [0] * (n + 1)
    for people in range(1, n + 1):
        if color[people] == 0:
            queue = deque([people])
            color[people] = 1
            while queue:
                current = queue.popleft()
                for dont_like in graph[current]:
                    if color[dont_like] == 0:
                        color[dont_like] = 3 - color[current]
                        queue.append(dont_like)
                    elif color[dont_like] == color[current]:
                        return False
    return True
