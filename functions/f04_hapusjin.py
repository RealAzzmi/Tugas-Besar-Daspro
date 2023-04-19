import variables
import database.user
import database.candi

def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa hapus jin.")
    else:
        username = input("Masukkan username jin: ")
        is_exist, user = database.user.is_user_exist(username)
        if not is_exist:
            print("Tidak ada jin dengan username tersebut.")
            return
        elif user.role != "jin_pengumpul" and user.role != "jin_pembangun":
            print(f"{user.username} bukan jin.")
            return
        confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        while confirmation != 'Y' and confirmation != 'y' and confirmation != 'N' and confirmation != 'n':
            print("Konfirmasi tidak valid. Ulangi lagi dengan merespon Y/y/N/n.")
            confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        if confirmation == 'Y' or confirmation == 'y':
            database.user.erase_user(username)
            database.candi.erase_candi_by_builder(username)
            print("Jin telah berhasil dihapus dari alam gaib beserta candi yang dibuatnya.")
        else:
            print(f"Jin {username} tidak jadi dihapus.")

