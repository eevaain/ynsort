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
        grouped_equation = collect(simplified_equation, solution_variables)

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
        # Handle any exceptions that may occur during the processing of the equation
        print("Error:", e)
        return None

# Define solution variables (unknowns to solve for and these will be defined by the user)
solution_variables = symbols('i1 i2 i3 i4')  # These variables will be solved in the system of equations.

# Define constant variables (parameters with predefined values)
constant_variables = symbols('IA Rw Rx Ry Rz')  # These are given constant parameters for the equations.

# Example variable substitutions (dynamically changes wrt to inputs given in frontend)
variable_values = {constant_variables[0]: 6,  
                   constant_variables[1]: 5.1,  
                   constant_variables[2]: 1.5,  
                   constant_variables[3]: 3.6,  
                   constant_variables[4]: 1.1}  

# Define equations (frontend will send an object with an equations array that looks like one below)
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
    [result['left_side'].coeff(var) for var in solution_variables] for result in equation_results
])  # Create the coefficient matrix (LHS) from the processed equations.

rhs_vector = Matrix([
    [result['right_side']] for result in equation_results
])  # Create the constant matrix (RHS) from the processed equations.

# Solve the system of equations
solution_vector = lhs_matrix.inv() * rhs_vector  # Use matrix inversion to solve the linear system.

# Print the results
print("LHS Matrix:")  # Display the coefficient matrix (LHS).
print(lhs_matrix)

print("RHS Vector:")  # Display the constant matrix (RHS).
print(rhs_vector)

print("Solution Vector:")  # Display the solution vector (the values of i1, i2, i3, i4).
print(solution_vector)
