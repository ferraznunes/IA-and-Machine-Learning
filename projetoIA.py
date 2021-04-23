# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import pandas as pd
import scipy as py
import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits import mplot3d
from mpl_toolkits.mplot3d import Axes3D
from sklearn import linear_model
from sklearn.metrics import r2_score


df = pd.read_table(r"C:\Users\Rodrigo\Documents\Projeto final - IA\airfoil_self_noise.dat",header=None)

df.columns = ["Frequency(Hz)", "Angle of Attack (degrees)","Chord Length(m)",
              "Velocity(m/s)","SS thickness","Sound pressure(dB)"]


#Variaveis de entrada
freq = df[["Frequency(Hz)"]].to_numpy()
ang = df[["Angle of Attack (degrees)"]].to_numpy()
chord = df[["Chord Length(m)"]].to_numpy()
vel = df[["Velocity(m/s)"]].to_numpy()
sst = df[["SS thickness"]].to_numpy()

#Saida
sp = df[["Sound pressure(dB)"]].to_numpy()


#Plotagem dos resultados
plt.scatter(df[["Frequency(Hz)"]],df[["Sound pressure(dB)"]])
plt.title("Frequency(Hz)")
plt.show()

plt.scatter(ang,sp)
plt.title("Angle of Attack (degrees)")
plt.show()

plt.scatter(chord,sp)
plt.title("Chord Length(m)")
plt.show()

plt.scatter(vel,sp)
plt.title("Velocity(m/s)")
plt.show()

plt.scatter(sst,sp)
plt.title("SS thickness")
plt.show()

print(df.describe())
print(df[["Frequency(Hz)"]].value_counts())
#Organizacao dos dados
    #auxilio do comando len()- tamanho dos vetores
    #Colocar o panda series para cada vetor


#plt.contourf(freq, ang, sp, levels=np.linspace(-50, 0, 20))
