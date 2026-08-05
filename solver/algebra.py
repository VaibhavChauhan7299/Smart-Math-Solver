from sympy import (
    symbols,
    sympify,
    solve,
    Eq,
    diff,
    integrate
)

x = symbols('x')


def solve_math(problem):
    problem = problem.strip()

    # Handle equations containing =
    if "=" in problem:
        left, right = problem.split("=", 1)

        left = sympify(left)
        right = sympify(right)

        equation = Eq(left, right)

        return solve(equation, x)

    # Handle calculus commands
    if problem.startswith("diff("):
        expression = problem[5:-1]
        expression = sympify(expression)

        return diff(expression, x)

    if problem.startswith("integrate("):
        expression = problem[9:-1]
        expression = sympify(expression)

        return integrate(expression, x)

    # Handle normal mathematical expressions
    expression = sympify(problem)

    # If x exists, solve it
    if x in expression.free_symbols:
        return solve(expression, x)

    # Otherwise calculate the expression
    return expression