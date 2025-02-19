import database.user, database.bahan_bangunan, database.candi
import variables

def run():
    # Mengecek apakah sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengeceh apakah rolenya adalah Roro Jonggrang.    
    elif variables.role != "roro_jonggrang" :
        print("Anda tidak mempunyai akses; hanya Roro Jonggrang yang bisa \"menghancurkan candi\".")
    # Mengecek apakah candi dengan ID tersebut ada atau tidak.
    else:
        id_candi = int(input("Masukkan ID candi: "))
        is_exist, candi = database.candi.is_candi_exist(id_candi)
        if not is_exist:
            print("Tidak ada candi dengan ID tersebut.")
            return
        # Mengecek apakah user ingin menghancurkan candi atau tidak.
        confirmation = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/N)? ")
        while not(confirmation == 'n' or confirmation == 'N' or confirmation == 'y' or confirmation == 'Y'):
            confirmation = input(f"Apakah anda yakin ingin menghancurkan candi ID: {id_candi} (Y/y/N/n)? ")
        if confirmation == 'y' or confirmation == 'Y':
            database.candi.erase_candi_by_id(id_candi)
            print("Candi berhasil dihapus.")
        else:
            print("Candi tidak jadi dihapus.")