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

# Define symbols (dynamically changes wrt to inputs given in frontend)
# v1, v2, v3, v4, v5, v6, IB = symbols('v1 v2 v3 v4 v5 v6 IB')
i1, i2, i3, i4, IA, Rw, Rx, Ry, Rz = symbols('i1 i2 i3 i4 IA Rw Rx Ry Rz')

# Define all variables in sorted order (dynamically changes wrt to inputs given in frontend)
all_variables = sorted([i1, i2, i3, i4], key=lambda x: x.name)
## ^^ can refactor this line of code and get rid of line 40? do so
## by scanning equations list and find highest value of v? or require user 
## to manually type in the highest value (subscript) of v and the loop from i = 1 to i <= to highest subscript of v 
## ...

# Example variable substitutions (dynamically changes wrt to inputs given in frontend)
variable_values = {IA: 6, Rw: 5.1, Rx: 1.5, Ry: 3.6, Rz: 1.1}

# Define equations (dynamically changes wrt to inputs given in frontend)
equations = [
    "Rx*(i4-i2) + Rx*iz = 0",
    "IA = i1-i2",
    "Rw*i1 + Ry*(i1-i3) + Rx*(i2-i4) = 0",
    "0 + Ry*(i3-i1) + Rz*i3 = 0"
]

# Process all equations
equation_results = [process_equation(eq, variable_values) for eq in equations]

# Combine left-hand sides into a matrix and right-hand sides into a column vector
lhs_matrix = Matrix([
    [result['left_side'].coeff(var) for var in all_variables] for result in equation_results
])

rhs_vector = Matrix([
    [result['right_side']] for result in equation_results
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
