from sympy import symbols, Eq, sympify

# Step 1: Define symbols
x_1, x_2, x_3 = symbols('x_1 x_2 x_3')

# Step 2: Hard-code the equation as a string
hardcoded_equation = "x_1 + x_2 - 2 * x_3 = -x_1"

# Step 3: Parse the hardcoded equation into a symbolic equation
try:
    # Parse the equation as a single sympy expression
    full_equation = sympify(hardcoded_equation.replace('=', '-(') + ')')

    # Simplify the full equation by combining terms and moving everything to one side
    simplified_equation = full_equation.simplify()

    # Reorganize terms in ascending order of variables (x_1, x_2, x_3)
    ordered_equation = simplified_equation.as_ordered_terms()

    # Combine the ordered terms back into a single expression
    reordered_expression = sum(ordered_equation)

    # Create the sympy Eq object with RHS = 0
    equation = Eq(reordered_expression, 0)

    # Print the reorganized equation
    print(f"Reorganized Equation: {equation}")

except Exception as e:
    print("Error:", e)
