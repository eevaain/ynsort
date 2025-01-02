from flask import Flask, request, jsonify
from flask_cors import CORS 
from sympy import symbols, Eq, sympify, expand, collect, Matrix

app = Flask(__name__)
CORS(app, origins=["http://localhost:3000"])  # Allow requests from the React frontend

def process_equation(equation_str, solution_variables, variable_values):
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
        return {"error": str(e)}

@app.route('/solve', methods=['POST'])
def solve_equations():
    try:
        # Get data from the request
        data = request.get_json()

        # Extract variables and equations
        solution_variable_names = data.get('solution_variables', [])
        constant_variables = data.get('constant_variables', {})
        equations = data.get('equations', [])

        # Define solution variables and constant values
        solution_variables = symbols(solution_variable_names)
        constant_symbols = symbols(list(constant_variables.keys()))
        variable_values = {var: constant_variables[var.name] for var in constant_symbols}

        # Process equations
        equation_results = [process_equation(eq, solution_variables, variable_values) for eq in equations]

        # Combine left-hand sides into a matrix and right-hand sides into a column vector
        lhs_matrix = Matrix([
            [result['left_side'].coeff(var) for var in solution_variables] for result in equation_results
        ])
        rhs_vector = Matrix([
            [result['right_side']] for result in equation_results
        ])

        # Solve the system of equations
        solution_vector = lhs_matrix.inv() * rhs_vector

        # Return the results as JSON
        return jsonify({
            "lhs_matrix": str(lhs_matrix),
            "rhs_vector": str(rhs_vector),
            "solution_vector": str(solution_vector)
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)