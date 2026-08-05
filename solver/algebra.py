from sympy import (
    symbols,
    sympify,
    solve,
    Eq,
    diff,
    integrate,
    simplify,
    expand,
    factor
)

# Define variables
x, y, z = symbols("x y z")


def solve_math(problem):
    """
    Solves algebraic expressions entered by the user.

    Supported Operations:
    - Solve equations
    - Evaluate expressions
    - Differentiate
    - Integrate
    - Simplify
    - Expand
    - Factor
    """

    try:

        # Remove extra spaces
        problem = problem.strip()

        # ============================
        # 1. Solve equations
        # Example:
        # 2*x + 5 = 15
        # ============================

        if "=" in problem:

            left, right = problem.split("=", 1)

            left = sympify(left)
            right = sympify(right)

            equation = Eq(left, right)

            return solve(equation)

        # ============================
        # 2. Differentiate
        # Example:
        # diff(x**2 + 5*x)
        # ============================

        if problem.startswith("diff("):

            expression = problem[5:-1]

            expression = sympify(expression)

            return diff(expression, x)

        # ============================
        # 3. Integrate
        # Example:
        # integrate(x**2)
        # ============================

        if problem.startswith("integrate("):

            expression = problem[10:-1]

            expression = sympify(expression)

            return integrate(expression, x)

        # ============================
        # 4. Simplify
        # Example:
        # simplify((x+2)*(x+3)-(x**2+5*x+6))
        # ============================

        if problem.startswith("simplify("):

            expression = problem[9:-1]

            expression = sympify(expression)

            return simplify(expression)

        # ============================
        # 5. Expand
        # Example:
        # expand((x+2)*(x+3))
        # ============================

        if problem.startswith("expand("):

            expression = problem[7:-1]

            expression = sympify(expression)

            return expand(expression)

        # ============================
        # 6. Factor
        # Example:
        # factor(x**2+5*x+6)
        # ============================

        if problem.startswith("factor("):

            expression = problem[7:-1]

            expression = sympify(expression)

            return factor(expression)

        # ============================
        # 7. Normal Expression
        # Example:
        # x**2 + 5*x + 6
        # ============================

        expression = sympify(problem)

        # Solve if variable exists
        if expression.free_symbols:

            return solve(expression)

        # Otherwise calculate
        return expression.evalf()

    except Exception as e:

        return f"Error: {e}"