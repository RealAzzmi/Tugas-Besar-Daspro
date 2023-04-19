import variables
import database.user

def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa ubah role jin.")
    else:
        username = input("Masukkan username jin: ")
        is_exist, user = database.user.is_user_exist(username)
        if not is_exist:
            print("Tidak ada jin dengan username tersebut.")
            return
        elif user.role != "jin_pengumpul" and user.role != "jin_pembangun":
            print(f"{user.username} bukan jin")
            return
        
        role_awal = user.role
        role_akhir = "jin_pembangun" if role_awal == "jin_pengumpul" else "jin_pengumpul"

        confirmation = input(f"Jin ini bertipe \"{role_awal}\". Yakin ingin mengubah ke tipe \"{role_akhir}\" (Y/N)? ")
        while confirmation != 'Y' and confirmation != 'y' and confirmation != 'N' and confirmation != 'n':
            print("Konfirmasi tidak valid. Ulangi lagi dengan merespon Y/y/N/n.")
            confirmation = input(f"Jin ini bertipe \"{role_awal}\". Yakin ingin mengubah ke tipe \"{role_akhir}\" (Y/N)? ")
        if confirmation == 'Y' or confirmation == 'y':
            user.role = role_akhir
            print(f"Jin {username} telah berhasil diubah role.")
        else:
            print(f"Jin {username} tidak jadi diubah role.")