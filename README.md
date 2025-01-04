# UAS-Pemrograman

Nama    : Zizantara Arzeva Cakra Kahana

NIM     : 312410298

Kelas   : TI,24.A.3

# Penjeasan Code 

1. **Struktur Class Product (data/savedata.py)**
```python
class Product:
    def __init__(self, id, name, price, stock):
        self.id = id          # Menyimpan ID produk
        self.name = name      # Menyimpan nama produk
        self.price = price    # Menyimpan harga produk
        self.stock = stock    # Menyimpan stok produk
```
- Class ini berfungsi sebagai template untuk menyimpan data produk
- Setiap produk memiliki 4 atribut: id, name, price, dan stock
- Ini adalah contoh konsep OOP untuk encapsulation (pengelompokan data)

2. **Class SupermarketProcess (data/prosesdata.py)**
```python
def __init__(self):
    self.products = [
        Product(1, "Beras", 15000, 50),
        Product(2, "Gula", 12000, 30),
        Product(3, "Minyak Goreng", 20000, 40),
        Product(4, "Telur", 25000, 100),
    ]
    self.cart = []
```
- Inisialisasi daftar produk dan keranjang belanja
- `self.products`: List yang berisi objek Product
- `self.cart`: List kosong untuk menyimpan item yang dibeli

```python
def get_product_by_id(self, id):
    for product in self.products:
        if product.id == id:
            return product
    return None
```
- Mencari produk berdasarkan ID
- Mengembalikan objek Product jika ditemukan, None jika tidak

```python
def add_to_cart(self, product_id, quantity):
    product = self.get_product_by_id(product_id)
    if product is None:
        raise ValueError("Produk tidak ditemukan!")
    if product.stock < quantity:
        raise ValueError(f"Stok tidak cukup! Stok tersedia: {product.stock}")
    
    self.cart.append({"product": product, "quantity": quantity})
    product.stock -= quantity
```
- Menambahkan produk ke keranjang
- Melakukan validasi:
  - Produk harus ada
  - Stok harus mencukupi
- Mengurangi stok produk setelah ditambahkan ke keranjang

```python
def calculate_total(self):
    return sum(item["product"].price * item["quantity"] for item in self.cart)
```
- Menghitung total harga belanjaan di keranjang

3. **Class SupermarketView (view/viewdata.py)**
```python
def display_products(self):
    print("\n=== Daftar Produk ===")
    print("ID  | Nama           | Harga    | Stok")
    print("-" * 40)
    for product in self.process.products:
        print(f"{product.id:<3} | {product.name:<14} | {product.price:<8} | {product.stock}")
```
- Menampilkan daftar produk dalam format tabel
- Output contoh:
```
=== Daftar Produk ===
ID  | Nama           | Harga    | Stok
----------------------------------------
1   | Beras         | 15000    | 50
2   | Gula          | 12000    | 30
3   | Minyak Goreng | 20000    | 40
4   | Telur         | 25000    | 100
```

```python
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
```
- Menampilkan isi keranjang belanja
- Output contoh:
```
=== Keranjang Belanja ===
Nama           | Harga    | Jumlah | Subtotal
---------------------------------------------
Beras         | 15000    | 2      | 30000
Gula          | 12000    | 1      | 12000
---------------------------------------------
Total: Rp 42000
```

```python
def run(self):
    # Menu utama program
```
- Menampilkan menu interaktif dengan 5 pilihan:
  1. Lihat Produk: Menampilkan daftar produk
  2. Tambah ke Keranjang: Meminta input ID produk dan jumlah
  3. Lihat Keranjang: Menampilkan isi keranjang
  4. Checkout: Menyelesaikan belanja
  5. Keluar: Mengakhiri program
- Memiliki penanganan error untuk:
  - Input tidak valid
  - Produk tidak ditemukan
  - Stok tidak cukup
  - Jumlah pembelian tidak valid

4. **File Main (main.py)**
```python
if __name__ == "__main__":
    process = SupermarketProcess()
    view = SupermarketView(process)
    view.run()
```
- Entry point program
- Membuat objek process dan view
- Menjalankan program dengan method run()

Program ini mengimplementasikan konsep OOP dengan:
1. Encapsulation: Pengelompokan data dan method dalam class
2. Separation of Concerns: Pemisahan antara:
   - Data (Product)
   - Process (SupermarketProcess)
   - View (SupermarketView)
3. Exception Handling: Penanganan error untuk input tidak valid
4. Modular Programming: Pemisahan kode dalam file-file terpisah

Apakah ada bagian yang ingin Anda tanyakan lebih lanjut?