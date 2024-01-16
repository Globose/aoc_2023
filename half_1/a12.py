def fill(B, order, index):
    # print(B[index:], order, index)
    comb = 0
    if len(order) == 0:
        if '#' not in B[index:]:
            return 1
        return 0
    if index >= len(B):
        return 0
    if B[index] == '?':
        B[index] = '#'

        i = 0
        order_done = True
        while i < order[0]:
            if i+index >= len(B) or B[i+index] == '.':
                order_done = False
                break
            i+=1

        if order_done and (i+index == len(B) or (i+index < len(B) and B[i+index] != '#')):
            comb = 1
            mult = fill(B, order[1:], index+i+1)
            comb *= mult

        B[index] = '.'
        comb += fill(B, order, index+1)
        B[index] = '?'
    elif B[index] == '#':
        i = 0
        if order[0] + index > len(B):
            return 0
        while i < order[0]:
            if B[i+index] == '.':
                return 0
            i+=1
        if i+index < len(B) and B[i+index] == '#':
            return 0
        comb = 1
        comb *= fill(B, order[1:], index+1+i)
    elif B[index] == '.':
        return fill(B, order, index+1)
    return comb

def p1():
    with open('data/a12.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            A[i] = a.split(" ")
            lst_int = [int(x) for x in A[i][1].split(",")]
            B = [*A[i][0]]
            result = fill(B, lst_int, 0)
            sum += result
        print(sum)


def r(A, O, onum, i, cache:dict):
    # print(A[i:], O[onum:])
    if onum >= len(O):
        if '#' in A[i:]:
            return 0
        return 1

    while i < len(A) and A[i] == '.':
        i += 1

    if i >= len(A):
        return 0

    h1 = hash((i,onum))
    if cache.get(h1) is not None:
        return cache.get(h1)

    ok = True
    for j in range(i,i+O[onum]):
        if j >= len(A):
            ok = False
            break
        if A[j] == '.':
            ok = False

    if ok and i+O[onum] < len(A) and A[i+O[onum]] == '#':
        ok = False

    r1 = r2 = 0
    if ok:
        r1 = r(A, O, onum+1, i+O[onum]+1, cache)

    if A[i] == '?':
        r2 = r(A, O, onum, i+1, cache)

    cache[h1] = r1+r2
    return r1+r2

def p2():
    with open('data/a12.txt', 'r', encoding='UTF-8') as file:
        A = []
        sum = 0
        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            # if i != 5:
            #     continue
            A[i] = a.split(" ")
            O = [int(x) for x in A[i][1].split(",")]*5
            A[i] = [*A[i][0]+'?']*5
            A[i] = A[i][:-1]

            cache = {}
            res = r(A[i], O, 0, 0, cache)
            sum += res
        print(sum)


p1()
p2()