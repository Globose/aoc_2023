def p1():
    with open('data/a14.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
        for i in range(len(A[0])):
            free_index = 0
            for j in range(len(A)):
                if A[j][i] == 'O':
                    sum += len(A)-free_index
                    free_index += 1
                elif A[j][i] == '#':
                    free_index = j+1
        print(sum)

def weigh(A):
    mass = 0
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j] == 'O':
                mass += len(A)-i
    return mass

def stack(V):
    i = 0
    while i < len(V):
        stones = 0
        end = len(V)
        for k in range(i,len(V)):
            if V[k] == '#':
                end = k+1
                break
            elif V[k] == 'O':
                V[k] = '.'
                stones += 1
        for k in range(stones):
            V[i+k] = 'O'
        i = end

def rot(A):
    # Up
    for i in range(len(A[0])):
        line = []
        for j in range(len(A)):
            line.append(A[j][i])
        stack(line)
        for j in range(len(A)):
            A[j][i] = line[j]

    # Left
    for a in A:
        stack(a)

    # Down
    for i in range(len(A[0])):
        line = []
        for j in range(len(A)-1, -1, -1):
            line.append(A[j][i])
        stack(line)
        for j in range(len(A)):
            A[len(A)-j-1][i] = line[j]

    # Right
    for a in A:
        a.reverse()
        stack(a)
        a.reverse()


def p2():
    with open('data/a14.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            A[i] = [*A[i]]

        tree_list = []
        d = {}
        cycle = 0
        hash_rep = 0
        while True:
            rot(A)
            tree_list.append(weigh(A))
            cycle += 1
            vector = ""
            for a in A:
                vector += "".join(a)
            h1 = hash(vector)
            if d.get(h1) is None:
                d[h1] = cycle
            else:
                hash_rep = h1
                break
        start_index = 0
        for k in d.items():
            if k[0] == hash_rep:
                start_index = k[1]
        t = 1000000000
        t = (t-start_index)%(cycle-start_index)+start_index
        w = tree_list[t-1]
        print(w)

p1()
p2()

