def add(cords, visited, unvisited, A, lower_limit, upper_limit):
    s = [(0,1), (1,0), (0,-1), (-1,0)]
    for dir, c in enumerate(s):
        current_dir = cords[3]
        if current_dir is not None and abs(current_dir-dir) == 2:
            continue

        x = cords[0] + c[0]
        y = cords[1] + c[1]

        if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A):
            continue

        cur_dist = cords[2]
        if current_dir is not None and cur_dist < lower_limit and current_dir != dir:
            continue

        dist = cur_dist+1

        if current_dir != dir:
            dist = 1
            new_x = cords[0]+c[0]*lower_limit
            new_y = cords[1]+c[1]*lower_limit

            # print("ny", new_x, new_y)
            if new_x < 0 or new_x >= len(A[0]) or new_y < 0 or new_y >= len(A):
                # print("out")
                continue

        if dist > upper_limit:
            continue

        key = (x,y, dist, dir)

        if visited.get(key) is not None:
            continue

        # print("adding", dir)
        new_w = (int)(A[y][x])+unvisited[cords]
        if unvisited.get(key) is None:
            unvisited[key] = (new_w)

            if x == len(A[0])-1 and y == len(A)-1:
                return new_w
            continue

        old_w = unvisited[key]
        if old_w > new_w:
            unvisited[key] = (new_w)

def dijkstra(A, lower_limit, upper_limit):
    unvisited = {(0,0,0,None):0}
    visited = {}

    counter = 0
    while True:
        if len(unvisited) == 0:
            print("too long")
            break
        cords = min(unvisited, key=unvisited.get)
        # print("\nvisit", cords, unvisited[cords])
        stop = add(cords, visited, unvisited, A, lower_limit, upper_limit)
        if counter % 10000 == 0:
            print(unvisited[cords])

        value = unvisited[cords]
        unvisited.pop(cords)
        visited[cords] = value
        counter += 1
        if stop is not None:
            print("stop", stop)
            break
    for x in unvisited:
        if x[0] == len(A[0])-1 and x[1] == len(A)-1:
            print(x)

def p1():
    with open('data/a17.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        dijkstra(A, 1, 3)

def p2():
    with open('data/a17.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        dijkstra(A, 4, 10)

# p1()
p2()
