def main():
    n, m = map(int, input().split())
    gr = [[] for _ in range(n + 1)]
    cnt = [0] * (n + 1)
    for _ in range(m):
        a, b = map(int, input().split())
        gr[a].append(b)
        cnt[b] += 1
    vis = [False] * (n + 1)
    stk = [False] * (n + 1)
    def dfs(u):
        vis[u] = stk[u] = True
        for v in gr[u]:
            if not vis[v]:
                if dfs(v): return True
            elif stk[v]: return True
        stk[u] = False
        return False
    cyc = False
    for i in range(1, n + 1):
        if not vis[i] and dfs(i):
            cyc = True
            break
    if cyc: print(-1)
    else:
        q = [i for i in range(1, n + 1) if cnt[i] == 0]
        ok = True
        while q:
            if len(q) > 1: ok = False
            x = q.pop(0)
            for y in gr[x]:
                cnt[y] -= 1
                if cnt[y] == 0: q.append(y)
        print("YES" if ok else "NO")
if __name__ == "__main__": main()