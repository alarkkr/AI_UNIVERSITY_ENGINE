def validate_input(q: str):

    if not q or len(q) > 500:
        raise ValueError("Invalid input")

    return q.strip()