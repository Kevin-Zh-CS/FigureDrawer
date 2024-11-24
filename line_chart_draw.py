import matplotlib.pyplot as plt

x = [0.6, 0.7, 0.8, 0.9, 0.95]
y1 = [24.1, 25.8, 27.1, 26.5 , 29.8]
y2 = [30.1, 30.3, 34.4, 31.9 , 37.1]
y3 = [29.7, 29.2, 34.1, 30.2 , 35.5]
y4 = [25.1, 25.7, 28.4, 27.5 , 30.6]
y5 = [23.5, 25.4, 26.8, 26.7 , 29.8]


# Enlarged fonts for axis labels
plt.xlabel('Temperature', fontsize=15)
plt.ylabel(r'ASR$_{\text{Decoding}}$ (%)', fontsize=15)

# Setting the log scale for x-axis
# plt.xscale('log', base=2)
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)
# Adding grid for better readability
plt.grid(linestyle=":", color="gray")

# Plotting data with distinct colors and highlighting "Ours" in red
plt.plot(x, y1, marker='o', markersize=6, linestyle='-', color='red', label='Llama-2-7b-Chat, W16A16')
plt.plot(x, y2, marker='s', markersize=6, linestyle='-', color='orange', label='QAT, W4A4')
plt.plot(x, y3, marker='^', markersize=6, linestyle='-', color='gold', label='QAT, W8A8')
plt.plot(x, y4, marker='x', markersize=6, linestyle='-',  color='deepskyblue', label='SAQ-T, W4A4')
plt.plot(x, y5, marker='D', markersize=6, linestyle='-',  color='dodgerblue',  label='SAQ-T, W8A8')

# Making the legend more prominent with a larger font and a box
plt.legend(loc='upper left', fontsize=10, frameon=True, shadow=True)
plt.rcParams.update({'font.size':10})
# Show plot
plt.show()

plt.savefig('./figs/line_chart_demo.png', dpi=300)