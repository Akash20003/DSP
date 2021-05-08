#WAP to Compute N-DFT

#imports math library as m for fumctions like SINE, COSINE, PI n etc
import math as m

#N is the length of Sequence to perform DFT operation
N = int(input("N : "))

#tf block performs TWIDDLE FACTOR Function n returns values when needed
def tf(n1,k1):
    a = m.cos((2 * m.pi * n1 * k1) / N)
    b = -m.sin((2 * m.pi * n1 * k1) / N)
    c = complex(a, b)
    return c

#this block accepts inputs from the user and updates the x(n)
xn = []
for n in range(0, N):
    x = float(input(""))
    xn.append(x)

#this blocks performs the DFT Operation and
# calls twiddle factor function
XK = [0]*N
for k in range(0, N):
    for n in range(0, N):
        XK[k] = (xn[n] * tf(n, k)) + XK[k]
    print(format(XK[k], ".3f"))

print("\nProgrammed By Akash Kulkarni")
