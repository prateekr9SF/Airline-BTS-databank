import pandas as pd



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

TRG_AIRLINE = DL

df15 = pd.read_csv("2015/T_T100D_SEGMENT_ALL_CARRIER.csv")
df16 = pd.read_csv("2016/T_T100D_SEGMENT_ALL_CARRIER.csv")
df17 = pd.read_csv("2017/T_T100D_SEGMENT_ALL_CARRIER.csv")
df18 = pd.read_csv("2018/T_T100D_SEGMENT_ALL_CARRIER.csv")
df19 = pd.read_csv("2019/T_T100D_SEGMENT_ALL_CARRIER.csv")
df20 = pd.read_csv("2020/T_T100D_SEGMENT_ALL_CARRIER.csv")

# Filter data for target airline with non-zero distance and air time
df15_F = df15[(df1['AIRLINE_ID'] == TRG_AIRLINE) & ((df15['DISTANCE'] != 0)) & ((df15['AIR_TIME'] != 0))]



# Write the filtered DataFrame to a CSV file
#df1_Filt.to_csv("filtered_airline_data.csv", index=False)




