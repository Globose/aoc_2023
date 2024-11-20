DIR = ((0,-1), (-1,0), (1,0), (0,1))
symbols = {'^':0, '<':1, '>':2, 'v':3}
from collections import deque

class Node:
    def __init__(self, x, y, value) -> None:
        self.value = value
        self.x = x
        self.y = y
        self.neighbors = []
        self.visited = False

    def add_neighbors(self, nodes):
        for d in DIR:
            neigbor = nodes.get((self.x+d[0],self.y+d[1]))
            if neigbor:
                self.neighbors.append(neigbor)

    def get_cords(self):
        return (self.x,self.y)

    def __eq__(self, other):
        if isinstance(other, Node):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}) = {self.value}"

    def __str__(self) -> str:
        return f"{self.value}"

class Grid:
    def __init__(self, grid) -> None:
        self.grid = {}
        self.width = len(grid[0])
        self.height = len(grid)
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                n = Node(x,y,cell)
                self.grid[n] = n

        for node in self.grid:
            node.add_neighbors(self.grid)
    
    def __repr__(self) -> str:
        s = ""
        for y in range(self.height):
            row = []
            for x in range(self.width):
                s += str(self.grid.get((x,y)))
            s += "\n"
        return s
    
    def __iter__(self):
        itr = []
        for y in range(self.height):
            for x in range(self.width):
                itr.append(self.grid.get((x,y)))
        return iter(itr)

    def get(self,x,y):
        return self.grid.get((x,y))

    def get_value(self, value):
        """Returns a square in the grid with a value"""
        for node in self.grid:
            if node.value == value:
                return node
    
    def count_value(self, value):
        """Returns the number of nodes in the grid with a given value"""
        counter = 0
        for node in self.grid:
            if node.value == value:
                counter += 1
        return counter

def main():
    A = []
    with open('data/a23.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    grid = Grid(A)
    goals = []
    d = deque()
    p_len = 0
    start = grid.get(1,0)
    d.append(start)
    while len(d) > 0:
        top = d[-1]
        if top.get_cords()[1] == grid.height-1:
            goals.append(p_len)
            p_len += 1
            top.visited = True
        if top.visited:
            top.visited = False
            d.pop()
            p_len -= 1
            continue
        p_len += 1
        top.visited = True
        if top.value != '.':
            n1 = top.neighbors[symbols[top.value]]
            if not n1.visited:
                d.append(n1)
        else:
            for n in top.neighbors:
                if n.value != '#' and not n.visited:
                    d.append(n)
    print(max(goals))
        

                    
if __name__ == '__main__':
    main()