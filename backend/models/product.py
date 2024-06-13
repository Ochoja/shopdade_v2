class Product:
    def __init__(self, name: str, description: str, price: float, category: str,
                 sizes: list[int], uom: str, images: list[str], quantity: int) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.sizes = sizes
        self.uom = uom
        self.images = images
        self.quantity = quantity

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "sizes": self.sizes,
            "uom": self.uom,
            "images": self.images,
            "quantity": self.quantity
        }

    @staticmethod
    def from_dict(item):
        return Product(
            item.get("name"),
            item.get("description"),
            item.get("price"),
            item.get("category"),
            item.get("sizes"),
            item.get("uom"),
            item.get("images"),
            item.get("quantity")
        )
