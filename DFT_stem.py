# N-DFT with Graph
import math as m
import matplotlib.pyplot as plt

N = int(input("Samples : "))

def tf(n1,k1):
    a = m.cos((2 * m.pi * n1 * k1) / N)
    b = -m.sin((2 * m.pi * n1 * k1) / N)
    return complex(a, b)

xn = []
for n in range(0, N):
    x = float(input(""))
    xn.append(x)

XK = [0]*N
for k in range(0, N):
    for n in range(0, N):
        XK[k] = (xn[n] * tf(n, k)) + XK[k]
    XK.append(complex(format(XK[k], ".3f")))

del XK[0:N]
print("\n",XK)
XKr = []
XKi = []
for j in XK:
    XKr.append(j.real)
    XKi.append(j.imag)

plt.subplot(2,1,1)
plt.plot(range(0,N),xn)
plt.title('Input-xn(Time Domain)')
plt.xlabel('Time')
plt.ylabel('Amplitude')
plt.grid()
plt.tight_layout()

plt.subplot(2,1,2)
plt.stem(XKr,XKi)
plt.title('Output-XK DFT(Time to Frequency Domain)')
plt.xlabel('Frequency\n(Real)')
plt.ylabel('Amplitude\n(Imag)')
plt.grid()
plt.tight_layout()
plt.show()

print("\nProgrammed By Akash Kulkarni")
