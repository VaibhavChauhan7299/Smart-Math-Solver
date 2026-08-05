import statistics


def calculate_statistics(numbers):

    result = {
        "mean": statistics.mean(numbers),
        "median": statistics.median(numbers),
        "mode": statistics.mode(numbers),
        "variance": statistics.variance(numbers),
        "standard_deviation": statistics.stdev(numbers)
    }

    return result