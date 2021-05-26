#Linear Convolution

#Length of x(n)
N1 = int(input("Enter the Length of xn : "))
#accepts x(n) from the user
xn = []
print("xn is : ")                                   
for i in range(N1):
    x = float(input(""))
    xn.append(x)
print(xn)

#Length of h(n)
N2 = int(input("Enter the Length of hn : "))
#accepts input from the user for h(n)
hn1 = []
print("hn is : ")
for j in range(N2):
    h = float(input(""))
    hn1.append(h)
print(hn1)

#Length of y(n), here its XK
N = N1 + N2 - 1

#this block gives Zero Padding for h(n)
while N != N2:
    zp = [0.0]
    hn1 = hn1 + zp
    N2 += 1

#this block gives index to h(n)
def hn(n,m):
    a1 = n - m
    if a1 < 0:
        return -1
    else:
        return a1

#defining X(K) ie y(n)
XK = [0]*N
#this block Convolutes x(n) with h(n) and gives results
print("\nLinear Convolution is : ")
for a in range(N):
    for b in range(N1):
        XK[a] += (xn[b] * hn1[hn(a,b)])
    print(format(XK[a],".3f"))
print(XK)
print("\nProgrammed by Akash Kulkarni")
