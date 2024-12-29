from sympy import symbols, Eq, sympify, expand

# Step 1: Define symbols
v_1, v_2, v_3, v_4, Gy, Gs, Gz = symbols('v_1 v_2 v_3 v_4 Gy Gs Gz')

# Step 2: Hard-code the equation as a string (TEST CASES)

# hardcoded_equation = "3 * v_1 + v_2 - 2 * v_3 = -v_1 - v_2"
# hardcoded_equation = "0.25 * Gs * (v_3 - 0) + Gy * (v_1 - v_3) + Gz * (v_1 - v_4) = 4"
hardcoded_equation = "-0.25 * Gs * (v_3 - 0) + Gy * (v_2 - v_3) + 4 = 0"

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

    # Define a sort key to prioritize variables explicitly (v_1 first, then v_2, v_3, v_4)
    def sort_key(term):
        variables = [v_1, v_2, v_3, v_4]
        for i, var in enumerate(variables):
            if term.has(var):
                return i  # Return the index of the variable in the priority list
        return len(variables)  # Non-v terms go to the end

    # Reorganize terms by sorting explicitly
    ordered_equation = sorted(simplified_equation.as_ordered_terms(), key=sort_key)

    print(f"Reorganized Equation: {ordered_equation}")

except Exception as e:
    print("Error:", e)
