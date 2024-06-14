import numpy as np
import scipy.stats as sc
import scipy.optimize as sc
import matplotlib.pyplot as plt
from collections import Counter
import csv
import pandas as pd
from matplotlib.ticker import FormatStrFormatter
#import matplotlib.axes as Axes
plt.rc("axes", labelsize=48)
plt.rc("xtick", labelsize=48, top=False, direction="in")
plt.rc("ytick", labelsize=48, right=True, direction="in")
plt.rc("axes", titlesize=48)
plt.rc("legend", fontsize=47, loc="center")
plt.rc("figure", figsize=(7, 5))
cm = 1/2.54
Br = 0.0174532925

depth_values = np.linspace(0, 160, 1000)

# Define the depth range (in cm)
depth_min, depth_max = 0, 8.19
depth_min1, depth_max1 = 0, 23.3

data98MeV_Step1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_Step0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_Step0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_Step0_005mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)

data180MeV_Step1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_Step0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_Step0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_Step0_005mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)




data180MeV_LET_Dose_0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Dose_0Deg_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_LET_Dose_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Dose_0Deg_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_LET_Dose_0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Dose_0Deg_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_LET_Dose_0_005mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Dose_0Deg_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)


data180MeV_LET_Track_0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Track_0Deg_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_LET_Track_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Track_0Deg_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_LET_Track_0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Track_0Deg_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_LET_Track_0_005mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_180MeV_LET_Track_0Deg_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)


data98MeV_LET_Dose_0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Dose_0Deg_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_LET_Dose_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Dose_0Deg_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_LET_Dose_0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Dose_0Deg_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_LET_Dose_0_005mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Dose_0Deg_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)


data98MeV_LET_Track_0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Track_0Deg_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_LET_Track_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Track_0Deg_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_LET_Track_0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Track_0Deg_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_LET_Track_0_005mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/Dose2D_98MeV_LET_Track_0Deg_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)


# Filter the data based on the depth range
def filter_data(data, depth_values, depth_min, depth_max):
    mask = (depth_values >= depth_min) & (depth_values <= depth_max)
    return data[mask], depth_values[mask]



data180MeV_LET_Dose_1mm, depth_values_filtered = filter_data(data180MeV_LET_Dose_1mm, depth_values, depth_min1, depth_max1)
data180MeV_LET_Dose_0_1mm, _ = filter_data(data180MeV_LET_Dose_0_1mm, depth_values, depth_min1, depth_max1)
data180MeV_LET_Dose_0_01mm, _ = filter_data(data180MeV_LET_Dose_0_01mm, depth_values, depth_min1, depth_max1)
data180MeV_LET_Dose_0_005mm, _ = filter_data(data180MeV_LET_Dose_0_005mm, depth_values, depth_min1, depth_max1)

data98MeV_LET_Dose_1mm, depth_values_filtered1 = filter_data(data98MeV_LET_Dose_1mm, depth_values, depth_min, depth_max)
data98MeV_LET_Dose_0_1mm, _ = filter_data(data98MeV_LET_Dose_0_1mm, depth_values, depth_min, depth_max)
data98MeV_LET_Dose_0_01mm, _ = filter_data(data98MeV_LET_Dose_0_01mm, depth_values, depth_min, depth_max)
data98MeV_LET_Dose_0_005mm, _ = filter_data(data98MeV_LET_Dose_0_005mm, depth_values, depth_min, depth_max)

data180MeV_LET_Track_1mm, depth_values_filtered = filter_data(data180MeV_LET_Track_1mm, depth_values, depth_min1, depth_max1)
data180MeV_LET_Track_0_1mm, _ = filter_data(data180MeV_LET_Track_0_1mm, depth_values, depth_min1, depth_max1)
data180MeV_LET_Track_0_01mm, _ = filter_data(data180MeV_LET_Track_0_01mm, depth_values, depth_min1, depth_max1)
data180MeV_LET_Track_0_005mm, _ = filter_data(data180MeV_LET_Track_0_005mm, depth_values, depth_min1, depth_max1)
data98MeV_LET_Track_1mm, depth_values_filtered1 = filter_data(data98MeV_LET_Track_1mm, depth_values, depth_min, depth_max)
data98MeV_LET_Track_0_1mm, _ = filter_data(data98MeV_LET_Track_0_1mm, depth_values, depth_min, depth_max)
data98MeV_LET_Track_0_01mm, _ = filter_data(data98MeV_LET_Track_0_01mm, depth_values, depth_min, depth_max)
data98MeV_LET_Track_0_005mm, _ = filter_data(data98MeV_LET_Track_0_005mm, depth_values, depth_min, depth_max)










# Plot LET Dose
fig, ax = plt.subplots(1, figsize=[26, 24])
ax.set_title('LET Dose', fontsize=58)
ax.set_xlabel('Depth cm', fontsize=55)
ax.set_ylabel('LET (keV/$\mu$m)', fontsize=55)
ax.plot(depth_values_filtered, data180MeV_LET_Dose_1mm, color='red', label="180MeV, 1 mm", linewidth=8, linestyle="-")
ax.plot(depth_values_filtered, data180MeV_LET_Dose_0_1mm, color='yellow', label="180MeV, 0.1 mm", linewidth=8, linestyle="--")
ax.plot(depth_values_filtered, data180MeV_LET_Dose_0_01mm, color='green', label="180MeV, 0.01 mm", linewidth=8, linestyle="-.")
ax.plot(depth_values_filtered, data180MeV_LET_Dose_0_005mm, color='orange', label="180MeV, 0.005 mm", linewidth=8, linestyle="--")
ax.plot(depth_values_filtered1, data98MeV_LET_Dose_1mm, color='blue', label="98MeV, 1 mm", linewidth=8, linestyle="-")
ax.plot(depth_values_filtered1, data98MeV_LET_Dose_0_1mm, color='purple', label="98MeV, 0.1 mm", linewidth=8, linestyle="--")
ax.plot(depth_values_filtered1, data98MeV_LET_Dose_0_01mm, color='brown', label="98MeV, 0.01 mm", linewidth=8, linestyle="-.")
ax.plot(depth_values_filtered1, data98MeV_LET_Dose_0_005mm, color='black', label="98MeV, 0.005 mm", linewidth=8, linestyle="--")
ax.set_xlim(depth_min, 25)
ax.legend()
plt.axvline(x=7.2, color='grey', linewidth=8, linestyle='--')
plt.axvline(x=21.2, color='grey', linewidth=8, linestyle='--')
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/LETDoseBoth.png", dpi=300)
plt.show()

# Plot LET Track
fig, ax = plt.subplots(1, figsize=[26, 24])
ax.set_title('LET Track', fontsize=58)
ax.set_xlabel('Depth cm', fontsize=55)
ax.set_ylabel('LET (keV/$\mu$m)', fontsize=55)
ax.plot(depth_values_filtered, data180MeV_LET_Track_1mm, color='red', label="180MeV, 1 mm", linewidth=8, linestyle="-")
ax.plot(depth_values_filtered, data180MeV_LET_Track_0_1mm, color='yellow', label="180MeV, 0.1 mm", linewidth=8, linestyle="--")
ax.plot(depth_values_filtered, data180MeV_LET_Track_0_01mm, color='green', label="180MeV, 0.01 mm", linewidth=8, linestyle="-.")
ax.plot(depth_values_filtered, data180MeV_LET_Track_0_005mm, color='orange', label="180MeV, 0.005 mm", linewidth=8, linestyle=":")
ax.plot(depth_values_filtered1, data98MeV_LET_Track_1mm, color='blue', label="98MeV, 1 mm", linewidth=8, linestyle="-")
ax.plot(depth_values_filtered1, data98MeV_LET_Track_0_1mm, color='purple', label="98MeV, 0.1 mm", linewidth=8, linestyle="--")
ax.plot(depth_values_filtered1, data98MeV_LET_Track_0_01mm, color='brown', label="98MeV, 0.01 mm", linewidth=8, linestyle="-.")
ax.plot(depth_values_filtered1, data98MeV_LET_Track_0_005mm, color='pink', label="98MeV, 0.005 mm", linewidth=8, linestyle=":")
ax.set_xlim(depth_min, 25)
plt.axvline(x=7.2, color='grey', linewidth=8, linestyle='--')
plt.axvline(x=21.2, color='grey', linewidth=8, linestyle='--')
ax.legend()
plt.grid()
plt.tight_layout()
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/LETTrackBoth.png", dpi=300)
plt.show()




























