import heapq

goal = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    return sum(abs((v-1)//3 - i//3) +
               abs((v-1)%3 - i%3)
               for i,v in enumerate(state) if v)

def neighbors(state):
    result = []
    z = state.index(0)
    r,c = divmod(z,3)

    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = r+dr,c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr*3+nc
            s = list(state)
            s[z],s[nz] = s[nz],s[z]
            result.append(tuple(s))

    return result

def astar(start):
    pq = [(heuristic(start), 0, start, [])]
    visited = set()

    while pq:
        f,g,state,path = heapq.heappop(pq)

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for n in neighbors(state):
            heapq.heappush(
                pq,
                (g+1+heuristic(n), g+1, n, path+[state])
            )

start = (1,2,3,
         4,0,6,
         7,5,8)

solution = astar(start)

for s in solution:
    print(s)