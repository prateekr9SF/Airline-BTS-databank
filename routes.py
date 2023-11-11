import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Create a figure with an Orthographic projection
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.Orthographic(-100, 40))

# Set extent to cover the CONUS area
ax.set_extent([-125, -66.5, 24, 49], crs=ccrs.PlateCarree())

# Add state boundaries to the map from the Natural Earth dataset
states_provinces = cfeature.NaturalEarthFeature(
    category='cultural',
    name='admin_1_states_provinces_lines',
    scale='50m',
    facecolor='none'
)

ax.add_feature(states_provinces, edgecolor='black')
ax.add_feature(cfeature.BORDERS)
ax.add_feature(cfeature.COASTLINE)

# Remove default gridlines and labels
#ax.gridlines(draw_labels=False)

# Instead of adding an ocean feature, we just fill the land to make the states and coastlines stand out.
ax.add_feature(cfeature.LAND, facecolor='white')
ax.add_feature(cfeature.LAKES, facecolor='azure', edgecolor='black')

plt.tight_layout()
plt.show()

