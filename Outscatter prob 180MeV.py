import numpy as np
import scipy.stats as sc
import scipy.optimize as sc
import matplotlib.pyplot as plt
from collections import Counter
import csv
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
#import matplotlib.axes as Axes
plt.rc("axes", labelsize=40)
plt.rc("xtick", labelsize=40, top=False, direction="in")
plt.rc("ytick", labelsize=40, right=True, direction="in")
plt.rc("axes", titlesize=40)
plt.rc("legend", fontsize=52, loc="upper left")
plt.rc("figure", figsize=(7, 5))
cm = 1/2.54
Br = 0.0174532925



Count0MeV180_1cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg0_98_1cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count5MeV180 = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg5_180.csv", skip_header = 8, usecols= (3), filling_values=0)
Count7_5MeV180 = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCount7.5deg_180.csv", skip_header = 8, usecols= (3), filling_values=0)
"""
Count3_5MeV180_1cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCount3.5Deg_180_1cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_1cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg3.5_180_0.1cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_001cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg3.5_180_0.001cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_0001cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg3.5_180_0.0001cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_5cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg3.5_180_0.5cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_05cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg3.5_180_0.05cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_005cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCount3.5Deg_180_0.005cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count3_5MeV180_0_0005cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCount3.5Deg_180_0.0005cm.csv", skip_header = 8, usecols= (3), filling_values=0)




Count10MeV180_1cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_1cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_1cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.1cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_01cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.01cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_001cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.001cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_5cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.5cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_05cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.05cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_005cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.005cm.csv", skip_header = 8, usecols= (3), filling_values=0)
Count10MeV180_0_0005cm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/ProtonCountDeg10_180_0.00005cm.csv", skip_header = 8, usecols= (3), filling_values=0)

"""

total_sum  = np.sum(Count0MeV180_1cm)
#total_sum1  = np.sum(Count3_5MeV180_1cm)
total_sum2  = np.sum(Count5MeV180)
total_sum3  = np.sum(Count7_5MeV180)
#total_sum4  = np.sum(Count10MeV180_1cm)

total_sum35_1  = 2230557
total_sum35_01  = 2234921
total_sum35_001  = 2246455
total_sum35_0001  =2249302
total_sum35_5  = 2230557
total_sum35_05  = 2236100
total_sum35_005  = 2241800
total_sum35_0005  =2247639

print("total sum 35 1:", total_sum35_1)
print("total sum 35 5:", total_sum35_5)
print("total sum 35 01:", total_sum35_01)
print("total sum 35 05:", total_sum35_05)
print("total sum 35 001:", total_sum35_001)
print("total sum 35 005:", total_sum35_005)
print("total sum 35 0001:", total_sum35_0001)
print("total sum 35 0005:", total_sum35_0005)


total_sum10_1  = 105296
total_sum10_01  = 107399
total_sum10_001  = 115391
total_sum10_0001  = 115500
total_sum10_05  = 105296
total_sum10_005  = 110686
total_sum10_0005  =114813
total_sum10_000005  = 115267

"""
print(total_sum)
print("")
print(total_sum1)
print("")
print(total_sum2)
print("")
print(total_sum3)
"""

OutScatter_Prob0Deg_180MeV_1cn = total_sum/10000000

#OutScatter_Prob5Deg_180MeV = total_sum1/10000000

OutScatter_Prob7_5Deg_180MeV = total_sum2/10000000


OutScatter_Prob3_5Deg_180MeV_1cn = total_sum35_1/10000000
OutScatter_Prob3_5Deg_180MeV_01cn = total_sum35_01/10000000
OutScatter_Prob3_5Deg_180MeV_001cn = total_sum35_001/10000000
OutScatter_Prob3_5Deg_180MeV_0001cn = total_sum35_0001/10000000
OutScatter_Prob3_5Deg_180MeV_05cn = total_sum35_5/10000000
OutScatter_Prob3_5Deg_180MeV_005cn = total_sum35_05/10000000
OutScatter_Prob3_5Deg_180MeV_0005cn = total_sum35_005/10000000
OutScatter_Prob3_5Deg_180MeV_00005cn = total_sum35_0005/10000000


OutScatter_Prob10Deg_180MeV_1cn = total_sum10_1/10000000
OutScatter_Prob10Deg_180MeV_01cn = total_sum10_01/10000000
OutScatter_Prob10Deg_180MeV_001cn = total_sum10_001/10000000
OutScatter_Prob10Deg_180MeV_0001cn = total_sum10_0001/10000000
OutScatter_Prob10Deg_180MeV_05cn = total_sum10_05/10000000
OutScatter_Prob10Deg_180MeV_005cn = total_sum10_005/10000000
OutScatter_Prob10Deg_180MeV_0005cn = total_sum10_0005/10000000
OutScatter_Prob10Deg_180MeV_00005cn = total_sum10_000005/10000000



print("OutScatter_Prob0Deg_180MeV_1cm: ", OutScatter_Prob0Deg_180MeV_1cn)

print("")
#print("OutScatter_Prob5Deg_180MeV: ", OutScatter_Prob5Deg_180MeV)
print("")
print("OutScatter_Prob7_5Deg_180MeV: ", OutScatter_Prob7_5Deg_180MeV)
print("")
print("OutScatter_Prob10Deg_180MeV_1cm: ", OutScatter_Prob10Deg_180MeV_1cn)
print("")
print("")
print("")
print("")
print("OutScatter_Prob3_5Deg_180MeV_1cm: ",OutScatter_Prob3_5Deg_180MeV_1cn)
print("OutScatter_Prob3_5Deg_180MeV_01cm: ",OutScatter_Prob3_5Deg_180MeV_01cn)
#print("OutScatter_Prob3_5Deg_180MeV_001cm: ",OutScatter_Prob3_5Deg_180MeV_001cn)
print("OutScatter_Prob3_5Deg_180MeV_0001cm: ",OutScatter_Prob3_5Deg_180MeV_0001cn)
print("OutScatter_Prob3_5Deg_180MeV_05cm: ",OutScatter_Prob3_5Deg_180MeV_05cn)
print("OutScatter_Prob3_5Deg_180MeV_005cm: ",OutScatter_Prob3_5Deg_180MeV_005cn)
print("OutScatter_Prob3_5Deg_180MeV_0005cm: ",OutScatter_Prob3_5Deg_180MeV_0005cn)
print("OutScatter_Prob3_5Deg_180MeV_00005cm: ",OutScatter_Prob3_5Deg_180MeV_00005cn)
print("")
print("")
print("")
print("")
print("OutScatter_Prob10Deg_180MeV_1cm: ",OutScatter_Prob10Deg_180MeV_1cn)
print("OutScatter_Prob10Deg_180MeV_01cm: ",OutScatter_Prob10Deg_180MeV_01cn)
print("OutScatter_Prob10Deg_180MeV_001cm: ",OutScatter_Prob10Deg_180MeV_001cn)
print("OutScatter_Prob10Deg_180MeV_0001cm: ",OutScatter_Prob10Deg_180MeV_0001cn)
print("OutScatter_Prob10Deg_180MeV_05cm: ",OutScatter_Prob10Deg_180MeV_05cn)
print("OutScatter_Prob10Deg_180MeV_005cm: ",OutScatter_Prob10Deg_180MeV_005cn)
print("OutScatter_Prob10Deg_180MeV_0005cm: ",OutScatter_Prob10Deg_180MeV_0005cn)
print("OutScatter_Prob10Deg_180MeV_00005cm: ",OutScatter_Prob10Deg_180MeV_00005cn)


x = [1, 0.5, 0.1, 0.05, 0.01, 0.005, 0.001, 0.0005]

OutScat_Prob_180_10 = [OutScatter_Prob10Deg_180MeV_1cn, OutScatter_Prob10Deg_180MeV_05cn, OutScatter_Prob10Deg_180MeV_01cn, OutScatter_Prob10Deg_180MeV_005cn, OutScatter_Prob10Deg_180MeV_001cn, OutScatter_Prob10Deg_180MeV_0005cn, OutScatter_Prob10Deg_180MeV_0001cn, OutScatter_Prob10Deg_180MeV_00005cn]

OutScat_Prob_180_35 = [OutScatter_Prob3_5Deg_180MeV_1cn, OutScatter_Prob3_5Deg_180MeV_05cn, OutScatter_Prob3_5Deg_180MeV_01cn, OutScatter_Prob3_5Deg_180MeV_005cn, OutScatter_Prob3_5Deg_180MeV_001cn, OutScatter_Prob3_5Deg_180MeV_0005cn, OutScatter_Prob3_5Deg_180MeV_0001cn, 0.2007]


fig,ax= plt.subplots(1, figsize=[30,12])
ax.set_title('Outscatter Probability, 180 MeV, 10 Degrees', fontsize  = 40)
ax.set_xlabel(r'$s_{\max}$ (cm)', fontsize = 40)
ax.set_ylabel(r'$P_S$', fontsize = 40)
ax.set_xscale('log')
plt.grid()
ax.plot(x, OutScat_Prob_180_10, 'bo-', color = 'red',markersize=16, linewidth=6, label = " 10 Deg")
plt.tick_params(axis='both', which='major', labelsize=40, length=10, width=5)
plt.tick_params(axis='both', which='minor', labelsize=10, length=5, width=3)
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/OutScatt_10Deg_180.png", dpi=300)

plt.show()

fig,ax= plt.subplots(1, figsize=[30,12])
ax.set_title('Outscatter Probability, 180 MeV, 3.5 Degrees', fontsize  = 40)
ax.set_xlabel(r'$s_{\max}$ (cm)', fontsize = 40)
ax.set_ylabel(r'$P_S$', fontsize = 40)
ax.set_xscale('log')
plt.grid()
ax.plot(x, OutScat_Prob_180_35, 'bo-', color = 'red',markersize=16, linewidth=6, label = " 3.5 Deg")
plt.tick_params(axis='both', which='major', labelsize=40, length=10, width=5)
plt.tick_params(axis='both', which='minor', labelsize=10, length=5, width=3)
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/OutScatt_3.5Deg_180.png", dpi=300)

plt.show()









