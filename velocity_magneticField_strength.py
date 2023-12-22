import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats


# Voltage 
V = 15

# Distnace
s = 0.0347

# Magnetic field

B_list = [150, 300, 450, 600, 750, 900]

df1 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/1_magnetbar.csv')
df2 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/2_magnetbar.csv')
df3 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/3_magnetbar.csv')
df4 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/4_magnetbar.csv')
df5 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/5_magnetbar.csv')
df6 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/MagneticField_Time/6_magnetbar.csv')


# Append all the data into one list
all_df = [df1, df2, df3, df4, df5, df6]

# Find the mean and standard deviation of the time
mean_time = []
std_time = []
velocity_list = [] 


for df in all_df:
    mean_time.append(round(stats.mean(df['Time'].astype(float)),2))

for df in all_df:
    std_time.append(round(stats.stdev(df['Time'].astype(float)),2))


for df in range (0, len(mean_time)):
    velocity = round(s / mean_time[df], 6)
    velocity_list.append(velocity)


fig, ax1 = plt.subplots()

# Plot the graph for T vs V on the left y-axis
graph1 = ax1.plot(B_list, velocity_list, '-x', markersize=15, markerfacecolor='red', markeredgecolor='red', linewidth=2, label='Fluid Velocity')
ax1.set_xlabel("Magnetic Field Strength (G)", size=20)
ax1.set_ylabel("Fluid Velocity ($m/s^2)$", size=20)

# Annotate each data point with its coordinates
for i, txt in enumerate(mean_time):
    ax1.annotate(f'({B_list[i]}, {velocity_list[i]})', (B_list[i], velocity_list[i]),
                 textcoords="offset points", xytext=(20, 11), ha='center')

# Create a secondary y-axis for time
ax2 = ax1.twinx()
ax2.set_ylabel("Time (s)", size=20)
ax2.tick_params(axis='y')

# Plot the time on the right y-axis
graph2 = ax2.plot(B_list, mean_time, 'k-o', linewidth=2, markerfacecolor='red', markeredgecolor='red', markersize=10, label='Time')

for i, txt in enumerate(mean_time):
    ax2.annotate(f'({B_list[i]}, {mean_time[i]})', (B_list[i], mean_time[i]),
                 textcoords="offset points", xytext=(20, 11), ha='center')

# Combine the legends at the middle on top
lns = graph1 + graph2 
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=9)


ax1.set_title("Fluid Velocity ($m/s^2$) and Time(s) vs Magnetic Field Strength (G)", size=20)
plt.grid()
plt.show()