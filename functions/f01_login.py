import variables
import database.user

def run():
    if variables.login == True:
        print(f"Login gagal!\nAnda telah login dengan username {variables.username}, silahkan lakukan \"logout\" sebelum melakukan login kembali.")
    else:
        username = input("Username: ")
        password = input("Password: ")

        is_exist, user = database.user.is_user_exist(username)
        if is_exist:
            if user.password == password:
                print(f"Selamat datang, {username}!\nMasukkan command \"help\" untuk daftar command yang dapat kamu panggil.")
                variables.username = user.username
                variables.password = user.password
                variables.role = user.role
                variables.login = True
            else:
                print("Password salah!")
        else:
            print(f"Username tidak terdaftar.")