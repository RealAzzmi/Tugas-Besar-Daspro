import variables

def run():
    # Mengecek jika sudah login.
    if not variables.login:
        print("Logout gagal!\nAnda belum login, silahkan login terlebih dahulu sebelum melakukan logout.")
    else:
        variables.login = False # Logout menge-set variabel global menjadi false sehingga di program tercatat bahwa 
                                # user tidak dalam keadaan login 
        print(f"Logout dari akun {variables.username} berhasil!")