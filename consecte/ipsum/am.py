import matplotlib.pyplot as plt

# Example data
x = [2, 4, 6, 6, 9, 2, 7, 2, 6, 1, 8, 4, 5, 9, 1, 2, 3, 7, 5, 8, 1, 3]
y = [7, 8, 2, 4, 6, 4, 9, 5, 9, 3, 6, 7, 2, 4, 6, 7, 1, 9, 4, 3, 6, 9]

# Creating the scatter plot with adjusted marker border width and color
plt.scatter(x, y, s=100, alpha=0.6, c='blue', edgecolor='black', linewidth=1)
plt.tight_layout()
plt.show()
