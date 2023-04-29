import database.user, database.bahan_bangunan, database.candi
import variables
import random
from constants import MAX_CANDI, MIN_RAND, MAX_RAND
from algorithms.math import max

    
def run():
    # Mengecek apakah user sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah rolenya adalah Bandung Bondowoso.
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa \"batch bangun\" candi.")
    else:
        # Menghitung jumlah jin pembangun yang terdapat.
        jin_pembangun_count = database.user.user_count(database.user.user_equality_by_role, role="jin_pembangun")
        # Mengecek apakah terdapat jin pembangun.
        if jin_pembangun_count == 0:
            print("Bangun gagal. Anda tidak punya jin pembangun. Silakan summon terlebih dahulu.")
            return

        # new_candi menyimpan bahan bangunan yang dibutuhkan oleh setiap candi yang dibuat setiap jin pembangun.
        new_candi = [None for i in range(jin_pembangun_count)]
        total_sand = 0
        total_stone = 0
        total_water = 0
        idx = 0
        # Dilakukan looping setiap jin pembangun dan di-generate bahan bangunan yang diperlukan untuk
        # candinya.
        for i in range(database.user.user_list.size):
            if database.user.user_list.array[i].role == "jin_pembangun":
                new_candi[idx] = random.randint(MIN_RAND, MAX_RAND), random.randint(MIN_RAND, MAX_RAND), random.randint(MIN_RAND, MAX_RAND)
                total_sand += new_candi[idx][0]
                total_stone += new_candi[idx][1]
                total_water += new_candi[idx][2]
                idx += 1
        print(f"Mengerahkan {jin_pembangun_count} jin untuk membangun {jin_pembangun_count} candi dengan total bahan {total_sand} pasir, {total_stone} batu, dan {total_water} air.")
        # Mengecek apakah kekurangan bahan bangunan.
        if not(database.bahan_bangunan.bahan_list.sand >= total_sand and database.bahan_bangunan.bahan_list.stone >= total_stone and database.bahan_bangunan.bahan_list.water >= total_water):
            needed_sand = max(0, total_sand - database.bahan_bangunan.bahan_list.sand)
            needed_stone = max(0, total_stone - database.bahan_bangunan.bahan_list.stone)
            needed_water = max(0, total_water - database.bahan_bangunan.bahan_list.water)
            if needed_sand != 0 and needed_stone != 0 and needed_water != 0:
                print(f"Bangun gagal. Kurang {needed_sand} pasir, {needed_stone} batu, dan {needed_water} air.")
            elif needed_sand == 0 and needed_stone == 0:
                print(f"Bangun gagal. Kurang {needed_water} air.")
            elif needed_sand == 0 and needed_water == 0:
                print(f"Bangun gagal. Kurang {needed_stone} batu.")
            elif needed_stone == 0 and needed_water == 0:
                print(f"Bangun gagal. Kurang {needed_sand} pasir.")
            elif needed_sand == 0:
                print(f"Bangun gagal. Kurang {needed_stone} batu dan {needed_water} air.")
            elif needed_stone == 0:
                print(f"Bangun gagal. Kurang {needed_sand} pasir dan {needed_water} air.")
            elif needed_water == 0:
                print(f"Bangun gagal. Kurang {needed_sand} pasir dan {needed_stone} batu.")
            return
        print(f"Jin berhasil membangun {jin_pembangun_count} candi.")
        idx = 0
        # Dilakukan looping setiap jin pembangun agar database candi diupdate dengan candi
        # yang dibangun oleh jin yang bersangkutan.
        for i in range(database.user.user_list.size):
            # Jika jumlah candi sudah mencapai nilai maksimal tetapi belum semua candi
            # yang dibuat oleh beberapa jin pembangun belum dimasukkan ke database candi, maka
            # program akan tidak mencatat candinya namun bahan bangunan akan tetap berkurang
            # akibat dibangunnya candi yang bersangkutan. 
            if idx != jin_pembangun_count and database.candi.candi_list.size == MAX_CANDI:
                print("Terdapat candi yang terbangun yang tidak akan tercatat karena melebihi jumlah maksimum candi. Namun, bahan bangunan akan tetap berkurang.")
                break
            if database.user.user_list.array[i].role == "jin_pembangun":
                database.candi.add_candi(database.candi.smallest_unavailable_id(), database.user.user_list.array[i].username, new_candi[idx][0], new_candi[idx][1], new_candi[idx][2])
                idx += 1
        # Bahan bangunan dikurangi akibat pembangunan candi-candi baru.  
        database.bahan_bangunan.bahan_list.sand -= total_sand
        database.bahan_bangunan.bahan_list.stone -= total_stone
        database.bahan_bangunan.bahan_list.water -= total_water
