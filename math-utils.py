def compute_mean(values):
    return sum(values) / len(values)

def compute_standard_deviation(values):
    mean = compute_mean(values)
    variance = sum((x - mean) ** 2 for x in values) / len(values)
    return variance ** 0.5