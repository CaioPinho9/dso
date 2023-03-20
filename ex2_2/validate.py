def validate_str(*args):
    for value in args:
        if not isinstance(value, str):
            raise ValueError
