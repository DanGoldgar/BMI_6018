#%% Libraries
from datetime import datetime

import pandas as pd
import numpy as np
pd.set_option('display.max_columns', None)


#%% Importing Data
flights_data = pd.read_csv('data/flights.csv')
flights_data.head(10)
weather_data_pd = pd.read_csv('data/weather.csv')
weather_data_np = weather_data_pd.to_numpy()

#%% Pandas Data Filtering/Sorting Question Answering
#use flights_data
print(flights_data.iloc[0])

# Question 1: Number of flights from JFK to SLC
from_JFK = flights_data.loc[flights_data['origin'] == 'JFK']
JFK_SLC = from_JFK.loc[from_JFK['dest'] == 'SLC']
q_1 = len(JFK_SLC.index)
print(q_1)

# Question 2: Number of airlines flying to SLC
dest_SLC = flights_data.loc[flights_data['dest'] == 'SLC']
q_2 = len(pd.unique(dest_SLC['carrier']))
print(q_2)

# Question 3: Average arrival delay for flights to RDU
dest_RDU = flights_data.loc[flights_data['dest'] == 'RDU']
q_3 = dest_RDU.loc[:, 'arr_delay'].mean()
print(q_3)

#Question 4 What proportion of flights to SEA come from the two NYC airports (LGA and JFK)?  float
dest_SEA = flights_data.loc[flights_data['dest'] == 'SEA']
ori_NYC = dest_SEA.loc[(dest_SEA['origin'] == 'JFK') | (dest_SEA['origin'] == 'LGA')]
q_4 = len(ori_NYC.index) / len(dest_SEA.index)
print(q_4)

dest_list = flights_data['dest'].unique()
for i in range(len(dest_list)):
    dest_slice = flights_data.loc[flights_data['dest'] == dest_list[i]]

# Questions 5-6: Find the date with the highest average departure delay, and the date with the
# highest arrival delay

# Pull y/m/d data from dataframe and assemble into list of date objects formatted as m/d/y
flight_year = flights_data['year']
flight_month = flights_data['month']
flight_day = flights_data['day']
flight_date = []
for i in range(len(flights_data.index)):
    x = datetime(flight_year[i], flight_month[i], flight_day[i])
    flight_date.append(x.strftime("%x"))
# Copy data into new df and add 'Date' column
flights_data_1 = flights_data.copy()
flights_data_1['Date'] = flight_date

# Create list of all unique Date entries
date_list = flights_data_1['Date'].unique()
# Initialize placeholders for tracking max delays
max_dep_delay = 0
max_arr_delay = 0
max_dep_date = date_list[0]
max_arr_date = date_list[0]

# Slice dataframe according to unique date instances, evaluate each slice for average delay times
for i in date_list:
    date_slice = flights_data_1.loc[flights_data_1['Date'] == i]
    # Calculate avg airspeed for slice
    avg_dep_delay = date_slice['dep_delay'].mean()
    avg_arr_delay = date_slice['arr_delay'].mean()
    if avg_dep_delay > max_dep_delay:
        max_dep_delay = avg_dep_delay
        max_dep_date = i
    if avg_arr_delay > max_arr_delay:
        max_arr_delay = avg_arr_delay
        max_arr_date = i
print(f"The largest avg departure delay was {max_dep_delay} min on {max_dep_date}")
print(f"The largest avg arrival delay was {max_arr_delay} min on {max_arr_date}")
q_5 = flights_data_1.loc[flights_data_1['Date'] == max_dep_date]
q_6 = flights_data_1.loc[flights_data_1['Date'] == max_arr_date]

"""

# Question 7:
Note to instructor: I was unable to correct a logic error resulting in exception. I have commented out
the code below for partial credit

dep_filter = flights_data.loc[(flights_data['origin'] == 'JFK') | (flights_data['origin'] == 'LGA')]
dep_filter_speed = dep_filter.assign(speed = dep_filter['distance'] / dep_filter['air_time'])
print(dep_filter_speed)
max_speed = dep_filter_speed['speed'].max()
max_spd_index = dep_filter_speed['speed'].idxmax()
print(max_speed)
max_speed_row = dep_filter_speed.iloc[max_spd_index]
q_7 = max_speed_row.iloc[:,[9,17]]

"""

# Question 8: Replace all nans in the weather pd dataframe with 0s.
clean_weather = np.nan_to_num(weather_data_np)
q_8 = clean_weather
print(q_8)

# Question 9: How many observations were made in February?
months = clean_weather[:, 3]
q_9 = np.count_nonzero(months == 2)
print(q_9)

# Question 10: Mean humidity in February
# Create slice for February data
feb_slice = clean_weather[np.where(clean_weather[:,3] == 2)]
# Calculate mean for humidity column
q_10 = np.mean(feb_slice[:, 8])
print(q_10)

# Question 11: Standard deviation of humidity in Feb
q_11 = np.std(feb_slice[:,8])
print(q_11)
