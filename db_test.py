import mysql.connector

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

import pyfiglet
import time
import sys
from rich.console import Console
from rich.table import Table
from colorama import Fore, Style, init
from datetime import datetime

# Inisialisasi colorama
init(autoreset=True)


def tampilkan_header():
    ascii_art = pyfiglet.figlet_format("IP-NI   BOSS")
    print(Fore.CYAN + Style.BRIGHT + ascii_art)

# Fungsi untuk loading screen sederhana
def loading_screen():
    print(Fore.YELLOW + "\nBentar yaaakk....", end="")
    for i in range(5):  # Ulangi loading sebanyak 5 kali
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(0.5)  # Jeda 0.5 detik
    print(Fore.GREEN + "\nUdah ni\n")

# Fungsi utama 
def main():
    loading_screen()  # loading screen 
    tampilkan_header()  # header ASCII art
    print(Fore.YELLOW + "Selamat Datang di Aplikasi Penyewaan iPhone Kami")
    print(Fore.WHITE + "Masih bingung, Udah H-1 Reuni akbar tapi belum sempat ganti HP...")
    print(Fore.WHITE + "Amann ajaa di sini ada solusinya \n")

# Jalankan program utama
if __name__ == "__main__":
    main()


# Data iPhone (List of Dictionaries)
data_iphone = [
    {"ID": "IP11", "Model": "iPhone 11", "Stok": 5, "Harga": 100.000},
    {"ID": "IP12", "Model": "iPhone 12", "Stok": 4, "Harga": 150.000},
    {"ID": "IP13", "Model": "iPhone 13", "Stok": 3, "Harga": 200.000},
    {"ID": "IP14", "Model": "iphone 14", "Stok": 4, "Harga": 250.000},
    
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


# Fungsi menampilkan tabel iPhone
def tampilkan_tabel(data, title):
    table = Table(title=title)
    table.add_column("ID", justify="center", style="cyan")
    table.add_column("Model", style="magenta")
    table.add_column("Stok", justify="center", style="yellow")
    table.add_column("Harga (Rp)", justify="right", style="green")
    for item in data:
        table.add_row(item['ID'], item['Model'], str(item['Stok']), f"{item['Harga']:,}")
    console.print(table)

# Fungsi CRUD: Tambah iPhone
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


# Data Penyewaan
data_penyewaan = []

# Console untuk rich
console = Console()
# Fungsi CRUD: Update iPhone
def update_iphone():
    print(Fore.YELLOW + "\nUpdate Data iPhone:")
    tampilkan_tabel(data_iphone, "Daftar iPhone")
    id_hp = input("Masukkan ID iPhone yang ingin diupdate: ").upper()
    for item in data_iphone:
        if item['ID'] == id_hp:
            item['Model'] = input(f"Model ({item['Model']}): ") or item['Model']
            item['Stok'] = int(input(f"Stok ({item['Stok']}): ") or item['Stok'])
            item['Harga'] = int(input(f"Harga ({item['Harga']}): ") or item['Harga'])
            print(Fore.GREEN + "Data iPhone berhasil diupdate!")
            return
    print(Fore.RED + "ID iPhone tidak ditemukan!")

# Fungsi CRUD: Hapus iPhone
def hapus_iphone():
    print(Fore.RED + "\nHapus Data iPhone:")
    tampilkan_tabel(data_iphone, "Daftar iPhone")
    id_hp = input("Masukkan ID iPhone yang ingin dihapus: ").upper()
    for item in data_iphone:
        if item['ID'] == id_hp:
            data_iphone.remove(item)
            print(Fore.GREEN + "Data iPhone berhasil dihapus!")
            return
    print(Fore.RED + "ID iPhone tidak ditemukan!")

# Fungsi Proses Penyewaan
def sewa_iphone():
    print(Fore.BLUE + "\nProses Penyewaan iPhone:")
    tampilkan_tabel(data_iphone, "Daftar iPhone Tersedia")
    id_hp = input("Masukkan ID iPhone yang ingin disewa: ").upper()
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
                return
            else:
                print(Fore.RED + "Stok iPhone habis!")
                return
    print(Fore.RED + "ID iPhone tidak ditemukan!")

# Fungsi Menampilkan Riwayat Penyewaan
def tampilkan_penyewaan():
    print(Fore.CYAN + "\nRiwayat Penyewaan:")
    table = Table(title="Riwayat Penyewaan")
    table.add_column("Model", style="magenta")
    table.add_column("Lama Sewa", justify="center", style="yellow")
    table.add_column("Total Biaya", justify="right", style="green")
    table.add_column("Tanggal", style="cyan")
    for item in data_penyewaan:
        table.add_row(item['Model'], str(item['Lama Sewa']), f"{item['Total Biaya']:,}", item['Tanggal'])
    console.print(table)


from PIL import Image
import os

def tampilkan_gambar(iPhone15Pro.png):
    try:
        # Buka gambar
        img = Image.open(os.path.join("images", iPhone15Pro.png))
        img.show()  # Menampilkan gambar dengan aplikasi bawaan sistem
    except FileNotFoundError:
        print(Fore.RED + f"Gambar {iPhone15Pro.png} tidak ditemukan!")

def menu_utama():
    while True:
        print(Fore.BLUE + "\n=== SISTEM PENYEWAAN iPHONE ===")
        print("1. Lihat Daftar iPhone")
        print("2. Tambah Data iPhone")
        print("3. Update Data iPhone")
        print("4. Hapus Data iPhone")
        print("5. Sewa iPhone")
        print("6. Lihat Riwayat Penyewaan")
        print("7. Tampilkan Gambar iPhone")
        print("8. Keluar")

        pilihan = input("Masukkan pilihan (1-8): ")

        if pilihan == "1":
            tampilkan_tabel(data_iphone, "Daftar iPhone")
        elif pilihan == "2":
            tambah_iphone()
        elif pilihan == "3":
            update_iphone()
        elif pilihan == "4":
            hapus_iphone()
        elif pilihan == "5":
            sewa_iphone()
        elif pilihan == "6":
            tampilkan_penyewaan()
        elif pilihan == "7":
            id_hp = input("Masukkan ID iPhone untuk melihat gambarnya: ").upper()
            gambar = {
                "IP11": "iPhone15Pro.png",
               
            }
            if id_hp in gambar:
                tampilkan_gambar(gambar[id_hp])
            else:
                print(Fore.RED + "Gambar untuk ID tersebut tidak tersedia!")
        elif pilihan == "8":
            print(Fore.YELLOW + "Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid! Silakan coba lagi.")





if pilihan == "1":
            tampilkan_tabel(data_iphone, "Daftar iPhone")
        elif pilihan == "2":
            tambah_iphone()
        elif pilihan == "3":
            update_iphone()
        elif pilihan == "4":
            hapus_iphone()
        elif pilihan == "5":
            sewa_iphone()
        elif pilihan == "6":
            tampilkan_penyewaan()
        elif pilihan == "7":
            print(Fore.YELLOW + "Terima kasih telah menggunakan aplikasi ini!")
            break
        else:
            print(Fore.RED + "Pilihan tidak valid! Silakan coba lagi.")

# Program Utama
if __name__ == "__main__":
    menu_utama()