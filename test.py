from sympy import symbols, Eq, sympify, expand, collect

# Step 1: Define symbols (THESE WILL LATER BE MANUALLY INPUTTED THROUGH A ...
# TEXTBOX (EXCEPT FOR THE V VALUES))
v_1, v_2, v_3, v_4, Gy, Gs, Gz, IB = symbols('v_1 v_2 v_3 v_4 Gy Gs Gz IB')

# Step 2: Hard-code the equation as a string (DO NOT REMOVE THESE COMMENTED TEST CASES)
# hardcoded_equation = "0.25 * Gs * (v_3 - 0) + Gy * (v_1 - v_3) + Gz * (v_1 - v_4) = 4"
# hardcoded_equation = "3 * v_1 + v_2 - 2 * v_3 = -v_1 - v_2"
hardcoded_equation = "v_3 - 0 = 0.75*(v_4 - v_3) + IB"
# hardcoded_equation = "-0.25 * Gs * (v_3 - 0) + Gy * (v_2 - v_3) = -4"

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

    # Collect terms by variables (v_1, v_2, v_3, v_4)
    grouped_equation = collect(simplified_equation, [v_1, v_2, v_3, v_4])

    # Print the grouped and simplified equation
    print(f"Grouped Equation: {grouped_equation}")

    # Substitute values for Gy, Gs, Gz
    variable_values = {Gy: 3, Gs: 2, Gz: -1, IB: 69}  # Example values
    substituted_equation = grouped_equation.subs(variable_values)

    # Print the substituted equation (EVERYTHING IS ON THE LEFT SIDE BTW)
    print(f"Substituted Equation: {substituted_equation}")

except Exception as e:
    print("Error:", e)
