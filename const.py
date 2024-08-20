import numpy as np

# Window Dimensions
WINDOW_WIDTH = 1400
WINDOW_HEIGHT = 480*1.7
FRAMERATE = 60

# Number of random objects to be spawned
QUANTITY = 1000
# Maximum initial mass of random objects 
MAX_MASS = 1
# Maximum initial velocity 
MAX_INITIAL_VELOCITY = 1

# Scales the attractive force 
ATTRACTION = 1
ATTRACTION_MATRIX = np.array([[1, 1, 3],
                              [1, 2, 1],
                              [3, 1, -2]])
# Any entities outside of x units don't ineract; helps with performance
EFFECT_RANGE = 200
# Additional range where entities will merge (can reduce max forces)
MERGE_RANGE = 10
COLLISION_ENABLED = False
VISCOSITY = 0.1

BASE_DT = 1

# Determines size of objects relative to mass
ENTITY_DENSITY = 1 
RADIUS_SCALING = 5


