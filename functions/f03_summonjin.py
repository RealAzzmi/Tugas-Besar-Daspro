import variables
import database.user
from constants import MAX_JIN, MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH

def run():
     # Mengecek jika sudah login.
    if variables.login == False:
        print("Anda belum login.")
    # Mengecek apakah usernya Bandung Bondowoso.
    elif variables.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya Bandung Bondowoso yang bisa summon jin.")
    # Mengecek apakah jumlah jin sudah mencapai MAX_JIN (100).
    # Jumlah jin adalah jumlah user dikurangi 2 karena terdapat Bandung dan Roro.
    elif database.user.user_list.size - 2 == MAX_JIN:
        print(f"Jumlah jin telah maksimal ({MAX_JIN} jin). Bandung tidak dapat meng-summon lebih dari itu.")
    else:
        print("Jenis jin yang dapat dipanggil:\n\t(1) Pengumpul - Bertugas mengumpulkan bahan bangunan.\n\t(2) Pembangun - Bertugas membangun candi.\n")
        
        # Input nomor jenis jin.
        nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        # Looping sampai nomor jenis jin valid.
        while nomor_jenis_jin != 1 and nomor_jenis_jin != 2:
            print(f"Tidak ada jenis jin bernomor \"{nomor_jenis_jin}\"!")
            nomor_jenis_jin = int(input("Masukkan nomor jenis jin yang ingin dipanggil: "))
        
        if nomor_jenis_jin == 1:
            print("Memilih jin \"Pengumpul\".")
            # Jika nomornya 1, rolenya adalah jin pengumpul.
            role = "jin_pengumpul"
        else:
            print("Memilih jin \"Pembangun\".")
            # Jika nomornya 2, rolenya adalah jin pembangun.
            role = "jin_pembangun"

        # Input username jin.
        username = input("Masukkan username jin: ")
        # is_exist adalah boolean sedangkan user adalah tipe bentukan User. 
        is_exist, user = database.user.is_user_exist(username)
        # Mengecek apakah username eksis atau username tidak valid.
        while is_exist or not database.user.is_username_valid(username):
            # Jika username eksis, ulangi.
            if is_exist: 
                print(f"Username \"{user.username}\" sudah diambil!")
            # Jika username tidak eksis tetapi username tidak valid, ulangi.
            else:
                print(f"Username tidak valid.")
            username = input("Masukkan username jin: ")
            is_exist, user = database.user.is_user_exist(username)

        # Username sudah valid. Sekarang, dilakukan input password.
        password = input("Masukkan password jin: ")
        # Mengecek apakah password valid. Panjangnya harus >= 5 dan <= 25. 
        is_password_valid = database.user.is_password_valid(password)
        # Looping sampai password valid.
        while not is_password_valid:
            print(f"Panjang password harus {MIN_PASSWORD_LENGTH}-{MAX_PASSWORD_LENGTH} karakter.")
            password = input("Masukkan password jin: ")
            is_password_valid = database.user.is_password_valid(password)
        # Username, password, dan role sudah valid semua. Dilakukan proses penambahan pada database user.
        database.user.add_user(username, password, role)

        print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")
