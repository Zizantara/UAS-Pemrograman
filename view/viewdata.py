class SupermarketView:
    def __init__(self, process):
        self.process = process

    def display_products(self):
        print("\n=== Daftar Produk ===")
        print("ID  | Nama           | Harga    | Stok")
        print("-" * 40)
        for product in self.process.products:
            print(f"{product.id:<3} | {product.name:<14} | {product.price:<8} | {product.stock}")

    def display_cart(self):
        if not self.process.cart:
            print("\nKeranjang belanja kosong!")
            return

        print("\n=== Keranjang Belanja ===")
        print("Nama           | Harga    | Jumlah | Subtotal")
        print("-" * 45)
        for item in self.process.cart:
            subtotal = item["product"].price * item["quantity"]
            print(f"{item['product'].name:<14} | {item['product'].price:<8} | {item['quantity']:<6} | {subtotal}")
        print("-" * 45)
        print(f"Total: Rp {self.process.calculate_total()}")

    def run(self):
        while True:
            try:
                print("\n=== Supermarket Program ===")
                print("1. Lihat Produk")
                print("2. Tambah ke Keranjang")
                print("3. Lihat Keranjang")
                print("4. Checkout")
                print("5. Keluar")
                
                choice = input("Pilih menu (1-5): ")
                
                if choice == "1":
                    self.display_products()
                
                elif choice == "2":
                    self.display_products()
                    product_id = int(input("Masukkan ID produk: "))
                    quantity = int(input("Masukkan jumlah: "))
                    
                    if quantity <= 0:
                        raise ValueError("Jumlah harus lebih dari 0!")
                    
                    self.process.add_to_cart(product_id, quantity)
                    print("Produk berhasil ditambahkan ke keranjang!")
                
                elif choice == "3":
                    self.display_cart()
                
                elif choice == "4":
                    if not self.process.cart:
                        print("Keranjang belanja kosong!")
                        continue
                    self.display_cart()
                    print("\nTerima kasih telah berbelanja!")
                    break
                
                elif choice == "5":
                    print("Program selesai.")
                    break
                
                else:
                    print("Menu tidak valid!")
                    
            except ValueError as e:
                print(f"Error: {str(e)}")
            except Exception as e:
                print(f"Terjadi kesalahan: {str(e)}")
