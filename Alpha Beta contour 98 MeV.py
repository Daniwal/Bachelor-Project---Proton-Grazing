import math
import numpy as np
import scipy.stats as sc
import scipy.optimize as sc
import matplotlib.pyplot as plt
from collections import Counter
import csv
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
import matplotlib.colors as mcolors
#import matplotlib.axes as Axes
plt.rc("axes", labelsize=40)
plt.rc("xtick", labelsize=40, top=False, direction="in")
plt.rc("ytick", labelsize=40, right=True, direction="in")
plt.rc("axes", titlesize=40)
plt.rcParams['axes.titlesize'] = 38  
plt.rc("legend", fontsize=40, loc="upper left")
plt.rc("figure", figsize=(7, 5))
cm = 1/2.54
Br = 0.0174532925


contour_levels = [10, 50, 90]




file_path = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_0deg_1cm.csv'
data = pd.read_csv(file_path, comment='#', header=None, names=['x', 'y', 'z', 'dose'])



file_path2 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_5deg.csv'
data2 = pd.read_csv(file_path2, comment='#', header=None, names=['x', 'y', 'z', 'dose'])

file_path3 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_7.5deg.csv'
data3 = pd.read_csv(file_path3, comment='#', header=None, names=['x', 'y', 'z', 'dose'])

file_path4 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_10Deg_1cm.csv'
data4 = pd.read_csv(file_path4, comment='#', header=None, names=['x', 'y', 'z', 'dose'])




file_path35_1 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_1cm.csv'
data35_1 = pd.read_csv(file_path35_1, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_05 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.5cm.csv'
data35_05 = pd.read_csv(file_path35_05, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_01 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.1cm.csv'
data35_01 = pd.read_csv(file_path35_01, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_005 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.05cm.csv'
data35_005 = pd.read_csv(file_path35_005, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_001 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.01cm.csv'
data35_001 = pd.read_csv(file_path35_001, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_0005 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.005cm.csv'
data35_0005 = pd.read_csv(file_path35_0005, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_0001 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.001cm.csv'
data35_0001 = pd.read_csv(file_path35_0001, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path35_00005 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_3.5Deg_0.0005cm.csv'
data35_00005 = pd.read_csv(file_path35_00005, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#







def convertToAlpha(data):
   # print(len(data))
    alpha = []
    
    columnY = data['y']*0.375 - 75
   # print(len(columnY))
    columnZ = 45 # Distance from impact point on tungsten to scoring entrance XY
    for i in range(len(columnY)):
        calcAlpha = math.degrees(math.atan(columnY[i]/columnZ))
        alpha.append(calcAlpha)
   # print(len(alpha))
    return alpha
    

def convertToBeta(data):
    #print(len(data))
    beta = []
    
    columnX = data['x']*0.375 - 75
   # print(len(columnX))
    columnZ = 45
    for i in range(len(columnX)):
        calcBeta = math.degrees(math.atan(columnX[i]/columnZ))
        beta.append(calcBeta)
   # print(len(beta))
    return beta

def convertToNormalize(data):
    norm = data['dose'] / data['dose'].max()
    return norm


beta_unique = np.unique(np.array(convertToBeta(data)))
alpha_unique = np.unique(np.array(convertToAlpha(data)))

zNorm = convertToNormalize(data)

Z = zNorm.values.reshape(len(alpha_unique), len(beta_unique))
X, Y = np.meshgrid(beta_unique, alpha_unique)



plt.figure(figsize=(12, 8))
contour = plt.contour(Y, X, Z, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)


# Create the contour line plot
contour_lines = plt.contour(Y, X, Z*100,levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: Dose Distribution 0 deg, 98 MeV')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_0Deg.png", dpi=300)

plt.show()





beta_unique2 = np.unique(np.array(convertToBeta(data2)))
alpha_unique2 = np.unique(np.array(convertToAlpha(data2)))

zNorm2 = convertToNormalize(data2)

Z2 = zNorm2.values.reshape(len(alpha_unique2), len(beta_unique2))
X2, Y2 = np.meshgrid(beta_unique2, alpha_unique2)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y2, X2, Z2*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y2, X2, Z2*100,levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: Dose Distribution 5 deg, 98 MeV \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_5Deg.png", dpi=300)

plt.show()


beta_unique3 = np.unique(np.array(convertToBeta(data3)))
alpha_unique3 = np.unique(np.array(convertToAlpha(data3)))

zNorm3 = convertToNormalize(data3)

Z3 = zNorm3.values.reshape(len(alpha_unique3), len(beta_unique3))
X3, Y3 = np.meshgrid(beta_unique3, alpha_unique3)




plt.figure(figsize=(12, 8))
contour = plt.contour(Y3, X3, Z3*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y3, X3, Z3*100,levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: Dose Distribution 7.5 deg, 98 MeV \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_7.5Deg.png", dpi=300)

plt.show()


beta_unique4 = np.unique(np.array(convertToBeta(data4)))
alpha_unique4 = np.unique(np.array(convertToAlpha(data4)))

zNorm4 = convertToNormalize(data4)

Z4 = zNorm4.values.reshape(len(alpha_unique4), len(beta_unique4))
X4, Y4 = np.meshgrid(beta_unique4, alpha_unique4)




plt.figure(figsize=(12, 8))
contour = plt.contour(Y4, X4, Z4*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y4, X4, Z4*100,levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: Dose Distribution 10 deg, 98 MeV \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg.png", dpi=300)

plt.show()




####
beta_unique35_1 = np.unique(np.array(convertToBeta(data35_1)))
alpha_unique35_1 = np.unique(np.array(convertToAlpha(data35_1)))


Z35_1 = data35_1['dose'].values.reshape(len(alpha_unique35_1), len(beta_unique35_1))

zNorm35_1 = convertToNormalize(data35_1)

Z35_1 = zNorm35_1.values.reshape(len(alpha_unique35_1), len(beta_unique35_1))
X35_1, Y35_1 = np.meshgrid(beta_unique35_1, alpha_unique35_1)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_1, X35_1, Z35_1*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_1, X35_1, Z35_1*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 1cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg1.png", dpi=300)

plt.show()


####
beta_unique35_05 = np.unique(np.array(convertToBeta(data35_05)))
alpha_unique35_05 = np.unique(np.array(convertToAlpha(data35_05)))

zNorm35_05 = convertToNormalize(data35_05)

Z35_05 = zNorm35_05.values.reshape(len(alpha_unique35_05), len(beta_unique35_05))
X35_05, Y35_05 = np.meshgrid(beta_unique35_05, alpha_unique35_05)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_05, X35_05, Z35_05*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_05, X35_05, Z35_05*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.5 \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg2.png", dpi=300)

plt.show()




####
beta_unique35_01 = np.unique(np.array(convertToBeta(data35_01)))
alpha_unique35_01 = np.unique(np.array(convertToAlpha(data35_01)))

zNorm35_01 = convertToNormalize(data35_01)

Z35_01 = zNorm35_01.values.reshape(len(alpha_unique35_01), len(beta_unique35_01))
X35_01, Y35_01 = np.meshgrid(beta_unique35_01, alpha_unique35_01)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_01, X35_01, Z35_01*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_01, X35_01, Z35_01*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.1cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg3.png", dpi=300)

plt.show()


####
beta_unique35_005 = np.unique(np.array(convertToBeta(data35_005)))
alpha_unique35_005 = np.unique(np.array(convertToAlpha(data35_005)))

zNorm35_005 = convertToNormalize(data35_005)

Z35_005 = zNorm35_005.values.reshape(len(alpha_unique35_005), len(beta_unique35_005))
X35_005, Y35_005 = np.meshgrid(beta_unique35_005, alpha_unique35_005)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_005, X35_005, Z35_005*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_005, X35_005, Z35_005*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.05cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg4.png", dpi=300)

plt.show()


###
beta_unique35_001 = np.unique(np.array(convertToBeta(data35_001)))
alpha_unique35_001 = np.unique(np.array(convertToAlpha(data35_001)))

zNorm35_001 = convertToNormalize(data35_001)

Z35_001 = zNorm35_001.values.reshape(len(alpha_unique35_001), len(beta_unique35_001))
X35_001, Y35_001 = np.meshgrid(beta_unique35_001, alpha_unique35_001)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_001, X35_001, Z35_001*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_001, X35_001, Z35_001*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.01cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg5.png", dpi=300)

plt.show()


####
beta_unique35_0005 = np.unique(np.array(convertToBeta(data35_0005)))
alpha_unique35_0005 = np.unique(np.array(convertToAlpha(data35_0005)))

zNorm35_0005 = convertToNormalize(data35_0005)

Z35_0005 = zNorm35_0005.values.reshape(len(alpha_unique35_0005), len(beta_unique35_0005))
X35_0005, Y35_0005 = np.meshgrid(beta_unique35_0005, alpha_unique35_0005)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_0005, X35_0005, Z35_0005*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_0005, X35_0005, Z35_0005*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.005cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/ContourPlot_98_3.5Deg6.png", dpi=300)

plt.show()


####
beta_unique35_0001 = np.unique(np.array(convertToBeta(data35_0001)))
alpha_unique35_0001 = np.unique(np.array(convertToAlpha(data35_0001)))

zNorm35_0001 = convertToNormalize(data35_0001)

Z35_0001 = zNorm35_0001.values.reshape(len(alpha_unique35_0001), len(beta_unique35_0001))
X35_0001, Y35_0001 = np.meshgrid(beta_unique35_0001, alpha_unique35_0001)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_0001, X35_0001, Z35_0001*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_0001, X35_0001, Z35_0001*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.001cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg7.png", dpi=300)

plt.show()


####
beta_unique35_00005 = np.unique(np.array(convertToBeta(data35_00005)))
alpha_unique35_00005 = np.unique(np.array(convertToAlpha(data35_00005)))

zNorm35_00005 = convertToNormalize(data35_00005)

Z35_00005 = zNorm35_00005.values.reshape(len(alpha_unique35_00005), len(beta_unique35_00005))
X35_00005, Y35_00005 = np.meshgrid(beta_unique35_00005, alpha_unique35_00005)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_00005, X35_00005, Z35_00005*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_00005, X35_00005, Z35_00005*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 3.5 deg, 98 MeV, SL= 0.0005cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.tight_layout()
plt.grid()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_3.5Deg8.png", dpi=300)

plt.show()


#
#
#
#
#


file_path10_1 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_10Deg_1cm.csv'
data10_1 = pd.read_csv(file_path10_1, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_05 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_Deg10_0.5cm.csv'
data10_05 = pd.read_csv(file_path10_05, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_01 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_Deg10_0.1cm.csv'
data10_01 = pd.read_csv(file_path10_01, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_005 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_Deg10_0.05cm.csv'
data10_005 = pd.read_csv(file_path10_005, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_001 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_Deg10_0.01cm.csv'
data10_001 = pd.read_csv(file_path10_001, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_0005 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_Deg10_0.005cm.csv'
data10_0005 = pd.read_csv(file_path10_0005, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_0001 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_Deg10_0.01cm.csv'
data10_0001 = pd.read_csv(file_path10_0001, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
file_path10_00005 = '/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/GE_F1.14438563/98MeV_Dose2D_10Deg_0.0005cm.csv'
data10_00005 = pd.read_csv(file_path10_00005, comment='#', header=None, names=['x', 'y', 'z', 'dose'])
#
beta_unique10_1 = np.unique(np.array(convertToBeta(data10_1)))
alpha_unique10_1 = np.unique(np.array(convertToAlpha(data10_1)))


Z35_1 = data10_1['dose'].values.reshape(len(alpha_unique10_1), len(beta_unique10_1))

zNorm35_1 = convertToNormalize(data10_1)

Z35_1 = zNorm35_1.values.reshape(len(alpha_unique10_1), len(beta_unique10_1))
X35_1, Y35_1 = np.meshgrid(beta_unique10_1, alpha_unique10_1)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_1, X35_1, Z35_1*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_1, X35_1, Z35_1*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 1cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg1.png", dpi=300)

plt.show()


####
beta_unique10_05 = np.unique(np.array(convertToBeta(data10_05)))
alpha_unique10_05 = np.unique(np.array(convertToAlpha(data10_05)))

zNorm35_05 = convertToNormalize(data10_05)

Z35_05 = zNorm35_05.values.reshape(len(alpha_unique10_05), len(beta_unique10_05))
X35_05, Y35_05 = np.meshgrid(beta_unique10_05, alpha_unique10_05)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_05, X35_05, Z35_05*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_05, X35_05, Z35_05*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.5 \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg2.png", dpi=300)

plt.show()




####
beta_unique10_01 = np.unique(np.array(convertToBeta(data10_01)))
alpha_unique10_01 = np.unique(np.array(convertToAlpha(data10_01)))

zNorm35_01 = convertToNormalize(data10_01)

Z35_01 = zNorm35_01.values.reshape(len(alpha_unique10_01), len(beta_unique10_01))
X35_01, Y35_01 = np.meshgrid(beta_unique10_01, alpha_unique10_01)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_01, X35_01, Z35_01*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_01, X35_01, Z35_01*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.1cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg3.png", dpi=300)

plt.show()


####
beta_unique10_005 = np.unique(np.array(convertToBeta(data10_005)))
alpha_unique10_005 = np.unique(np.array(convertToAlpha(data10_005)))

zNorm35_005 = convertToNormalize(data10_005)

Z35_005 = zNorm35_005.values.reshape(len(alpha_unique10_005), len(beta_unique10_005))
X35_005, Y35_005 = np.meshgrid(beta_unique10_005, alpha_unique10_005)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_005, X35_005, Z35_005*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_005, X35_005, Z35_005*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.05cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg4.png", dpi=300)

plt.show()


###
beta_unique10_001 = np.unique(np.array(convertToBeta(data10_001)))
alpha_unique10_001 = np.unique(np.array(convertToAlpha(data10_001)))

zNorm35_001 = convertToNormalize(data10_001)

Z35_001 = zNorm35_001.values.reshape(len(alpha_unique10_001), len(beta_unique10_001))
X35_001, Y35_001 = np.meshgrid(beta_unique10_001, alpha_unique10_001)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_001, X35_001, Z35_001*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_001, X35_001, Z35_001*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.01cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg5.png", dpi=300)

plt.show()


####
beta_unique10_0005 = np.unique(np.array(convertToBeta(data10_0005)))
alpha_unique10_0005 = np.unique(np.array(convertToAlpha(data10_0005)))

zNorm35_0005 = convertToNormalize(data10_0005)

Z35_0005 = zNorm35_0005.values.reshape(len(alpha_unique10_0005), len(beta_unique10_0005))
X35_0005, Y35_0005 = np.meshgrid(beta_unique10_0005, alpha_unique10_0005)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_0005, X35_0005, Z35_0005*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_0005, X35_0005, Z35_0005*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.005cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/ContourPlot_98_10Deg6.png", dpi=300)

plt.show()


####
beta_unique10_0001 = np.unique(np.array(convertToBeta(data10_0001)))
alpha_unique10_0001 = np.unique(np.array(convertToAlpha(data10_0001)))

zNorm35_0001 = convertToNormalize(data10_0001)

Z35_0001 = zNorm35_0001.values.reshape(len(alpha_unique10_0001), len(beta_unique10_0001))
X35_0001, Y35_0001 = np.meshgrid(beta_unique10_0001, alpha_unique10_0001)


plt.figure(figsize=(12, 8))
contour = plt.contour(Y35_0001, X35_0001, Z35_0001*100, cmap='viridis', levels=10)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_0001, X35_0001, Z35_0001*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.001cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg7.png", dpi=300)

plt.show()


####
beta_unique10_00005 = np.unique(np.array(convertToBeta(data10_00005)))
alpha_unique10_00005 = np.unique(np.array(convertToAlpha(data10_00005)))

zNorm35_00005 = convertToNormalize(data10_00005)

Z35_00005 = zNorm35_00005.values.reshape(len(alpha_unique10_00005), len(beta_unique10_00005))
X35_00005, Y35_00005 = np.meshgrid(beta_unique10_00005, alpha_unique10_00005)


plt.figure(figsize=(12, 8))
norm = mcolors.Normalize(vmin=0, vmax=100)
contour = plt.contour(Y35_00005, X35_00005, Z35_00005*100, cmap='viridis', levels=10, norm=norm)
cbar = plt.colorbar(contour)
cbar.set_ticks(np.linspace(0, 100, 11))
cbar.set_ticklabels([f'{int(t)}%' for t in np.linspace(0, 100, 11)], fontsize=32)

# Create the contour line plot
contour_lines = plt.contour(Y35_00005, X35_00005, Z35_00005*100, levels=contour_levels, colors='black')
# Add labels to contour lines with percentages
fmt = lambda x: f'{x*100:.1f}%'  # Function to format labels as percentages
plt.clabel(contour_lines, fmt='%1.0f%%', colors='black', fontsize=24)  
plt.xlim(-30, 30)
plt.ylim(-10, 30)
plt.axhline(y=0, color='grey', linestyle='--')
plt.axvline(x=0, color='grey', linestyle='--')
plt.title('Angular Dist. Contour: 10 deg, 98 MeV, SL= 0.0005cm \n')
plt.xlabel(r'$\alpha$ ($^\circ$)')
plt.ylabel(r'$\beta$ ($^\circ$)')
plt.tight_layout()
plt.grid()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/ContourPlot_98_10Deg8.png", dpi=300)

plt.show()



