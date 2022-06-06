from random import shuffle
from random import choice
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt 
import matplotlib.colors
import copy

class Cell:
    
    oppositeWall = {"top": "bottom", "left": "right", "bottom": "top", "right": "left"}
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.walls = {"top": True, "left": True, "bottom": True, "left": True}
        self.visited = False
        self.finished = False
        
    def visit(self):
        self.visited = True
        
    def knockDownWall(self, other, wall):
        self.walls[wall] = False
        other.walls[Cell.oppositeWall[wall]] = False

class Grid:
    
    DIRECTIONS = [
            ("left", (-1, 0)),
            ("right", (1, 0)),
            ("top", (0, -1)),
            ("bottom", (0, 1))
        ]
    
    def __init__(self, width, height, start):
        self.height = height
        self.width = width
        self.start = start
        self.maze_map = [[Cell(x, y) for x in range(self.width)] for y in range(self.height)]
        self.__step = 1
        self.__isMazeDone = False
        self.__saveSteps = False
        self.frames = []
        
    def generate_maze_recurs(self):
        self.checkCell(self.start)
        print("Finished generating")
        
    def generate_maze_iter(self, saveSteps=False):
        if saveSteps: 
            self.saveFrame()
            self.__saveSteps = True
            
        self.cellAt(self.start).visit()
        cellStack = [self.cellAt(self.start)]
        if saveSteps: self.progress()
        
        while cellStack:
            currCell = cellStack.pop()
            neighbors = self.find_valid_neighbors(currCell)
            
            if not neighbors: 
                currCell.finished = True
                if saveSteps: self.progress()
                continue
            
            cellStack.append(currCell)
            nextCell = choice(neighbors)
            currCell.knockDownWall(nextCell[0], nextCell[1])
            nextCell[0].visit()
            if saveSteps: self.progress()
            cellStack.append(nextCell[0])
        
        self.__isMazeDone = True
        print("Finished generating")
            
    def checkCell(self, coordinates):
        self.cellAt(coordinates).visit()
        directions = copy.copy(self.DIRECTIONS)
        shuffle(directions)
        
        for direction in directions:
            next = (coordinates[0] + direction[1][0], coordinates[1] + direction[1][1])
            
            if not self.isInsideGrid(next) or self.wasVisited(next): continue
            
            if self.cellIsValid(next, Cell.oppositeWall[direction[0]]):
                self.cellAt(coordinates).knockDownWall(self.cellAt(next), direction[0])
                self.checkCell(next)
                
        self.cellAt(coordinates).finished = True
            
    def find_valid_neighbors(self, cell):
        neighbors = []
        
        for direction in self.DIRECTIONS:
            neighbor = (cell.x + direction[1][0], cell.y + direction[1][1])
            
            if not self.isInsideGrid(neighbor) or self.wasVisited(neighbor): continue
            
            if self.cellIsValid(neighbor, Cell.oppositeWall[direction[0]]):
                neighbors.append((self.cellAt(neighbor), direction[0]))
        
        return neighbors
        
    def cellAt(self, coordinates):
        return self.maze_map[coordinates[1]][coordinates[0]]
    
    def isInsideGrid(self, cooridnates):
        return (0 <= cooridnates[0] < self.width) and (0 <= cooridnates[1] < self.height) 
    
    def wasVisited(self, coordinates):
        return self.cellAt(coordinates).visited

    def cellIsValid(self, coordinates, comesFrom):
        isValid = True
        
        for direction in self.DIRECTIONS:
            if direction[0] == comesFrom: continue
            neighbor = (coordinates[0] + direction[1][0], coordinates[1] + direction[1][1])
            
            if self.isInsideGrid(neighbor) and self.wasVisited(neighbor): 
                isValid = False
                break
        
        return isValid
    
    
    def __str__(self):
        
        maze = []
        
        for row in self.maze_map:
            maze_row = []
            
            for cell in row:
                sign = "#"
                if cell.finished:
                    sign = " "
                elif cell.visited:
                    sign = "."
                    
                maze_row.append(sign)
                
            maze.append(maze_row)
        
        return maze
    
    def saveFrame(self):
        self.frames.append(self.__redraw(self.__str__()))
        
    def show(self, title="maze", save=False, fps=60):
        self.__drawB(fps, save, title)        
        
    def __drawB(self, fps, save, title):
        draw = self.frames[0] if self.__saveSteps else self.__redraw(self.__str__()) 
        
        cvals  = [0, 1, 2]
        colors = ["white", "black", "blue"]

        self.norm = plt.Normalize(min(cvals),max(cvals))
        tuples = list(zip(map(self.norm,cvals), colors))
        self.cmap = matplotlib.colors.LinearSegmentedColormap.from_list("", tuples)
        
        self.fig = plt.figure(figsize=(self.width + 2, self.height + 2))
        self.ax = self.fig.add_axes([0.0, 0.0, 1.0, 1.0], frame_on=False, aspect=1)
        self.im = self.ax.imshow(draw, norm=self.norm, cmap=self.cmap,
                   interpolation='nearest', animated=True)
        self.ax.set_xticks([])
        self.ax.set_yticks([])
        
        if self.__saveSteps and save:
            self.animation = FuncAnimation(self.fig, self.__update, interval=1000 / fps, frames=len(self.frames))
            self.animation.save(f'{title}.gif', fps=fps, dpi=80, bitrate=-1,
            metadata={'artist':'Damian K.'})
            plt.savefig(f'{title}.png')
        elif self.__saveSteps:
            self.animation = FuncAnimation(self.fig, self.__update, interval=1000 / fps, frames=len(self.frames))
        elif save:
            plt.savefig(f'{title}.png')
             
        
        plt.show()
        
                
    def __redraw(self, mazeFrame):
        draw = [[1 for _ in range(self.width + 2)]]
        for row in mazeFrame:
            draw_row = []
            draw_row.append(1)
            for item in row:
                sign = 1
                if item == ".":
                    sign = 2
                elif item == " ":
                    sign = 0
                draw_row.append(sign)
            draw_row.append(1)
            draw.append(draw_row)
        draw.append([1 for _ in range(self.width + 2)])
        
        return draw
        
        
        
    def __update(self, frame):
        self.im.set_array(self.frames[frame])
        return self.im,
        
        
    def progress(self):
        self.__step += 1
        self.saveFrame()

 
if __name__ == "__main__":
    pass