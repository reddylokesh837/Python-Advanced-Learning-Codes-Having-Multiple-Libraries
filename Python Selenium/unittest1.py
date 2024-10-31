from math import  pi
def circle_area(radius):
    if type(radius) not in [int, float]:
        raise TypeError("The radius must be a non-negative real number")
    if radius < 0:
        raise ValueError("The radius cannot be negative.")
    return pi*(radius**2)
#Logic to test: lets execute the above function for all the values in the list
#A positive number, negative number,zero,boolean value, string and also a complex number
radii=[2,0,"radius",-3,3+5j,True]


if __name__== "__main__":
    #Loop through the list to pass on each value of the list as input to the function
    for r in radii:
        try:
            print(circle_area(r))
        except Exception as e:
            print(f"Error is r= {r} with e= {e}")