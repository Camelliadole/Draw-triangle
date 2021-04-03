# Draw-triangle
n = 7
j = (n+1)/2
i = 1
while i <= j:
    if i == 1:
        print ("*"*n)
    else:
        a = "*"*n
        for m in range(0, int(i-1)):
            a = a.replace(a[m], " ")
            #break
        for n in range(n-i+1, n):
            a = a.replace(str(a[n]), " ")
            #break
        print (a)
    i += 1
 #this is my idea to solve this pro, but don't know why it not run correctly
