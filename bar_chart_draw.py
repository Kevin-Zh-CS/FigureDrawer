import matplotlib.pyplot as plt
import numpy as np


categories = ['LAN', r'WAN$^1$', r'WAN$^2$', r'WAN$^3$', r'WAN$^4$']
iron = [475, 6453, 6845, 12759, 12996]
bolt = [185, 1563, 1949, 2855, 3139]
bumblebee = [204, 971, 1257, 1322, 1578]
nexus = [857, 869, 869, 881, 881]


x = np.arange(len(categories))  # the label locations
width = 0.2  # the width of the bars

fig, ax = plt.subplots(figsize=(10, 6))

# Plotting
rects1 = ax.bar(x - 1.5 * width, iron, width, label='Iron', color='tab:blue')
rects2 = ax.bar(x - 0.5 * width, bolt, width, label='BOLT', color='tab:orange')
rects3 = ax.bar(x + 0.5 * width, bumblebee, width, label='BumbleBee', color='tab:green')
rects4 = ax.bar(x + 1.5 * width, nexus, width, label='NEXUS', color='tab:red')

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Comm (GB)', fontsize=24)
ax.set_xticks(x)
plt.yticks(fontsize=19)
ax.set_xticklabels(categories, fontsize=24)

# Function to attach a text label above each bar in *rects*, displaying its height.
def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        ax.annotate(f'{height}',
                    xy=(rect.get_x() + rect.get_width() / 2, height),
                    xytext=(0, 3),  # 3 points vertical offset
                    textcoords="offset points",
                    ha='center', va='bottom', rotation=70, fontsize=19)

autolabel(rects1)
autolabel(rects2)
autolabel(rects3)
autolabel(rects4)

plt.legend(loc='upper left', fontsize='20', frameon=True, shadow=True)
fig.tight_layout()
# Remove the plot border while keeping the axes
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['bottom'].set_visible(True)
ax.spines['left'].set_visible(True)
ax.yaxis.grid(True, linestyle='--', which='major', color='grey', alpha=0.7)
plt.show()

plt.savefig('./figs/bar_chart_demo.png', dpi=300)