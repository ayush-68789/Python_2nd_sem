n = int(input())
a = 0 
b = 1 
for i in range (0,n+1):
    print(a)
    c = a+ b
    a = b 
    b = c
