import numpy as np

def main():
    A = []
    with open('data/a24.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    lines = []
    for a in A:
        mod = a.replace(" @", ',')
        values = [int(x) for x in mod.split(',')]
        lines.append((values[0], values[1], values[3], values[4]))

    p1 = 200000000000000
    p2 = 400000000000000

    counter = 0
    for i in range(len(lines)):
        vx, vy, vdx, vdy = lines[i]
        for j in range(i+1, len(lines)):
            ux, uy, udx, udy = lines[j]
            a1 = np.array([[vdx, -udx],[vdy, -udy]])
            a2 = np.array([ux-vx, uy-vy])
            rank = np.linalg.matrix_rank(a1)
            if rank == 2:
                k1, k2 = np.linalg.solve(a1,a2)
                if k1 >= 0 and k2 >= 0:
                    x = round(vx+vdx*k1,3)
                    y = round(vy+vdy*k1,3)
                    if p1 <= x <= p2 and p1 <= y <= p2:
                        counter += 1
    print(counter)

if __name__ == '__main__':
    main()