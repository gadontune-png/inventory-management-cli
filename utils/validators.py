def validate_positive(value):
    if value < 0:
        raise ValueError("Must be positive")