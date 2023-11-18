import pandas as pd
import numpy as np
import matplotlib.ticker as tck
import matplotlib.ticker as ticker
import matplotlib.pyplot as plt

plt.style.use('seaborn-v0_8-deep')

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
    plt.savefig('Plots/FSC_ASM.jpg')
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
    plt.savefig('Plots/FSC_RSM.jpg')
    plt.show()

