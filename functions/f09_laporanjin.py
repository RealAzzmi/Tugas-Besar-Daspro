import variables
import database.user, database.candi, database.bahan_bangunan
from constants import MAX_CANDI

def run():
    # Mengecek apakah sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah rolenya adalah Bandung Bondowoso.
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa \"ambil laporan jin\".")
    else:
        # Menghitung jumlah jin pembangun, jin pengumpul, dan total jin.
        jin_pembangun_count = database.user.user_count(database.user.user_equality_by_role, role="jin_pembangun")
        jin_pengumpul_count = database.user.user_count(database.user.user_equality_by_role, role="jin_pengumpul")
        jin_count = jin_pembangun_count + jin_pengumpul_count

        best_jin = '-'
        best_jin_candi = 0
        # Menentukan Jin Terajin
        for i in range(2, database.user.user_list.size):
            username = database.user.user_list.array[i].username
            candi_count = database.candi.candi_count(username)
            if candi_count > best_jin_candi:
                best_jin = username
                best_jin_candi = candi_count
            elif candi_count == best_jin_candi and username < best_jin:
                best_jin = username

        worst_jin = '-'
        worst_jin_candi = MAX_CANDI
        # Menentukan Jin Termalas
        for i in range(2, database.user.user_list.size):
            username = database.user.user_list.array[i].username
            candi_count = database.candi.candi_count(username)
            if candi_count == 0 and database.user.user_list.array[i].role != "jin_pembangun":
                continue
            if candi_count < worst_jin_candi:
                worst_jin = username
                worst_jin_candi = candi_count
            elif candi_count == worst_jin_candi and username > worst_jin:
                worst_jin = username
        # Menghitung total bahan bangunan
        total_sand = database.bahan_bangunan.bahan_list.sand
        total_stone = database.bahan_bangunan.bahan_list.stone
        total_water = database.bahan_bangunan.bahan_list.water

        print()
        print(f"> Total Jin: {jin_count}")
        print(f"> Total Jin Pengumpul: {jin_pengumpul_count}")
        print(f"> Total Jin Pembangun: {jin_pembangun_count}")
        print(f"> Jin Terajin: {best_jin}")
        print(f"> Jin Termalas: {worst_jin}")
        print(f"> Jumlah Pasir: {total_sand} unit")
        print(f"> Jumlah Batu: {total_stone} unit")
        print(f"> Jumlah Air: {total_water} unit")