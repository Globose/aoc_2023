def p1():
    with open('data/a20.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        modules = {}
        flops = {}
        sources = {}
        for i, a in enumerate(A):
            A[i] = a.split(" -> ")
            destinations = tuple(A[i][1].split(", "))
            type = None
            name = A[i][0]
            if A[i][0][0] == "%":
                type = "%"
                name = name[1:]
                flops[name] = False
            elif A[i][0][0] == "&":
                type = "&"
                name = name[1:]
                sources[name] = {}
            modules[name] = (type, destinations)

            # modules['button'] = (None, ('broadcaster',))

        for m in modules:
            dests = modules[m][1]
            for d in dests:
                if d == 'output':
                    continue
                mod = modules.get(d)
                if mod is None:
                    continue
                if mod[0] == '&':
                    sources[d][m] = "low"
        low = 0
        high = 0
        counter = 0
        # que = [("inv", "low")]
        for i in range(1000):
            que = [("broadcaster", "low", "button")]
            while len(que) > 0:
                pulse = que.pop(0)
                print(pulse[2], f"-{pulse[1]}->",pulse[0])
                if pulse[1] == "low":
                    low += 1
                else:
                    high += 1
                # print("pulse", pulse, low, high)
                module = modules.get(pulse[0])
                if module is None:
                    continue

                send_signal = None
                if module[0] == '%':
                    if pulse[1] == "high":
                        continue
                    on = flops[pulse[0]]
                    flops[pulse[0]] = not on
                    send_signal = "high"
                    if on:
                        send_signal = "low"
                elif module[0] == '&':
                    send_signal = "low"
                    sources[pulse[0]][pulse[2]] = pulse[1]
                    for s in sources[pulse[0]].values():
                        if s == "low":
                            send_signal = "high"
                            break
                else:
                    send_signal = pulse[1]
                if send_signal is None:
                    continue

                for d in module[1]:
                    que.append((d, send_signal, pulse[0]))
            counter += 1
            print(f"{counter}. {low}; {high}")
            low = high = 0
        print(low, high)
        print(low*high)


<<<<<<< Updated upstream
p1()
=======
def p2():
    with open('data/a20.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        modules = {}
        flops = {}
        sources = {}
        for i, a in enumerate(A):
            A[i] = a.split(" -> ")
            destinations = tuple(A[i][1].split(", "))
            type = None
            name = A[i][0]
            if A[i][0][0] == "%":
                type = "%"
                name = name[1:]
                flops[name] = False
            elif A[i][0][0] == "&":
                type = "&"
                name = name[1:]
                sources[name] = {}
            modules[name] = (type, destinations)

            # modules['button'] = (None, ('broadcaster',))

        for m in modules:
            dests = modules[m][1]
            for d in dests:
                if d == 'output':
                    continue
                mod = modules.get(d)
                if mod is None:
                    continue
                if mod[0] == '&':
                    sources[d][m] = "low"
        print(sources.get("xm"))
        # return
    
        low = 0
        high = 0
        # que = [("inv", "low")]
        for i in range(1):
            print(i, "\n")
            que = [("broadcaster", "low", "button")]
            while len(que) > 0:
                pulse = que.pop(0)
                print(pulse[2], f"-{pulse[1]}->",pulse[0])
                if pulse[1] == "low":
                    low += 1
                else:
                    high += 1
                # print("pulse", pulse, low, high)
                module = modules.get(pulse[0])
                if module is None:
                    continue

                send_signal = None
                if module[0] == '%':
                    if pulse[1] == "high":
                        continue
                    on = flops[pulse[0]]
                    flops[pulse[0]] = not on
                    send_signal = "high"
                    if on:
                        send_signal = "low"
                elif module[0] == '&':
                    send_signal = "low"
                    sources[pulse[0]][pulse[2]] = pulse[1]
                    for s in sources[pulse[0]].values():
                        if s == "low":
                            send_signal = "high"
                            break
                    if pulse[0] == "xm":
                        print(pulse[0], sources[pulse[0]])
                else:
                    send_signal = pulse[1]
                if send_signal is None:
                    continue

                for d in module[1]:
                    que.append((d, send_signal, pulse[0]))
        print(low, high)
        print(low*high)

#p1()
p2()
>>>>>>> Stashed changes
