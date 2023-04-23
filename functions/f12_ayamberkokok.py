import variables
import database.candi
from constants import MAX_CANDI
import sys

def run():
    if variables.login == False:
        print("Anda belum login")
    elif variables.role != "roro_jonggrang":
        print("Anda tidak mempunyai akses; hanya Roro Jonggrang yang memiliki kemampuan ini.")
    else:
        if database.candi.candi_list.size < MAX_CANDI:
            print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {database.candi.candi_list.size}

Selamat, Roro Jonggrang memenangkan permainan!

*Bandung Bondowoso angry noise*
Roro Jonggrang dikutuk menjadi candi.""")
        else: # database.candi.candi_list.size >= MAX_CANDI
            print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {database.candi.candi_list.size}

Yah, Bandung Bondowoso memenangkan permainan!""")
        sys.exit()