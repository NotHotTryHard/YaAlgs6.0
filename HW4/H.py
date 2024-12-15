import sys
sys.setrecursionlimit(10000000)


def func(N, adj, a):
    if N == 1:
        answ = a[0]
        res = [1]
        return answ, res
    
    
    root = 0
    ne = -1
    
    dp = [[0, 0] for _ in range(N)]

    def dfs(u, parent):
        tmp0 = 0
        tmp1 = a[u]
        for v in adj[u]:
            if v == parent:
                continue
            dfs(v, u)
            tmp0 += dp[v][1]
            tmp1 += min(dp[v][0], dp[v][1])
        dp[u][0] = tmp0
        dp[u][1] = tmp1
    dfs(root, ne)

    res = []
    #stack = []
    #visited = [False] * N
    
    
    def rec(u, parent, flag):
        if flag:
            res.append(u + 1)
            for v in adj[u]:
                if v == parent:
                    continue
                if dp[v][0] <= dp[v][1]:
                    rec(v, u, 0)
                else:
                    rec(v, u, 1)
        else:
            #res.append(u + 1)
            for v in adj[u]:
                if v == parent:
                    continue
                rec(v, u, 1)

    if dp[root][1] <= dp[root][0]:
        answ = dp[root][1]
        rec(root, ne, 1)
    else:
        answ = dp[root][0]
        rec(root, ne, 0)
    
    return answ, res


if __name__ == '__main__':
    N = int(input())
    adj = [list() for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, input().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    a = list(map(int, input().split()))
    
    answ, res = func(N, adj, a)
    print(answ, len(res))
    print(' '.join(map(str, res)))


'''

import sys
sys.setrecursionlimit(10000000)


def func(N, adj, a):
    dp = [[0, 0] for _ in range(N)]

    def dfs(u, parent):
        dp[u][1] = a[u]
        dp[u][0] = 0
        for v in adj[u]:
            if v == parent:
                continue
            dfs(v, u)
            dp[u][0] += dp[v][1]
            dp[u][1] += min(dp[v][0], dp[v][1])
    dfs(0, -1)

    res = []
    def rec(u, parent, flag):
        if flag:
            res.append(u + 1)
            for v in adj[u]:
                if v == parent:
                    continue
                if dp[v][0] <= dp[v][1]:
                    rec(v, u, False)
                else:
                    rec(v, u, True)
        else:
            #res.append(u + 1)
            for v in adj[u]:
                if v == parent:
                    continue
                rec(v, u, True)

    if dp[0][1] <= dp[0][0]:
        total_cost = dp[0][1]
        rec(0, -1, True)
    else:
        total_cost = dp[0][0]
        rec(0, -1, False)

    print(total_cost, len(res))
    print(' '.join(map(str, res)))


if __name__ == '__main__':
    N = int(sys.stdin.readline())
    adj = [[] for _ in range(N)]
    for _ in range(N - 1):
        u, v = map(int, sys.stdin.readline().split())
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)
    a = list(map(int, sys.stdin.readline().split()))
    func(N, adj, a)

'''