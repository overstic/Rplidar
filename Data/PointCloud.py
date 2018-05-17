#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun May  6 00:15:46 2018

@author: yifengluo
"""
import numpy as np
import os
import matplotlib.pyplot as plt  
from mpl_toolkits.mplot3d import Axes3D 
import scipy.io as sio



def Data_create(Name):
    Database = {}     
    for i in range(len(Name)):
        name = [] 
        for filename in os.listdir(r'%s'%(Name[i])):
            name.append(filename) 
        name.remove('.DS_Store')
        Cloud_data = []
        for j in range(len(name)):
          a = np.loadtxt(r'%s/%s'%(Name[i],name[j]))           
          Database[int('%s'%(name[j]))]=a
    return Database




DB = Data_create(['Database'])

Result = {}
List_x = []
List_y = []
List_z = []

for i in DB:
    X= np.array(
    [[1,0,0,0],
    [0,np.cos(np.pi*i/180),-np.sin(np.pi*i/180),0],
    [0,np.sin(np.pi*i/180),np.cos(np.pi*i/180),0],
    [0,0,0,1]])
    for k in range(DB[i].shape[0]):
        for j in range(DB[i].shape[1]):
            if DB[i][k,j]!=np.inf: 
            
                x_c = DB[i][k,j]*np.cos(np.pi*j/180)
                y_c = DB[i][k,j]*np.sin(np.pi*j/180)
                z_c = 0
                coordinate = np.array([[x_c],[y_c],[z_c],[1]])
                result = np.dot(X,coordinate)
                List_x.append(result[0][0])
                List_y.append(result[1][0])
                List_z.append(result[2][0])
                

#sio.savemat('saveddata.mat', {'x': List_x ,'y': List_y,'z':  List_z})            



import vtk_visualizer as vv
import numpy as np
import sys
from PyQt5.QtWidgets import *


xyz = np.zeros([len(List_x),3])
xyz[:,0] = List_x
xyz[:,1] = List_y
xyz[:,2] = List_z

Subsequence = [xyz[100*i:100*i+101,:] for i in range(int(len(List_x)/100))]







for i in range(len(Subsequence)):
    vtkControl = vv.VTKVisualizerControl()
    app = QApplication.instance()
    if app is None:
        vtkControl.AddPointCloudActor(Subsequence[i])
        app = QApplication(sys.argv)
    app.exec_()
    
        

