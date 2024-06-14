
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

# Load the spectrum data file, skipping the first 6 lines of metadata
#data98MeV_Step1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_BeforeScatt_98MeV_0deg_1cm.csv", delimiter=',', skip_header=6)

#dataDeg0_98MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_0deg_1cm.csv", delimiter=',', skip_header=6)
dataDeg5_98MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_5Deg.csv", delimiter=',', skip_header=6)
dataDeg7_5_98MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_7.5Deg.csv", delimiter=',', skip_header=6)

dataDeg5_98MeV_Step0_05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg5_0.05.csv", delimiter=',', skip_header=6)
dataDeg7_5_98MeV_Step0_05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg7.5_0.05.csv", delimiter=',', skip_header=6)



dataDeg3_5_98MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_1cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_98MeV_Step05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.5cm.csv", delimiter=',', skip_header=6)
#dataDeg3_5_98MeV_Step01cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.1cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_98MeV_Step005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.05cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_98MeV_Step001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.05cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_98MeV_Step0005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.005cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_98MeV_Step0001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.0005cm.csv", delimiter=',', skip_header=6)
dataDeg3_5_98MeV_Step00005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_3.5Deg_0.0005cm.csv", delimiter=',', skip_header=6)


dataDeg10_98MeV_Step1cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg10_1cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step05cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_10Deg_0.5cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step01cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg10_0.1cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg10_0.05cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg10_0.01cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step0005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_10Deg_0.005cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step0001cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_Deg10_0.01cm.csv", delimiter=',', skip_header=6)
dataDeg10_98MeV_Step00005cm_AfterScatter = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/EnergySpectrum_AfterScatt_98MeV_10Deg_0.0005cm.csv", delimiter=',', skip_header=6)




# Flatten the array and remove NaN values to get a single list of numeric values


Deg5_98MeV_Step1cm_AfterScatter = dataDeg5_98MeV_Step1cm_AfterScatter.flatten()
#
Deg7_5_98MeV_Step1cm_AfterScatter = dataDeg7_5_98MeV_Step1cm_AfterScatter.flatten()
#
Deg5_98MeV_Step005cm_AfterScatter = dataDeg5_98MeV_Step0_05cm_AfterScatter.flatten()
#
Deg7_5_98MeV_Step005cm_AfterScatter = dataDeg7_5_98MeV_Step0_05cm_AfterScatter.flatten()
#


Deg10_98MeV_Step1cm_AfterScatter = dataDeg10_98MeV_Step1cm_AfterScatter.flatten()



Deg3_5_98MeV_Step1cm_AfterScatter = dataDeg3_5_98MeV_Step1cm_AfterScatter.flatten()
#
Deg3_5_98MeV_Step05cm_AfterScatter = dataDeg3_5_98MeV_Step05cm_AfterScatter.flatten()
#
#Deg3_5_98MeV_Step01cm_AfterScatter = dataDeg3_5_98MeV_Step01cm_AfterScatter.flatten()
#
Deg3_5_98MeV_Step005cm_AfterScatter = dataDeg3_5_98MeV_Step005cm_AfterScatter.flatten()
#
Deg3_5_98MeV_Step001cm_AfterScatter = dataDeg3_5_98MeV_Step001cm_AfterScatter.flatten()
#
Deg3_5_98MeV_Step0005cm_AfterScatter = dataDeg3_5_98MeV_Step0005cm_AfterScatter.flatten()
#
Deg3_5_98MeV_Step0001cm_AfterScatter = dataDeg3_5_98MeV_Step0001cm_AfterScatter.flatten()
#
Deg3_5_98MeV_Step00005cm_AfterScatter = dataDeg3_5_98MeV_Step00005cm_AfterScatter.flatten()
#


Deg10_98MeV_Step1cm_AfterScatter = dataDeg10_98MeV_Step1cm_AfterScatter.flatten()
#
Deg10_98MeV_Step05cm_AfterScatter = dataDeg10_98MeV_Step05cm_AfterScatter.flatten()
#
Deg10_98MeV_Step01cm_AfterScatter = dataDeg10_98MeV_Step01cm_AfterScatter.flatten()
#
Deg10_98MeV_Step005cm_AfterScatter = dataDeg10_98MeV_Step005cm_AfterScatter.flatten()
#
Deg10_98MeV_Step001cm_AfterScatter = dataDeg10_98MeV_Step001cm_AfterScatter.flatten()
#
Deg10_98MeV_Step0005cm_AfterScatter = dataDeg10_98MeV_Step0005cm_AfterScatter.flatten()
#
Deg10_98MeV_Step0001cm_AfterScatter = dataDeg10_98MeV_Step0001cm_AfterScatter.flatten()
#
Deg10_98MeV_Step00005cm_AfterScatter = dataDeg10_98MeV_Step00005cm_AfterScatter.flatten()
#








# Generate the x-bins from 0 to 200 with 2000 bins
x_bins = np.linspace(0, 200, 2002)
"""

# Print the numeric values to verify
#print(Deg0_98MeV_Step1cm_BeforeScatter)
print("")
#print(sum(Deg0_98MeV_Step1cm_BeforeScatter))

print(Deg0_98MeV_Step1cm_AfterScatter)
print("")
print(sum(Deg0_98MeV_Step1cm_AfterScatter))
print("")
print(Deg0_98MeV_Step1cm_AfterScatter[900])
"""
def convertToY(data):
    y = []
    for i in range(len(data)):
        spec = data[i]
        calcSpec = spec/(10000000*0.1)
        y.append(calcSpec)
    return y

#YDeg0_98MeV_Step1cm_AfterScatter = convertToY(Deg0_98MeV_Step1cm_AfterScatter)
#

YDeg5_98MeV_Step1cm_AfterScatter = convertToY(Deg5_98MeV_Step1cm_AfterScatter)
#
YDeg7_5_98MeV_Step1cm_AfterScatter = convertToY(Deg7_5_98MeV_Step1cm_AfterScatter)
#
YDeg10_98MeV_Step1cm_AfterScatter = convertToY(Deg10_98MeV_Step1cm_AfterScatter)


YDeg3_5_98MeV_Step1cm_AfterScatter = convertToY(Deg3_5_98MeV_Step1cm_AfterScatter)
#
YDeg3_5_98MeV_Step05cm_AfterScatter = convertToY(Deg3_5_98MeV_Step05cm_AfterScatter)
#
#YDeg3_5_98MeV_Step01cm_AfterScatter = convertToY(Deg3_5_98MeV_Step01cm_AfterScatter)
#
YDeg3_5_98MeV_Step005cm_AfterScatter = convertToY(Deg3_5_98MeV_Step005cm_AfterScatter)
#
YDeg3_5_98MeV_Step001cm_AfterScatter = convertToY(Deg3_5_98MeV_Step001cm_AfterScatter)
#
YDeg3_5_98MeV_Step0005cm_AfterScatter = convertToY(Deg3_5_98MeV_Step0005cm_AfterScatter)
#
YDeg3_5_98MeV_Step0001cm_AfterScatter = convertToY(Deg3_5_98MeV_Step0001cm_AfterScatter)
#
YDeg3_5_98MeV_Step00005cm_AfterScatter = convertToY(Deg3_5_98MeV_Step00005cm_AfterScatter)
#


#############
x_bins1 = np.linspace(0, 200, 2003)
#x_bins1 = np.linspace(0, 200, 83)




fig, ax2 = plt.subplots(1, figsize=[24, 20])
ax2.set_title('Energy Spectrum, 5 Deg, 98 MeV', fontsize=54)
ax2.set_xlabel('E(Mev)', fontsize=54)
ax2.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
#ax2.set_yscale('log')
ax2.plot(x_bins1, convertToY(Deg5_98MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='SL: Default')
ax2.plot(x_bins1, convertToY(Deg5_98MeV_Step005cm_AfterScatter), color='blue',  linewidth=6, label='SL: 0.05cm')
ax2.set_xlim(0, 100)
#ax2.set_ylim(0, 20000)
ax2.legend(loc= "lower center")
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum98_5.png", dpi=300)

plt.show()


fig, ax3 = plt.subplots(1, figsize=[24, 20])
ax3.set_title('Energy Spectrum, 7.5 Deg, 98 MeV', fontsize=54)
ax3.set_xlabel('E(Mev)', fontsize=54)
ax3.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
#ax3.set_yscale('log')
ax3.plot(x_bins1, convertToY(Deg7_5_98MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='SL: Default')
ax3.plot(x_bins1, convertToY(Deg7_5_98MeV_Step005cm_AfterScatter), color='blue',  linewidth=6, label='SL: 0.05cm')

ax3.set_xlim(0, 100)
#ax3.set_ylim(0, 20000)
#ax.set_ylim(0, 10000000)
ax3.legend(loc='lower center')
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )

plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum98_7.5.png", dpi=300)

plt.show()


x_bins1 = np.linspace(0, 200, 2003)



fig, ax1 = plt.subplots(1, figsize=[24, 20])
ax1.set_title('Energy Spectrum, 3.5 Deg, 98 MeV', fontsize=54)
ax1.set_xlabel('E(MeV)', fontsize=54)
ax1.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)

print(len(convertToY(Deg3_5_98MeV_Step1cm_AfterScatter)))
print(len(x_bins1))

  
ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='1cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step05cm_AfterScatter), color='green',  linewidth=6, label='0.5cm')
#ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step01cm_AfterScatter), color='blue',  linewidth=6, label='0.1cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step005cm_AfterScatter), color='orange',  linewidth=6, label='0.05cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step001cm_AfterScatter), color='yellow',  linewidth=6, label='0.01cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step0005cm_AfterScatter), color='purple',  linewidth=6, label='0.005cm')
ax1.scatter(x_bins1,convertToY(Deg3_5_98MeV_Step0001cm_AfterScatter), color='gray',  linewidth=6, label='0.001cm')
ax1.scatter(x_bins1, convertToY(Deg3_5_98MeV_Step00005cm_AfterScatter), color='black',  linewidth=6, label='0.0005cm')

ax1.set_xlim(0, 100)
ax1.legend(loc='upper left')
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )

plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum98_3.5All.png", dpi=300)
plt.show()



###############

YDeg10_98MeV_Step1cm_AfterScatter = convertToY(Deg10_98MeV_Step1cm_AfterScatter)
#
YDeg10_98MeV_Step05cm_AfterScatter = convertToY(Deg10_98MeV_Step05cm_AfterScatter)
#
YDeg10_98MeV_Step01cm_AfterScatter = convertToY(Deg10_98MeV_Step01cm_AfterScatter)
#
YDeg10_98MeV_Step005cm_AfterScatter = convertToY(Deg10_98MeV_Step005cm_AfterScatter)
#
YDeg10_98MeV_Step001cm_AfterScatter = convertToY(Deg10_98MeV_Step001cm_AfterScatter)
#
YDeg10_98MeV_Step0005cm_AfterScatter = convertToY(Deg10_98MeV_Step0005cm_AfterScatter)
#
YDeg10_98MeV_Step0001cm_AfterScatter = convertToY(Deg10_98MeV_Step0001cm_AfterScatter)
#
YDeg10_98MeV_Step00005cm_AfterScatter = convertToY(Deg10_98MeV_Step00005cm_AfterScatter)
#

fig, ax1 = plt.subplots(1, figsize=[24, 20])
ax1.set_title('Energy Spectrum, 10 Deg, 98 MeV', fontsize=54)
ax1.set_xlabel('E(MeV)', fontsize=54)
ax1.set_ylabel(r'$N_{\mathrm{out}}/N_{\mathrm{in}} \, / \, 0.1 \, \mathrm{MeV}$', fontsize=54)
  
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step1cm_AfterScatter), color='red',  linewidth=6, label='1cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step05cm_AfterScatter), color='green',  linewidth=6, label='0.5cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step01cm_AfterScatter), color='blue',  linewidth=6, label='0.1cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step005cm_AfterScatter), color='orange',  linewidth=6, label='0.05cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step001cm_AfterScatter), color='yellow',  linewidth=6, label='0.01cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step0005cm_AfterScatter), color='purple',  linewidth=6, label='0.005cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step0001cm_AfterScatter), color='gray',  linewidth=6, label='0.001cm')
ax1.scatter(x_bins1, convertToY(Deg10_98MeV_Step00005cm_AfterScatter), color='black',  linewidth=6, label='0.0005cm')

ax1.set_xlim(0, 100)
ax1.legend()
plt.grid()
plt.tight_layout()
plt.ticklabel_format(axis='y', style= 'sci', scilimits = (1,3) )

plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/EnergySpectrum98_10All.png", dpi=300)
plt.show()







