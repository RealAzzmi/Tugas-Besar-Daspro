import variabel

def run():
    if not variabel.login:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout")
    else:
        variabel.login = False
        print(f"Logout dari akun {variabel.username} berhasil!")