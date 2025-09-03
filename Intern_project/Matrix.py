import numpy as np

def input_matrix(name="Matrix"):
    rows = int(input(f"Enter number of rows for {name}: "))
    cols = int(input(f"Enter number of columns for {name}: "))
    matrix = []
    print(f"Enter elements row-wise for {name}:")
    for i in range(rows):
        row = []
        for j in range(cols):
            val = int(input(f"Enter element [{i+1}][{j+1}]: "))
            row.append(val)
        matrix.append(row)
    return np.array(matrix)

def main():
    print("===== Matrix Operations Tool =====")
    print("1. Addition of two matrices")
    print("2. Subtraction of two matrices")
    print("3. Multiplication of two matrices")
    print("4. Transpose of a matrix")
    print("5. Determinant of a matrix")
    print("6. Exit")
    
    while 1:
        choice = int(input("\nEnter your choice (1-6): "))

        if choice == 1:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                print("\nResult of Addition:\n", A + B)
            else:
                print("\nError: Matrices must have same dimensions for addition.")

        elif choice == 2:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape == B.shape:
                print("\nResult of Subtraction:\n", A - B)
            else:
                print("\nError: Matrices must have same dimensions for subtraction.")

        elif choice == 3:
            A = input_matrix("Matrix A")
            B = input_matrix("Matrix B")
            if A.shape[1] == B.shape[0]:
                print("\nResult of Multiplication:\n", np.dot(A, B))
            else:
                print("\nError: Columns of A must equal rows of B for multiplication.")

        elif choice == 4:
            A = input_matrix("Matrix")
            print("\nTranspose of Matrix:\n", A.T)

        elif choice == 5:
            A = input_matrix("Square Matrix")
            if A.shape[0] == A.shape[1]:
                print("\nDeterminant of Matrix:", round(np.linalg.det(A), 2))
            else:
                print("\nError: Determinant can only be calculated for square matrices.")

        elif choice == 6:
            print("Thank you for using the Matrix Operations Tool.")
            break

        else:
            print("Invalid choice! Please select between 1-6.")


main()
