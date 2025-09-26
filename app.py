from services import UserService, OrderService
from testing.tools.func import add
import utils


def main():
    # Initialize services
    user_service = UserService()
    order_service = OrderService()

    # Create a user
    user = user_service.create_user("Alice", "alice@example.com")
    print(f"Created user: {utils.mask_email(user.email)}")

    # Create some orders for this user
    order1 = order_service.create_order(user, "Laptop", 1299.99)
    order2 = order_service.create_order(user, "Mouse", 25.50)
    order3 = order_service.create_order(user, "Keyboard", 89.99)

    print(f"\nOrders for {user.name}:")
    for order in order_service.get_orders_by_user(user.id):
        print(f"- {order}")

    # Calculate total
    total = order_service.calculate_user_total(user.id)
    print(f"\nTotal spent by {user.name}: ${total}")
    
    add(1,2)


if __name__ == "__main__":
    main()
