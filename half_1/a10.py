
def p1():
    with open('data/a10.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        pos = (0,0)
        for y, line in enumerate(A):
            for x, char in enumerate(line):
                if char == 'S':
                    pos = (x,y)
                    break
        # print(pos)
        dir = (1,0)
        pos = (pos[0]+1,pos[1])
        current = A[pos[1]][pos[0]]
        counter = 1
        while current != 'S':
            counter += 1
            # print(current, pos, dir)
            if current == 'J':
                if dir[0] == 1:
                    dir = (0,-1)
                else:
                    dir = (-1,0)
            elif current == 'F':
                if dir[0] == -1:
                    dir = (0,1)
                else:
                    dir = (1,0)
            elif current == '7':
                if dir[0] == 1:
                    dir = (0, 1)
                else:
                    dir = (-1,0)
            elif current == 'L':
                if dir[0] == -1:
                    dir = (0,-1)
                else:
                    dir = (1,0)
            elif current == '-':
                dir = (dir[0], 0)
            elif current == '|':
                dir = (0, dir[1])

            pos = (pos[0]+dir[0], pos[1]+dir[1])
            current = A[pos[1]][pos[0]]
        print((int)(counter/2))

def p2():
    with open('data/a10.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        pos = (0,0)
        pipes = {}
        for y, line in enumerate(A):
            for x, char in enumerate(line):
                pipes[(x,y)]=A[y][x]
                if char == 'S':
                    pos = (x,y)
                    pipes[pos] = 'S'
        nmap = {}
        addeddots = 0
        sym = {'F':'....F-.|.', '7':'...-7..|.', 'L':'.|..L-...','J':'.|.-J....','|':'.|..|..|.', '-':'...---...', 'S':'...-S-...', '.':'.........'}
        for y in range(len(A)):
            for x in range(len(A[0])):
                c = 0
                key = pipes[(x,y)]
                for s in sym[key]:
                    nmap[(x*3+c%3,y*3+c//3)] = sym[key][c]
                    c+=1
                    if sym[key] == '.':
                        addeddots += 8
                    else:
                        addeddots += sym[key].count('.')

        D = []
        for y in range(3*len(A)):
            newline = ""
            for x in range(3*len(A[0])):
                newline += nmap[(x,y)]
                if nmap[(x,y)] == 'S':
                    pos = (x,y)
            D.append(newline)

        line = {}
        line[pos] = True
        dir = (1,0)
        pos = (pos[0]+dir[0],pos[1])
        current = D[pos[1]][pos[0]]
        while current != 'S':
            line[pos] = True
            nmap[pos] = current
            if current == 'J':
                if dir[0] == 1:
                    dir = (0,-1)
                else:
                    dir = (-1,0)
            elif current == 'F':
                if dir[0] == -1:
                    dir = (0,1)
                else:
                    dir = (1,0)
            elif current == '7':
                if dir[0] == 1:
                    dir = (0, 1)
                else:
                    dir = (-1,0)
            elif current == 'L':
                if dir[0] == -1:
                    dir = (0,-1)
                else:
                    dir = (1,0)
            elif current == '-':
                dir = (dir[0], 0)
            elif current == '|':
                dir = (0, dir[1])

            pos = (pos[0]+dir[0], pos[1]+dir[1])
            current = D[pos[1]][pos[0]]

        changed = []
        for y in range(len(D)):
            if not line.get((0,y)):
                nmap[(0,y)] = 0
                changed.append((0,y))
            if not line.get((len(D[0])-1,y)):
                nmap[(len(D[0])-1,y)] = 0
                changed.append((len(D[0])-1,y))
        for x in range(len(D[0])):
            if not line.get((x,0)):
                nmap[(x,0)] = 0
                changed.append((x,0))
            if not line.get((x,len(D)-1)):
                nmap[(x,len(D)-1)] = 0
                changed.append((x,len(D)-1))

        nlist = [(-1,-1),(0,-1), (1,-1), (-1,0), (1,0), (-1,1), (0,1), (1,1)]
        while len(changed) > 0:
            for cpos in changed.copy():
                for n in nlist:
                    npos = (cpos[0]+n[0], cpos[1]+n[1])
                    if npos[0] >= len(D[0]) or npos[0] < 0 or npos[1] >= len(D) or npos[1] < 0:
                        continue
                    if line.get(npos) is None and nmap.get(npos) != 0:
                        nmap[npos] = 0
                        changed.append(npos)
                changed.remove(cpos)

        for y in range(len(D)):
            for x in range(len(D[0])):
                if line.get((x,y)) is not None:
                    for n in nlist:
                        npos = (x+n[0], y+n[1])
                        if npos[0] >= len(D[0]) or npos[0] < 0 or npos[1] >= len(D) or npos[1] < 0:
                            continue
                        nmap[npos] = 1

        counter = 0
        for y in range(len(D)):
            for x in range(len(D[0])):
                value = nmap.get((x,y))
                if value != 1 and value != 0:
                    counter += 1
        print((int)(counter/9))


p1()
p2()
