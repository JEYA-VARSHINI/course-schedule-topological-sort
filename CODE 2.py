from collections import defaultdict, deque

def canFinish(numCourses, prerequisites):
    g = defaultdict(list)
    indeg = [0]*numCourses

    for a, b in prerequisites:
        g[b].append(a)
        indeg[a] += 1

    q = deque()
    for i in range(numCourses):
        if indeg[i] == 0:
            q.append(i)

    done = 0
    while q:
        c = q.popleft()
        done += 1
        for nxt in g[c]:
            indeg[nxt] -= 1
            if indeg[nxt] == 0:
                q.append(nxt)

    return done == numCourses
print(canFinish(2, [[1, 0]]))
