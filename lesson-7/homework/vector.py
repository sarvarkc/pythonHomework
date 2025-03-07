import math

class Vector:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
    
    def __add__(self, other):
        new_x = self.x + other.x
        new_y = self.y + other.y
        new_z = self.z + other.z
        return Vector(new_x, new_y, new_z)

    def __sub__(self,other):
        new_x = abs(self.x - other.x)
        new_y = abs(self.y - other.y)
        new_z = abs(self.z - other.z)
        return Vector(new_x, new_y, new_z)
    
    def __mul__(self,other):
        if isinstance(other, Vector):
            new_x = self.x * other.x
            new_y = self.y * other.y
            new_z = self.z * other.z
            return new_x+new_y+new_z
        elif isinstance(other, (int, float)):
            new_x = self.x * other
            new_y = self.y * other
            new_z = self.z * other
            return Vector(new_x,new_y,new_z)
        
    def magnitude(self):
        return math.sqrt(self.x**2+self.y**2+self.z**2)
    
    def normalize(self):
        magnitude = self.magnitude()
        return Vector(round(self.x/magnitude,3), round(self.y/magnitude,3), round(self.z/magnitude,3))
        
    def __str__(self):
        return f"Vector({self.x},{self.y},{self.z})"

v1 = Vector(1,2,3)
v2 = Vector(4,5,6)
v3 = v1 + v2
v4 = v1 - v2
dot_product = v1 * v2
v5 = v1 * 3
magnitude = v1.magnitude()
v_unit = v1.normalize()

print(v1)
print(v3)
print(v4)
print(dot_product)
print(v5)
print(magnitude)
print(v_unit)