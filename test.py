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
v1, v2, v3, v4, v5, v6 = symbols('v1 v2 v3 v4 v5 v6')

# Define all variables in sorted order
all_variables = sorted([v1, v2, v3, v4, v5, v6], key=lambda x: x.name)

# Example variable substitutions
variable_values = {}

# Define equations
equation_1 = "4.5*v1 + 2.2*v2 = 0"
equation_2 = "-1.8*v1 + 10*v2 - 6.2*v3 = -8"
equation_3 = "0.75*v1 - 0.75*v2 - v3 + v6 = 0"
equation_4 = "v6 = 7"
equation_5 = "-4*v2 + 4.8*v4 = 0"
equation_6 = "-1.5*v4 + 7.5*v5 - 7.5*v6 = 8"

# Process all equations
results = [
    process_equation(equation_1, variable_values),
    process_equation(equation_2, variable_values),
    process_equation(equation_3, variable_values),
    process_equation(equation_4, variable_values),
    process_equation(equation_5, variable_values),
    process_equation(equation_6, variable_values)
]

# Combine left-hand sides into a matrix and right-hand sides into a column vector
lhs_matrix = Matrix([
    [result['left_side'].coeff(var) for var in all_variables] for result in results
])

rhs_vector = Matrix([
    [result['right_side']] for result in results
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
