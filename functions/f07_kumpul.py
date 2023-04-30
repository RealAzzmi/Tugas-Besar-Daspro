import variables
import database.user, database.bahan_bangunan
from constants import MIN_RAND, MAX_RAND
import random

def run():
    # Mengecek apakah user sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah rolenya adalah jin pengumpul.
    elif variables.role != "jin_pengumpul":
        print("Anda tidak mempunyai akses; hanya jin pengumpul yang bisa kumpul bahan.")
    else:
        # Meng-generate bahan yang dikumpulkan oleh jin yang bersangkutan diantara
        # MIN_RAND (1) dan MAX_RAND (5) inklusif. 
        sand_candi = random.randint(MIN_RAND, MAX_RAND)
        stone_candi = random.randint(MIN_RAND, MAX_RAND)
        water_candi = random.randint(MIN_RAND, MAX_RAND)
        print(f"Bahan bangunan yang dimiliki sebelum kumpul bahan: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
        print(f"Bahan bangunan yang didapatkan: (pasir: {sand_candi}, batu: {stone_candi}, air: {water_candi}).")
        # Database diupdate dengan menambahkan bahan yang dikumpulkan oleh jin yang bersangkutan.
        database.bahan_bangunan.bahan_list.sand += sand_candi
        database.bahan_bangunan.bahan_list.stone += stone_candi
        database.bahan_bangunan.bahan_list.water += water_candi
        print(f"Bahan bangunan yang dimiliki setelah kumpul bahan: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")