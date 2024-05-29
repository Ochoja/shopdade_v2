class Product:
    def __init__(self, name: str, description: str, price: str, category: str,
                 sizes: list[int], uom: str, images: list[str]) -> None:
        self.name = name
        self.description = description
        self.price = price
        self.category = category
        self.sizes = sizes
        self.uom = uom
        self.images = images

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "price": self.price,
            "category": self.category,
            "sizes": self.sizes,
            "uom": self.uom,
            "images": self.images
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
            item.get("images")
        )
