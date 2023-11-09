# A helper script to post-process BTS Form 41 Traffic data

import pandas as pd
import numpy as np
import matplotlib.ticker as tck
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt
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

df15 = pd.read_csv("2015/T_T100D_SEGMENT_ALL_CARRIER.csv")
df16 = pd.read_csv("2016/T_T100D_SEGMENT_ALL_CARRIER.csv")
df17 = pd.read_csv("2017/T_T100D_SEGMENT_ALL_CARRIER.csv")
df18 = pd.read_csv("2018/T_T100D_SEGMENT_ALL_CARRIER.csv")
df19 = pd.read_csv("2019/T_T100D_SEGMENT_ALL_CARRIER.csv")
df20 = pd.read_csv("2020/T_T100D_SEGMENT_ALL_CARRIER.csv")

  
def  plot_asm_FSC(AA_metrics, UA_metrics, DL_metrics, labels):
    # Number of groups
    n_groups = AA_metrics.shape[0]
    
    # Create the figure and the axes
    fig = plt.figure()
    ax1 = fig.gca()

    # Set the position of bar on X axis
    index = np.arange(n_groups)
    bar_width = 0.25
    
    # Factor for better data representation
    Factor = 10**(-11)

    # Plot ASM
    plt.bar(index, AA_metrics[:, 0]* Factor, bar_width, label='American Airlines ASM', alpha=0.9, edgecolor= 'black')
    plt.bar(index + bar_width, UA_metrics[:, 0]* Factor, bar_width, label='United Airlines ASM', alpha=0.9,edgecolor= 'black')
    plt.bar(index + bar_width * 2, DL_metrics[:, 0]* Factor, bar_width, label='Delta Airlines ASM', alpha=0.9,edgecolor= 'black')
    
    # Adding Xticks
    plt.xlabel('Year', fontname ='Times New Roman', fontsize = 22)
    plt.ylabel(r'ASM (Available Seat Miles) $\times 10^{11} $', fontname ='Times New Roman', fontsize = 22)
    plt.xticks(index + bar_width, labels)
    
    # Add a legend
    handles, labels = [], []
    for ax in fig.axes:
        for h, l in zip(*ax.get_legend_handles_labels()):
            handles.append(h)
            labels.append(l)

    for axis in ['top','bottom','left','right']:
        ax1.spines[axis].set_linewidth(1.5)

    # Modify axes ticks properties
    plt.xticks(fontname = "Times New Roman", fontsize  = 20)
    plt.yticks(fontname = "Times New Roman", fontsize = 20)

    ax1.tick_params(bottom=True, top=True, left=True, right=True)
    ax1.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False)

    # Plot grid properties
    ax1.grid(which='major', color='black', linestyle='-', linewidth='0.01')


    F = plt.gcf()
    Size = F.get_size_inches()
    F.set_size_inches(Size[0]*1.5, Size[1]*1.5, forward=True) # Set forward to True to resize window along with plot in figure.
    
    # ASM legend
    plt.legend(handles[:3], labels[:3], loc='upper right')  


    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300

    # Show the plot
    #plt.title('ASM metrics for FSC per Year')
    plt.tight_layout()
    plt.savefig('FSC_ASM.jpg')
    plt.show()


def  plot_rsm_FSC(AA_metrics, UA_metrics, DL_metrics, labels):
    # Number of groups
    n_groups = AA_metrics.shape[0]
    
    # Create the figure and the axes
    fig2 = plt.figure()
    ax2 = fig2.gca()

    # Set the position of bar on X axis
    index = np.arange(n_groups)
    bar_width = 0.25
    
    # Factor for better data representation
    Factor = 10**(-11)

    # Plot RSM
    plt.bar(index, AA_metrics[:, 1]* Factor, bar_width, label='American Airlines RSM', alpha=0.9, edgecolor= 'black')
    plt.bar(index + bar_width, UA_metrics[:, 1]* Factor, bar_width, label='United Airlines RSM', alpha=0.9,edgecolor= 'black')
    plt.bar(index + bar_width * 2, DL_metrics[:, 1]* Factor, bar_width, label='Delta Airlines RSM', alpha=0.9,edgecolor= 'black')
    
    # Adding Xticks
    plt.xlabel('Year', fontname ='Times New Roman', fontsize = 22)
    plt.ylabel(r'RSM (Revenue Seat Miles) $\times 10^{11} $', fontname ='Times New Roman', fontsize = 22)
    plt.xticks(index + bar_width, labels)
    
    # Add a legend
    handles, labels = [], []
    for ax in fig2.axes:
        for h, l in zip(*ax.get_legend_handles_labels()):
            handles.append(h)
            labels.append(l)

    for axis in ['top','bottom','left','right']:
        ax2.spines[axis].set_linewidth(1.5)

    # Modify axes ticks properties
    plt.xticks(fontname = "Times New Roman", fontsize  = 20)
    plt.yticks(fontname = "Times New Roman", fontsize = 20)

    ax2.tick_params(bottom=True, top=True, left=True, right=True)
    ax2.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False)

    # Plot grid properties
    ax2.grid(which='major', color='black', linestyle='-', linewidth='0.01')


    F = plt.gcf()
    Size = F.get_size_inches()
    F.set_size_inches(Size[0]*1.5, Size[1]*1.5, forward=True) # Set forward to True to resize window along with plot in figure.
    
    # ASM legend
    plt.legend(handles[:3], labels[:3], loc='upper right')  


    plt.rcParams['figure.dpi'] = 300
    plt.rcParams['savefig.dpi'] = 300

    # Set limits
    ax2.set_ylim([0,1.6])

    # Show the plot
    #plt.title('ASM metrics for FSC per Year')
    plt.tight_layout()
    plt.savefig('FSC_RSM.jpg')
    plt.show()




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



data_frames = [df15, df16, df17, df18, df19, df20]

# Get data for FSCs

#Totals_array format: (6,2) -> (asm, rpm)
AA_metrics = eval_rpm_asm(AA, data_frames)
DL_metrics = eval_rpm_asm(DL, data_frames)
UA_metrics = eval_rpm_asm(UA, data_frames)


# Years you have data for
years = ['2015', '2016', '2017', '2018', '2019', '2020']

# Call the function with the metrics and the years as the labels
#plot_asm_FSC(AA_metrics, UA_metrics, DL_metrics, years)

# Call the function with the metrics and the years as the labels
plot_rsm_FSC(AA_metrics, UA_metrics, DL_metrics, years)

