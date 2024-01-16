def p1():
    with open('data/a5.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        seeds = A[0].split(" ")[1:]
        for i, s in enumerate(seeds):
            seeds[i] = (int)(s)

        locations = []
        for s in seeds:
            # print("seed", s)
            key = s
            i = 1
            map_key = False
            st = ""
            while i < len(A):
                if len(A[i])==0:
                    # if map_key:
                        # print(st, key)
                    map_key = True
                    st = A[i+1]
                    i += 2
                    continue
                a_split = A[i].split(" ")
                t = ((int)(a_split[0]), (int)(a_split[1]), (int)(a_split[2]))
                if key in range(t[1],t[1]+t[2]) and map_key:
                    map_key = False
                    key = t[0]+key-t[1]
                    # print(st, key)
                i+=1
            locations.append(key)
        locations.sort()
        print(locations[0])

def p2():
    with open('data/a5.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        seeds = A[0].split(" ")[1:]
        for i, s in enumerate(seeds):
            seeds[i] = (int)(s)

        ranges = []
        for i in range (0, len(seeds), 2):
            ranges.append((seeds[i],seeds[i]+seeds[i+1]))

        j = 0
        min_loc = None
        while min_loc is None:
            if j%10000 == 0:
                print(j)
            key = j
            map_key = True
            i = len(A)-1
            while i > 2:
                if len(A[i]) == 0 or A[i][0].isalpha():
                    map_key = True
                    i -= 2
                if not map_key:
                    i-=1
                    continue

                a_split = A[i].split(" ")
                t = ((int)(a_split[0]), (int)(a_split[1]), (int)(a_split[2]))

                if key in range(t[0],t[0]+t[2]):
                    map_key = False
                    key = key-t[0]+t[1]

                i -= 1
            for r in ranges:
                if key in range(r[0],r[1]):
                    min_loc = j
                    break
            j+=1

        print(min_loc)

def p2_2():
    with open('data/a5.txt', 'r', encoding='UTF-8') as file:
        sum = 0
        A = []
        for s in file:
            A.append(s.strip("\n"))
        seeds = A[0].split(" ")[1:]
        for i, s in enumerate(seeds):
            seeds[i] = (int)(s)

        ranges = []
        for i in range (0, len(seeds), 2):
            ranges.append((seeds[i],seeds[i]+seeds[i+1]))

        j = 3
        while True:
            fixed_ranges = []
            while j < len(A) and len(A[j]) > 0:
                a_split = A[j].split(" ")
                t = ((int)(a_split[0]), (int)(a_split[1]), (int)(a_split[2]))
                t = (t[1], t[1]+t[2], t[0]-t[1])
                j+=1

                for i, r in enumerate(ranges.copy()):
                    if t[0] <= r[0] <= t[1] and t[0] <= r[1] <= t[1]:
                        ranges.remove(r)
                        new_range = (r[0]+t[2], r[1]+t[2])
                        fixed_ranges.append(new_range)
                    elif t[0] <= r[0] <= t[1] and r[1] > t[1]:
                        ranges.remove(r)
                        new_range_fixed = (r[0]+t[2], t[1]+t[2])
                        old_range = (t[1], r[1])
                        ranges.append(old_range)
                        fixed_ranges.append(new_range_fixed)
                    elif t[0] <= r[1] <= t[1] and r[0] < t[0]:
                        ranges.remove(r)
                        new_range_fixed = (t[0]+t[2], r[1]+t[2])
                        old_range = (r[0], t[0])
                        ranges.append(old_range)
                        fixed_ranges.append(new_range_fixed)
                    elif r[0] < t[0] and r[1] > t[1]:
                        ranges.remove(r)
                        new_range_fixed = (t[0]+t[2], t[1]+t[2])
                        old_range_1 = (r[0], t[0])
                        old_range_2 = (t[1], r[1])
                        ranges.append(old_range_1)
                        ranges.append(old_range_2)
                        fixed_ranges.append(new_range_fixed)

            for f in fixed_ranges:
                ranges.append(f)
            j += 2
            if j >= len(A):
                break
        ranges.sort()
        print(ranges[0][0])
        # print(ranges)

p1()
# p2()
p2_2()