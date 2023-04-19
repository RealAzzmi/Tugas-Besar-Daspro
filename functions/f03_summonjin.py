import variables
import database.user
from constants import MAX_JIN, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH

def run():
    if variables.login == False:
        print("Anda belum login.")
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa summon jin.")
    elif database.user.user_list.size - 2 == MAX_JIN: # Dikurangi 2 karena terdapat Bandung dan Roro.
        print(f"Jumlah jin telah maksimal ({MAX_JIN} jin). Bandung tidak dapat meng-summon lebih dari itu.")
    else:
        print("Jenis jin yang dapat dipanggil:\n\t(1) Pengumpul - Bertugas mengumpulkan bahan bangunan.\n\t(2) Pembangun - Bertugas membangun candi.\n")
        
        nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        while nomor_jenis_jin != 1 and nomor_jenis_jin != 2:
            print(f"Tidak ada jenis jin bernomor \"{nomor_jenis_jin}\"!")
            nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        
        if nomor_jenis_jin == 1:
            print("Memilih jin \"Pengumpul\".")
            role = "jin_pengumpul"
        else:
            print("Memilih jin \"Pembangun\".")
            role = "jin_pembangun"

        username = input("Masukkan username jin: ")
        is_exist, user = database.user.is_user_exist(username)
        while is_exist or not database.user.is_username_valid(username):
            if is_exist:
                print(f"Username \"{user.username}\" sudah diambil!")
            else:
                print(f"Username tidak valid.")
            username = input("Masukkan username jin: ")
            is_exist, user = database.user.is_user_exist(username)

        password = input("Masukkan password jin: ")
        is_password_valid = database.user.is_password_valid(password)
        while not is_password_valid:
            print(f"Panjang password harus {MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH} karakter.")
            password = input("Masukkan password jin: ")
            is_password_valid = database.user.is_password_valid(password)
        
        database.user.add_user(username, password, role)

        print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")
