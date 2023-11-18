# This script computes metrics for years 09-19 for all FSC and ULCC

import pandas as pd
import numpy as np
import matplotlib.ticker as tck
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
import airportsdata
import matplotlib.cm as cm
import cartopy.crs as ccrs
import cartopy.feature as cfeature
import matplotlib.colors as mcolors
from matplotlib.cm import ScalarMappable

#plt.style.use('seaborn-v0_8-dark-palette')
plt.style.use('seaborn-v0_8-deep')

#------------------------ AIRLINE CODES --------------------------#
#---- FSC ----#
AA = 19805 # American
AS = 19930 # Alaska Airlines
DL = 19790 # Delta
UA = 19977 # United
HA = 19690 # Hawaiian

#---- LCC ----#
NK = 20416 # Spirit
B6 = 20409 # Jet blue
WN = 19393 # Southwest
F9 = 20436 # Fontier


df0 = pd.read_csv("Data/2005/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df1 = pd.read_csv("Data/2009/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df2 = pd.read_csv("Data/2010/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df3 = pd.read_csv("Data/2011/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df4 = pd.read_csv("Data/2012/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df5 = pd.read_csv("Data/2013/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df6 = pd.read_csv("Data/2014/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df7 = pd.read_csv("Data/2015/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df8 = pd.read_csv("Data/2016/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df9 = pd.read_csv("Data/2017/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df10 = pd.read_csv("Data/2018/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df11 = pd.read_csv("Data/2019/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df12 = pd.read_csv("Data/2020/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df13 = pd.read_csv("Data/2021/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df14 = pd.read_csv("Data/2022/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")

def eval_rpm_ULCC(ULCC, dataFrames):
    all_results = []

    # Initialize the total RPM
    for df in dataFrames:
        results = []
        for ulcc in ULCC:

            df_filtered = df[(df['AIRLINE_ID'] == ulcc) & (df['DISTANCE'] != 0) & (df['PASSENGERS'] != 0) & (df['AIR_TIME'] != 0)].copy()
            
            df_filtered['RPM_Segment'] = df_filtered['DISTANCE'] * df_filtered['PASSENGERS']


            # Calculate the total RSM for this specific ULCC
            rpm_sum = df_filtered['RPM_Segment'].sum()
            results.append(rpm_sum)

        RPM_sum = sum(results)    
        all_results.append(RPM_sum)    

    return np.array(all_results)

data_frames = [df1, df2, df3, df4, df5, df6, df7, df8, df9, df10, df11, df12, df13, df14]

#data_frames = [df1, df14]

# Year 2009-2019
#data_frames = [df1, df11]

ULCC = [NK, B6, WN, F9]


RPM = eval_rpm_ULCC(ULCC, data_frames)


print(RPM)
print(RPM.shape)

delta_RPM = ((RPM[-1] - RPM[0])/(RPM[0]) ) * 100

print("Increase:",delta_RPM )