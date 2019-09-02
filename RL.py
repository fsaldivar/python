import numpy as np

R=0.2
L = 0.01
f = 60.0
V_a = 230.0*np.exp(1j*0.0)
V_b = 220.0*np.exp(1j*(-20.0*np.pi/180.0))
X = 2.0*np.pi*f*L
Z = R + 1j*X
I_ab = (V_a-V_b)/(Z)
print (I_ab)
print ('I̲ab = ',(np.abs(I_ab)),"angulo ", np.angle(I_ab, deg=True))
print ('I̲ab = %4.2f angulo %4.2f '  %(np.abs(I_ab),np.angle(I_ab, deg=True)))
print ("I̲ab = {} angulo {} ".format((np.abs(I_ab)),np.angle(I_ab, deg=True)))
