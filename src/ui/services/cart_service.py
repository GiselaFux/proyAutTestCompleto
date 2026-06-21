class CartService:
    def __init__(self):
        self.items = []

    def add_item(self, product_id: str, price: float):
        self.items.append({"product_id": product_id, "price": price})

    def total_items(self) -> int:
        return len(self.items)

    def total_price(self) -> float:
        return sum(item["price"] for item in self.items)