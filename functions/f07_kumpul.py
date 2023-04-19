import variables
import database.user, database.bahan_bangunan
from constants import MAX_CANDI, MIN_RAND, MAX_RAND
import random

def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "jin_pengumpul":
        print("Anda tidak mempunyai akses; hanya jin pengumpul yang bisa kumpul bahan.")
    else:
        sand_candi = random.randint(MIN_RAND, MAX_RAND)
        stone_candi = random.randint(MIN_RAND, MAX_RAND)
        water_candi = random.randint(MIN_RAND, MAX_RAND)
        print(f"Bahan bangunanan yang dimilki sebelum kumpul bahan: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
        print(f"Bahan bangunan yang didapatkan: (pasir: {sand_candi}, batu: {stone_candi}, air: {water_candi}).")
        database.bahan_bangunan.bahan_list.sand += sand_candi
        database.bahan_bangunan.bahan_list.stone += stone_candi
        database.bahan_bangunan.bahan_list.water += water_candi
        print(f"Bahan bangunanan yang dimilki setelah kumpul bahan: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")