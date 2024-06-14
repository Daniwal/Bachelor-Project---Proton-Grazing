
import numpy as np
import scipy.stats as sc
import scipy.optimize as sc
import matplotlib.pyplot as plt
from collections import Counter
import csv
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
#import matplotlib.axes as Axes
plt.rc("axes", labelsize=44)
plt.rc("xtick", labelsize=44, top=False, direction="in")
plt.rc("ytick", labelsize=44, right=True, direction="in")
plt.rc("axes", titlesize=44)
plt.rc("legend", fontsize=54, loc="upper left")
plt.rc("figure", figsize=(7, 5))
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )
cm = 1/2.54
Br = 0.0174532925

depth_min, depth_max = 0, 8.168
x_bins1 = np.linspace(0, 200, 2003)
#x_bins1 = np.linspace(0, 200, 83)

dataDeg5_180MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg5.csv", delimiter=',', skip_header=6)
dataDeg7_5_180MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg7.5.csv", delimiter=',', skip_header=6)

dataDeg5_180MeV_Step0_05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg5_0.05.csv", delimiter=',', skip_header=6)
dataDeg7_5_180MeV_Step0_05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg7.5_0.05.csv", delimiter=',', skip_header=6)



dataDeg3_5_180MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_1cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.5cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step01cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.1cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.05cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.05cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step0005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.005cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step0001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.0005cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_180MeV_Step00005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_3.5Deg_0.0005cm.csv", delimiter=',', skip_header=6)


dataDeg10_180MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_10Deg_1cm.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg10_0.5cm.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step01cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg10_0.1cm.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_10Deg_0.05.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg10_0.01cm.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step0005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_10Deg_0.005cm.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step0001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_Deg10_0.001cm.csv", delimiter=',', skip_header=6)
dataDeg10_180MeV_Step00005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_180MeV_10Deg_0.0005.csv", delimiter=',', skip_header=6)




# Flatten the array and remove NaN values to get a single list of numeric values


Deg5_180MeV_Step1cm_AfterScatter = dataDeg5_180MeV_Step1cm_AfterScatter.flatten()
#
Deg7_5_180MeV_Step1cm_AfterScatter = dataDeg7_5_180MeV_Step1cm_AfterScatter.flatten()
#
Deg5_180MeV_Step005cm_AfterScatter = dataDeg5_180MeV_Step0_05cm_AfterScatter.flatten()
#
Deg7_5_180MeV_Step005cm_AfterScatter = dataDeg7_5_180MeV_Step0_05cm_AfterScatter.flatten()
#


Deg10_180MeV_Step1cm_AfterScatter = dataDeg10_180MeV_Step1cm_AfterScatter.flatten()



Deg3_5_180MeV_Step1cm_AfterScatter = dataDeg3_5_180MeV_Step1cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step05cm_AfterScatter = dataDeg3_5_180MeV_Step05cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step01cm_AfterScatter = dataDeg3_5_180MeV_Step01cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step005cm_AfterScatter = dataDeg3_5_180MeV_Step005cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step001cm_AfterScatter = dataDeg3_5_180MeV_Step001cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step0005cm_AfterScatter = dataDeg3_5_180MeV_Step0005cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step0001cm_AfterScatter = dataDeg3_5_180MeV_Step0001cm_AfterScatter.flatten()
#
Deg3_5_180MeV_Step00005cm_AfterScatter = dataDeg3_5_180MeV_Step00005cm_AfterScatter.flatten()
#


Deg10_180MeV_Step1cm_AfterScatter = dataDeg10_180MeV_Step1cm_AfterScatter.flatten()
#
Deg10_180MeV_Step05cm_AfterScatter = dataDeg10_180MeV_Step05cm_AfterScatter.flatten()
#
Deg10_180MeV_Step01cm_AfterScatter = dataDeg10_180MeV_Step01cm_AfterScatter.flatten()
#
Deg10_180MeV_Step005cm_AfterScatter = dataDeg10_180MeV_Step005cm_AfterScatter.flatten()
#
Deg10_180MeV_Step001cm_AfterScatter = dataDeg10_180MeV_Step001cm_AfterScatter.flatten()
#
Deg10_180MeV_Step0005cm_AfterScatter = dataDeg10_180MeV_Step0005cm_AfterScatter.flatten()
#
Deg10_180MeV_Step0001cm_AfterScatter = dataDeg10_180MeV_Step0001cm_AfterScatter.flatten()
#
Deg10_180MeV_Step00005cm_AfterScatter = dataDeg10_180MeV_Step00005cm_AfterScatter.flatten()
#










# Generate the x-bins from 0 to 200 with 2000 bins

"""

# Print the numeric values to verify
#print(Deg0_180MeV_Step1cm_BeforeScatter)
print("")
#print(sum(Deg0_180MeV_Step1cm_BeforeScatter))
"""



def convertToY(data):
    y = []
    for i in range(len(data)):
        spec = data[i]
        
        calcSpec = (spec/(10000000*0.1))
      
        y.append(calcSpec)
    return y


#

YDeg5_180MeV_Step1cm_AfterScatter = convertToY(Deg5_180MeV_Step1cm_AfterScatter)
#
YDeg7_5_180MeV_Step1cm_AfterScatter = convertToY(Deg7_5_180MeV_Step1cm_AfterScatter)
#
YDeg10_180MeV_Step1cm_AfterScatter = convertToY(Deg10_180MeV_Step1cm_AfterScatter)


YDeg3_5_180MeV_Step1cm_AfterScatter = convertToY(Deg3_5_180MeV_Step1cm_AfterScatter)
#
YDeg3_5_180MeV_Step05cm_AfterScatter = convertToY(Deg3_5_180MeV_Step05cm_AfterScatter)
#
YDeg3_5_180MeV_Step01cm_AfterScatter = convertToY(Deg3_5_180MeV_Step01cm_AfterScatter)
#
YDeg3_5_180MeV_Step005cm_AfterScatter = convertToY(Deg3_5_180MeV_Step005cm_AfterScatter)
#
YDeg3_5_180MeV_Step001cm_AfterScatter = convertToY(Deg3_5_180MeV_Step001cm_AfterScatter)
#
YDeg3_5_180MeV_Step0005cm_AfterScatter = convertToY(Deg3_5_180MeV_Step0005cm_AfterScatter)
#
YDeg3_5_180MeV_Step0001cm_AfterScatter = convertToY(Deg3_5_180MeV_Step0001cm_AfterScatter)
#
YDeg3_5_180MeV_Step00005cm_AfterScatter = convertToY(Deg3_5_180MeV_Step00005cm_AfterScatter)
#


#############




"""
fig, ax = plt.subplots(1, figsize=[24, 20])
ax.set_title('Energy Spectrum, 0 Deg, 180 MeV', fontsize=54)
ax.set_xlabel('E(Mev)', fontsize=54)
ax.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
ax.set_yscale('log')
ax.plot(x_bins, convertToY(Deg0_180MeV_Step1cm_AfterScatter), color='red',  linewidth=6)
ax.set_xlim(0, 200)
#ax.set_ylim(0, 20000)
ax.legend()
plt.grid()
plt.tight_layout()
#plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum180_0.png", dpi=300)

plt.show()
"""



fig, ax2 = plt.subplots(1, figsize=[24, 20])
ax2.set_title('Energy Spectrum, 5 Deg, 180 MeV', fontsize=54)
ax2.set_xlabel('E(Mev)', fontsize=54)
ax2.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
#ax2.set_yscale('log')
ax2.plot(x_bins1, convertToY(Deg5_180MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='SL: Default')
ax2.plot(x_bins1, convertToY(Deg5_180MeV_Step005cm_AfterScatter), color='blue',  linewidth=6, label='SL: 0.05cm')
ax2.set_xlim(0, 200)
#ax2.set_ylim(0, 20000)
ax2.legend(loc= "lower center")
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum180_5.png", dpi=300)

plt.show()


fig, ax3 = plt.subplots(1, figsize=[24, 20])
ax3.set_title('Energy Spectrum, 7.5 Deg, 180 MeV', fontsize=54)
ax3.set_xlabel('E(Mev)', fontsize=54)
ax3.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
#ax3.set_yscale('log')
ax3.plot(x_bins1, convertToY(Deg7_5_180MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='SL: Default')
ax3.plot(x_bins1, convertToY(Deg7_5_180MeV_Step005cm_AfterScatter), color='blue',  linewidth=6, label='SL: 0.05cm')

ax3.set_xlim(0, 200)
#ax3.set_ylim(0, 20000)
#ax.set_ylim(0, 10000000)
ax3.legend(loc='lower center')
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )

plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum180_7.5.png", dpi=300)

plt.show()






"""
fig, ax4 = plt.subplots(1, figsize=[24, 20])
ax4.set_title('Energy Spectrum, 10 Deg, 180 MeV', fontsize=54)
ax4.set_xlabel('E(Mev)', fontsize=54)
ax4.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}}$', fontsize=54)
ax4.set_yscale('log')
ax4.plot(x_bins, Deg10_180MeV_Step1cm_AfterScatter, color='red',  linewidth=6)
ax4.set_xlim(0, 200)
#ax.set_ylim(0, 10000000)
ax4.legend()
plt.grid()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum180_10.png", dpi=300)

plt.show()

"""

fig, ax1 = plt.subplots(1, figsize=[24, 20])
ax1.set_title('Energy Spectrum, 3.5 Deg, 180 MeV', fontsize=54)
ax1.set_xlabel('E(Mev)', fontsize=54)
ax1.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
#ax1.set_yscale('log')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='1cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step05cm_AfterScatter), color='green',  linewidth=6, label='0.5cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step01cm_AfterScatter), color='blue',  linewidth=6, label='0.1cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step005cm_AfterScatter), color='blue',  linewidth=6, label='0.05cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step001cm_AfterScatter), color='yellow',  linewidth=6, label='0.01cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step0005cm_AfterScatter), color='purple',  linewidth=6, label='0.005cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step0001cm_AfterScatter), color='gray',  linewidth=6, label='0.001cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_180MeV_Step00005cm_AfterScatter), color='black',  linewidth=6, label='0.0005cm')

ax1.set_xlim(0, 200)
ax1.legend(loc= "lower center")
plt.grid()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )

plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum180_3.5All.png", dpi=300)
plt.show()

x_bins2 = np.linspace(0, 200, 601800)

###############

YDeg10_180MeV_Step1cm_AfterScatter = convertToY(Deg10_180MeV_Step1cm_AfterScatter)
#
YDeg10_180MeV_Step05cm_AfterScatter = convertToY(Deg10_180MeV_Step05cm_AfterScatter)
#
YDeg10_180MeV_Step01cm_AfterScatter = convertToY(Deg10_180MeV_Step01cm_AfterScatter)
#
YDeg10_180MeV_Step005cm_AfterScatter = convertToY(Deg10_180MeV_Step005cm_AfterScatter)
#
YDeg10_180MeV_Step001cm_AfterScatter = convertToY(Deg10_180MeV_Step001cm_AfterScatter)
#
YDeg10_180MeV_Step0005cm_AfterScatter = convertToY(Deg10_180MeV_Step0005cm_AfterScatter)
#
YDeg10_180MeV_Step0001cm_AfterScatter = convertToY(Deg10_180MeV_Step0001cm_AfterScatter)
#
YDeg10_180MeV_Step00005cm_AfterScatter = convertToY(Deg10_180MeV_Step00005cm_AfterScatter)

#


print("Len of deg10 180:  ",len(Deg10_180MeV_Step0001cm_AfterScatter))



fig, ax1 = plt.subplots(1, figsize=[24, 20])
ax1.set_title('Energy Spectrum, 10 Deg, 180 MeV', fontsize=54)
ax1.set_xlabel('E(Mev)', fontsize=54)
ax1.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
#ax1.set_yscale('log')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='1cm')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step05cm_AfterScatter), color='green',  linewidth=6, label='0.5cm')
ax1.scatter(x_bins1,convertToY(Deg10_180MeV_Step01cm_AfterScatter), color='blue',  linewidth=6, label='0.1cm')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step005cm_AfterScatter), color='blue',  linewidth=6, label='0.05cm')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step001cm_AfterScatter), color='yellow',  linewidth=6, label='0.01cm')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step0005cm_AfterScatter), color='purple',  linewidth=6, label='0.005cm')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step0001cm_AfterScatter), color='gray',  linewidth=6, label='0.001cm')
ax1.scatter(x_bins1, convertToY(Deg10_180MeV_Step00005cm_AfterScatter), color='black',  linewidth=6, label='0.0005cm')

ax1.set_xlim(0, 200)
ax1.legend(loc= "upper right")
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )

plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum180_10All.png", dpi=300)
plt.show()









