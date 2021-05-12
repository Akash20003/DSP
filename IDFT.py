#WAP to Compute N-IDFT

#import math library as m, for functions
# like SINE, COSINE, PI n etc
import math as m
#N is the length of Sequence to perform DFT operation
N = int(input("N : "))

#tf block performs TWIDDLE FACTOR Function n returns values when needed
def tf(n1,k1):
    a = m.cos((2 * m.pi * n1 * k1) / N)
    b = m.sin((2 * m.pi * n1 * k1) / N)
    c = complex(a, b)
    return c

#this block accepts inputs from the user and updates the X(k)
XK = []
for k in range(0, N):
    r = float(input("Real : "))
    i = float(input("Imaginary : "))
    X = complex(r,i)
    XK.append(X)

#this blocks performs the IDFT Operation and 
# calls twiddle factor function
print("\nIDFT is : ")
xn = [0]*N
xn1 = [0]*N
for n in range(0, N):
    for k in range(0, N):
        xn1[n] = (XK[k] * tf(n, k)) + xn1[n]
        xn[n] = xn1[n] / N
    print(format(xn[n], ".1f"))
print("\nProgrammed by Akash Kulkarni")
