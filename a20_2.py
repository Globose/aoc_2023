from math import lcm

class Flop:
    def __init__(self, name) -> None:
        self.status = False
        self.targets = []
        self.roots = []
        self.name = name
    
    def receive(self, origin, signal):
        if signal == 1:
            return
        self.status = not self.status
        sig = 0
        if self.status:
            sig = 1
        slist = []
        for t in self.targets:
            slist.append((self, t, sig))
        return slist

    def add_root(self, r):
        self.roots.append(r)

    def __repr__(self) -> str:
        return self.name

class Con:
    def __init__(self, name) -> None:
        self.roots = []
        self.targets = []
        self.name = name

    def add_root(self, r):
        self.roots.append((r,0))

    def status(self):
        for r in self.roots:
            if r[1] == 0:
                return False
        return True

    def change_stat(self, root, signal):
        for i, r in enumerate(self.roots):
            if r[0] == root:
                self.roots[i] = (root, signal)

    def receive(self, origin, signal):
        self.change_stat(origin, signal)
        sig = 1
        if self.status():
            sig = 0
        slist = []
        for t in self.targets:
            slist.append((self, t, sig))
        return slist

    def __repr__(self) -> str:
        return self.name

class Bc:
    def __init__(self, targets, name) -> None:
        self.targets = targets
        self.name = name

    def receive(self, origin, signal):
        slist = []
        for t in self.targets:
            slist.append((self, t,0))
        return slist

class Rec:
    def __init__(self, name) -> None:
        self.roots = []
        self.name = name
    
    def add_root(self, r):
        self.roots.append(r)

    def receive(self, origin, signal):
        return []
    

def p2():
    with open('data/a20.txt', 'r', encoding='UTF-8') as file:
        A = []
        for s in file:
            A.append(s.strip("\n"))
        flops = {}
        bc = None

        for a in A:
            mtype = a[0]
            mname = a.split(' ')[0][1:]
            f = None
            if mtype == '%':
                f = Flop(mname)
                flops[mname] = f
            elif mtype == '&':
                f = Con(mname)
                flops[mname] = f
            else:
                bc = a[15:].split(',')

        for i, a in enumerate(A):
            if a[0] == 'b':
                continue
            mname = a.split(' ')[0][1:]
            mtarget = a.split('>')[1].split(',')
            for target in mtarget:
                tname = target.strip()
                # print(f"name |{mname}|{tname}|")

                f = flops.get(tname)
                this = flops.get(mname)
                if f is None:
                    f = Rec(tname)
                this.targets.append(f)
                f.add_root(this)
        
        targets= []
        for target in bc:
            tn = target.strip()
            targets.append(flops.get(tn))
        bc = Bc(targets, 'Broadcaster')

        lh = [0,0]
        ts = []
        xm_r = ("ft", "jz", "sv", "ng")
        d = {}
        for x in xm_r:
            d[x] = []

        for i in range(15000):
            ts.append((None, bc, 0))
            while len(ts) > 0:
                t1 = ts.pop(0)
                signal = t1[2]
                lh[signal] += 1

                low = "low"
                if signal == 1:
                    low = "high"

                name = "button"
                if t1[0] is not None:
                    name = t1[0].name

                if t1[1].name == "xm" and signal == 1:
                    d[t1[0].name].append(i)

                # print(f"{name} -{low}-> {t1[1].name}")
                lst = t1[1].receive(t1[0], signal)
                if lst is not None:
                    ts.extend(lst) 
        # print(lh, lh[0]*lh[1])
        tf = []
        for entry in d:
            r = d.get(entry)
            for i in range(len(r)-1, 0,-1):
                r[i] = r[i]-r[i-1]
            print(r)
            tf.append(r[1])
        print(lcm(*tf))

p2()