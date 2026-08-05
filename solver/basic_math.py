from sympy import sympify


def calculate(expression):
    """
    Evaluate a mathematical expression entered by the user.
    """

    try:
        answer = sympify(expression).evalf()

        # Remove unnecessary .0 for whole numbers
        if answer == int(answer):
            return int(answer)

        return round(float(answer), 6)

    except Exception:
        return "Invalid mathematical expression."