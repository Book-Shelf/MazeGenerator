from maze_generator import Grid
from maze_generator_animation import Grid as GridAnim

###############################
###### RECURSIVE OPTION ######
###############################
# import sys
# grid = Grid(10, 10, (0, 0))

# sys.setrecursionlimit(10000)
# grid.generate_maze_recurs()
# sys.setrecursionlimit(1000)
# grid.show()
##############################



###############################
###### ITERATIVE OPTION ######
###############################

###############################
###### JOIN IMAGES OPTION ######
###############################
# grid = Grid(15, 15, (5, 5))
# grid.generate_maze_iter(saveSteps=True)
# grid.show()
# grid.createGif("Maze_15x15")

########################################
###### MATPLOTLIB ANIMATION OPTION ######
#######################################
grid_anim = GridAnim(10, 10, (0, 0))
grid_anim.generate_maze_iter(saveSteps=True)
grid_anim.show("Maze_10x10", save=True)
##############################