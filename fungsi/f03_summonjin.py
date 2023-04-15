import variabel
import database


def run():
    if variabel.login == False:
        print("Anda belum login")
    elif variabel.role != "bandung_bondowoso":
        print("Anda tidak mempunyai akses; hanya bandung bondowoso yang bisa summon jin")
    elif database.jin_count == 100:
        print("Jumlah Jin telah maksimal (100 jin). Bandung tidak dapat men-summon lebih dari itu.")
    else:
        print("Jenis jin yang dapat dipanggil:\n\t(1) Pengumpul - Bertugas mengumpulkan bahan bangunan\n\t(2) Pembangun - Bertugas membangun candi\n")
        
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
        is_exist, user = database.is_user_exist(username)
        while is_exist:
            print(f"Username \"{user.username}\" sudah diambil!")
            username = input("Masukkan username jin: ")
            is_exist, user = database.is_user_exist(username)

        password = input("Masukkan password jin: ")
        is_password_valid = database.is_password_valid(password)
        while not is_password_valid:
            print(f"Password panjangnya harus 5-25 karakter")
            password = input("Masukkan password jin: ")
            is_password_valid = database.is_password_valid(password)
        
        database.add_user(username, password, role)
        print("\nMengumpulkan sesajen...\nMenyerahkan sesajen...\nMembacakan mantra...\n")
        print(f"Jin {username} berhasil dipanggil!")
