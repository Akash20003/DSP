#Circular Convolution

#Accepts the Length for x(n) n h(n)
N = int(input("Enter the Seq : "))
#Accepts the sequence for x(n) from the user
xn = []
print("xn is : ")
for i in range(0,N):
    x = float(input(""))
    xn.append(x)
print(xn)

#Accepts the sequence for h(n) from the user
hn = []
print("hn is : ")
for j in range(0,N):
    h = float(input(""))
    hn.append(h)
print(hn)

#this function returns the value of h(n) for further Computation
def hm(k,n):
    if k >= n:
        return hn[k-n]
    else:
        b = k - n
        return (hn[N - (-b)])

#this block performs Circular Convolution of x(n) and h(n)
XK = [0]*N
print("\nCircular Convolution is : ")
for k in range(0,N):
    for n in range(0,N):
         XK[k] = (xn[n] * hm(k,n)) + XK[k]
    print(format(XK[k],".3f"))
print(XK)

print("\nProgrammed by Akash Kulkarni")
