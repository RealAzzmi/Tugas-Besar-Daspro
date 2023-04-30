import variables
import database.candi
from constants import MAX_CANDI
import sys

def run():
    # Mengecek apakah sudah login
    if variables.login == False:
        print("Anda belum login")
    # Mengecek apakah role-nya Roro Jonggrang
    elif variables.role != "roro_jonggrang":
        print("Anda tidak mempunyai akses; hanya Roro Jonggrang yang memiliki kemampuan ini.")
    else:
        # Jika kondisi jumlah candi kurang dari 100 (jumlah maksimal candi)
        if database.candi.candi_list.size < MAX_CANDI:
            print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {database.candi.candi_list.size}

Selamat, Roro Jonggrang memenangkan permainan!

*Bandung Bondowoso angry noise*
Roro Jonggrang dikutuk menjadi candi.""")
        else: # database.candi.candi_list.size >= MAX_CANDI (jumlah candi lebih dari atau sama dengan 100)
            print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {database.candi.candi_list.size}

Yah, Bandung Bondowoso memenangkan permainan!""")
        sys.exit() # Otomatis keluar dari program
