from sympy import symbols, Eq, sympify, expand

# Step 1: Define symbols
v_1, v_2, v_3 = symbols('v_1 v_2 v_3')

# Step 2: Hard-code the equation as a string
# hardcoded_equation = "3 * v_1 + v_2 - 2 * v_3 = -v_1 - v_2"
hardcoded_equation = "3 * (v_1 + v_2) = -3 * v_1 + -3 * v_1"

# Step 3: Parse the hardcoded equation into a symbolic equation
try:
    # Parse the equation as a single sympy expression
    full_equation = sympify(hardcoded_equation.replace('=', '-(') + ')')

    # Apply distributive property to expand terms
    expanded_equation = expand(full_equation)

    # Simplify the expanded equation by combining terms and moving everything to one side
    simplified_equation = expanded_equation.simplify()

    # Reorganize terms in ascending order of variables (v_1, v_2, v_3)
    ordered_equation = simplified_equation.as_ordered_terms()

    # Combine the ordered terms back into a single expression
    reordered_expression = sum(ordered_equation)

    # Create the sympy Eq object with RHS = 0
    equation = Eq(reordered_expression, 0)

    # Print the reorganized equation
    print(f"Reorganized Equation: {equation}")

except Exception as e:
    print("Error:", e)
