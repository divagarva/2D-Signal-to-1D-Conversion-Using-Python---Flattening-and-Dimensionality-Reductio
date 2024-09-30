import numpy as np
import matplotlib.pyplot as plt

# Generate a 2D signal (for example, a 2D sine wave or image-like structure)
rows, cols = 50, 50
x = np.linspace(0, 4 * np.pi, rows)
y = np.linspace(0, 4 * np.pi, cols)
X, Y = np.meshgrid(x, y)

# 2D Signal - Sinusoidal Wave Pattern
signal_2d = np.sin(X) * np.cos(Y)

# Convert the 2D signal to a 1D signal by flattening
signal_1d = signal_2d.flatten()

# Plot the original 2D signal
plt.figure(figsize=(8, 6))
plt.subplot(2, 1, 1)
plt.imshow(signal_2d, cmap='jet', aspect='auto')
plt.title('Original 2D Signal')
plt.colorbar()

# Plot the flattened 1D signal
plt.subplot(2, 1, 2)
plt.plot(signal_1d)
plt.title('Flattened 1D Signal from 2D Signal')
plt.tight_layout()
plt.show()
