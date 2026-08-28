def valid(m, c):
    if m < 0 or c < 0 or m > 3 or c > 3:
        return False

    if m > 0 and m < c:
        return False

    rm, rc = 3-m, 3-c

    if rm > 0 and rm < rc:
        return False

    return True


def heuristic(state):
    m,c,b = state
    return m + c


def ao_star(start, goal):
    open_list = [(heuristic(start), start, [])]
    visited = set()

    while open_list:
        _, state, path = min(open_list)
        open_list.remove((_, state, path))

        if state == goal:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        m,c,b = state

        if b == 0:
            moves = [(1,0),(2,0),(0,1),(0,2),(1,1)]
        else:
            moves = [(-1,0),(-2,0),(0,-1),(0,-2),(-1,-1)]

        for dm,dc in moves:
            nm,nc = m-dm,c-dc

            if valid(nm,nc):
                new_state = (nm,nc,1-b)

                if new_state not in visited:
                    cost = len(path) + heuristic(new_state)
                    open_list.append(
                        (cost,new_state,path+[state])
                    )

    return None


start = (3,3,0)
goal = (0,0,1)

solution = ao_star(start, goal)

for s in solution:
    print(s)