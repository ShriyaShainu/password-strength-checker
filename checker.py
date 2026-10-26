"""Score a password using basic character variety and length checks."""

import string


def check_password(password: str) -> str:
    """Return a simple strength label for ``password``.

    This uses the original five checks: at least eight characters, uppercase,
    lowercase, digit, and ASCII punctuation.
    """
    if not isinstance(password, str):
        raise TypeError("password must be a string")

    score = 0

    if len(password) >= 8:
        score += 1

    if any(char.isupper() for char in password):
        score += 1

    if any(char.islower() for char in password):
        score += 1

    if any(char.isdigit() for char in password):
        score += 1

    if any(char in string.punctuation for char in password):
        score += 1

    if score <= 2:
        return "Weak password"
    if score <= 4:
        return "Moderate password"
    return "Strong password"
