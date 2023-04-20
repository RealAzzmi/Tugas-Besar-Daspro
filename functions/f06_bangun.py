import variables
import database.user, database.bahan_bangunan, database.candi
from constants import MAX_CANDI, MIN_RAND, MAX_RAND
import random

def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "jin_pembangun":
        print("Anda tidak mempunyai akses; hanya jin pembangun yang bisa membangun candi.")
    else:
        sand_candi = random.randint(MIN_RAND, MAX_RAND)
        stone_candi = random.randint(MIN_RAND, MAX_RAND)
        water_candi = random.randint(MIN_RAND, MAX_RAND)
        print(f"Bahan bangunan yang dimiliki: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
        print(f"Bahan bangunan yang dibutuhkan untuk membuat 1 candi: (pasir: {sand_candi}, batu: {stone_candi}, air: {water_candi}).")
        if not(sand_candi <= database.bahan_bangunan.bahan_list.sand and stone_candi <= database.bahan_bangunan.bahan_list.stone and water_candi <= database.bahan_bangunan.bahan_list.water):
            print("Bahan bangunan tidak mencukupi. Candi tidak bisa dibangun!")
            return
        database.bahan_bangunan.bahan_list.sand -= sand_candi
        database.bahan_bangunan.bahan_list.stone -= stone_candi
        database.bahan_bangunan.bahan_list.water -= water_candi
        if database.candi.candi_list.size == MAX_CANDI:
            print(f"Jumlah candi sudah mencapai nilai maksimum ({MAX_CANDI}). Candi akan dibangun dan bahan bangunan akan berkurang, namun candi tidak akan tercatat.")
            print(f"Sisa bahan bangunan yang dimiliki: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
            print(f"Sisa candi yang perlu dibangun: 0.")
            return
        database.candi.add_candi(database.candi.smallest_unavailable_id(), variables.username, sand_candi, stone_candi, water_candi)
        print("Candi berhasil dibangun.")
        print(f"Sisa bahan bangunan yang dimiliki: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
        print(f"Sisa candi yang perlu dibangun: {MAX_CANDI - database.candi.candi_list.size}.")


