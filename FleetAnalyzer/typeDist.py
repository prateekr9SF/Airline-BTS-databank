import pandas as pd
import matplotlib.pyplot as plt
plt.style.use('seaborn-v0_8-deep')

import matplotlib.ticker as tck
import matplotlib.ticker as ticker

bar_thickness = 0.30

# Reading data from the provided CSV file
df = pd.read_csv('data/Brazil/LATAM_Airlines Brazil_status_12-Nov-2023.csv')

# Sorting the dataframe in descending order based on the 'Total' column
df_sorted = df.sort_values(by='Total', ascending=True)

# Extracting categories (Series) and values for each status from the sorted dataframe
categories = df_sorted['Series']
in_service = df_sorted['In Service']
on_order = df_sorted['On Order']
storage = df_sorted['Storage']

fig1 = plt.figure()
ax1 = fig1.gca()


# Creating the horizontal stacked bar chart
plt.barh(categories, in_service, height=bar_thickness,label='In Service')
plt.barh(categories, on_order, left=in_service,height=bar_thickness, label='On Order')
plt.barh(categories, storage, left=in_service + on_order,height=bar_thickness, label='Storage')

# Plot grid properties
ax1.grid(which='major', color='black', linestyle='-', linewidth='0.05')

for axis in ['top','bottom','left','right']:
  ax1.spines[axis].set_linewidth(1.5)


# Remove frame boxes
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)


# Modify axes ticks properties
plt.xticks(fontname = "Times New Roman", fontsize  = 20)
plt.yticks(fontname = "Times New Roman", fontsize = 20)

ax1.tick_params(bottom=True, top=False, left=True, right=False)
ax1.tick_params(labelbottom=True, labeltop=False, labelleft=True, labelright=False)

F = plt.gcf()
Size = F.get_size_inches()
F.set_size_inches(Size[0]*1.5, Size[1]*1.5, forward=True) # Set forward to True to resize window along with plot in figure.
#F.set_size_inches(Size[0]*3.5, Size[1]*1.5, forward=True) # Set forward to True to resize window along with plot in figure.


# Adding labels, title, and adjusting layout for better visibility
#plt.ylabel('Aircraft Series',fontname ='Times New Roman', fontsize = 22)
plt.xlabel('Number of Aircraft',fontname ='Times New Roman', fontsize = 22)
plt.legend(frameon=True, fontsize = 14)
plt.tight_layout()

plt.rcParams['figure.dpi'] = 300
plt.rcParams['savefig.dpi'] = 300
plt.savefig("LATAM_fleet.jpg")
# Display the plot
plt.show()
