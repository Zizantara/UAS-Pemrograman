
from data.savedata import Product


class SupermarketProcess:
    def __init__(self):
        self.products = [
            Product(1, "Beras", 15000, 50),
            Product(2, "Gula", 12000, 30),
            Product(3, "Minyak Goreng", 20000, 40),
            Product(4, "Telur", 25000, 100),
        ]
        self.cart = []

    def get_product_by_id(self, id):
        for product in self.products:
            if product.id == id:
                return product
        return None

    def add_to_cart(self, product_id, quantity):
        product = self.get_product_by_id(product_id)
        if product is None:
            raise ValueError("Produk tidak ditemukan!")
        if product.stock < quantity:
            raise ValueError(f"Stok tidak cukup! Stok tersedia: {product.stock}")
        
        self.cart.append({"product": product, "quantity": quantity})
        product.stock -= quantity

    def calculate_total(self):
        return sum(item["product"].price * item["quantity"] for item in self.cart)