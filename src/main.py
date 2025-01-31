# src/main.py

from fractal import generate_mandelbrot, generate_julia, plot_fractal

def main():
    fractal_type = input("Enter fractal type (mandelbrot/julia): ").strip().lower()
    if fractal_type not in ["mandelbrot", "julia"]:
        print("Invalid fractal type. Please enter 'mandelbrot' or 'julia'.")
        return

    iterations = int(input("Enter maximum iterations: ").strip())
    output_file = input("Enter output filename (leave blank to display without saving): ").strip()

    if fractal_type == 'mandelbrot':
        fractal_data = generate_mandelbrot(max_iterations=iterations)
        plot_fractal(fractal_data, filename=output_file if output_file else None)
    else:
        real_part = float(input("Enter real part of c: ").strip())
        imag_part = float(input("Enter imaginary part of c: ").strip())
        c = complex(real_part, imag_part)
        fractal_data = generate_julia(c, max_iterations=iterations)
        plot_fractal(fractal_data, filename=output_file if output_file else None, cmap='magma')

if __name__ == "__main__":
    main()
