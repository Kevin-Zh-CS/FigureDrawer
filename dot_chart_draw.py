import matplotlib.pyplot as plt

# Sample data
time = [216, 52, 26.3, 14.6, 0.6]
comm = [281, 59.61, 8.58, 0.16, 0.16]
labels = ["$25.4", "$5.44", "$0.86", "$0.36", "$0.05"]

# Markers
markers = ['s', 'v', '>', '*', '*']
colors = ['purple', 'green', 'orange', 'blue', 'red']
names = ["Iron", "BOLT", "BumbleBee", "NEXUS (CPU)", "NEXUS (GPU)"]

# Create plot
plt.figure(figsize=(12, 8))

for i in range(len(time)):
    plt.scatter(time[i], comm[i], marker=markers[i], color=colors[i], s=300 if 'NEXUS' in names[i] else 200, linewidth=1.5)
    plt.text(time[i], comm[i] + 0.25 * comm[i], labels[i], fontsize=12, ha='center', va='bottom', bbox=dict(facecolor='white', alpha=0.5, edgecolor='none'))

# Set x-scale to log
plt.xscale('log', base=2)
plt.yscale('log', base=2)
plt.xlabel('Time (min)', fontsize=14)
plt.ylabel('Comm. (GB)', fontsize=14)

# Create custom legend
legend_elements = [plt.Line2D([0], [0], marker=markers[0], color='w', markerfacecolor=colors[0], markersize=12, label='Iron'),
                   plt.Line2D([0], [0], marker=markers[1], color='w', markerfacecolor=colors[1], markersize=12, label='BOLT'),
                   plt.Line2D([0], [0], marker=markers[2], color='w', markerfacecolor=colors[2], markersize=12, label='BumbleBee'),
                   plt.Line2D([0], [0], marker=markers[3], color='w', markerfacecolor=colors[3], markersize=12, label='NEXUS (CPU)'),
                   plt.Line2D([0], [0], marker=markers[4], color='w', markerfacecolor=colors[4], markersize=12, label='NEXUS (GPU)')]

plt.legend(handles=legend_elements, loc='best', fontsize=10, frameon=True, shadow=True)

# Add grid
plt.grid(True, which='both', linestyle='--', linewidth=0.5)

# Set tick parameters
plt.tick_params(axis='both', which='major', labelsize=14)
plt.tick_params(axis='both', which='minor', labelsize=10)
ax = plt.subplot()
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
# Set tighter layout
plt.tight_layout()

# Show plot
plt.show()
