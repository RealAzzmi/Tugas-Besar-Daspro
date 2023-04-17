import variabel
import database

def run():
    if variabel.login == True:
        print(f"Login gagal!\nAnda telah login dengan username {variabel.username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
    else:
        username = input("Username APA: ")
        password = input("Password: ")

        is_exist, user = database.is_user_exist(username)
        if is_exist:
            if user.password == password:
                print(f"Selamat datang, {username}!\nMasukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                variabel.username = user.username
                variabel.password = user.password
                variabel.role = user.role
                variabel.login = True
            else:
                print("Password salah!")
        else:
            print(f"Username tidak terdaftar")