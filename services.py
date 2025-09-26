from models import User, Order
import utils


class UserService:
    """Handles user creation and retrieval."""

    def __init__(self):
        self.users = {}

    def create_user(self, name: str, email: str) -> User:
        user_id = utils.generate_user_id()
        user = User(id=user_id, name=name, email=email)
        self.users[user_id] = user
        return user

    def get_user(self, user_id: int) -> User:
        return self.users.get(user_id)


class OrderService:
    """Handles order creation and retrieval."""

    def __init__(self):
        self.orders = {}

    def create_order(self, user: User, item: str, price: float) -> Order:
        order_id = utils.generate_order_id()
        order = Order(id=order_id, user_id=user.id, item=item, price=price)
        self.orders[order_id] = order
        return order

    def get_orders_by_user(self, user_id: int):
        return [o for o in self.orders.values() if o.user_id == user_id]

    def calculate_user_total(self, user_id: int) -> float:
        user_orders = self.get_orders_by_user(user_id)
        return utils.calculate_total([o.price for o in user_orders])
