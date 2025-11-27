import numpy as np
# Les constantes :
a= 0.3658         #Pa.m^6.Mol^-1
b= 4.267*10**-5   #m^3.Mol^-1
T= 300       #K
R=8.314      #J.mol^-1.K^-1
P= 50*10**5  #Pa
A= 1
B=-(b+(R*T)/P)
C= a/P
D= a*b/P
coefficients=[A,B,C,D]
Racines=np.roots(coefficients)
print(Racines)