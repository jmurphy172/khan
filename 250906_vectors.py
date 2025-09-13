from utils import *

import math

from math import *


magnitude = sqrt(

                    ( 8*dcos(140) + 4*dcos(40) )**2
                        
                +   ( 8*dsin(140) + 4*dsin(40) )**2

        ) 
    

theta = datan(

            ( 8*dsin(140) + 4*dsin(40) )/

            ( 8*dcos(140) + 4*dcos(40) )

            )+180

print(

        f"\n\nmagnitude = {magnitude} \n\ntheta\n\n = {theta}"    
)
