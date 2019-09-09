#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 09:53:12 2019

@author: nadia
"""
def cargar(dir_salida,Lx,Ly,nx,ny): 

    #Cargamos las librerias necesarias
    import os
    import numpy as np

    archivos=os.listdir(dir_salida) # nombre de los archivos en el directorio actual + \output

    tiempos=0

    for name in archivos:
        if name[0:3]=='psi':
            tiempos=tiempos+1

    # Creacion de las matriz para recibir los datos
    psi_temp=np.empty(shape=[ny+2,nx+2,tiempos])
    psi_temp[:]=np.nan
    vort_temp=np.empty(shape=[ny+2,nx+2,tiempos])
    vort_temp[:]=np.nan
         
    # Extraccion
    for name in archivos:
        if name[0:3]=='psi':
            k1=name[3]+name[4]
            psi_temp[:,:,int(k1)-1]=np.loadtxt(dir_salida+name) #fromfile(name)
        if name[0:3]=='vor':
            k2=name[3]+name[4]
            vort_temp[:,:,int(k2)-1]=np.loadtxt(dir_salida+name) #fromfile(name)
        if name[0:7]=='QG_diag':
            QG_diag=np.loadtxt(dir_salida+name) #fromfile(name) 
            # En el punto central del dominio
            # (Tiempo, Funcion Corriente,Vorticidad, EnCin)
        if name[0:7]=='QG_wind':
            QG_curlw=np.loadtxt(dir_salida+name) #fromfile(name)
 
    # Recorte de los datos
    a1=1; a2=np.size(vort_temp,0)-1;
    b1=1; b2=np.size(vort_temp,1)-1;

    psi_temp=psi_temp[a1:a2,b1:b2,:]
    psiF=psi_temp[:,:,np.size(psi_temp,2)-1]

    vort_temp=vort_temp[a1:a2,b1:b2,:]
    vortF=vort_temp[:,:,np.size(vort_temp,2)-1]

    X=np.linspace(0,Lx,num=nx)
    Y=np.linspace(0,Ly,num=ny)    

    dx=Lx/(nx-1);
    dy=Ly/(ny-1);
    
    return psi_temp,vort_temp,psiF,vortF,QG_diag,QG_curlw,X,Y,dx,dy
    
