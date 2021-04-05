# Draw-triangle
n = int(input("nhap so le nha ban iu: "))
for i in range (1, int((n+1)/2+1)):
    print(" "*(i-1) + "*"*(n-2*i+2) + " "*(i-1))

