import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats


# Voltage 
V = 15

# Magnetic field

B_list = [150, 300, 450, 600, 750, 900]

df1 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/1_magnetbar.csv')
df2 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/2_magnetbar.csv')
df3 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/3_magnetbar.csv')
df4 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/4_magnetbar.csv')
df5 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/5_magnetbar.csv')
df6 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/6_magnetbar.csv')


# Append all the data into one list
all_df = [df1, df2, df3, df4, df5, df6]

# Find the mean and standard deviation of the time
mean_time = []
std_time = []

for df in all_df:
    mean_time.append(round(stats.mean(df['Time'].astype(float)),2))

for df in all_df:
    std_time.append(round(stats.stdev(df['Time'].astype(float)),2))


print('Mean Time for each Voltage = ',mean_time)
print('Standard Deviation for each Voltage =',std_time)

# PLot the graph vor T vs V
plt.plot(B_list, mean_time, '-x', markersize = 15, markerfacecolor = 'red', markeredgecolor = 'red' , linewidth = 2)
plt.grid()
plt.xlabel("Magnetic Field Strength (G)", size = 20)
plt.ylabel("Time of fluid flow across a fixed distance (s)", size = 20)
plt.title("Time of fluid flow across a fixed distance (s) vs Magnetic Field Strength (G)" ,size = 20)

# Annotate each data point with its coordinates
for i, txt in enumerate(mean_time):
    plt.annotate(f'({B_list[i]}, {mean_time[i]})', (B_list[i], mean_time[i]),
                 textcoords="offset points", xytext=(20, 11), ha='center')

plt.show()
