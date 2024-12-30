from sympy import symbols, Eq, sympify, expand, collect, Matrix, solve

def process_equation(equation_str, variable_values):
    """
    Process a single symbolic equation.

    Args:
        equation_str (str): The equation as a string (e.g., "3*v1 + v2 = 4").
        variable_values (dict): A dictionary of variable substitutions.

    Returns:
        dict: A dictionary containing the LHS and RHS of the simplified equation.
    """
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

        # Collect terms by variables
        grouped_equation = collect(simplified_equation, all_variables)

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
v1, v3, v4 = symbols('v1 v3 v4')

# Define all variables in sorted order
all_variables = sorted([v1, v3, v4], key=lambda x: x.name)

# Example variable substitutions
variable_values = {}

# Define equations
equation_1 = "2*v1 + v3 = 10"
equation_2 = "3*v1 - 2*v3 + v4 = -5"
equation_3 = "v3 + 4*v4 = 15"

# Process all equations
result_1 = process_equation(equation_1, variable_values)
result_2 = process_equation(equation_2, variable_values)
result_3 = process_equation(equation_3, variable_values)

# Combine left-hand sides into a matrix and right-hand sides into a column vector
lhs_matrix = Matrix([
    [result_1['left_side'].coeff(var) for var in all_variables],
    [result_2['left_side'].coeff(var) for var in all_variables],
    [result_3['left_side'].coeff(var) for var in all_variables]
])

rhs_vector = Matrix([
    [result_1['right_side']],
    [result_2['right_side']],
    [result_3['right_side']]
])

# Solve the system of equations
solution_vector = lhs_matrix.inv() * rhs_vector

# Print the results
print("LHS Matrix:")
print(lhs_matrix)

print("RHS Vector:")
print(rhs_vector)

print("Solution Vector:")
print(solution_vector)
