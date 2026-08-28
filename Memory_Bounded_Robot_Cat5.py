goal = (1,2,3,4,5,6,7,8,0)

def heuristic(state):
    return sum(abs((v-1)//3 - i//3) +
               abs((v-1)%3 - i%3)
               for i,v in enumerate(state) if v)


def search(state, g, bound, path):
    f = g + heuristic(state)

    if f > bound:
        return f

    if state == goal:
        return path

    minimum = float('inf')
    zero = state.index(0)
    r,c = divmod(zero,3)

    for dr,dc in [(1,0),(-1,0),(0,1),(0,-1)]:
        nr,nc = r+dr,c+dc

        if 0 <= nr < 3 and 0 <= nc < 3:
            nz = nr*3+nc

            new_state = list(state)
            new_state[zero],new_state[nz] = \
                new_state[nz],new_state[zero]

            new_state = tuple(new_state)

            if new_state not in path:
                result = search(
                    new_state,
                    g+1,
                    bound,
                    path+[new_state]
                )

                if isinstance(result,list):
                    return result

                minimum = min(minimum,result)

    return minimum


def ida_star(start):
    bound = heuristic(start)
    path = [start]

    while True:
        result = search(start,0,bound,path)

        if isinstance(result,list):
            return result

        bound = result


start = (1,2,3,
         4,0,6,
         7,5,8)

solution = ida_star(start)

for s in solution:
    print(s)