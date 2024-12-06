# import numpy as np
# from scipy.fft import fft

# a = -1  # Lower bound
# b = 1   # Upper bound

# t = np.linspace(a, b, 1000)  # Adjust sample size as needed
# def f(t):
#   return 1 - t ** 2

# # Compute the Fourier transform using the FFT algorithm
# F_t = fft(f(t)) * (b - a) / np.sqrt(2 * np.pi)  # Scaling factor for proper normalization

# print(F_t)

# import numpy as np
# from scipy.integrate import quad

# # Define the function to be integrated
# def integrand(t, omega):
#     return np.exp(-t) * np.exp(-1j * omega * t)

# # Define the Fourier transform function
# def fourier_transform(omega):
#     # Integration limits
#     lower_limit = 0
#     upper_limit = 1000  # Choose a large upper limit

#     # Perform numerical integration
#     integral_result, _ = quad(integrand, lower_limit, upper_limit, args=(omega,))

#     return integral_result

# # Compute the Fourier transform for a given omega
# omega_value = 1.0  # Example value for omega
# result = fourier_transform(omega_value)
# print("Fourier Transform of exp(-t) at omega =", omega_value, ":", result)


# Process or plot the Fourier transform (F_t) as needed

# from sympy import symbols, integrate

# # Define variables
# x = symbols('x')

# # Define the integrand (function to be integrated)
# f = x**2

# # Define the definite integral
# definite_integral = integrate(f, (x, 1, 4))  # Integrate f from x=1 to x=4

# # Define the indefinite integral
# indefinite_integral = integrate(f)

# # Print the results
# print("Definite integral:", definite_integral)
# print("Indefinite integral:", indefinite_integral)

import sympy as sp
import numpy as np
from scipy.integrate import quad

# Define symbols
t, omega = sp.symbols('t omega')

# Define the function to be integrated
def f(t):
    return 4 * sp.exp(-t) * (t * sp.cosh(t) - sp.sinh(t)) / t**3

# Create a numerical function from the symbolic expression
f_numeric = sp.lambdify(t, f(t), modules='numpy')

# Numerical FT using SciPy's quad for definite integral (handles infinite bound)
def numerical_FT(f, a, b, omega_val):
    """Computes the numerical FT of f(t) over [a, b] using SciPy."""
    
    # Define the integrand
    def integrand(t):
        return f(t) * np.exp(-1j * omega_val * t)
    
    # Perform numerical integration and cast the result to complex
    FT_value, _ = quad(integrand, a, b)
    return complex(FT_value)

# Integrate over a large but finite range
a = 0
b = 100
omega_value = 1.0  # Example value for omega
numerical_FT_result = numerical_FT(f_numeric, a, b, omega_value)
print("Numerical FT (approximate):", numerical_FT_result)
