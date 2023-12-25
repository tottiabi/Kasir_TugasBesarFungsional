import tkinter as tk

# Pure function untuk menghitung total pembayaran
def calculate_total(items):
    return sum(float(item[1]) * float(item[2]) for item in items)

# Closure untuk menyimpan riwayat transaksi
def transaction_history():
    history = []

    def add_to_history(items, total):
        nonlocal history
        history.append({'items': items, 'total': total})
        print("Riwayat Transaksi:")
        for idx, transaction in enumerate(history, start=1):
            print(
                f"Transaksi ke-{idx}: {transaction['items']} - Total: {transaction['total']}")

    return add_to_history

# Decorator untuk menampilkan pesan sebelum dan setelah menjalankan fungsi
def message_decorator(func):
    def wrapper(*args, **kwargs):
        print("Mengeksekusi fungsi...")
        result = func(*args, **kwargs)
        print("Fungsi selesai dieksekusi.")
        return result
    return wrapper

# High-order function yang menggunakan lambda
def apply_discount(discount):
    return lambda price: price * (1 - discount)

# List comprehension untuk menghasilkan data item
def generate_items():
    items = [
        ('Gula', 10000, 2),
        ('Telur', 20000, 1),
        ('Minyak', 25000, 2)
    ]
    return items

# Generator untuk menghasilkan nilai secara lazim
def generate_numbers(n):
    for i in range(n):
        yield i

# GUI menggunakan Tkinter
def create_gui():
    def calculate():
        total = calculate_total(cart)
        total_label.config(text=f"Total Pembayaran: Rp {total:,}")

    def add_to_cart():
        item = tuple(
            map(lambda x: x.get(), (item_name, item_price, item_quantity)))
        cart.append(item)
        item_name.delete(0, tk.END)
        item_price.delete(0, tk.END)
        item_quantity.delete(0, tk.END)

    def show_history():
        history_function = transaction_history()
        history_function(cart, calculate_total(cart))

    cart = generate_items()

    root = tk.Tk()
    root.title("Program Kasir")

    item_name_label = tk.Label(root, text="Nama Barang:")
    item_name_label.pack()
    item_name = tk.Entry(root)
    item_name.pack()

    item_price_label = tk.Label(root, text="Harga Barang (Rp):")
    item_price_label.pack()
    item_price = tk.Entry(root)
    item_price.pack()

    item_quantity_label = tk.Label(root, text="Jumlah Barang:")
    item_quantity_label.pack()
    item_quantity = tk.Entry(root)
    item_quantity.pack()

    add_to_cart_button = tk.Button(
        root, text="Tambah ke Keranjang", command=add_to_cart)
    add_to_cart_button.pack()

    calculate_button = tk.Button(root, text="Hitung Total", command=calculate)
    calculate_button.pack()

    total_label = tk.Label(root, text="Total Pembayaran: Rp 0")
    total_label.pack()

    history_button = tk.Button(
        root, text="Tampilkan Riwayat Transaksi", command=show_history)
    history_button.pack()

    root.mainloop()


# Menjalankan GUI
if __name__ == "__main__":
    create_gui()
