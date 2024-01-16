def move(A, beam):
    beams = []
    done = {}
    energized = {}
    while True:
        x = beam[0]+beam[2]
        y = beam[1]+beam[3]
        if x < 0 or x >= len(A[0]) or y < 0 or y >= len(A):
            if len(beams) == 0:
                break
            beam = beams.pop()
            continue

        sign = A[y][x]
        energized[(x,y)] = 1
        v_y = beam[3]
        v_x = beam[2]
        new_beam = None
        if sign == '\\':
            v_x = beam[3]
            v_y = beam[2]
        elif sign == '/':
            v_x = -beam[3]
            v_y = -beam[2]
        elif sign == '|':
            if beam[2] != 0:
                new_beam = (x,y,0, -beam[2])
                v_y = beam[2]
                v_x = 0
        elif sign == '-':
            if beam[3] != 0:
                new_beam = (x,y, -beam[3], 0)
                v_x = beam[3]
                v_y = 0
        if new_beam is not None and done.get(new_beam) is None:
            done[new_beam] = 1
            beams.append(new_beam)
        beam = (x,y,v_x,v_y)
        if done.get(beam) is not None:
            if len(beams) == 0:
                break
            beam = beams.pop()
            continue
        done[beam] = 1
    return(len(energized))

def p1():
    with open('data/a16.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        print(move(A, (-1,0,1,0)))

def p2():
    with open('data/a16.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        lst = []
        for i in range(len(A)):
            lst.append((move(A,(-1,i,1,0))))
            lst.append((move(A,(len(A[0]),i,-1,0))))
        for i in range(len(A[0])):
            lst.append((move(A,(i,-1,0,1))))
            lst.append((move(A,(i,len(A),0,-1))))

        print(max(lst))

p1()
p2()
