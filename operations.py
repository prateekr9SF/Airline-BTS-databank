# A helper script to post-process BTS Form 41 Traffic data

import pandas as pd
import numpy as np
import matplotlib.ticker as tck
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
from metrics import *
import airportsdata
import cartopy.crs as ccrs
import cartopy.feature as cfeature

#plt.style.use('seaborn-v0_8-dark-palette')
plt.style.use('seaborn-v0_8-deep')



#------------------------ AIRLINE CODES --------------------------#
AA = 19805 # American
AS = 19930 # Alaska Airlines
B6 = 20409 # Jet blue
DL = 19790 # Delta
HA = 19690 # Hawaiian
NK = 20416 # Spirit
UA = 19977 # United
WN = 19393 # Southwest
#------------------------ AIRLINE CODES --------------------------#

df15 = pd.read_csv("Data/2015/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df16 = pd.read_csv("Data/2016/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df17 = pd.read_csv("Data/2017/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df18 = pd.read_csv("Data/2018/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df19 = pd.read_csv("Data/2019/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")
df20 = pd.read_csv("Data/2020/Ops/T_T100D_SEGMENT_ALL_CARRIER.csv")



def eval_rpm_asm(TRG_AIRLINE, data_frames):
    results = []

    for df in data_frames:
        df_filtered = df[(df['AIRLINE_ID'] == TRG_AIRLINE) & (df['DISTANCE'] != 0) & (df['AIR_TIME'] != 0)].copy()
        df_filtered['ASM_Segment'] = df_filtered['DISTANCE'] * df_filtered['SEATS']
        df_filtered['RPM_Segment'] = df_filtered['DISTANCE'] * df_filtered['PASSENGERS']
        
        # Calculate the total ASM and RPM
        total_asm = df_filtered['ASM_Segment'].sum()
        total_rpm = df_filtered['RPM_Segment'].sum()
        
        # Append the results to the list
        results.append([total_asm, total_rpm])

    # Convert the list of results into a numpy array
    return np.array(results)
#end

def routeRPM(TRG_AIRLINE, df):

    df_filtered = df[(df['AIRLINE_ID'] == TRG_AIRLINE) & (df['DISTANCE'] != 0) & (df['AIR_TIME'] != 0)].copy()


    df_filtered['ASM_Segment'] = df_filtered['DISTANCE'] * df_filtered['SEATS']
    df_filtered['RPM_Segment'] = df_filtered['DISTANCE'] * df_filtered['PASSENGERS']

    # Group data by 'ORIGIN'
    df_grouped = df_filtered.groupby('ORIGIN')

    # Load airports data
    airports = airportsdata.load('IATA')

    # Create a figure with PlateCarree projection
    fig = plt.figure(figsize=(15, 10))
    ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())

    # Add geographical features
    ax.add_feature(cfeature.COASTLINE)
    ax.add_feature(cfeature.BORDERS)
    ax.add_feature(cfeature.OCEAN)
    ax.add_feature(cfeature.LAKES, alpha=0.5)
    ax.add_feature(cfeature.RIVERS)

    # Set extent to cover the CONUS area
    ax.set_extent([-125, -66.5, 24, 49], crs=ccrs.PlateCarree())

    # Loop through each flight
    for index, row in df_filtered.iterrows():
        origin = row['ORIGIN']
        destination = row['DEST']


        # Retrieve coordinates for the origin and destination
        if origin in airports and destination in airports:
    
            orig_coords = airports[origin]
            dest_coords = airports[destination]
            orig_lat, orig_lon = orig_coords['lat'], orig_coords['lon']
            dest_lat, dest_lon = dest_coords['lat'], dest_coords['lon']


            # Plot the great circle route
            ax.plot([orig_lon, dest_lon], [orig_lat, dest_lat],
                    color='k', linewidth=1, marker='o',
                    transform=ccrs.Geodetic())
    plt.show()




#end


data_frames = [df15, df16, df17, df18, df19, df20]

# Get data for FSCs

#Totals_array format: (6,2) -> (asm, rpm)
AA_metrics = eval_rpm_asm(AA, data_frames)
DL_metrics = eval_rpm_asm(DL, data_frames)
UA_metrics = eval_rpm_asm(UA, data_frames)


years = ['2015', '2016', '2017', '2018', '2019', '2020']

# Call the function with the metrics and the years as the labels
#plot_asm_FSC(AA_metrics, UA_metrics, DL_metrics, years)

# Call the function with the metrics and the years as the labels
#plot_rsm_FSC(AA_metrics, UA_metrics, DL_metrics, years)


routeRPM(DL, df15)

