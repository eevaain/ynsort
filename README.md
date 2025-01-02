# YNsort

YNsort is a tool designed to help solve systems of equations by taking user-defined variables, constants, and equations as inputs and returning the solution. The tool is designed to (hopefully) be intuitive and user-friendly.

## Features
- Define **solution variables** for the system of equations.
- Provide **constants** in JSON format for substitution.
- Input **equations** as plain text, one per line.
- Get results including:
  - Left-hand side (LHS) and right-hand side (RHS) matrices.
  - The solution for each variable.

---

## How to Use

### **Frontend**
The interface is available at [YNsort.com](https://www.ynsort.com).

1. Open the app.
2. Input the following:
   - **Solution Variables**: Enter variables separated by commas (e.g., `i1, i2, i3`).
   - **Constants**: Provide constants in valid JSON format (e.g., `{"IA": 6, "VB": 5.1}`).
   - **Equations**: Add equations, one per line (e.g., `IA = i1 - i2`).
3. Click the **Solve!** button.
4. View the results:
   - LHS matrix.
   - RHS matrix.
   - Solution vector.

---
