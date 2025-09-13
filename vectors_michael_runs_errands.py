import numpy as np

from numpy import array as array

from utils import *

"""


Michael is running some errands.

He runs in four directions

North => +y

South => -y

East => +x 

West => -x


"""


# list based approach

north = [5]

south = [3]

east = [6]

west = [2] 

south.append(1)

west.append(7)



north = sum(north)

south = sum(south)

east = sum(east)

west = sum(west)



x = east - west

y = north - south


print (f"New position ({x},{y})")



# direction from east

# rise over run # gradient # tangent
slope = y/x


print (f"Slope = {slope}")

# tan(theta) = y / x

# theta = atan(y / x)

theta = angle_from_coordinates(x,y)

print (f"Angle = {round(theta,2)}")

































