DIR = ((0,-1), (-1,0), (1,0), (0,1))
symbols = {'^':0, '<':1, '>':2, 'v':3}
from collections import deque

class Cell:
    def __init__(self, x, y, value) -> None:
        self.value = value
        self.x = x
        self.y = y
        self.adj = []
        self.connections = []
        self.visited = False

    def add_neighbors(self, cells):
        for d in DIR:
            neighbor = cells.get((self.x+d[0],self.y+d[1]))
            if neighbor:
                self.adj.append(neighbor)

    def cords(self):
        return (self.x,self.y)

    def __eq__(self, other):
        if isinstance(other, Cell):
            return self.x == other.x and self.y == other.y
        elif isinstance(other, tuple):
            return (self.x, self.y) == other
        return False

    def __hash__(self) -> int:
        return hash((self.x, self.y))

    def __repr__(self) -> str:
        return f"({self.x}, {self.y}) = {self.value}"

    def __str__(self) -> str:
        return f"({self.x}, {self.y}) = {self.value}"

class Grid:
    def __init__(self, grid) -> None:
        self.grid = {}
        self.width = len(grid[0])
        self.height = len(grid)
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                n = Cell(x,y,cell)
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


def get_unvisited(cell):
    adj_cells = []
    for c2 in cell.adj:
        if c2.value != '#' and not c2.visited: 
            adj_cells.append(c2)
    return len(adj_cells), adj_cells

def longest_path(start_node, end_node):
    if end_node == start_node:
        return 1
    start_node.visited = True
    p_len = 0
    for c in start_node.connections:
        if not c[0].visited:
            p_value = longest_path(c[0], end_node)
            if p_value:
                p_len = max(p_len, c[1]+p_value)
    start_node.visited = False
    return p_len

def main():
    A = []
    with open('data/a23.txt', 'r', encoding='UTF-8') as file:
        A = [line.strip() for line in file]
    grid = Grid(A)
    unvisited_node_cells = [grid.get(1,0)]
    nodes = [grid.get(1,0)]
    while len(unvisited_node_cells) > 0:
        current_cell = unvisited_node_cells.pop()
        current_cell.visited = True

        for c_neigh in current_cell.adj:
            if c_neigh.value == '#' or c_neigh.visited:
                continue
            w_len = 1
            walker: Cell
            walker = c_neigh
            num_paths, paths = get_unvisited(walker)
            
            while num_paths == 1 and not walker in nodes:
                w_len += 1
                walker.visited = True
                walker = paths[0]
                num_paths, paths = get_unvisited(walker)

            if walker not in nodes:
                nodes.append(walker)
            if num_paths > 1:
                unvisited_node_cells.append(walker) 
            current_cell.connections.append((walker, w_len))
            walker.connections.append((current_cell, w_len))
        current_cell.visited = False 

    # for n in nodes:
    #     n:Cell
    #     print(n, n.connections, n.visited)

    lp = longest_path(grid.get(1,0), grid.get(grid.width-2,grid.height-1))-1
    print(lp)

                    
if __name__ == '__main__':
    main()