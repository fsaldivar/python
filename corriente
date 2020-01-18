def corriente (kVA,VL,Conexion):
  iL= (kVA*1000)/(np.sqrt(3)*VL)
  if Conexion == "Delta":
   iF =iL/np.sqrt(3)
   Vf= VL
  elif Conexion == "Estrella":
    iF= iL 
    Vf=VL/np.sqrt(3)
  else:
    print("Error en la Conexion")
  return iL,iF,VL,Vf

import numpy as np
kVA = 300 # Capacidad del Transformador
ConexionAT="Delta" # Conexion del lado de AT
ConexionBT="Estrella" # Conexion del lado de BT
vAT=23000  #Voltaje de Linea de Alta Tensión
vBT=220    #Voltaje de Linea de Baja Tensión

iLAT,iFAT,vLAT,vFAT = corriente(kVA,vAT,ConexionAT)
iLBT,iFBT,vLBT,vFBT = corriente(kVA,vBT,ConexionBT)


print("\nALTA TENSION:")
print("La corriente de linea de AT = {0:3.2f}A, La corriente de fase de AT = {1:3.2f}A".format(iLAT,iFAT))
print("El voltaje de linea de AT = {0:3.0f}V, El voltaje de fase de AT = {1:3.0f}V".format(vLAT,vFAT))

print("\nBAJA TENSION:")
print("La corriente de linea de BT = {0:3.2f}A, La corriente de fase de BT = {1:3.2f}A".format(iLBT,iFBT))
print("El voltaje de linea de BT = {0:3.0f}V, El voltaje de fase de BT = {1:3.0f}V".format(vLBT,vFBT))
