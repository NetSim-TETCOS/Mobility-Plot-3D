import pandas as pd
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Importing 3D axes

# Path of the mobility log file from temp path
log_file_path = 'C:\\Users\\MARK\\AppData\\Local\\Temp\\netsim\\pro_14.1\\log\\Mobility_log.csv'

# Load data from the file, skipping the first row containing column headers
data = pd.read_csv(log_file_path)

# Define device names array (modify as needed)
Device_names = ['Drone 1', 'Drone 2', 'Helicopter', 'Vehicle 1', 'Vehicle 2','Control Center']

device_ids = data['Device Id'].unique()  # Unique device IDs
num_devices = len(device_ids)  # Number of devices

# Create a 3D plot
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Color map for devices
colors = plt.cm.tab10(range(num_devices))

line_width = 1.5

for i, device_id in enumerate(device_ids):
    # Data for a particular device
    device_data = data[data['Device Id'] == device_id]
    x = device_data['Position X(m)'] / 1000  # X coordinates
    y = device_data['Position Y(m)'] / 1000  # Y coordinates
    z = device_data['Position Z(m)']   # Z coordinates

    # Access device name from the defined array
    device_name = Device_names[i]

    # Plotting with legend entry set to device name
    ax.plot(x, y, z, 'o-', linewidth=line_width, color=colors[i], label=device_name)

# Add labels and legend
ax.set_xlabel('X Distance (km)', fontsize=12)
ax.set_ylabel('Y Distance (km)', fontsize=12)
ax.set_zlabel('Z Distance (m)', fontsize=12)
ax.set_title('Vehicle, Drone, and Helicopter Movement Patterns', fontsize=14, fontweight='bold', fontname='Arial')

# Customize ticks
plt.tick_params(axis='both', which='major', labelsize=10)

# Set legend and grid
ax.legend(loc='center left', bbox_to_anchor=(1, 0.5), fontsize=10)  # Move legend to the right outside the plot
ax.grid(True, linestyle='--', alpha=0.7)  # Add grid lines with dashed style and transparency

plt.show()
