def p1():
    data = [(41,249), (77,1362), (70,1127), (96,1011)]
    
    margin = 1
    for x in data:
        times = []
        for i in range(x[0]+1):
            d = (x[0] - i)*i
            # print(i, d)
            if d > x[1]:
                times.append(i)

        m = max(times)-min(times)+1
        margin *= m

    print(margin)

def p2():
    data = (41777096, 249136211271011)

    n_1 = (int)(0.5*data[0]-(0.25*(data[0]**2)-data[1])**0.5+1)
    n_2 = (0.5*data[0]+(0.25*(data[0]**2)-data[1])**0.5)
    n_2_int = (int)(n_2)
    if n_2 - n_2_int == 0:
        n_2_int -=1
    n_1_int = (int)(n_1)

    gap = n_2_int-n_1_int+1
    print(gap)

p1()
p2()