import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# The correct file has been uploaded. Let's read the data from the Excel file this time.
excel_file_path = 'data/Brazil/Age/LATAM_Airlines Brazil_age_12-Nov-2023.xlsx'
data = pd.read_excel(excel_file_path)

# Now let's plot the data as before
plt.figure(figsize=(10, 6))

# Plotting the 'Mean' age as a scatter plot
# We'll use 'Series' for y-axis and 'Mean' for x-axis
sns.scatterplot(data=data, x='Mean', y='Series', color='skyblue', s=100)

# Drawing error bars for the range from 'Youngest' to 'Oldest'
# The error bar will be centered at 'Mean' and will extend from 'Mean' - 'Youngest' to 'Oldest' - 'Mean'
for index, row in data.iterrows():
    plt.errorbar(x=row['Mean'], y=row['Series'], xerr=[[row['Mean'] - row['Youngest']], [row['Oldest'] - row['Mean']]],
                 fmt='none', color='black', capsize=5)

# Adding the 'Median' as a scatter plot
sns.scatterplot(data=data, x='Median', y='Series', color='red', s=100, marker='X')

plt.title('Aircraft Age')
plt.xlabel('Age')
plt.ylabel('Series')

# Show the plot
plt.show()