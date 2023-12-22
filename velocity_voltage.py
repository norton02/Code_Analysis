import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats


# Distance
s = 0.0347

# Voltage
voltage_list = [9.0, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]

# Time 
df1 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_9.csv')
df2 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_9.5.csv')
df3 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_10.csv')
df4 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_10.5.csv')
df5 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_11.csv')
df6 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_11.5.csv')
df7 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_12.csv')
df8 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_12.5.csv')
df9 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_13.csv')
df10 = pd.read_csv('C:/Users/aleis/Desktop\Study\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_13.5.csv')

# Append all the data into one list
all_df = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]

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
    
print('Mean Time for each Voltage = ',mean_time)
print('Standard Deviation for each Voltage =',std_time)



fig, ax1 = plt.subplots()

# Plot the graph for T vs V on the left y-axis
graph1 = ax1.plot(voltage_list, velocity_list, '-x', markersize=15, markerfacecolor='red', markeredgecolor='red', linewidth=2, label='Fluid Velocity')
ax1.set_xlabel("Voltage (V)", size=20)
ax1.set_ylabel("Fluid Velocity ($m/s^2)$", size=20)

for i, txt in enumerate(mean_time):
    ax1.annotate(f'({voltage_list[i]}, {velocity_list[i]})', (voltage_list[i], velocity_list[i]),
                 textcoords="offset points", xytext=(20, -15), ha='center')
    
# Create a secondary y-axis for time
ax2 = ax1.twinx()
ax2.set_ylabel("Time (s)", size=20)
ax2.tick_params(axis='y')

graph2 = ax2.plot(voltage_list, mean_time, 'k-o', linewidth=2, markerfacecolor='red', markeredgecolor='red', markersize=10, label='Time')

for i, txt in enumerate(mean_time):
    ax2.annotate(f'({voltage_list[i]}, {mean_time[i]})', (voltage_list[i], mean_time[i]),
                 textcoords="offset points", xytext=(20, 11), ha='center')

# Combine the legends at the middle on top
lns = graph1 + graph2 
labs = [l.get_label() for l in lns]
ax1.legend(lns, labs, loc=9)


ax1.set_title("Fluid Velocity ($m/s^2$) and Time(s) vs Voltage (V)", size=20)
plt.grid()
plt.show()








