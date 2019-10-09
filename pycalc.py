from banner import banner
import math
banner("Pyhtagorean Calculator" , "Dylan Cook")
print("The Pythagorean Calculator will help you find the missing side lengths of a triangle.")
print("Enter the lengths of all of the sides you know, if you do not know the length then leave it blank")

a = input("a = ")
b = input("b = ")
c = input("c = ")

if a == "":
    b = float(b)
    c = float(c)
    a = float(math.sqrt(c*c - b*b))
    print(f"Your missing side is {a}")

elif b == "":
     a = float(a)
     c = float(c)
     b = float(math.sqrt(c*c - a*a))
     print(f"Your missing side is {b}")
elif c == "":
    a = float(a)
    b = float(b)
    c = float(math.sqrt(a*a + b*b))
    print(f"Your missing side is {c}")