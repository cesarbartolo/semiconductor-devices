"""
Code created to calculate the fill ratio  
(holes/active) in PDs and its consequences in
their properties

COmands
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import csv

#CONSTANTS

eo=8.854e-12 #Fm-1
thickness= 2e-6 # 2um

def capacitance(area_flat,area_withHoles, eo, thickness):
    capacitance_flat=(eo*area_flat/thickness)
    capacitance_witHoles=(eo*area_withHoles/thickness)
    return (capacitance_flat, capacitance_witHoles)

"""

def area_hole (diameter_hole):
    area_hole= np.pi * (diameter_hole/2)**2
    return (area_hole)



def area_unitcell_square(periodicity,diameter_hole):
    area_unitcell= ((periodicity)**2) - area_hole(diameter_hole)
    return (area_unitcell)

def complete_area(complete_diameter):
    complete_area_device= np.pi * (complete_diameter/2)**2
    return (complete_area_device)
    
"""

def fill_ratio_square( diameter_hole, period,diameter_pd ):
    area_hole=np.pi * (diameter_hole/2)**2
    area_device=np.pi * (diameter_pd/2)**2
    area_unitcell_square=(period**2)# considering square lattice
    numberHoles_inDevice=area_device/area_unitcell_square #square lattice
    area_air=numberHoles_inDevice*area_hole
    fillRatio=area_air/area_device
    Effective_Area_Device=area_device - area_air
    return (numberHoles_inDevice,area_device,Effective_Area_Device,fillRatio)



def fill_ratio_hexagonal( diameter_hole, period,diameter_pd, diameter_general ):
    '''
    diameter_pd=diameter of harea were holes are located
    diameter_general= total diameter of device
    
    '''
    area_hole=np.pi * (diameter_hole/2)**2
    area_device=np.pi * (diameter_pd/2)**2
    area_unitcell_hexagonal=(period*np.sin(np.deg2rad(60))*period)# considering hexagonal lattice
    numberHoles_inDevice=area_device/area_unitcell_hexagonal #hexagonal lattice
    
    area_air=numberHoles_inDevice*area_hole
    area_flat=np.pi*(diameter_general/2)**2
    
    area_total=area_flat - area_air
    
    percentage_difference=100-(area_total*100/area_flat)
    #fillRatio=area_air/area_total
  
    return (diameter_hole*1e9, period*1e9,numberHoles_inDevice,area_flat, area_total,percentage_difference)


hole_designs=({1500:[3000,2500,2200,2000,1800], 1300:[3500,3000,2300,2000,1600], 1150:[2250,2000,1750,1500],1000:[1500,2000,1500,1300],
                800:[1800,1300,1050], 700:[1700,1300,1200,1000], 630:[1630,1200,1000,900], 1200:[3000,2200,2000,1800] })

periods=list (hole_designs.values())
diameters=list(hole_designs.keys())


DIAMETER_HOLES=[]
PERIOD=[]
#DIAMETER_PD=[]
NUMBER_HOLES=[]
#AREA_DEVICE=[]
#EFFECTIVE_AREA=[]
AREA_FLAT=[]
TOTAL_EFFECTIVE_AREA=[]
PERCENTAGE=[]
CAPACITANCE_HOLES=[]
CAPACITANCE_FLAT=[]
CAPACITANCE_PERCENTAGE_DIFFERENCE=[]

"""
device
500um-460um diameter of holes
100um -70um diameter of holes
30um - 16um diamteter of holes
"""


for d in diameters:
    for p in periods[diameters.index(d)]:
        diameter_hole, period,numberHoles_inDevice, area_flat, total_effective_area, percentage = fill_ratio_hexagonal( d*1e-9, p*1e-9, 460e-6, 500e-6)
        DIAMETER_HOLES.append(diameter_hole)
        PERIOD.append(period)
        NUMBER_HOLES.append(numberHoles_inDevice)
        AREA_FLAT.append(area_flat*1e12)
        TOTAL_EFFECTIVE_AREA.append(total_effective_area*1e12)
        PERCENTAGE.append(percentage)
        capacitance_flat,capacitance_effective=capacitance(area_flat,total_effective_area, eo, thickness)
        CAPACITANCE_HOLES.append(capacitance_effective)
        CAPACITANCE_FLAT.append(capacitance_flat)
        CAPACITANCE_PERCENTAGE_DIFFERENCE.append(100- (capacitance_effective*100/capacitance_flat))
        
'''
    
csvfile= './csvfile.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(results)
'''

data={'diameter_holes (nm)':DIAMETER_HOLES,
        'period(nm)': PERIOD,
        'number_holes':NUMBER_HOLES,
        'area_flat (um2)': AREA_FLAT,
        'total_effective_area (um2)': TOTAL_EFFECTIVE_AREA,
        'percentage_difference':PERCENTAGE,
        'capacitance_flat': CAPACITANCE_FLAT,
        'capacitance_holes':CAPACITANCE_HOLES,
        'capacitance difference((%)': CAPACITANCE_PERCENTAGE_DIFFERENCE
 
}
 
results_holes=pd.DataFrame(data)
export_csv=results_holes.to_csv('./results_calculations_hexagonal.csv')

