import variables
import database.user, database.bahan_bangunan, database.candi
from constants import MAX_CANDI, MIN_RAND, MAX_RAND
import random

def run():
    # Mengecek apakah sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah role adalah jin pembangun.
    elif variables.role != "jin_pembangun":
        print("Anda tidak mempunyai akses; hanya jin pembangun yang bisa membangun candi.")
    else:
        # Meng-generate bahan bangunan yang dibutuhkan untuk membuat candi secara acak dari
        # MIN_RAND (1) sampai MAX_RAND (5) inklusif.
        sand_candi = random.randint(MIN_RAND, MAX_RAND)
        stone_candi = random.randint(MIN_RAND, MAX_RAND)
        water_candi = random.randint(MIN_RAND, MAX_RAND)
        print(f"Bahan bangunan yang dimiliki: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
        print(f"Bahan bangunan yang dibutuhkan untuk membuat 1 candi: (pasir: {sand_candi}, batu: {stone_candi}, air: {water_candi}).")
        # Mengecek apakah bahan bangunan yang dimiliki cukup untuk membuat candinya.
        # Jika tidak cukup, program meng-return.
        if not(sand_candi <= database.bahan_bangunan.bahan_list.sand and stone_candi <= database.bahan_bangunan.bahan_list.stone and water_candi <= database.bahan_bangunan.bahan_list.water):
            print("Bahan bangunan tidak mencukupi. Candi tidak bisa dibangun!")
            return
        # Bahan bangunan yang dimiliki cukup membuat candinya sehingga stock bahan bangunan dikurangkan
        # dengan bahan yang dibutuhkankan untuk membuat candinya.
        database.bahan_bangunan.bahan_list.sand -= sand_candi
        database.bahan_bangunan.bahan_list.stone -= stone_candi
        database.bahan_bangunan.bahan_list.water -= water_candi
        # Jika total candi (sebelum dibangun) sudah mencapai maksimum (100), candi tidak
        # akan tercatat di database namun bahan bangunan tetap berkurang.
        if database.candi.candi_list.size == MAX_CANDI:
            print(f"Jumlah candi sudah mencapai nilai maksimum ({MAX_CANDI}). Candi akan dibangun dan bahan bangunan akan berkurang, namun candi tidak akan tercatat.")
            print(f"Sisa bahan bangunan yang dimiliki: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
            print(f"Sisa candi yang perlu dibangun: 0.")
            return
        # Total candi (sebelum dibangun) belum mencapai maksimum (100) sehingga candi
        # dapat dimasukkan ke dalam database dengan nomor id terkecil yang tersedia.
        database.candi.add_candi(database.candi.smallest_unavailable_id(), variables.username, sand_candi, stone_candi, water_candi)
        print("Candi berhasil dibangun.")
        print(f"Sisa bahan bangunan yang dimiliki: (pasir: {database.bahan_bangunan.bahan_list.sand}, batu: {database.bahan_bangunan.bahan_list.stone}, air: {database.bahan_bangunan.bahan_list.water}).")
        print(f"Sisa candi yang perlu dibangun: {MAX_CANDI - database.candi.candi_list.size}.")


