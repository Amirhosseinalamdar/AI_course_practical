def is_active(last, s, node):
    if last is None:
        return True
    return not is_blocking(last, s, node)


def final_dfs(visited, s, d, last=None):
    visited[s] = True

    if s == d:
        return True
    for node in undirected[s]:
        if not visited[node]:
            if is_active(last, s, node):  
                res = final_dfs(visited, node, d, s)
                if res:
                    return res

    visited[s] = False


def my_dfs(s, visited):
    visited[s] = True

    if is_given[s] == 1:
        return True
    else:
        for node in directed[s]:
            if not visited[node]:
                res = my_dfs(node, visited)
                if res:
                    return res


def is_blocking(x, y, z):
    if is_given[y] == 1:
        if (adj[x][y] == 1 and adj[y][z] == 1) or (adj[y][x] == 1 and adj[z][y] == 1):
            return True
        if adj[y][x] == 1 and adj[y][z] == 1:
            return True

    else:
        visited = [False] * len(adj)
        if adj[z][y] == 1 and adj[x][y] == 1 and my_dfs(y, visited) != True:
            return True

    return False


n = int(input()) + 1
m = int(input())
adj = [[0 for i in range(n)] for i in range(n)]
undirected = [[] for i in range(n)]
directed = [[] for i in range(n)]

for i in range(m):
    u, v = [int(i) for i in input().split('->')]
    undirected[u].append(v)
    undirected[v].append(u)
    directed[u].append(v)
    adj[u][v] = 1

testnum = int(input())
for t in range(testnum):
    is_given = [0 for i in range(n)]
    u = int(input())
    v = int(input())

    lst = [int(i) for i in input().split()]
    for i in lst:
        is_given[i] = 1

    all_paths = []
    path = []
    visited = [False] * n
    is_independent = not final_dfs(visited, u, v)
    
    print(is_independent)
