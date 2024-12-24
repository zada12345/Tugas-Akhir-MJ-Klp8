import mysql.connector  # Koneksi database
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style, init
from datetime import datetime
import pyfiglet
import time
import sys

# Koneksi ke database
connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="db_kios"
)
cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")
current_db = cursor.fetchone()
print(f"Database yang digunakan: {current_db[0]}")

# Inisialisasi
init(autoreset=True)
console = Console()

# Header
def tampilkan_header():
    ascii_art = pyfiglet.figlet_format("IP-NI   BOSS")
    print(Fore.CYAN + Style.BRIGHT + ascii_art)

def loading_screen():
    print(Fore.YELLOW + "\nBentar yaaakk....", end="")
    for i in range(5):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)
    print(Fore.GREEN + "\nUdah ni\n")

def main():
    loading_screen()
    tampilkan_header()
    print(Fore.YELLOW + "Selamat Datang di Aplikasi Penyewaan iPhone Kami")
    print(Fore.WHITE + "Masih bingung, Udah H-1 Reuni akbar tapi belum sempat ganti HP...")
    print(Fore.WHITE + "Amann ajaa di sini ada solusinya \n")

# Data utama
data_iphone = [
    {"ID": "IP11", "Model": "iPhone 11", "Stok": 5, "Harga": 100000},
    {"ID": "IP12", "Model": "iPhone 12", "Stok": 4, "Harga": 150000},
    {"ID": "IP13", "Model": "iPhone 13", "Stok": 3, "Harga": 200000},
    {"ID": "IP14", "Model": "iPhone 14", "Stok": 4, "Harga": 250000},
]

data_iphone_pro = [
    {"ID": "IP12-PRO", "Model": "iPhone 12 Pro", "Stok": 4, "Harga": 170000},
    {"ID": "IP13-PRO", "Model": "iPhone 13 Pro", "Stok": 3, "Harga": 220000},
    {"ID": "IP14-PRO", "Model": "iPhone 14 Pro", "Stok": 5, "Harga": 300000},
]

data_iphone_xr = [
    {"ID": "IPXR", "Model": "iPhone XR", "Stok": 6, "Harga": 80000},
    {"ID": "IPXS", "Model": "iPhone XS", "Stok": 5, "Harga": 90000},
]

# Fungsi tampilkan tabel
def tampilkan_tabel(data, title):
    table = Table(title=title)
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("Stok", justify="center", style="yellow")
    table.add_column("Harga (Rp)", justify="right", style="green")
    for item in data:
        table.add_row(item['ID'], item['Model'], str(item['Stok']), f"{item['Harga']:,}")
    console.print(table)

# Menu utama
def menu_utama():
    while True:
        print(Fore.BLUE + "\n=== SISTEM PENYEWAAN iPHONE ===")
        print("1. Lihat Daftar iPhone")
        print("2. Lihat Daftar iPhone Pro")
        print("3. Lihat Daftar iPhone XR")
        print("4. Tambah Data iPhone")
        print("5. Keluar")

        pilihan = input("Masukkan pilihan (1-5): ")

        if pilihan == "1":
            tampilkan_tabel(data_iphone, "Daftar iPhone")
        elif pilihan == "2":
            tampilkan_tabel(data_iphone_pro, "Daftar iPhone Pro")
        elif pilihan == "3":
            tampilkan_tabel(data_iphone_xr, "Daftar iPhone XR")
        elif pilihan == "4":
            tambah_iphone()
        elif pilihan == "5":
            print(Fore.YELLOW + "Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid! Silakan coba lagi.")

# Fungsi tambah iPhone
def tambah_iphone():
    print(Fore.GREEN + "\nTambah Data iPhone:")
    print("1. Tambah ke Daftar iPhone")
    print("2. Tambah ke Daftar iPhone Pro")
    print("3. Tambah ke Daftar iPhone XR")

    sub_pilihan = input("Pilih daftar (1-3): ")

    id_hp = input("Masukkan ID iPhone: ").upper()
    model = input("Masukkan Model iPhone: ")
    stok = int(input("Masukkan Stok: "))
    harga = int(input("Masukkan Harga: "))

    data_baru = {"ID": id_hp, "Model": model, "Stok": stok, "Harga": harga}

    if sub_pilihan == "1":
        data_iphone.append(data_baru)
    elif sub_pilihan == "2":
        data_iphone_pro.append(data_baru)
    elif sub_pilihan == "3":
        data_iphone_xr.append(data_baru)
    else:
        print(Fore.RED + "Pilihan tidak valid!")
        return

    print(Fore.CYAN + "Data iPhone berhasil ditambahkan!")

# Program Utama
if __name__ == "__main__":
    main()
    menu_utama()
