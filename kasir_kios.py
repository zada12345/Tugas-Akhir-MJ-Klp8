import mysql.connector

connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="",
    database="db_kios1"  
)
cursor = connection.cursor()
cursor.execute("SELECT DATABASE();")  
current_db = cursor.fetchone()
print(f"Database yang digunakan: {current_db[0]}")

import mysql.connector
import pyfiglet
import time
import sys
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style, init
from datetime import datetime
from tabulate import tabulate  # Pindahkan ke atas!


# Inisialisasi colorama
init(autoreset=True)


def tampilkan_header():
    ascii_art = pyfiglet.figlet_format("IP - NI   BOSS")
    print(Fore.CYAN + Style.BRIGHT + ascii_art)

# loading screen 
def loading_screen():
    print(Fore.YELLOW + "\nBentar yaaakk....", end="")
    for i in range(5):  # Ulangi loading sebanyak 5 kali
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)  # Jeda 0.5 detik
    print(Fore.GREEN + "\n\n")


def main():
    loading_screen()  # loading screen 
    tampilkan_header()  # header ASCII art
    print(Fore.YELLOW + "Selamat Datang di Aplikasi Penyewaan iPhone Kami")
    print(Fore.WHITE + "Masih bingung, Udah H-1 Reuni akbar tapi belum sempat ganti HP...")
    print(Fore.WHITE + "Amann ajaa di sini ada solusinya \n")

# program utama
if __name__ == "__main__":
    main()


# Data iPhone (List of Dictionaries)
data_iphone = [
    {"ID": "IP11", "Model": "iPhone 11", "Stok": 5, "Harga": 100_000},
    {"ID": "IP12", "Model": "iPhone 12", "Stok": 4, "Harga": 150_000},
    {"ID": "IP13", "Model": "iPhone 13", "Stok": 0, "Harga": 200_000},
    {"ID": "IP14", "Model": "iphone 14", "Stok": 4, "Harga": 250_000},
    {"ID": "IP15", "Model": "iphone 15", "Stok": 2, "Harga": 380_000},

    {"ID": "14PLUS", "Model": "iPhone 14 Plus", "Stok": 3, "Harga": 250_000},
    {"ID": "14PRO", "Model": "iPhone 14 Pro", "Stok": 4, "Harga": 300_000},
    {"ID": "15PRO", "Model": "iphone 15 Pro", "Stok": 11, "Harga": 400_000},
    {"ID": "14PRO-X", "Model": "iPhone 14 Pro Max", "Stok": 6, "Harga": 350_000},
    {"ID": "15PRO-X", "Model": "iphone 15 Pro Max", "Stok": 7, "Harga": 500_000},
]

# Console untuk rich
console = Console()

# Data Penyewaan
data_penyewaan = []

# menampilkan tabel iPhone
def tampilkan_tabel(data, title):
    table = Table(title=title)
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("Stok", justify="center", style="yellow")
    table.add_column("Harga (Rp)", justify="right", style="green")
    for item in data:
        table.add_row(item['ID'], item['Model'], str(item['Stok']), f"{item['Harga']:,}")
    console.print(table)

# Proses Penyewaan
from tabulate import tabulate
from datetime import datetime

from tabulate import tabulate
from datetime import datetime

# Fungsi untuk mencetak struk
def cetak_struk(nama, alamat, model, lama_sewa, total_biaya):
    tanggal = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data_struk = [
        ["Nama", nama],
        ["Alamat", alamat],
        ["Model iPhone", model],
        ["Lama Sewa (hari)", f"{lama_sewa} hari"],
        ["Total Biaya", f"Rp {total_biaya:,}"],
        ["Tanggal", tanggal]
    ]
    print("\n===== STRUK PENYEWAAN =====")
    print(tabulate(data_struk, tablefmt="fancy_grid"))
    print("===========================\n")

def sewa_iphone():
    print(Fore.BLUE + "\nProses Penyewaan iPhone:")
    tampilkan_tabel(data_iphone, "Daftar iPhone Tersedia")
    nama = input("Nama Costumer: ").upper()
    alamat = input("Alamat Costumer: ")
    id_hp = input("Masukkan ID iPhone yang ingin disewa: ")
    lama_sewa = int(input("Masukkan lama sewa (hari): "))

    for item in data_iphone:
        if item['ID'] == id_hp:
            if item['Stok'] > 0:
                item['Stok'] -= 1  # Kurangi stok
                total_biaya = item['Harga'] * lama_sewa
                data_penyewaan.append({
                    "Model": item['Model'],
                    "Lama Sewa": lama_sewa,
                    "Total Biaya": total_biaya,
                    "Tanggal": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                })
                print(Fore.GREEN + f"Penyewaan berhasil! Total Biaya: Rp {total_biaya:,}")

                # Cetak struk
                cetak_struk(nama, alamat, item['Model'], lama_sewa, total_biaya)
                return
            else:
                print(Fore.RED + "Waduh lagi kosong rupanya, yg lain aja yaa..")
                return
    print(Fore.RED + "ID iPhone tidak ditemukan!")

# Menu Utama
def menu_utama():
    while True:
        menu = [
            ["1", "Lihat Daftar iPhone"],
            ["2", "Tambah Data iPhone"],
            ["3", "Update Data iPhone"],
            ["4", "Hapus Data iPhone"],
            ["5", "Sewa iPhone"],
            ["6", "Keluar"]
        ]

        print(Fore.BLUE + "\n=== SISTEM PENYEWAAN iPHONE ===")
        print(tabulate(menu, headers=["Pilihan", "Deskripsi"], tablefmt="fancy_grid"))

        pilihan = input("Masukkan pilihan (1-6): ")

        if pilihan == "1":
            tampilkan_tabel(data_iphone, "Daftar iPhone")
        elif pilihan == "5":
            sewa_iphone()
        elif pilihan == "6":
            print(Fore.YELLOW + "Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid! Silakan coba lagi.")

if __name__ == "__main__":
    menu_utama()
