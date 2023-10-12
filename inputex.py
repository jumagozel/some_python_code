#1 assigment
# a=int(input ("Enter the number:"))

# P=4*a

# print("Perimeter of the square:", P)

#2 assigment
# a=int(input('Enter the number:'))
# S=(a*a)

# print("area S of the square:", S)

#3 assigment
# a=int(input('san giriz:'))
# b=int(input('san giriz'))

# S=a*b
# P=2*(a+b)

# print('area:', S)
# print('perimeter:', P)

#4 Assigment
# d=int(input('Enter the diameter:'))
# p=3.14

# L=p*d
# print('length of the circle: ', L)

#5 assigment
# a=float(input('enter the edge:'))

# V=pow(a, 3)
# S=6*a**2
# S1=pow(a,2)
# S2=a*a
# print('The volume of the cube', V)
# print('the surface area of the cube:', S)

#6 assigment
# a=int(input("Enter the edge:"))
# b=int(input("Enter the edge:"))
# c=int(input("Enter the edge:"))

# V=a*b*c
# S=2*(a*b+b*c+a*c)

# print('Volume of the parallelepiped', V)
# print('surface area of the parallelepiped:', S)

#7 assigment
# R=float(input('Enter the radius:'))
# p=3.14
# L=2*p*R
# S=p*R**2

# print("lenrth of the circumference:", L)
# print("area of the circle:", S)

#8 assigment
# a=float(input("enter the number:"))
# b=float(input("enter the number:"))

# c=(a+b)/2
# print("average:", c)

#9 assigment
# import math
# a=int(input("enter the a side: "))
# b=int(input("enter the b side: "))

# Gmean = pow((a*b), 1/2)
# #use math package
# NewGMean=math.sqrt(a*b)

# print("Geometric Mean: ", Gmean)
# print("Geometric Mean: ", NewGMean)


#10 assigment
# a=float(input("enter the a number:"))
# b=float(input("enter the number:"))

# c=a+b
# d=a-b
# e=a*b
# f=a**2
# g=b**2
# h=f/g

# print("result the sum:", c)
# print("result the difference:", d)
# print("result the product:", e)
# print("result the quotient:", h)

#11 assigment
# a=float(input("enter the number:"))
# b=float(input("enter the number:"))

# c=a+b
# d=a-b
# e=a*b
# mod=a%b
# neverminus = abs(a-b)

# #12 assigment
# a=int(input("enter the number: "))
# b=int(input("enter the number: "))

# c=pow((a**2+b**2),1/2)
# p=a+b+c

# print("hypetanuse:", c)
# print("perimeter:", p)

#13 assigment
# R1=int(input('input the number:'))
# R2=int(input('input the number:'))
# pi=3.14
# S1=pi*pow(R1,2)
# S2=pi*pow(R2,2)

# S3=S1-S2

# print(S3)
# x1=int(input("x1: "))
# x2=int(input("x2: "))

# distance = abs(x1-x2)
# print("distance: ", distance)

#19 assigment
# x1=int(input('enter the number:'))
# x2=int(input('enter the number:'))
# y1=int(input('enter the number:'))
# y2=int(input('enter the number:'))

# a=x1-x2
# b=y1-y2

# S=a*b
# p=2*(a+b)
# print('perimeter:', p)
# print('perimeter:', S)

#22 assigment
# a=int(input("a: "))
# b=int(input("b: "))
# d=a
# a=b
# b=d
# print("new value a: ", a)
# print("new value b: ", b)

#26 assigment

# x=int(input('enter the number:'))

# y=4*pow((x-3), 6)-7*pow((x-3), 3)+2
# print ('value of function:', y)

#27 assigment
# a=int(input("a: "))
# a=a*a #a^2
# print("a1^2 ===>>> :", a)
# a=a*a #a^4
# print("a1^2 ===>>> :", a)

# a=a*a #a^8
# print(a)

#28 assigment
# a=int(input('enter the number:'))
# k=a*a #a^2
# print("a^2: ", k)
# b=a*k # a^3
# print("a^3: ", b)
# d=b*k #a^5
# print('a^5: ', d)
# c=d*d #a^10
# print('a^10: ', c)
# i=c*d #a^15
# print('a^15: ', i)

#34 assigment
# x=float(input('chocolates kg: '))
# a=float(input('price A: '))
# y=float(input('sugar kg: '))
# b=float(input('price B: '))

# c=a/x
# d=b/y

# e=c/d

# print("1 kg chocolate: ", c)
# print('1 kg sugar:', d)
# print(e,'times expensive')

#39 assigment
import math
a=int(input('a: '))
b=int(input('b: '))
c=int(input('c: '))

value=b*b-4*a*c
d=math.sqrt(value)
#d=pow(value, 1/2)

x1=((-1)*b-d)/(2*a)
x2=((-1)*b+d)/(2*a)

print("x1: ", x1)
print("x2: ", x2)

