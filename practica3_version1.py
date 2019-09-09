#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 10:52:34 2019

@author: nadia

Este codigo resuelve la practica 3 de Circulacion general
"""



#%% cargo librerias
import numpy as np
import os #para setear directorio desde el codigo
import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import cm

#%%cargo las salidas del modelo para las 5 simulaciones con la funcion cargar dentro de Cargar2.py
#ruta="/home/nadia/Documentos/materias/circulaciongeneral/practica3/Modelo_QG/" #ruta NANU
ruta="/Users/macbookair/Desktop/practicasCG/Practica 3/Modelo_QG/" #ruta CARO
os.chdir(ruta)
from Cargar2 import cargar 
psi_temp_1,vort_temp_1,psiF_1,vortF_1,QG_diag_1,QG_curlw_1,X_1,Y_1,dx_1,dy_1=cargar(ruta+"out_tmp_1/",1500000,1500000,150,150)
psi_temp_2,vort_temp_2,psiF_2,vortF_2,QG_diag_2,QG_curlw_2,X_2,Y_2,dx_2,dy_2=cargar(ruta+"out_tmp_2/",1500000,1500000,150,150)
psi_temp_3,vort_temp_3,psiF_3,vortF_3,QG_diag_3,QG_curlw_3,X_3,Y_3,dx_3,dy_3=cargar(ruta+"out_tmp_3/",1500000,1500000,150,150)
psi_temp_4,vort_temp_4,psiF_4,vortF_4,QG_diag_4,QG_curlw_4,X_4,Y_4,dx_4,dy_4=cargar(ruta+"out_tmp_4/",1500000,1500000,150,150)
psi_temp_5,vort_temp_5,psiF_5,vortF_5,QG_diag_5,QG_curlw_5,X_5,Y_5,dx_5,dy_5=cargar(ruta+"out_tmp_5/",1500000,1500000,150,150)
psi_temp_6,vort_temp_6,psiF_6,vortF_6,QG_diag_6,QG_curlw_6,X_6,Y_6,dx_6,dy_6=cargar(ruta+"out_tmp_6/",1500000,1500000,150,150)


#%% clasifico
s1_params=[0.00005,0.01,0.001] #[Ro, eps, Ah]
s2_params=[0.0005,0.01,0.001] 
s3_params=[0.005,0.01,0.001]
s4_params=[0.005,0.025,0.001]
s5_params=[0.005,0.05,0.001]
params=[s1_params,s2_params,s3_params,s4_params,s5_params]
cociente1=[]
cociente2=[]
for i in range(0,5):
    cociente1.append(np.sqrt(params[i][0])/((params[i][2])**(1/3.0)))
    cociente2.append(np.sqrt(params[i][0])/(params[i][1]))

#muestro resultados en tabla

clasificacion= {' ': ["delta i / delta v1","delta i / delta f"],
     "S1":[round(cociente1[0],3),round(cociente2[0],3)],
     'S2':[round(cociente1[1],3),round(cociente2[1],3)],
     "S3":[round(cociente1[2],3),round(cociente2[2],3)],
     'S4':[round(cociente1[3],3),round(cociente2[3],3)],
     "S5":[round(cociente1[4],3),round(cociente2[4],3)]}

clasificacion = pd.DataFrame(data=clasificacion)
clasificacion.to_excel("clasificacion.xls",index=False)
#%% ejercicio 1 Energia cinetica
#Grafique la energia cinetica total de la cuenca (adimensional) en funcion del numero de iteracion temporal para cada simulacion (en un mismo grafico).
#tomo la cuarta columna de la salida QG_diag que tiene la energia cinetica para cada paso temporal (10000 pasos) en el punto central del dominio
plt.figure()
plt.plot()
plt.plot(QG_diag_1[:,0],QG_diag_1[:,3],label="S1")
plt.plot(QG_diag_2[:,0],QG_diag_2[:,3],linestyle="--",label="S2")
plt.plot(QG_diag_3[:,0],QG_diag_3[:,3],label="S3")
plt.plot(QG_diag_4[:,0],QG_diag_4[:,3],label="S4")
plt.plot(QG_diag_5[:,0],QG_diag_5[:,3],label="S5")
plt.xlabel("Paso temporal")
plt.ylabel("Energia cinetica")
plt.title("Evolucion de energia cinetica total")
plt.legend(loc='upper right')
plt.savefig("ejercicio1_cinetica", dpi=100)

#%% ejercicio 1 campo funcion corriente, vorticidad y transporte meridional
##defino magnitudes tipicas para dimensionalizar 
L=1500000 #longitud de la cuenca en METROS. practica 1 lo dimensionalizamos con L en km 
#(verificar que sea en metros y cambiarlo en practica 1). poniendo esto en metros la vorticidad
#nos queda razonable 
tau=0.3 #tension del viento en superficie
D=3000 #profundidad del oceano EN metros
rho=1025 #densidad
betha=1e-11 
U=2*np.pi*tau/(rho*D*betha*L) 

#
#dimensionalizo funciones corriente
psiF_1_dim=psiF_1*U*L # funcion corriente dimensionalizada (dimension m*m/s) S1
psiF_2_dim=psiF_2*U*L # funcion corriente dimensionalizada (dimension m*m/s) S2
psiF_3_dim=psiF_3*U*L # funcion corriente dimensionalizada (dimension m*m/s) S3
psiF_4_dim=psiF_4*U*L # funcion corriente dimensionalizada (dimension m*m/s) S4
psiF_5_dim=psiF_5*U*L # funcion corriente dimensionalizada (dimension m*m/s) S5
psiF_6_dim=psiF_6*U*L # funcion corriente dimensionalizada (dimension m*m/s) S6
psiF_dim=[psiF_1_dim,psiF_2_dim,psiF_3_dim,psiF_4_dim,psiF_5_dim,psiF_6_dim]

#dimensionalizo vorticidad 
vortF_1_dim=vortF_1*U/L 
vortF_2_dim=vortF_2*U/L 
vortF_3_dim=vortF_3*U/L 
vortF_4_dim=vortF_4*U/L 
vortF_5_dim=vortF_5*U/L 
vortF_6_dim=vortF_6*U/L 
vortF_dim=[vortF_1_dim,vortF_2_dim,vortF_3_dim,vortF_4_dim,vortF_5_dim,vortF_6_dim]

#calculo vorticidad total
vort_planetaria=(betha*(np.zeros((150,150),dtype=(Y_1).dtype)+Y_1)).T #estar atentas que la
#vort planetaria total es esto mas f0 que es una constante de un numero de magnitud mayor del orden
#de 10 a la menos 4 y negativo para el hemisferio sur. pero cmo solo nos interesa ver las variaciones
#aproximamos a la planetaria como solo el termino de variacion. Tenerlo presente en la interpretacion
vortF_T_dim=vortF_dim+vort_planetaria

#calculo transporte meridional
My_1=D*(np.diff(psiF_1_dim,n=1, axis=1))/1e6 
My_2=D*(np.diff(psiF_2_dim,n=1, axis=1))/1e6
My_3=D*(np.diff(psiF_3_dim,n=1, axis=1))/1e6
My_4=D*(np.diff(psiF_4_dim,n=1, axis=1))/1e6
My_5=D*(np.diff(psiF_5_dim,n=1, axis=1))/1e6
My_6=D*(np.diff(psiF_6_dim,n=1, axis=1))/1e6
My=[My_1,My_2,My_3,My_4,My_5,My_6]


#ploteo
X=[X_1/1000,X_2/1000,X_3/1000,X_4/1000,X_5/1000,X_6/1000] #en km
Y=[Y_1/1000,Y_2/1000,Y_3/1000,Y_4/1000,Y_5/1000,Y_6/1000] #en km
sim=["S1","S2","S3","S4","S5","S6"]
#funcion corriente
levels_psi=np.arange(-9,1.5,0.5)
for i in range(0,6):
    plt.figure()
    #plt.contourf(X[i],Y[i],psiF_dim[i]/100000, cmap=cm.jet)
    plt.contourf(X[i],Y[i],psiF_dim[i]/100000,levels_psi, cmap=cm.jet)
    plt.title("Campo de funcion corriente "+sim[i])
    cbar=plt.colorbar()
    plt.contour(X[i], Y[i],psiF_dim[i], levels=0,colors="white")
    cbar.ax.set_title("1e5 m2/s")
    plt.xlabel("longitud (km)")
    plt.ylabel("latitud (km)")
    plt.savefig("Funcion corriente "+sim[i], npi=100)

#vorticidad no grafico la s6 porque se me va la escala y se dejan de ver las cosas en las otras simulaciones
levels_vort=np.arange(-30,110,5)
for i in range(0,5):
    plt.figure()
    #multiplique a la vort poe e7 para que me quede en las mismas magnitudes la barra que en la P1 
    #plt.contourf(X[i],Y[i],vortF_dim[i]*1e7,cmap=cm.jet) #para analizar cual es la escala mas grande 
    plt.contourf(X[i],Y[i],vortF_dim[i]*1e7,levels=levels_vort,cmap=cm.jet) #defino la escala mas arriba en funcion de lo que de el ploteo con la linea anterior descomentada
    cbar=plt.colorbar()
    plt.title("Campo de vorticidad relativa "+sim[i])
    cbar.ax.set_title("1/s 1e-7")
    plt.contour(X[i], Y[i],vortF_dim[i]*1e7, levels=0,colors="white")
    plt.xlabel("longitud (km)")
    plt.ylabel("latitud (km)")
    plt.savefig("Campo de vorticidad relativa "+sim[i], npi=100)

#vorticidad total tampoco grafico s6 para que no se me vaya la escala
levels_vort_T=np.arange(-20,200,20)
for i in range(0,5):
    plt.figure()
    #multipli1ue a la vort poe e7 para que me quede en las mismas magnitudes la barra que en la P1 
    #plt.contourf(X[i],Y[i],vortF_T_dim[i]*1e7,cmap=cm.jet) #para analizar cual es la escala mas grande 
    plt.contourf(X[i],Y[i],vortF_T_dim[i]*1e7,levels=levels_vort_T,cmap=cm.jet) #defino la escala mas arriba en funcion de lo que de el ploteo con la linea anterior descomentada
    cbar=plt.colorbar()
    plt.title("Campo de vorticidad total "+sim[i])
    cbar.ax.set_title("1/s 1e-7")
    plt.contour(X[i], Y[i],vortF_T_dim[i], levels=0,colors="white")
    plt.xlabel("longitud (km)")
    plt.ylabel("latitud (km)")
    plt.savefig("Campo de vorticidad total"+sim[i], npi=100)  
    
#transporte tambien se me va de escala la ultima simulacion asi que la hago aparte
levels_my=np.arange(-700,300,50)
for i in range(0,5):
    plt.figure()
    #plt.contourf(X[i][0:149],Y[i],My[i], cmap=cm.jet)
    plt.contourf(X[i][0:149],Y[i],My[i],levels_my, cmap=cm.jet)
    plt.title("Campo de transporte "+sim[i])
    cbar=plt.colorbar()
    plt.contour(X[i][0:149], Y[i],My[i], levels=0,colors="white")
    cbar.ax.set_title("m3/s")
    plt.xlabel("longitud (km)")
    plt.ylabel("latitud (km)")
    plt.savefig("transporte"+sim[i], npi=100)

#hago el transporte de la simulacion 6 aparte
plt.figure()
plt.contourf(X[5][0:149],Y[5],My[5],cmap=cm.jet)
plt.title("Campo de transporte "+sim[5])
cbar=plt.colorbar()
plt.contour(X[5][0:149], Y[5],My[5], levels=0,colors="white")
plt.xlabel("longitud (km)")
plt.ylabel("latitud (km)")
cbar.ax.set_title("m3/s")
plt.savefig("transporte"+sim[5], npi=100)


    
#%%   falta hacer
    


plt.close(all)