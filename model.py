from dataclasses import dataclass
from datetime import datetime


@dataclass
class User:
    id: int
    name: str
    email: str
    created_at: datetime = datetime.now()

    def __str__(self):
        return f"User({self.id}, {self.name}, {self.email})"


@dataclass
class Order:
    id: int
    user_id: int
    item: str
    price: float
    created_at: datetime = datetime.now()

    def __str__(self):
        return f"Order({self.id}, User={self.user_id}, Item={self.item}, Price={self.price})"