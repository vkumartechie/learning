import math

def radius_of_circle(redius):

    area=math.pi*redius*redius
    return area

def main():
    #take user input
    num=input('Enter the redius of circle :')
    radius=float(num)
    area=radius_of_circle(radius)
    print(f'The area of circle with radius {radius} is {area}')
    
#calling main function - special built in variable in python
if __name__=='__main__':
    main()



