import statistics


def calculate_statistics(numbers):
    """Calculate common statistics for a list of numbers."""

    result = {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "mode": statistics.multimode(numbers),
        "range": max(numbers) - min(numbers),
        "variance": statistics.variance(numbers),
        "standard_deviation": statistics.stdev(numbers)
    }

    return result


def input_numbers():
    """Get numbers from the user."""

    while True:

        user_input = input(
            "\nEnter numbers separated by spaces: "
        )

        try:

            numbers = [
                float(value)
                for value in user_input.split()
            ]

            if len(numbers) < 2:
                print("Please enter at least 2 numbers.")
                continue

            return numbers

        except ValueError:

            print("Please enter valid numbers.")