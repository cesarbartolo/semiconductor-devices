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

"""

def area_hole (diameter_hole):
    area_hole= np.pi * (diameter_hole/2)**2
    return (area_hole)



def area_unitcell_square(periodicity,diameter_hole):
    area_unitcell= ((periodicity)**2) - area_hole(diameter_hole)
    return (area_unitcell)

"""


def complete_area(complete_diameter):
    complete_area_device= np.pi * (complete_diameter/2)**2
    return (complete_area_device)

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
    area_total=np.pi*(diameter_general/2)**2 - area_air
    
    Effective_Area_Device=area_device - area_air
    fillRatio=area_air/area_total
  
    return (diameter_hole*1e9, period*1e9, diameter_pd*1e6,numberHoles_inDevice,area_device,Effective_Area_Device,fillRatio, area_total)


    
    
#diameters=np.arange(400,1400,100)*1e-9
    
#numberofHoles,fill_ratios=fill_ratio_square(diameters,1300e-9,500e-6)

#plt.plot (diameters,fill_ratios)
#plt.show()
#plt.plot (diameters,numberofHoles)
#plt.show()


#hole_degins = {diameter:period}
hole_designs=({1500:[3000,2500,2200,2000,1800], 1300:[3500,3000,2300,2000,1600], 1150:[2250,2000,1750,1500],1000:[1500,2000,1500,1300],
                800:[1800,1300,1050], 700:[1700,1300,1200,1000], 630:[1630,1200,1000,900], 1200:[3000,2200,2000,1800] })

periods=list (hole_designs.values())
diameters=list(hole_designs.keys())


DIAMETER_HOLES=[]
PERIOD=[]
DIAMETER_PD=[]
NUMBER_HOLES=[]
AREA_DEVICE=[]
EFFECTIVE_AREA=[]
FILL_RATIO=[]
TOTAL_EFFECTIVE_AREA=[]

"""
results  =  [DIAMETER_HOLES, PERIOD,
DIAMETER_PD, NUMBER_HOLES, AREA_DEVICE,
EFFECTIVE_AREA, FILL_RATIO]
"""


for d in diameters:
    for p in periods[diameters.index(d)]:
        diameter_hole, period, diameter_pd,numberHoles_inDevice,area_device,Effective_Area_Device,fillRatio, total_effective_area = fill_ratio_hexagonal( d*1e-9, p*1e-9, 70e-6, 100e-6)
        DIAMETER_HOLES.append(diameter_hole)
        PERIOD.append(period)
        DIAMETER_PD.append(diameter_pd)
        NUMBER_HOLES.append(numberHoles_inDevice)
        AREA_DEVICE.append(area_device)
        EFFECTIVE_AREA.append(Effective_Area_Device)
        FILL_RATIO.append(fillRatio)
        TOTAL_EFFECTIVE_AREA.append(total_effective_area)
        
'''
    
csvfile= './csvfile.csv'
with open(csvfile, "w") as output:
    writer = csv.writer(output, lineterminator='\n')
    writer.writerows(results)
'''



data={'diameter_holes':DIAMETER_HOLES,
        'period': PERIOD,
        'diameter_pd':DIAMETER_PD,
        'number_holes':NUMBER_HOLES,
        'area_device': AREA_DEVICE,
        'effective_area':EFFECTIVE_AREA,
        'fill_ratio': FILL_RATIO,
        'total_effective_area': TOTAL_EFFECTIVE_AREA
 
}
 
results_holes=pd.DataFrame(data)

export_csv=results_holes.to_csv('./results_calculations_hexagonal.csv')

