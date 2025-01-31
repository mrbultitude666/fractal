# src/fractal.py

import numpy as np
import matplotlib.pyplot as plt

def generate_mandelbrot(width=800, height=800, max_iterations=100):
    real = np.linspace(-2, 1, width)
    imag = np.linspace(-1.5, 1.5, height)
    real, imag = np.meshgrid(real, imag)
    c = real + 1j * imag
    z = np.zeros(c.shape, dtype=np.complex128)
    mask = np.full(c.shape, True, dtype=bool)
    output = np.zeros(c.shape, dtype=int)

    for i in range(max_iterations):
        z[mask] = z[mask]**2 + c[mask]
        mask = (np.abs(z) <= 2)
        output += mask

    return output

def plot_fractal(data, filename=None, cmap='inferno'):
    plt.figure(figsize=(10, 10))
    plt.imshow(data, cmap=cmap, extent=(-2, 1, -1.5, 1.5))
    plt.axis('off')
    plt.tight_layout()
    if filename:
        plt.savefig(filename, dpi=300, bbox_inches='tight', pad_inches=0)
    else:
        plt.show()
    plt.close()

def generate_julia(c, width=800, height=800, max_iterations=100):
    real = np.linspace(-1.5, 1.5, width)
    imag = np.linspace(-1.5, 1.5, height)
    real, imag = np.meshgrid(real, imag)
    z = real + 1j * imag
    output = np.zeros(z.shape, dtype=int)

    for i in range(max_iterations):
        mask = np.abs(z) <= 2
        z[mask] = z[mask]**2 + c
        output += mask

    return output