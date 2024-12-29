from sympy import symbols, Eq, sympify, expand, collect

# Step 1: Define symbols
v1, v2, v3, v4, Gy, Gs, Gz, IB = symbols('v1 v2 v3 v4 Gy Gs Gz IB')

# Step 2: Hard-code the equation as a string (DO NOT REMOVE THESE COMMENTED TEST CASES)
# hardcoded_equation = "0.25 * Gs * (v3 - 0) + Gy * (v1 - v3) + Gz * (v1 - v4) = 4"
# hardcoded_equation = "3 * v1 + v2 - 2 * v3 = -v1 - v2"
# hardcoded_equation = "v3 - 0 = 0.75*(v4 - v3) + IB"
# hardcoded_equation = "-0.25 * Gs * (v3 - 0) + Gy * (v2 - v3) = -IB"

# Step 3: Parse the hardcoded equation into a symbolic equation
try:
    # Split the equation into left-hand side (LHS) and right-hand side (RHS)
    lhs, rhs = hardcoded_equation.split('=')

    # Parse both sides as sympy expressions
    lhs_expr = expand(sympify(lhs.strip()))
    rhs_expr = expand(sympify(rhs.strip()))

    # Create the sympy Eq object
    equation = Eq(lhs_expr, rhs_expr)

    # Simplify the expanded equation by combining terms
    simplified_equation = equation.lhs - equation.rhs

    # Collect terms by variables (v1, v2, v3, v4)
    grouped_equation = collect(simplified_equation, [v1, v2, v3, v4])

    # Print the grouped and simplified equation
    print(f"Grouped Equation: {grouped_equation}")

    # Substitute values for Gy, Gs, Gz
    variable_values = {Gy: 3, Gs: 2, Gz: -1, IB: 69}  # Example values
    substituted_equation = grouped_equation.subs(variable_values)

    # Separate constants and move them to the right-hand side
    constant_terms = sum(term for term in substituted_equation.args if term.is_number)
    left_side = substituted_equation - constant_terms
    right_side = -constant_terms

    # Print the left and right sides
    print(f"Left Side: {left_side}")
    print(f"Right Side: {right_side}")

except Exception as e:
    print("Error:", e)
