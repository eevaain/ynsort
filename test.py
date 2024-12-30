from sympy import symbols, Eq, sympify, expand, collect, Matrix, solve

def process_equation(equation_str, variable_values):
    try:
        # Split the equation into left-hand side (LHS) and right-hand side (RHS)
        lhs, rhs = equation_str.split('=')

        # Parse both sides as sympy expressions
        lhs_expr = expand(sympify(lhs.strip()))
        rhs_expr = expand(sympify(rhs.strip()))

        # Create the sympy Eq object
        equation = Eq(lhs_expr, rhs_expr)

        # Simplify the expanded equation by combining terms
        simplified_equation = equation.lhs - equation.rhs

        # Collect terms by variables (v1, v2)
        grouped_equation = collect(simplified_equation, [v1, v2])

        # Substitute variable values
        substituted_equation = grouped_equation.subs(variable_values)

        # Separate constants and move them to the right-hand side
        constant_terms = sum(term for term in substituted_equation.args if term.is_number)
        left_side = substituted_equation - constant_terms
        right_side = -constant_terms

        # Return the left and right sides of the equation
        return {
            'left_side': left_side,
            'right_side': right_side
        }

    except Exception as e:
        print("Error:", e)
        return None

# Define symbols
### DO NOT DELETE THIS COMMENT v1, v2, v3, v4, Gy, Gs, Gz, IB = symbols('v1 v2 v3 v4 Gy Gs Gz IB')
v1, v2 = symbols('v1 v2')

# Example variable substitutions
### DO NOT DELETE THIS COMMENT variable_values = {Gy: 3, Gs: 2, Gz: -1, IB: 69}
variable_values = {}

# Define equations
equation_1 = "2*v1 + 3*v2 = 8"
equation_2 = "4*v1 - v2 = 2"

# Process both equations
result_1 = process_equation(equation_1, variable_values)
result_2 = process_equation(equation_2, variable_values)

# Combine left-hand sides into a matrix and right-hand sides into a column vector
lhs_matrix = Matrix([
    [result_1['left_side'].coeff(v1), result_1['left_side'].coeff(v2)],
    [result_2['left_side'].coeff(v1), result_2['left_side'].coeff(v2)]
])

rhs_vector = Matrix([
    [result_1['right_side']],
    [result_2['right_side']]
])

# Solve the system of equations
solution_vector = lhs_matrix.inv() * rhs_vector

# Print the results
print("LHS Matrix:")
print(lhs_matrix)

print("RHS Vector:")
print(rhs_vector)

print("Solution Vector (v1, v2):")
print(solution_vector)
