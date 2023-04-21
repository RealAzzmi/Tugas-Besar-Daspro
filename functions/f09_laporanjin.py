import variables
import database.user, database.candi, database.bahan_bangunan
from constants import MAX_JIN


def alphabetically_correct(first_name, second_name):
    is_first_name_shorter = True
    length = len(first_name)

    if len(second_name) < len(first_name):
        length = len(second_name)
        is_first_name_shorter = False

    for i in range(length):
        if ord(first_name[i]) < ord(second_name[i]):
            return True
        elif ord(second_name[i]) < ord(first_name[i]):
            return False

    return is_first_name_shorter


def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa \"ambil laporan jin\".")
    else:
        # hitung semua jin
        jin_pembangun_count = database.user.user_count(database.user.user_equality_by_role, role="jin_pembangun")
        jin_pengumpul_count = database.user.user_count(database.user.user_equality_by_role, role="jin_pengumpul")
        jin_count = jin_pembangun_count + jin_pengumpul_count
        total_candi = 0

        # bikin array nama jin dan urutin sesuai alphabet
        jin_names = []  # nama-nama jin

        for i in range(jin_count-1):
            for j in range(i+1, jin_count-1):
                if not alphabetically_correct(jin_names[i], jin_names[j]):
                    jin_names[i], jin_names[j] = jin_names[j], jin_names[i]

        # menghitung total candi
        for i in range(MAX_JIN):
            total_candi += database.candi.candi_count(jin_names[i])

        if total_candi == 0 and jin_pembangun_count == 0:
            best_jin_name = "-"
            worst_jin_name = "-"
        else:
            for i in range(jin_count):
                is_first_jin_found = False
                # cari jin yang pembangun
                if database.user.user_equality_by_role(jin_names[i], role = "jin_pembangun") or database.candi.candi_count(jin_names[i]) != 0:
                    if not is_first_jin_found:
                        best_jin_candi = database.candi.candi_count(jin_names[i])
                        worst_jin_candi = database.candi.candi_count(jin_names[i])
                        best_jin_name = jin_names[i]
                        worst_jin_name = jin_names[i]
                        is_first_jin_found = True
                    else:
                        if database.candi.candi_count(jin_names[i]) > best_jin_candi:
                            best_jin_candi = database.candi.candi_count(jin_names[i])
                            best_jin_name = jin_names[i]
                        elif database.candi.candi_count(jin_names[i]) < best_jin_candi:
                            worst_jin_candi = database.candi.candi_count(jin_names[i])
                            worst_jin_name = jin_names[i]

        total_sand = database.bahan_bangunan.bahan_list.sand
        total_stone = database.bahan_bangunan.bahan_list.stone
        total_water = database.bahan_bangunan.bahan_list.water

        print()
        print(f"> Total Jin: {jin_count}")
        print(f"> Total Jin Pengumpul: {jin_pengumpul_count}")
        print(f"> Total Jin Pembangun: {jin_pembangun_count}")
        print(f"> Jin Terajin: {best_jin_name}")
        print(f"> Jin Termalas: {worst_jin_name}")
        print(f"> Jumlah Pasir: {total_sand} unit")
        print(f"> Jumlah Air: {total_water} unit")
        print(f"> Jumlah Batu: {total_stone} unit")