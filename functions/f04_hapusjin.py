import variables
import database.user
import database.candi

def run():
    # Mengecek jika sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah usernya Bandung Bondowoso.
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa hapus jin.")
    else:
        # Input username jin.
        username = input("Masukkan username jin: ")
        # is_exist adalah boolean sedangkan user adalah tipe bentukan User
        is_exist, user = database.user.is_user_exist(username)
        # Mengecek jika user dengan username yang diinput eksis.
        if not is_exist:
            print("Tidak ada jin dengan username tersebut.")
            return
        # Mengecek jika username yang eksis tersebut adalah jin.
        elif user.role != "jin_pengumpul" and user.role != "jin_pembangun":
            print(f"{user.username} bukan jin.")
            return
        # Input konfirmasi dan looping hingga mendapatkan respon yang valid Y/y/N/n.
        confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        while confirmation != 'Y' and confirmation != 'y' and confirmation != 'N' and confirmation != 'n':
            print("Konfirmasi tidak valid. Ulangi lagi dengan merespon Y/y/N/n.")
            confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        if confirmation == 'Y' or confirmation == 'y':
            # Jika setuju, akan dicari entry pada database yang memiliki username yang bersangkutan
            # dan akan dihapus entry tersebut.
            database.user.erase_user(username)
            # Candi-candi yang dibuat oleh user dengan username yang diinput juga akan dihapus dari database.
            database.candi.erase_candi_by_builder(username)
            print("Jin telah berhasil dihapus dari alam gaib beserta candi yang dibuatnya.")
        else:
            # Jika tidak setuju, jin tidak jadi dihapus.
            print(f"Jin {username} tidak jadi dihapus.")

