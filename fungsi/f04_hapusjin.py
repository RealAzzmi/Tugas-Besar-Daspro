import variabel
import database

def run():
    if variabel.login == False:
        print("Anda belum login")
    elif variabel.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya bandung bondowoso yang bisa menghilangkan jin")
    else:
        username = input("Masukkan username jin: ")
        is_exist, user = database.is_user_exist(username)
        if not is_exist:
            print("Tidak ada jin dengan username tersebut.")
            return
        elif user.role != "jin_pengumpul" and user.role != "jin_pembangun":
            print(f"{user.username} bukan jin")
            return
        confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        while confirmation != 'Y' and confirmation != 'y' and confirmation != 'N' and confirmation != 'n':
            print("Konfirmasi tidak valid. Ulangi lagi dengan merespon Y/y/N/n")
            confirmation = input(f"Apakah anda yakin ingin menghapus jin dengan username {username} (Y/N)? ")
        if confirmation == 'Y' or confirmation == 'y':
            database.erase_user(user.username, user.password, user.role)
            # Belum implementasi hapus candi
            print("Jin telah berhasil dihapus dari alam gaib")
        else:
            print(f"Jin {username} tidak jadi dihapus")

