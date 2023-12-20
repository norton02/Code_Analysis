import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as stats

# Distance
s = 0.0347

# Voltage
voltage_list = [9.0, 9.5, 10, 10.5, 11, 11.5, 12, 12.5, 13, 13.5]

# Time 
df1 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_9.csv')
df2 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_9.5.csv')
df3 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_10.csv')
df4 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_10.5.csv')
df5 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_11.csv')
df6 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_11.5.csv')
df7 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_12.csv')
df8 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_12.5.csv')
df9 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_13.csv')
df10 = pd.read_csv('C:/Users/aleis/Desktop\School\Year 2 Sem 3\Physics Lab IV/DataAnalysis/Voltage_Time/voltage_13.5.csv')

# Append all the data into one list
all_df = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10]

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
plt.plot(voltage_list, mean_time, '-x', markersize = 15, markerfacecolor = 'red', markeredgecolor = 'red' , linewidth = 2)
plt.grid()
plt.xlabel("Voltage (V)", size = 28)
plt.ylabel("Time of fluid flow across a fixed distance (s)", size = 28)
plt.title("Time of fluid flow across a fixed distance (s) vs Voltage (V)" ,size = 28)   

# Annotate each data point with its coordinates
for i, txt in enumerate(mean_time):
    plt.annotate(f'({voltage_list[i]}, {mean_time[i]})', (voltage_list[i], mean_time[i]),
                 textcoords="offset points", xytext=(20, 11), ha='center')

plt.show()






