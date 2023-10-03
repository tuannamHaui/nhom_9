import numpy as np
from sympy import symbols, Eq, solve, Matrix
import tkinter as tk
from tkinter import messagebox

# Define your linear algebra functions here

# Create a function to handle button click
def calculate_button_click():
    # Get the matrix A and vector b from user input or other sources
    A = np.array([[2, 1], [1, -1]])
    b = np.array([3, 1])

    # Perform the calculations using your functions
    solution = solve_linear_equation(A, b)
    A_inverse = calculate_inverse_matrix(A)
    eigenvals, eigenvects = calculate_eigen(A)
    determinant = calculate_determinant(A)
    nullspace, columnspace = calculate_basis_column_space(A)

    # Display the results using message boxes
    messagebox.showinfo("Solution", f"Nghiệm của hệ phương trình:\n{solution}")
    messagebox.showinfo("Inverse Matrix", f"Ma trận nghịch đảo:\n{A_inverse}")
    messagebox.showinfo("Eigenvalues", f"Giá trị riêng:\n{eigenvals}")
    messagebox.showinfo("Eigenvectors", f"Vector riêng:\n{eigenvects}")
    messagebox.showinfo("Determinant", f"Định thức của ma trận:\n{determinant}")
    messagebox.showinfo("Nullspace", f"Cơ sở không gian cột:\n{nullspace}")
    messagebox.showinfo("Columnspace", f"Không gian cột:\n{columnspace}")

# Create the main GUI window
root = tk.Tk()
root.title("Linear Algebra Calculator")

# Add a button to trigger the calculations
calculate_button = tk.Button(root, text="Calculate", command=calculate_button_click)
calculate_button.pack()

# Run the GUI main loop
root.mainloop()





