
# this a programe of counting area and perimeter of a circle.

radius = float(input('input the radius: \n'))

class Area:
    
        
    def area_perimeter(self,r,pi=3.1415):
        
        area = pow(r,2)*pi
        print('area is ',area)
        perimeter = pi*r
        print('perimeter is ',perimeter)
    
counting = Area()
counting.area_perimeter(radius)
