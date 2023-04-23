import database.user, database.bahan_bangunan, database.candi
import variables

def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "roro_jonggrang" :
        print("Anda tidak mempunyai akses; hanya Roro Jonggrang yang bisa \"menghancurkan candi\".")
    else:
        id_candi = int(input("Masukkan ID candi: "))
        is_exist, candi = database.candi.is_candi_exist(id_candi)
        if not is_exist:
            print("Tidak ada candi dengan ID tersebut.")
            return
        confirmation = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        while not(confirmation == 'n' or confirmation == 'N' or confirmation == 'y' or confirmation == 'Y'):
            confirmation = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/y/N/n)? ")
        if confirmation == 'y' or confirmation == 'Y':
            database.candi.erase_candi_by_id(id_candi)
            print("Candi berhasil dihapus.")
        else:
            print("Candi tidak jadi dihapus.")