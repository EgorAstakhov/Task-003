print("S = (p(p-a)(p-b)(p-c))*0.5")
print("p = 1/2 (a+b+c)")
a = int(input("Enter a - "))
b = int(input("Enter b - "))
c = int(input("Enter b - "))
p = 0.5*(a+b+c)
S = (p*(p-a)*(p-b)*(p-c))*0.5
print("P = ", p ,"; S = ", S)