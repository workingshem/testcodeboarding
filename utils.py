import random
import string
from typing import List


def generate_user_id() -> int:
    """Generate a random user ID."""
    return random.randint(1000, 9999)


def generate_order_id() -> int:
    """Generate a random order ID."""
    return random.randint(50000, 99999)


def mask_email(email: str) -> str:
    """Mask an email for privacy."""
    user, domain = email.split("@")
    masked = user[0] + "***" + user[-1]
    return f"{masked}@{domain}"


def calculate_total(orders: List[float]) -> float:
    """Calculate the total cost of all orders."""
    return round(sum(orders), 2)
