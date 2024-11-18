from collections import deque

DIR = ((1,0), (0,1), (-1,0), (0,-1))

class Node:
    def __init__(self, x, y, value) -> None:
        self.value = value
        self.x = x
        self.y = y
        self.neighbors = []

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
    
    def get_value(self, value):
        """Returns a square in the grid with a value"""
        for node in self.grid:
            if node.value == value:
                return node
    
    def count(self, value):
        """Returns the number of nodes in the grid with a given value"""
        counter = 0
        for node in self.grid:
            if node.value == value:
                counter += 1
        return counter

def main():
    A = []
    with open('data/a21.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    grid = Grid(A)
    d = deque()
    d.append((grid.get_value("S"), 0))

    plot_counter = 0
    while len(d) > 0:
        plot, path_len = d.popleft()
        if path_len > 64:
            break
        if plot.value != '.' and plot.value != 'S':
            continue
        if path_len%2 == 0:
            plot_counter += 1
        plot.value = 0

        d.extend([(x,path_len+1) for x in plot.neighbors])

    print(plot_counter)

if __name__ == '__main__':
    main()
