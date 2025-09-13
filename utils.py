from math import *

import math

def dsin(x):
	return sin(radians(x))

def dcos(x):
    return cos(radians(x))


def datan(x):
    return degrees(atan(x))


def angle_from_coordinates(x,y):

    if x > 0 and y > 0:
    
        return datan(y/x)

    elif x < 0 and y > 0:

        return 180 - abs(datan(y/x))

    elif x < 0 and y < 0:

        return 180 + abs(datan(y/x))

    elif x > 0  and y < 0:
    

        
        angle = 360 + abs(datan(y/x))


        return angle
    



    else: print("Something has gone wrong")



def mag_of_vector_from_coords(x1y1, x2y2):

    """
    Returns magnitude for two sets of 

    coordinates given as two tuples

    """

    x1, y1 = x1y1

    x2, y2 = x2y2



    return sqrt(

                    (x2 - x1)**2 + (y2 - y1)**2


                )


def v_coords_from_angle_and_magnitude(angle, mag):

    """

    sin (angle) = opp/hyp

    cos (angle) = adj/hyp

    tan(theta) = opp/adj


    hyp * cos (angle) = adj


    hyp * sin (angle) = opp

    """


    adj = mag * dcos(angle)

    opp = mag * dsin(angle)                           

    
    coords = (adj, opp)


    return coords



test_v_coords_from_angle_and_magnitude = False


if test_v_coords_from_angle_and_magnitude:

    angle = 300

    mag = 8

    print(
            
    v_coords_from_angle_and_magnitude(angle, mag) 

                )





class Vector:

    @staticmethod
    def angle_from_coords(coords):

        x, y = coords

        if x > 0 and y > 0:
        
            return datan(y/x)


        elif x < 0 and y > 0:

            return 180 - abs(datan(y/x))

        elif x < 0 and y < 0:

            return 180 + abs(datan(y/x))


        elif x > 0  and y < 0:
            
            angle = 360 + abs(datan(y/x))

            return angle

        
        else:

            print("Something has gone wrong")


    @staticmethod
    def mag_from_coords(x1y1 = None, x2y2 = None):

        """
        Returns magnitude from one or two sets of 

        coordinates given as two tuples

        """


        if x1y1 is not None and x2y2 is not None:

            x1, y1 = x1y1

            x2, y2 = x2y2



            return sqrt(

                        (x2 - x1)**2 + (y2 - y1)**2


                        )


        elif x1y1 is not None:

            x, y = x1y1


            return sqrt(x**2 + y**2)


        else:


            raise ValueError("Coordinates not given?")








    @staticmethod
    def coords_from_angle_and_mag(angle, mag):

           
        adj = mag * dcos(angle)

        opp = mag * dsin(angle)                           

        
        coords = (adj, opp)


        return coords



    def __init__(

            self,

            coords = None,

            coords2 = None,

            angle = None,

            mag = None

            ):

                self.coords = coords

                self.coords2 = coords2
                
                if self.coords is not None:

                    self.x1, self.y1 = self.coords


                if self.coords2 is not None:

                    self.x2, self.y2 = self.coords2


                self.angle = angle

                self.mag = mag
            
                if self.coords is not None and self.coords2 is not None:

                    self.mag = Vector.mag_from_coords(

                            self.coords, self.coords2

                            )

                elif self.coords is not None:
                    
                    self.angle = Vector.angle_from_coords(self.coords)

                    self.mag = Vector.mag_from_coords(self.coords)



                elif self.angle is not None and self.mag is not None:

                    self.coords = Vector.coords_from_angle_and_mag(

                            self.angle,

                            self.mag 

                            )

                    self.x1 , self.y1 = self.coords

                
                else: 

                    raise ValueError(

                            "Not enough informtion provided to initialize variable"

                            )



    def __add__(self, other):

        if self.coords2 is not None or other.coords2 is not None:

            print ("Addition for vectors not centred on the origin is not supported yet")

        else:

            return Vector((self.x1 + other.x1, self.y1 + other.y1))




        






##########################################################

test_add = True

if test_add == True:

    v1 = Vector((3,4))

    v2 = Vector((2,1))

    v3 = v1 + v2

    print (v3.coords)


    z1 = Vector( angle = 170, mag = 5 )

    z2 = Vector( angle = 300, mag = 8 )

    z3 = z1 + z2




    print (f"coords = {z3.coords}")

    print (f"mag = {z3.mag}")

    print (f"angle = {z3.angle}")


test_vector = False

if test_vector:

    v1 = Vector(

            coords = (2,9)

            )


    v2 = Vector(

            angle = 45,

            mag = 10

            )


    print (v1)

    print (v1.angle)




test_mag_of_vector_from_coords = False

if test_mag_of_vector_from_coords:

    print(

        mag_of_vector_from_coords(

            (-2,-8) , (4,-4)

                                   )

        )


test_angle_from_coordinates = False

if test_angle_from_coordinates:

    x = 4

    y = -8

    print(f"""

The angle is:

            {angle_from_coordinates(x, y)} degrees

          """
          )

    print(datan(x/y))
    

