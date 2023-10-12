#################### function1 ##################################
# def PowerA3(A):
#     B=A**3
#     return B

# for i in range(5):
#     number=int(input("enter number: "))
#     result = PowerA3(number)
#     print(result)

############################# function2 #############################
# def PowerA3(A):
#     B=A**2
#     C=A**3
#     D=A**4
#     return B, C, D

# for i in range(5):
#     number=int(input("enter number: "))
#     result = PowerA3(number)
#     print(result)

############################### function3 ################################
def Mean(X, Y):
    AMean = (X+Y)/2
    GMean = pow((X*Y), (1/2))
    return AMean, GMean

A = int(input("A: "))
B = int(input("A: "))
C = int(input("A: "))
D = int(input("A: "))

print("A and B", Mean(A, B))
print("A and B", Mean(A, B))
print("A and B", Mean(A, B))

