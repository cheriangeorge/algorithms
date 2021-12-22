class Triangle:
    def __init__(self,a,b,c):
        self.a=a
        self.b=b
        self.c=c
    def is_valid(self):
        if self.a>self.b+self.c or self.b>self.a+self.c or self.c>self.b+self.a:
            return "Invalid"
        else:
            return "Valid"
    def Side_Classification(self):
        if self.is_valid()=="Invalid":
            return "Invalid"
        if self.a == self.b == self.c:
            return "Equilateral"
        elif self.a == self.b or self.a == self.c or self.c == self.b:
            return "Isosceles"
        else:
            return "Scalene"
    def Angle_Classification(self):
        if  self.is_valid()=="Invalid":
            return "Invalid"
        sides=[self.a,self.b,self.c]
        sides.sort()
        if sides[2]**2<sides[1]**2+sides[0]**2:
            return "Acute"
        if sides[2]**2==sides[1]**2+sides[0]**2:
            return "Right"
        if sides[2]**2>sides[1]**2+sides[0]**2:
            return "Obtuse"    
    def Area(self):
        if  self.is_valid()=="Invalid":
            return "Invalid"
        s=(self.a+self.b+self.c)/2
        return (s*(s-self.a)*(s-self.b)*(s-self.c))**0.5
a=int(input())
b=int(input())
c=int(input())
T=Triangle(a,b,c)
print(T.is_valid())
print(T.Side_Classification())
print(T.Angle_Classification())
print(T.Area())
