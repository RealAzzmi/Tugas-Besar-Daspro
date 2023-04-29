import variables
import database.user

def run():
    # Mengecek jika belum login.
    if variables.login == True:
        print(f"Login gagal!\nAnda telah login dengan username {variables.username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
    else:
        # input username dan password dari console.
        username = input("Username: ")
        password = input("Password: ")

        # is_exist adalah boolean sedangkan user adalah tipe bentukan User. 
        is_exist, user = database.user.is_user_exist(username)
        
        # Mengecek jika user dengan username yang diinput sebelumnya eksis.
        if is_exist:
            # Jika password benar, login berhasil.
            if user.password == password:
                print(f"Selamat datang, {username}!\nMasukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                # Menyimpan identitas user yang sedang login di variabel global agar dapat digunakan
                # oleh fungsi lain seperti untuk mengecek permission menjalankan command, dll. 
                variables.username = user.username
                variables.password = user.password
                variables.role = user.role
                variables.login = True
            # Jika username yang diinput eksis, tapi password salah.
            else:
                print("Password salah!")
        # Jika username yang diinput tidak eksis.
        else:
            print(f"Username tidak terdaftar.")