class Vector:
    def __init__(self, x, y, z) -> None:
        self.x = x
        self.y = y
        self.z = z

    def __eq__(self, other):
        if isinstance(other, Vector):
            return self.x == other.x and self.y == other.y and self.z == other.z
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y, self.z))
    
    def __repr__(self) -> str:
        return f"({self.x}, {self.y}, {self.z})"

class Brick:
    def __init__(self, x0, y0, z0, x1, y1, z1) -> None:
        self.cubes = []
        for x in range(x0,x1+1):
            for y in range(y0,y1+1):
                for z in range(z0,z1+1):
                    self.cubes.append(Vector(x,y,z))
        self.support = set()
        self.low = z0
        self.safe_to_remove = True

    def __lt__(self, other):
        return self.low < other.low
    
    def __repr__(self) -> str:
        return f"{self.low} {self.cubes}"

    def fall(self, room):
        free = True
        new_values = []
        for c in self.cubes:
            v = Vector(c.x, c.y, c.z-1)
            new_values.append(v)
            if room.get(v) is not None and room.get(v) != self:
                self.support.add(room.get(v))
                free = False
            if v.z == 0:
                free = False
        if free:
            for i in range(len(self.cubes)):
                room[self.cubes[i]] = None
                self.cubes[i] = new_values[i]
                room[self.cubes[i]] = self
        return free
    
    def dependence(self):
        if len(self.support) == 1:
            support = self.support.pop()
            support.safe_to_remove = False

def p1():
    A = []
    with open('data/a22.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]

    bricks = []
    for b in A:
        cords = [int(x) for s in b.split('~') for x in s.split(',')]
        bricks.append(Brick(*cords))
    
    ### Create room
    room = {}
    for b in bricks:
        for v in b.cubes:
            room[v] = b
    bricks.sort()

    ### Move bricks down
    locked_bricks = []
    while len(bricks) > 0:
        locked = []
        for b in bricks:
            if not b.fall(room):
                locked.append(b)
        for l in locked:
            bricks.remove(l)
        locked_bricks.extend(locked)

    ### Find safe bricks
    for b in locked_bricks:
        b.dependence()

    free_bricks = 0
    for b in locked_bricks:
        if b.safe_to_remove:
            free_bricks += 1
    
    print(free_bricks)
    


if __name__ == '__main__':
    p1()