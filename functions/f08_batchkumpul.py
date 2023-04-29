import variables
import database.user, database.bahan_bangunan, database.candi
from constants import MIN_RAND, MAX_RAND
import random

def run():
    # Mengecek apakah sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah rolenya adalah Bandung Bondowoso.
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa \"batch kumpul\" candi.")
    else:
        # Menghitung jumlah jin pengumpul.
        jin_pengumpul_count = database.user.user_count(database.user.user_equality_by_role, role="jin_pengumpul")
        # Mengecek apakah terdapat jin pengumpul.
        if jin_pengumpul_count == 0:
            print("Kumpul gagal. Anda tidak punya jin pengumpul. Silakan summon terlebih dahulu.")
            return
        # Menyimpan total pasir, batu, dan air yang di-generate.
        total_sand = 0
        total_stone = 0
        total_water = 0
        # Dilakukan looping setiap jin pengumpul untuk melakukan pengumpulan bahan bangunan.
        for i in range(jin_pengumpul_count):
            total_sand += random.randint(MIN_RAND, MAX_RAND)
            total_stone += random.randint(MIN_RAND, MAX_RAND)
            total_water += random.randint(MIN_RAND, MAX_RAND)
        print(f"Mengerahkan {jin_pengumpul_count} jin pengumpul untuk mengumpulkan bahan.")
        print(f"Ditemukan {total_sand} pasir, {total_stone} batu, dan {total_water} air.")
        # Hasil batch kumpul disimpan pada database.
        database.bahan_bangunan.bahan_list.sand += total_sand
        database.bahan_bangunan.bahan_list.stone += total_stone
        database.bahan_bangunan.bahan_list.water += total_water

