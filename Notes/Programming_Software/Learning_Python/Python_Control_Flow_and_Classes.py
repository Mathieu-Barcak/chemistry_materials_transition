"""This is what I learned about python in the last week.

I plan to continue to expand upon the class written at the bottom of this document,
and turning the class into a part of a mini project to familiarize myself with python
I also plan to expand to have multiple classes, and make a sort of complex number and 
matrix calculater, this would allow me to go over how to compute with both mathmatical
sturcutres, while also helping to improve my skills in python.

Plans for next week, I plan to learn more about these topics:
Lamdba functions
Generator functions
as, in and other keywords
else: statements following a loop
Arguments that are passed to a funciton (/, *, *args, **list, ect.) 


Sources:
All of my learning has been from the official python documentation and tutorial sections:
docs.python.org/3/reference/index.html
docs.python.org/3/library/index.html
docs.python.org/3/tutorial/index.html
"""

# Scopes and Namespaces

def scope_test(): #Function
    def local_test():
        current_scope = "local"
        print("Inside local:", current_scope)
    
    def non_local_test():
        nonlocal current_scope
        current_scope = "non_local"
    
    def global_test():
        global current_scope 
        current_scope = "global"
    
    #Test the scope within function
    current_scope = "test"
    print("Original value", current_scope)
    local_test()
    print("After local:", current_scope)
    non_local_test()
    print("After nonlocal:", current_scope)
    global_test()
    print("After global:", current_scope)
    
scope_test() #Calls the scope_test function
print("Outside of scope_test function:", current_scope,"\n")
del current_scope #Not using any more so I will delete it
#Output: 
"""
Original value: test
Inside local: local
After local: test
After nonlocal: non_local
After global: non_local
Outside of scope_test function: global
"""

#Control Flow

#if statment
def simpleifexample(x=3):
    if x == 1:
        print("x=1")
    elif x == 2:
        print("x=2")
    else:
        print("x not equal to 1 or 2")

simpleifexample() #calls the function with defalt value (3)
simpleifexample(1)
simpleifexample(x=2)
print("\n")
#Output:
"""
x not equal to 1 or 2
x=1
x=2
"""

#match/case same as if statment function
def simplematchexample(x=3):
    match x:
        case 1:
            print("x=1")
        case 2:
            print("x=2")
        case _:
            print("x not equal to 1 or 2")

simplematchexample()
simplematchexample(2)
simplematchexample(1)
print("\n")
#Output:
"""
x not equal to 1 or 2
x=2
x=1
"""

#for loop
for x in range(1, 9, 2): #1 inclusive, 9 exclusive or [1,9)
    print(x)

print("\n")
#Output:
"""
1
3
5
7
"""

#while loop same as for loop function
x=1
while x < 9:
    print(x)
    x += 2

print("\n")
del x
#Output:
"""
1
3
5
7
"""

#Classes

class TestClass:
    '''A simple class'''
    
    i = 12345
    
    def __init__(self, lon=0, lat=0):
        self.lon = lon
        self.lat = lat
    
    def f(self):
        return 'hello world'        

x = TestClass(lat=2)
print(x.__doc__)
print(x.i)
print(x.lon,x.lat)
print(x.f(),"\n")
del x
#Output:
"""
A simple class
12345
0 2
hello world
"""

#Inheritance
class Mapping:
    def __init__(self, iterable):
        self.items_list = []
        self.__update(iterable)

    def update(self, iterable):
        for item in iterable:
            self.items_list.append(item)

    __update = update   #Private copy of original update() method

class MappingSubclass(Mapping):
#Subclass of Mapping
    def update(self, keys, values):
        #Provides new signature for update()
        #But does not break __init__()
        for item in zip(keys, values):
            self.items_list.append(item)

x = Mapping([1,2,4,8,16])
x.items_list
y = MappingSubclass(x.items_list)
y.update([2, 3, 6], [1, 2, 3])
print(x.items_list, y.items_list)
x.update([12,21,11])
print(x.items_list, "\n")
#Output:
'''
[1, 2, 4, 8, 16] [1, 2, 4, 8, 16, (2, 1), (3, 2), (6, 3)]
[1, 2, 4, 8, 16, 12, 21, 11]
'''

#Integration of Control Flow and Classes
'''
I plan to continue to imporve this and other parts as a mini python project to
increase my understanding of python, and the standard library.
I have made a class to repersent complex numbers
This class can:
compare complex numbers (distance from orgin, not equality)
+, -, * complex numbers
returns a clean string in the form:
    (-)realnumber+/-imaginarynumberi
    (-)realnumber
    (-)imaginarynumberi
    (-)i
    (-)realnumber+/-i
    0
'''
class Complex:
    def __init__(self, realpart, imagpart):
    #Will allow you to change the starting arguments, runs when Complex object is created
        self.r = realpart
        self.i = imagpart
        
    def __str__(self):
    #Print(Complex) calls for string, runs this method
        return self.FullNumber()

    def cleanup(self, imagpart, realpart):
    #Will remove 1 and -1 from imaginary component, and add formatting for FullNumber
        match (imagpart <= 0, imagpart):
            case (_, 1):
                if realpart != 0:
                    imagpart = "+"
                else:
                    imagpart = ""
            case (_, -1):
                imagpart = "-"
            case (False, _):
                if realpart != 0:
                    imagpart = f"+{imagpart}"
                else:
                    imagpart = f"{imagpart}"
        return imagpart

    def FullNumber(self, realpart=None, imagpart=None):
    #Organizes the object into a string that can be printed
    #This match will make it so that you use self.r or self.i if real or imaginary components are missing
        match (realpart is None, imagpart is None):
            case (True, True):
                realpart = self.r
                imagpart = self.i
            case (True, False):
                realpart = self.r
            case (False, True):
                imagpart = self.i
        
    #This match will remove the parts that are equal to 0
        match (imagpart < 0, realpart == 0, imagpart == 0):
            case (False, True, True):
                return("0")
            case (_, False, False):
                return(f"{realpart}{self.cleanup(imagpart, realpart)}i")
            case (_, True, False):
                return(f"{self.cleanup(imagpart, realpart)}i")
            case (False, False, True):
                return(f"{realpart}")
            
    def __iadd__(self, other):
    #Called when Complex += Complex or int or float
        if isinstance(other, Complex):
            self.r += other.r
            self.i += other.i
        elif isinstance(other, (int, float)):
            self.r += other
        else:
            return NotImplemented
        return self
        
    def __isub__(self, other):
    #Called when Complex -= Complex or int or float
        if isinstance(other, Complex):
            self.r -= other.r
            self.i -= other.i
        elif isinstance(other, (int, float)):
            self.r -= other
        else:
            return NotImplemented
        return self
    
    def __imul__(self, other):
    #Called when Complex *= Complex or int or float
        if isinstance(other, Complex):
            imaganswer = self.i * other.r + other.i * self.r
            realanswer = self.r * other.r - (self.i * other.i)
            self.i = imaganswer
            self.r = realanswer
        elif isinstance(other, (int, float)):
            self.i *= other
            self.r *= other
        else:
            return NotImplemented
        return (self)
    
    def __add__(self, other):
    #Called when Complex + Complex or int or float
        return self.addition(other)
        
    def __radd__(self, other):
    #Called when int or float + Complex
        return self.addition(other)
        
    def __sub__(self, other):
    #Called when Complex - Complex or int or float
        if isinstance(other, Complex):
            return Complex(self.r - other.r, self.i - other.i) 
        elif isinstance(other, (int, float)):
            return Complex(self.r - other, self.i)
        return NotImplemented
        
    def __rsub__(self, other):
    #Called when int or float - Complex
        if isinstance(other, Complex):
            return Complex(other.r - self.r, other.i - self.i)
        elif isinstance(other, (int, float)):
            return Complex(other - self.r, self.i)
        return NotImplemented
        
    def addition(self, other):
    #Does addition
        if isinstance(other, Complex):
            realpart = other.r + self.r
            imagpart = other.i + self.i
            return Complex(realpart=realpart,imagpart=imagpart)
        elif isinstance(other, (int, float)):
            realpart = other + self.r
            return Complex(realpart=realpart,imagpart=self.i)
        return NotImplemented
    
    def __mul__(self, other):
    #Called when Complex * Complex or int or float
        return self.multiply(other)
        
    def __rmul__(self, other):
    #Called when int or float * Complex
        return self.multiply(other)
    
    def multiply(self, other):
    #Does multiplication
        if isinstance(other, Complex):
            imagpart = self.i * other.r + other.i * self.r
            realpart = self.r * other.r - (self.i * other.i)
            return Complex(realpart=realpart, imagpart=imagpart)
        elif isinstance(other, (int, float)):
            realpart = self.r * other
            imagpart = self.i * other
            return Complex(realpart=realpart, imagpart=imagpart)
        return NotImplemented
    
    def __abs__(self):
    #Called when abs(Complex)
        return Complex(abs(self.r), abs(self.i))
    
    def __neg__(self):
    #Called when -Complex
        return Complex(-self.r, -self.i)
    
    def __lt__(self, other):
    #Called when Complex < Complex or int or float
        return not self.greater(other) and not self.equal(other)
    
    def __le__(self, other):
    #Called when Complex <= Complex or int or float
        return not self.greater(other)
    
    def __eq__(self, other):
    #Called when Complex == Complex or int or float
        return self.equals(other)
    
    def __ne__(self, other):
    #Called when Complex != Complex or int or float
        return not self.equals(other)
    
    def __gt__(self, other):
    #Called when Complex > Complex or int or float
        return self.greater(other)
    
    def __ge__(self, other):
    #Called when Complex >= Complex or int or float
        return self.greater(other) or self.equals(other)
    
    def equals(self, other):
    #find and compare distance to orgin
        selfdist = (self.r**2+self.i**2)**(0.5)
        if isinstance(other, Complex):
            otherdist = (other.r**2+other.i**2)**(0.5)
            return selfdist == otherdist
        elif isinstance(other, (int, float)):
            return selfdist == other
        return NotImplemented
    
    def greater(self, other):
    #find and comapre distance to orgin
        selfdist = (self.r**2+self.i**2)**(0.5)
        if isinstance(other, Complex):
            otherdist = (other.r**2+other.i**2)**(0.5)
            return selfdist > otherdist
        elif isinstance(other, (int, float)):
            return selfdist > other
        return NotImplemented        

x = Complex(3.0, -4.5)
print(x)
y = Complex(1.0, 2.0)
print(x+y)
print(y*x)
print(y*x-15)
x *= x
print(x)
print(x-y)
print(abs(x-y))
z = Complex(0,-1)
print(z)
print(z*5)
print(abs(z))
print(abs(z)*5)
print(Complex(1,-1))
print(Complex(-1,-1))
print(-Complex(1,-1)*Complex(1,1))
print(Complex(1,-1)*Complex(1,1))
print(Complex(1,1))
print(Complex(1,1)-2)
print(z+Complex(0,1))
del x, y, z
#Output:
"""
3.0-4.5i
4.0-2.5i
12.0+1.5i
-3.0+1.5i
-11.25-27.0i
-12.25-29.0i
12.25+29.0i
-i
-5i
i
5i
1-i
-1-i
-2
2
1+i
-1+i
0
"""