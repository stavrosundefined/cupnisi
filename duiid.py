# Initial values
Y0_1 = 10.0  # Initial value for Y0$1
W0 = 5       # Weight or smoothing factor
y = 12.0     # New value

# Update rule
Y0_1 += (y - Y0_1) / W0

print(Y0_1)  # This will print the updated value of Y0_1
