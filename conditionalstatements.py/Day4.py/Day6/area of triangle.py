
'''
def area_triangle(base, height):
    area = (base*height)/2
    return area
b = float(input("enter base"))
h = float(input("enter height"))
result = area_triangle(b, h)
print("area of triangle=", result)

'''

area = lambda b,h:(b*h)/2
base = float(input("enter base:"))
height = float(input("enter height"))
print("area of triangle=", area(base,height))



   
    