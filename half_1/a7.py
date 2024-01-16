CARDS = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
C1 = "AKQJT98765432"
C1 = "AKQT98765432J"

def rank(hand):
    d = {}
    for c in hand:
        if d.get(c) is None:
            d[c] = 1
        else:
            d[c] += 1

    counter = [0 for x in range(1,6)]

    for k in d.keys():
        counter[d[k]-1] += 1

    if counter[4] == 1:
        return 6
    if counter[3] == 1:
        return 5
    if counter[2] == 1:
        if counter[1] == 1:
            return 4
        return 3
    if counter[1] == 2:
        return 2
    if counter[1] == 1:
        return 1
    return 0


def rank_j(hand):
    d = {}
    for c in hand:
        if d.get(c) is None:
            d[c] = 1
        else:
            d[c] += 1

    counter = [0 for x in range(1,6)]

    for k in d.keys():
        if k == "J":
            continue
        counter[d[k]-1] += 1
    
    joker = d.get("J")
    if joker is None:
        joker = 0

    if counter[4] == 1:
        return 6
    if counter[3] == 1:
        return 5+joker
    if counter[2] == 1:
        if counter[1] == 1:
            return 4
        if joker > 0:
            return 4+joker
        return 3
    if counter[1] == 2:
        if joker > 0:
            return 4
        return 2
    if counter[1] == 1:
        if joker == 1:
            return 3
        if joker == 2:
            return 5
        if joker == 3:
            return 6
        return 1
    if joker == 1:
        return 1
    if joker == 2:
        return 3
    if joker == 3:
        return 5
    if joker == 4:
        return 6
    if joker == 5:
        return 6
    return 0


def p1():
    with open('data/a7.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            p = A[i].split(" ")
            A[i] = (rank(p[0]), p[0], (int)(p[1]))
        
        A.sort()

        for i in range(1, len(A)):
            key = A[i]
            for j in range(i-1, -1, -1):
                if key[0] > A[j][0]:
                    break
                
                swap = False
                for k in range(0,5):
                    key_1 = C1.find(key[1][k])
                    alt_1 = C1.find(A[j][1][k])
                    if key_1 > alt_1:
                        swap = True
                        break
                    elif key_1 < alt_1:
                        break
                
                if not swap:
                    break
                else:
                    A[j+1] = A[j]
                    A[j] = key
        sum = 0
        for i, e in enumerate(A):
            sum += e[2]*(i+1)
        print(sum)

def p2():
    with open('data/a7.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []

        for s in file:
            A.append(s.strip("\n"))
        for i, a in enumerate(A):
            p = A[i].split(" ")
            A[i] = (rank_j(p[0]), p[0], (int)(p[1]))
        
        A.sort()

        for i in range(1, len(A)):
            key = A[i]
            for j in range(i-1, -1, -1):
                if key[0] > A[j][0]:
                    break
                
                swap = False
                for k in range(0,5):
                    key_1 = C1.find(key[1][k])
                    alt_1 = C1.find(A[j][1][k])
                    if key_1 > alt_1:
                        swap = True
                        break
                    elif key_1 < alt_1:
                        break
                
                if not swap:
                    break
                else:
                    A[j+1] = A[j]
                    A[j] = key
        sum = 0
        for i, e in enumerate(A):
            sum += e[2]*(i+1)

        print(sum)

p1()
p2()