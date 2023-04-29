from algorithms.string_processing import split, strip
import variables
import os

# Tipe bentukan untuk menyimpan informasi mengenai total bahan bangunan yang tersedia.
class BahanList:
    def __init__(self, sand=0, stone=0, water=0):
        self.sand = sand
        self.stone = stone
        self.water = water

# Variabel global berfungsi sebagai database untuk mengload file csv, 
# melakukan perubahan (penambahan/penghapusan) bahan bangunan, dan sumber ketika penyimpanan diakhir.
bahan_list = BahanList()

bahan_list.sand = 0
bahan_list.stone = 0
bahan_list.water = 0

sand_description = 'Pasir yang halus'
stone_description = 'Batu yang keras'
water_description = 'Air yang mengalir'


def load():
    global bahan_list
    global sand_description, stone_description, water_description
    bahan_count = 0
    # Menghitung jumlah baris (3).
    with open(os.path.join(variables.load_folder, "bahan_bangunan.csv")) as file:
        file.readline()
        for line in file:
            bahan_count += 1
    # Memproses setiap baris dan menyimpannya di database.
    with open(os.path.join(variables.load_folder, "bahan_bangunan.csv")) as file:
        file.readline()
        for i in range(bahan_count):
            name, description, quantity = split(strip(file.readline()), ';')
            quantity = int(quantity)
            if name == "pasir":
                sand_description = description
                bahan_list.sand += quantity
            elif name == "batu":
                stone_description = description
                bahan_list.stone += quantity
            else:
                water_description = description
                bahan_list.water += quantity

# Melakukan penyimpanan.
def save(location):
    with open(os.path.join(location, "bahan_bangunan.csv"), 'w') as file:
        file.write("nama;deskripsi;jumlah\n")
        file.write(f"pasir;{sand_description};{bahan_list.sand}\n")
        file.write(f"batu;{stone_description};{bahan_list.stone}\n")
        file.write(f"air;{water_description};{bahan_list.water}\n")

# Menambahkan bahan pada database.
def add_bahan(name, quantity):
    global bahan_list
    if name == "pasir":
        bahan_list.sand += quantity
    elif name == "batu":
        bahan_list.stone += quantity
    else:
        bahan_list.water += quantity