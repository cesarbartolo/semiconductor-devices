import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

import os
rootdir = './'
extensions = ('.csv')

if not os.path.exists('./fitting_images'):
    os.makedirs('./fitting_images')


def gauss(x,a,x0,sigma):
    return a*np.exp(-(x-x0)**2/(2*sigma**2))


def find_nearest(v_norm,value):
    idx = (np.abs(v_norm-value)).argmin()
    return v_norm[idx]


def find_midpoint(array,value):
    mid_value=find_nearest(array, value)
    max_valuetoFit=array.index(mid_value)
    return (max_valuetoFit)



def percentage_impulseResponse(slow,fast):
    totalImpulse=(fast+slow)
    percentageSlow=(slow*100)/totalImpulse
    percentageFast=(fast*100)/totalImpulse
    return (percentageSlow,percentageFast)




#print ('Percentage: ',percentageCurve )


for subdir, dirs, files in os.walk(rootdir):
    
    try:
    
        for file in files:
            ext = os.path.splitext(file)[-1].lower()
            if ext in extensions:
                path_file2=os.path.join(subdir, file)
                print (path_file2)
    
    
    
    
    
                data=np.genfromtxt(path_file2, delimiter=",")
                
                t=data[370:,0]
                v=data[370:,1]
                
                ###normalizing data####
                t_norm=[i-t[0] for i in t]
                v_norm=[volt - v[0] for volt in v]
                
                
                ##find the moint of the data
                #plt.plot(t_norm, v_norm)
                half_point=(np.max(v_norm))/2
                print('Half point:', half_point)
                
                
                
                #value = half_point
                #mid_value=find_nearest(v_norm, value)
                max_valuetoFit=find_midpoint(v_norm, half_point)
                #max_valuetoFit
                
                
                
                t_fit=t_norm[:max_valuetoFit]
                v_fit=v_norm[:max_valuetoFit]
                
                
                t_fit=np.asarray(t_fit)
                v_fit=np.asarray(v_fit)
                
                
                #########################################################
                ## CURVE FITTING
                #use the weighted arithmetic mean - divide by the sum of all values)
                ## estimated values
                mean = sum(t_fit * v_fit) / sum(v_fit)
                sigma = np.sqrt(abs(sum(v_fit * (t_fit - mean)**2) / sum(v_fit)))
                
                
                #p0= initial guess
                popt,pcov = curve_fit(gauss, t_fit, v_fit, p0=[max(v_fit), mean, sigma])
                perr = np.sqrt(np.diag(pcov))
                
                #plt.plot(t_fit, v_fit, label='Data')
                #plt.plot(t_fit, gauss(t_fit, popt[0], popt[1], popt[2]), label='Fitting')
                #plt.legend()
                
                #popt2=sigma calculated
                FWHM = 2*np.sqrt(2*np.log(2))*popt[2]
                FWHM_ps=FWHM*1*10**12
                #print ("FWHM", FWHM)
                
                integral_first_part=np.trapz([v_fit], x=[t_fit], dx=[1e-12])
                print ('Integral_fast:',integral_first_part)
                integral_second_part=np.trapz([v_norm[max_valuetoFit:]], x=[t_norm[max_valuetoFit:]], dx=[1e-12])
                print ('Integral_slow:',integral_second_part)
                
                percentageCurve=percentage_impulseResponse(integral_first_part,integral_second_part)
                print ('Percentage: ',percentageCurve )
                
                ########################################################
                
                ################################################################################
                #Rise Time (90%-10%)
                #def riseTime(point10, point90):
                ####################################################################################
                max_point_amplitude=np.max(v_norm)
                TenPercent=max_point_amplitude*.10
                NinetyPercent=max_point_amplitude*.90
                
                point_middleX=v_norm.index(max_point_amplitude)
                
                rangeX_fast=v_norm[:point_middleX]
                
                valuefor10=find_midpoint(rangeX_fast, TenPercent)
                t_norm[valuefor10]
                
                
                valuefor90=find_midpoint(rangeX_fast, NinetyPercent)
                t_norm[valuefor90]
                
                
                risetime=t_norm[valuefor90]-t_norm[valuefor10]
                print ('rise time:', risetime*1e12)
                ##################################################################################
                
                ##fallTime
                
                
                rangeX_slow=v_norm[point_middleX:]
                
                valuefor10_slow=find_midpoint(rangeX_slow, TenPercent)
                
                valuefor90_slow=find_midpoint(rangeX_slow, NinetyPercent)
                
                t_norm_slow=t_norm[point_middleX:]
                falltime=t_norm_slow[valuefor10_slow]-t_norm_slow[valuefor90_slow]
                print ('fall time:', falltime*1e12)


                #######################################################
                
                fig, ax = plt.subplots()
                plot1=ax.plot(t_norm,v_norm, label='Data')
                plot2=ax.plot(t_norm, gauss(t_norm, popt[0], popt[1], popt[2]), label='Fitting')
                plt.legend()
                plt.title(path_file2)
                plt.text(0, half_point, 'FWHM:'+str(round(FWHM_ps,2))+ ' ps', style='italic',bbox={'facecolor':'red', 'alpha':0.5, 'pad':10})
                #plt.text(0, half_point*2, 'Integral_fast:'+str(round(integral_first_part,2))+ ' ps', style='italic',bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
                #plt.text(0, (half_point*2)-.01, 'Integral_slow:'+str(round(integral_second_part,2))+ ' ps', style='italic',bbox={'facecolor':'red', 'alpha':0.1, 'pad':10})
                plt.xlabel('Time')
                plt.ylabel('Amplitude(V)')
                print ('FWHM: ' + '' + 'ps', round(FWHM*1e12,1))
                
                
                plt.savefig('./fitting_images'+path_file2 +'.png', format='png', dpi=1000)
                plt.show()
                


    except:
        continue     # we don't want to handle these ones


