# Pattern program 

# n = 5
# for i in range (n):
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range (n):
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range (n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     print()

# n = 5
# for i in range (n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# change inner j loop to reduce the middle value
# n = 5
# for i in range (n):
#     for j in range(i,n):
#         print(" ",end=" ")
#     for j in range(i+1):
#         print("*",end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()

# we need to write n-1 in j loop 
# n = 5
# for i in range (n):
#     for j in range(i+1):
#         print(" ",end=" ")
#     for j in range(i,n-1):
#         print("*",end=" ")
#     for j in range(i,n):
#         print("*",end=" ")
#     print()

# Diamond Pattern
n = 5
for i in range (n-1):
    for j in range(i,n):
        print(" ",end=" ")
    for j in range(i+1):
        print("*",end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
for i in range (n):
    for j in range(i+1):
        print(" ",end=" ")
    for j in range(i,n-1):
        print("*",end=" ")
    for j in range(i,n): 
        print("*",end=" ")
    print()