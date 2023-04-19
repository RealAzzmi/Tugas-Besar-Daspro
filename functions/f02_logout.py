import variables

def run():
    if not variables.login:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    else:
        variables.login = False
        print(f"Logout dari akun {variables.username} berhasil!")