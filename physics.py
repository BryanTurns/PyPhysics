from const import QUANTITY, MERGE_RANGE, EFFECT_RANGE, ATTRACTION, WINDOW_HEIGHT, WINDOW_WIDTH, ENTITY_DENSITY, RADIUS_SCALING, COLLISION_ENABLED, ATTRACTION_MATRIX, VISCOSITY
import numpy as np
import math
from numba import jit
from utils import timer_func


# @timer_func
@jit(nopython=True)
def update_entities(entityList, dt):

    forces = np.zeros((QUANTITY, 2))
    for i in range(QUANTITY):
        if entityList[i][0] == 0:
            continue
        for j in range(QUANTITY):
            if i == j:
                continue
            elif entityList[j][0] == 0:
                continue
        
            # Calculate distance from each entity
            dx = entityList[j][1]- entityList[i][1]
            dy = entityList[j][2] - entityList[i][2]
            distance = math.sqrt(pow(dx, 2) + pow(dy, 2))
            if distance > EFFECT_RANGE:
                continue
            
            # Merge objects if they are close enough
            if distance < (entityList[i][5] + entityList[j][5] + MERGE_RANGE):
                if COLLISION_ENABLED:
                    calculateCollision(entityList[i], entityList[j])
                    for col in range(len(entityList[j])):
                        entityList[j][col] = 0
                    return -1
                else:
                    continue
            
            # Calculate unit vector for direction
            dxUnit = dx/distance
            dyUnit = dy/distance
            # Calculate forces
            f = (ATTRACTION * entityList[i][0] * entityList[j][0])/pow(distance, 2)
            fx = f * dxUnit
            fy = f * dyUnit
            forces[i][0] += fx
            forces[i][1] += fy 
    
    # maybe change time scale?
    for i in range(len(entityList)):
        if entityList[i][0] == 0:
            continue
        ax = forces[i][0] / entityList[i][0]
        ay = forces[i][1] / entityList[i][0]

        entityList[i][3] += ax * dt
        entityList[i][4] += ay * dt

        entityList[i][1] += entityList[i][3] * dt
        entityList[i][2] += entityList[i][4] * dt

        if entityList[i][1] > WINDOW_WIDTH:
            entityList[i][1] = WINDOW_WIDTH - 1
            entityList[i][3] = -entityList[i][3]
        elif entityList[i][1] < 0:
            entityList[i][1] = 1
            entityList[i][3] = -entityList[i][3]

        if entityList[i][2] > WINDOW_HEIGHT:
            entityList[i][2] = WINDOW_HEIGHT - 1
            entityList[i][4] = -entityList[i][4]
        elif entityList[i][2] < 0:
            entityList[i][2] = 1
            entityList[i][4] = -entityList[i][4]
    return 0

@jit(nopython=True)
def update_entities_multi(entityList, dt):

    forces = np.zeros((QUANTITY, 2))
    for i in range(QUANTITY):
        if entityList[i][0] == 0:
            continue
        for j in range(QUANTITY):
            if i == j:
                continue
            elif entityList[j][0] == 0:
                continue
        
            # Calculate distance from each entity
            dx = entityList[j][1]- entityList[i][1]
            dy = entityList[j][2] - entityList[i][2]
            distance = math.sqrt(pow(dx, 2) + pow(dy, 2))
            if distance > EFFECT_RANGE:
                continue
            
            # Merge objects if they are close enough
            if distance < (entityList[i][5] + entityList[j][5] + MERGE_RANGE):
                if COLLISION_ENABLED:
                    calculateCollision(entityList[i], entityList[j])
                    for col in range(len(entityList[j])):
                        entityList[j][col] = 0
                    return -1
                else:
                    continue
            
            # Calculate unit vector for direction
            dxUnit = dx/distance
            dyUnit = dy/distance
            # Calculate forces
            attraction = ATTRACTION_MATRIX[int(entityList[i][6])][int(entityList[j][6])]
            f = ( attraction * entityList[i][0] * entityList[j][0])/pow(distance, 2)
            fx = f * dxUnit
            fy = f * dyUnit
            forces[i][0] += fx
            forces[i][1] += fy 
    
    # maybe change time scale?
    for i in range(len(entityList)):
        if entityList[i][0] == 0:
            continue
        ax = forces[i][0] / entityList[i][0]
        ay = forces[i][1] / entityList[i][0]

        entityList[i][3] += ax * dt
        entityList[i][4] += ay * dt

        entityList[i][1] += entityList[i][3] * dt
        entityList[i][2] += entityList[i][4] * dt

        if entityList[i][1] > WINDOW_WIDTH:
            entityList[i][1] = WINDOW_WIDTH - 1
            entityList[i][3] = -entityList[i][3]
        elif entityList[i][1] < 0:
            entityList[i][1] = 1
            entityList[i][3] = -entityList[i][3]

        if entityList[i][2] > WINDOW_HEIGHT:
            entityList[i][2] = WINDOW_HEIGHT - 1
            entityList[i][4] = -entityList[i][4]
        elif entityList[i][2] < 0:
            entityList[i][2] = 1
            entityList[i][4] = -entityList[i][4]
    return 0



@jit(nopython=True)
def calculateRadius(mass):
    return  (((3/(4 * math.pi)) * mass * ENTITY_DENSITY) ** (1/3.0)) * RADIUS_SCALING 


@jit(nopython=True)
def calculateCollision(primaryEntity, secondaryEntity):
    px = primaryEntity[3]*primaryEntity[0] + secondaryEntity[3]*secondaryEntity[0]
    py = primaryEntity[4]*primaryEntity[0] + secondaryEntity[4]*secondaryEntity[3]
    primaryEntity[0] = primaryEntity[0] + secondaryEntity[0]

    primaryEntity[3] = px / primaryEntity[0]
    primaryEntity[4] = py / primaryEntity[0]

    primaryEntity[5] = calculateRadius(primaryEntity[0])
    return primaryEntity