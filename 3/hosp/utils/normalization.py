def normalize_data(matrix):
    max_value = max(max(row) for row in matrix)
    if max_value == 0:
        return matrix
    return [[num / max_value for num in row] for row in matrix]

def calculate_average(matrix):
    total = sum(sum(row) for row in matrix)
    count = sum(len(row) for row in matrix)
    return total / count if count > 0 else 0
