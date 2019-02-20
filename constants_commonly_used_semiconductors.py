#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 11 00:46:22 2017

@author: cesarbartolo
"""


q=1.602*10**-19 #[C] charge

m0=9.10938356*10**-31 #[kg]  #mass at rest
  
#Plack Constant [h]
h=6.626070040 *10**-34  #[J.s]
hbar=6.626*10**-34 #[J.s]
hbar_eV=4.135*10**-15 #[eV.s]

#Boltzman constant
k=1.38064852*10**-23 #J/K
kb=8.6173*10**-5 #eV/K  
e0=8.85*10**-14 #Permitivity of vacuum

#Ligth speed
2.999792*10**8 #[ms/]

""""
Silicon
"""

ni_si=1.45*10**10 #cm-3
Eg_si=1.12 #eV
n0=2*10**10
miu_n=1350 #mobility of electrons
miu_p=450 #mobility of holes
#Effective mass of silicon
mp=0.81*m0
mn=1.08*m0
er_si=11.7#*(8.85*10**-14)

"""
SIO2
"""
e_ins= 3.9 #permitivity inslutor SiO2


"""
GaAs
"""

Er_GaAs=12.9
