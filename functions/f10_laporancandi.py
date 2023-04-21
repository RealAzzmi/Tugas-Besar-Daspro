import database.user, database.bahan_bangunan, database.candi
import variables
import random
from constants import MAX_CANDI

def run():
    if variables.login = False:
        print("Anda belum login.")
    elif variables.role != "bandung_bondowoso" :
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa \"ambil laporan candi\".")
    else:
        total_candi = 0
        total_pasir = 0
        total_batu = 0
        total_air = 0
        id_candi_termahal = 0
        harga_candi_termahal = 0
        id_candi_termurah = 0
        harga_candi_termurah = 0

        # Cek semua candi
        for i in range(database.candi, MAX_CANDI):
            if database.candi [i][1] is not None:
                pasir = database.candi[i][2]
                batu = database.candi[i][3]
                air = database.candi[i][4]

                total_pasir += pasir
                total_batu += batu
                total_air += air
                total_candi += 1

                harga_candi = 10000 * pasir + 15000* batu + 7500 * air

                if harga_candi > harga_candi_termahal:
                    id_candi_termahal = database.candi[i][0]
                    harga_candi_termahal = harga_candi
                if harga_candi < harga_candi_termurah:
                    id_candi_termurah = database.candi[i][0]
                    harga_candi_termurah = harga_candi
        print()
        print(f"Total Candi: {total_candi}")
        print(f"Total Pasir yang digunakan: {total_pasir}")
        print(f"Total Batu yang digunakan: {total_batu}")
        print(f"Total Air yang digunakan: {total_air}")

        if total_candi == 0:
            print(f"ID Candi Termahal: -")
            print(f"ID Candi Termurah: -")
        else:
            print(f"ID Candi Termahal: {id_candi_termahal} (Rp {harga_candi_termahal})")
            print(f"ID Candi Termurah: {id_candi_termurah} (Rp {harga_candi_termurah})")