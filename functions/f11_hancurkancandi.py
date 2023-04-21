import database.user, database.bahan_bangunan, database.candi
import variables
import random
from constants import MAX_CANDI

def run():
    if variables.login = False:
        print("Anda belum login.")
    elif variables.role != "roro_jonggrang" :
        print("Anda tidak mempunyai akses; hanya Roro Jonggrang yang bisa \"menghancurkan candi\".")
    else:
        id_candi = int(input("Masukkan ID candi: "))
        candi_ditemukan = False
    
    # Cari id candi
    for i in range(database.candi, MAX_CANDI):
        if database.candi[i][0] == id_candi:
            if database.candi[i][1] is not None:
                candi_ditemukan = True
                confirm = ""

                # konfirmasi
                while confirm.lower() != "y" and confirm.lower != "n":
                    confirm = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N) ")

                print()

                if confirm.lower() == "y":
                        # hapus candi
                        data_candi = hapus_candi (i, data_candi)
                        print("Candi telah berhasil dihancurkan.")

                    else:
                        print("Candi tidak berhasil dihancurkan.")

                break

        if not candi_ditemukan:
            print()
            print("Tidak ada candi dengan ID tersebut.")

    return data_candi 