# -*- coding: utf-8 -*-
"""
APD_analysis extended

This program contain the functions required to analyze and APD photodetector

* IV_Curves
* Multiplication Gain
* Responsivity
* Quantum Efficiency
* COnversions of EQE to Responsivity and viceversa
* Conversions from dBm to mW and viceversa

apd.import_data(data_path)
apd.plot_IV (data_dark, data_photo)
apd.Gain(data_dark, data_photo)
apd.Responsivity(data_current, gain, input_power)
apd.EQE(current,input_power, lamda):
apd.EQEtoResponsivity(EQE, lamda_EQE)
apd.ResponsivitytoEQE(Responsivity, lamda_EQE)
apd. mw_to_dbm(mw)
def dbm_to_mw(dbm)


Created on Sat Jan 12 23:11:07 2019
@author: cesarbartolo

"""


#Modules required to perform the analysis
import numpy as np
import matplotlib.pyplot as plt
import csv
import pandas as pd

#Constants required for analysis

#input_power=710e-6 #W
q=1.602176620e-19
c=2.997e8
h=6.6260e-34
lamda=850e-9
"""
print ("Functions" )
print ("1. import_data(data_path)" )
print ('2. plot_IV (data)')
"""

def import_data(data_path):
    APD_complete=pd.read_csv(data_path, sep=',')
    APD_complete=APD_complete.set_index(APD_complete.columns[0])
    APD_complete=abs(APD_complete)
    print('Name of IV data that you can plot:')
    print('*'*10)
    print (APD_complete.columns)
    print('*'*10)
    return(APD_complete)
    #print (data_path)
    #return(data_path)
    

def plot_IV(data_dark, data_photo):
    """
    Plot IV (data): plot the IV of the set of values "data"
    """
    plt.plot(data_dark,linewidth=4)
    plt.plot(data_photo,linewidth=4)
    plt.yscale('log')
    plt.ylabel('Current(A)', fontsize=16)
    plt.xlabel('Voltage(V)', fontsize=16)
    plt.legend()
    #plt.savefig('IV.png', format='png', dpi=600)
    return()


def Gain(data_dark, data_photo):
    """
    Gain(Responsivity,voltage)::
    """
    Ip=data_photo[-10]
    ID=data_dark[-10]
    I_MD=data_dark[-10:]
    I=data_photo[-10:]
    gain=(I-I_MD)/(Ip-ID)
    plt.plot(gain, linewidth=4)
    plt.yscale('log')
    plt.xlabel('Voltage(V)', fontsize=16)
    plt.ylabel('Multiplication Gain', fontsize=16)
    plt.legend()
    print('Maximum Gain: '+ str(gain.max()))
    return (gain)

    
def Responsivity(data_current, gain, input_power):
    """
    Responsivity(current, input_power):Calculate and plot the responsivity 
    """
    responsivity_PIN= data_current[-10]/input_power
    responsivity_APD=responsivity_PIN*gain
    plt.plot(responsivity_APD)
    plt.yscale('log')
    plt.xlabel('Voltage(V)', fontsize=16)
    plt.ylabel('Responsivity(A/W)', fontsize=16)
    plt.legend()
    print('Responsivity at -10V: '+ str(responsivity_PIN))
    return (responsivity_APD)


def EQE(current,input_power, lamda):
    """
    EQE((current,input_power, lamda))
    """
    quantum_efficiency=(current/q)/(input_power/(h*c/lamda))
    plt.plot(quantum_efficiency)
    plt.yscale('log')
    plt.xlabel('Voltage(V)', fontsize=16)
    plt.ylabel('EQE', fontsize=16)
    plt.legend()
    print('EQE at -10V: '+ str(quantum_efficiency[-10]))
    return (quantum_efficiency)

"""
Conversions
"""

def EQEtoResponsivity(EQE, lamda_EQE):
    responsivity=(EQE*lamda_EQE*q)/(h*c)
    return (responsivity)

def ResponsivitytoEQE(Responsivity, lamda_EQE):
    EQE=(Responsivity*h*c)/(lamda_EQE*q)
    return (EQE)

def mw_to_dbm(mw):
    dbm=10*np.log10(mw)
    return(dbm)
    
    
def dbm_to_mw(dbm):
    """
    Return the equivalent power value of dBm to mW
    """
    mw=10**(dbm/10)
    return(mw)
    
    
