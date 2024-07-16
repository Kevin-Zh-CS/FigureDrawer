import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Sample correlation data (replace this with your actual data)
data = np.array([
    [1.00, 0.26, 0.05, 0.21, -0.72, -0.14, 0.13, 0.46],
    [0.26, 1.00, 0.44, 0.03, 0.10, 0.17, 0.30, 0.07],
    [0.05, 0.44, 1.00, -0.08, 0.12, 0.33, 0.38, 0.03],
    [0.21, 0.03, -0.08, 1.00, -0.24, 0.04, 0.32, 0.33],
    [-0.72, 0.10, 0.12, -0.24, 1.00, 0.27, -0.09, -0.54],
    [-0.14, 0.17, 0.33, 0.04, 0.27, 1.00, 0.26, -0.03],
    [0.13, 0.30, 0.38, 0.32, -0.09, 0.26, 1.00, 0.41],
    [0.46, 0.07, 0.03, 0.33, -0.54, -0.03, 0.41, 1.00]
])

# Labels for the heatmap
labels = ['int.rate', 'installment', 'log.annual.inc', 'dti', 'fico', 'days.with.cr.line', 'revol.bal', 'revol.util']

# Create the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(data, annot=True, xticklabels=labels, yticklabels=labels, cmap='viridis', center=0)
plt.xticks(fontsize=15)
plt.yticks(fontsize=15)
# Display the heatmap
plt.show()