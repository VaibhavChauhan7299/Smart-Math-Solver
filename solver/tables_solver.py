def multiplication_table(number, limit=10):
    table = []

    for i in range(1, limit + 1):
        result = number * i
        table.append(f"{number} × {i} = {result}")

    return table