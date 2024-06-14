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
plt.rc("legend", fontsize=40, loc="upper center")
plt.rc("figure", figsize=(7, 5))
cm = 1/2.54
Br = 0.0174532925



data98MeV_Step1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_Step0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_Step0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data98MeV_Step0_001mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_98MeV_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)



data180MeV_Step1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_Step0_1mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_0.1mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_Step0_01mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_0.01mm.csv", skip_header = 8, usecols= (3), filling_values=0)
data180MeV_Step0_001mm = np.genfromtxt("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Output files/Dose_LET(New SL)/DepthDose_180MeV_0.005mm.csv", skip_header = 8, usecols= (3), filling_values=0)


norm_max = data98MeV_Step1mm.max()

depth_values = np.linspace(0, 160, 1000)

# Define the depth range (in cm)
depth_min, depth_max = 0, 8.168
depth_min1, depth_max1 = 0, 23.2


# Function to filter data based on depth range
def filter_data(data, depth_values, depth_min, depth_max):
    mask = (depth_values >= depth_min) & (depth_values <= depth_max)
    return data[mask], depth_values[mask]


def Normalize(data):
    norm = data / norm_max
    return norm


# Filter the data based on the depth ranges
data98MeV_Step1mm_filtered, depth_values_filtered = filter_data(data98MeV_Step1mm, depth_values, depth_min, depth_max)
data98MeV_Step0_1mm_filtered, _ = filter_data(data98MeV_Step0_1mm, depth_values, depth_min, depth_max)
data98MeV_Step0_01mm_filtered, _ = filter_data(data98MeV_Step0_01mm, depth_values, depth_min, depth_max)
data98MeV_Step0_001mm_filtered, _ = filter_data(data98MeV_Step0_001mm, depth_values, depth_min, depth_max)

data180MeV_Step1mm_filtered, depth_values_filtered1 = filter_data(data180MeV_Step1mm, depth_values, depth_min1, depth_max1)
data180MeV_Step0_1mm_filtered, _ = filter_data(data180MeV_Step0_1mm, depth_values, depth_min1, depth_max1)
data180MeV_Step0_01mm_filtered, _ = filter_data(data180MeV_Step0_01mm, depth_values, depth_min1, depth_max1)
data180MeV_Step0_001mm_filtered, _ = filter_data(data180MeV_Step0_001mm, depth_values, depth_min1, depth_max1)

# Plot Dose at phantom for both energies
fig, ax = plt.subplots(1, figsize=[28, 14])
ax.set_title('Dose at phantom', fontsize=54)
ax.set_xlabel('Depth in cm', fontsize=50)
ax.set_ylabel('Dose', fontsize=50)
ax.set_xlim(xmin=-1, xmax=25)
plt.axvline(x=7.2, color='grey', linewidth=6, linestyle='--')
plt.axvline(x=21.2, color='grey', linewidth=6, linestyle='--')
ax.plot(depth_values_filtered, Normalize(data98MeV_Step1mm_filtered), color='red', label="ST: 1mm, 98 MeV", linewidth=6, linestyle="-")
ax.plot(depth_values_filtered, Normalize(data98MeV_Step0_1mm_filtered), color='orange', label="ST: 0.1mm, 98 MeV", linewidth=6, linestyle="--")
ax.plot(depth_values_filtered, Normalize(data98MeV_Step0_01mm_filtered), color='yellow', label="ST: 0.01mm, 98 MeV", linewidth=6, linestyle="-.")
ax.plot(depth_values_filtered, Normalize(data98MeV_Step0_001mm_filtered), color='green', label="ST: 0.005mm, 98 MeV", linewidth=6, linestyle=":")

ax.plot(depth_values_filtered1, Normalize(data180MeV_Step1mm_filtered), color='blue', label="ST: 1mm, 180 MeV", linewidth=6, linestyle="-")
ax.plot(depth_values_filtered1, Normalize(data180MeV_Step0_1mm_filtered), color='purple', label="ST: 0.1mm, 180 MeV", linewidth=6, linestyle="--")
ax.plot(depth_values_filtered1, Normalize(data180MeV_Step0_01mm_filtered), color='brown', label="ST: 0.01mm, 180 MeV", linewidth=6, linestyle="-.")
ax.plot(depth_values_filtered1, Normalize(data180MeV_Step0_001mm_filtered), color='gray', label="ST: 0.005mm, 180 MeV", linewidth=6, linestyle=":")
plt.grid()
ax.legend(loc='upper center', fontsize=32)
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/DoseDepthBoth.png", dpi=300)
plt.show()

# Plot Dose at phantom for 98 MeV
fig, ax1 = plt.subplots(1, figsize=[20, 16])
ax1.set_title('Dose at phantom 98 MeV', fontsize=54)
ax1.set_xlabel('Depth in cm', fontsize=50)
ax1.set_ylabel('Dose', fontsize=50)
ax1.set_xlim(xmin=-1, xmax=25)
plt.axvline(x=7.2, color='grey', linewidth=6, linestyle='--')
ax1.plot(depth_values_filtered, Normalize(data98MeV_Step1mm_filtered), color='red', label="ST: 1mm", linewidth=6, linestyle="-")
ax1.plot(depth_values_filtered, Normalize(data98MeV_Step0_1mm_filtered), color='orange', label="ST: 0.1mm", linewidth=6, linestyle="--")
ax1.plot(depth_values_filtered, Normalize(data98MeV_Step0_01mm_filtered), color='yellow', label="ST: 0.01mm", linewidth=6, linestyle="-.")
ax1.plot(depth_values_filtered, Normalize(data98MeV_Step0_001mm_filtered), color='green', label="ST: 0.001mm", linewidth=6, linestyle=":")
plt.grid()
ax1.legend(loc='upper right', fontsize=40)
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/DoseDepth98.png", dpi=300)
plt.show()

# Plot Dose at phantom for 180 MeV
fig, ax2 = plt.subplots(1, figsize=[20, 16])
ax2.set_title('Dose at phantom 180 MeV', fontsize=54)
ax2.set_xlabel('Depth in cm', fontsize=50)
ax2.set_ylabel('Dose', fontsize=50)
ax2.set_xlim(xmin=-1, xmax=25)
plt.axvline(x=21.2, color='grey', linewidth=6, linestyle='--')
ax2.plot(depth_values_filtered1, Normalize(data180MeV_Step1mm_filtered), color='red', label="ST: 1mm", linewidth=6, linestyle="-")
ax2.plot(depth_values_filtered1, Normalize(data180MeV_Step0_1mm_filtered), color='orange', label="ST: 0.1mm", linewidth=6, linestyle="--")
ax2.plot(depth_values_filtered1, Normalize(data180MeV_Step0_01mm_filtered), color='yellow', label="ST: 0.01mm", linewidth=6, linestyle="-.")
ax2.plot(depth_values_filtered1, Normalize(data180MeV_Step0_001mm_filtered), color='green', label="ST: 0.001mm", linewidth=6, linestyle=":")
plt.grid()
ax2.legend(loc='upper left', fontsize=40)
plt.savefig("/Users/danielwaldstromhenriksen/Documents/Documents copy/Skole/Uni/6. Semester/Bachelor Projekt/Plots/DoseDepth180.png", dpi=300)
plt.show()







