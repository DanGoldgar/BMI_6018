# -*- coding: utf-8 -*-
"""
Created on Wed Nov 24 09:47:55 2021

@author: u6026797
"""
import matplotx
#%% libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sea
import numpy as np
import datetime
#%% data

url = 'https://raw.githubusercontent.com/CSSEGISandData/COVID-19/master/csse_covid_19_data/csse_covid_19_time_series/time_series_covid19_confirmed_US.csv'
covid_df = pd.read_csv(url, index_col=0)

#%% Instructions
'''
Overall instructions:
As described in the homework description, each graphic you make must:
   1. Have a thoughtful title
   2. Have clearly labelled axes 
   3. Be legible
   4. Not be a pie chart
I should be able to run your .py file and recreate the graphics without error.
As per usual, any helper variables or columns you create should be thoughtfully
named.
'''

covid_df.rename(columns = {'Admin2' : 'County'}, inplace = True)
covid_df.set_index('County', inplace = True, drop = False)
# Variable stores index of first date column
date_index_st = 11

#%% viz 1
'''
Create a visualization that shows all of the counties in Utah as a time series,
similar to the one shown in slide 22 during the lecture. The graphic should
-Show cases over time
-Have all counties plotted in a background color (something like grey)
-Have a single county plotted in a contrasting color (something not grey)
-Have well formatted dates as the X axis
'''

# Create Utah df slice
utah_slice = covid_df[covid_df.Province_State == 'Utah']
# Create slice for time series by trimming non-numerical data
utah_slice_ts = utah_slice.iloc[:,date_index_st:]
# Transpose for plotting
utah_slice_ts = utah_slice_ts.T

# Set colors
highlight = 'r'
backcolor = 'grey'
interval = 90
# Set tick labels spaced by interval variable
tick_locations = []
tick_labels = []
for i in range(0, utah_slice_ts.shape[0], interval):
    tick_locations.append(i)
    tick_labels.append(utah_slice_ts.index[i])

# Plot each county in the utah slice, plot in blue for highlighted county
for i in range(utah_slice_ts.shape[1]):
    if utah_slice_ts.columns[i] == 'Bear River':
        plt.plot(utah_slice_ts.iloc[:,i], color= highlight, label = utah_slice_ts.columns[i])
    else:
        plt.plot(utah_slice_ts.iloc[:,i],color = backcolor)
plt.title('Total Cases by County')
plt.xticks(ticks = tick_locations, labels = tick_labels, rotation = 90)
matplotx.line_labels()
plt.tight_layout()
plt.show()

#%% viz 2
'''
Create a visualization that shows the contrast between the county in Utah with
the most cases to date to a county in Florida with the most cases to date.
The graphic should:
-Have only two counties plotted
-Highlight the difference between the two comparison counties
You may use any style of graphic you like as long as it is effective (dense)
and readable
'''

# Create florida slice and transpose
florida_slice = covid_df[covid_df.Province_State == 'Florida']
florida_final = florida_slice.iloc[:,-1]
florida_final = florida_final.T

# Slice final column from existing utah_slice and Transpose
utah_final = utah_slice.iloc[:,-1]
utah_final = utah_final.T
# Initialize variables for storing county name with maximum cases
florida_max =  florida_final.idxmax()
utah_max =  utah_final.idxmax()

# Obtain df slice for rows corresponding to FL and UT counties with the most cases
FL_UT_max = covid_df.loc[covid_df['County'].isin([florida_max, utah_max])]
FL_UT_max = FL_UT_max.iloc[:,date_index_st:]
# Transpose for plotting
FL_UT_max = FL_UT_max.T
# Plot data with a tick at every year transition (plus 1 at start). Tick label = year
plt.plot(FL_UT_max.iloc[:,0], label = 'Miami-Dade')
plt.plot(FL_UT_max.iloc[:,1], label = 'SLC')
matplotx.line_labels()

FL_UT_ticks = ['2020', '2021', '2022', '2023']
plt.xticks([0,342,707,1072], labels = FL_UT_ticks)
plt.title('Miami-Dade vs. Salt Lake County')
plt.tight_layout()
plt.show()

#%% viz 3
'''
Create a visualization that shows BOTH the running total of cases for a single
county AND the daily new cases. The graphic should:
-Use two y-axes (https://matplotlib.org/stable/gallery/subplots_axes_and_figures/two_scales.html)
-Use color to contrast the two series being plotted
-Have well formatted dates as the X axis
'''

# From the utah slice, select row for Salt Lake County
slc_slice = utah_slice.loc[['Salt Lake']]
# slc_slice.rename(columns = {'Admin2':'Salt Lake Cases'})
# Trim non-numerical data
slc_slice_ts = slc_slice.iloc[:,date_index_st:].copy()
# Rename first index to 'Total Cases'
slc_slice_ts.rename(index = {'Salt Lake':'Total Cases'}, inplace = True)
# Add row of 0 values labeled 'Daily Cases'
slc_slice_ts.loc['Daily Cases'] = pd.Series()
slc_slice_ts.iloc[1,0] = 0
# Calculate daily case values from total cases
for i in range(1, len(slc_slice_ts.columns)):
    slc_slice_ts.iloc[1,i] = (slc_slice_ts.iloc[0,i] - slc_slice_ts.iloc[0,i-1])
# Transpose for plotting
slc_slice_ts = slc_slice_ts.T

# Plot on 2 axes
data1 = slc_slice_ts.iloc[:,0]
data2 = slc_slice_ts.iloc[:,1]
fig, ax1 = plt.subplots()
color = 'r'
ax1.set_xlabel('Date')
ax1.set_ylabel('Total Cases', color=color)
ax1.set_ylim(0,500000)
ax1.plot(data1, color=color)
ax1.set_xticks(ticks = tick_locations, labels = tick_labels, rotation = 90)
ax1.tick_params(axis='y', labelcolor=color)

ax2 = ax1.twinx()
color = 'b'
ax2.set_ylabel('Daily Cases', color=color)
ax2.set_ylim(0,20000)
ax2.plot(data2, color=color)
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  # otherwise the right y-label is slightly clipped
plt.title('Salt Lake County Total and Daily Cases')
plt.show()

#%% viz 4
'''
Create a visualization that shows a stacked bar chart of county contributions
to a given state's total cases. You may choose any state (or states).
(https://matplotlib.org/stable/gallery/lines_bars_and_markers/bar_stacked.html#sphx-glr-gallery-lines-bars-and-markers-bar-stacked-py)
The graphic should:
-Have a single column delineate a state
-Have each 'slice' or column compontent represent a county
'''

# Create slice by state and final row
state = 'Wyoming'
state_slice = covid_df.loc[covid_df['Province_State'] == state]
state_final = state_slice.iloc[:,-1].T
state_final = state_final.drop('Unassigned')
state_final = state_final.drop('Out of WY')
state_final = state_final.to_frame()
state_final.rename(columns = {'3/9/23':'Total Cases'}, inplace = True)

# Create stacked bar chart
# Resize chart to 8x8
plt.rcParams["figure.figsize"] = (8,8)
state_final.T.plot.bar(stacked = True, width = .2)
plt.title('Wyoming Total Cases by County')
plt.show()

#%% extra credit (5 points)
'''
Use Seaborn to create a grouped box plot of all reported states. Each boxplot
should be a distinct state. Have the states ordered from most cases (FL) to fewest 
cases. (https://seaborn.pydata.org/examples/grouped_boxplot.html)
'''
