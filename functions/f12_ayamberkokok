import variables
import database.candi
from constants import MAX_CANDI

def run():
    if variables.login == False:
        print("Anda belum login")
    elif variables.role != "roro_jonggrang":
        print("Anda tidak mempunyai akses; hanya roro jonggrang yang memiliki kemampuan ini")
    elif database.candi.candi_list.size < MAX_CANDI:
        print("""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {database.candi.candi_list.size}

Selamat, Roro Jonggrang memenangkan permainan!

*Bandung Bondowoso angry noise*
Roro Jonggrang dikutuk menjadi candi.""")
    elif database.candi.candi_list.size == MAX_CANDI:
        print(f"""Kukuruyuk.. Kukuruyuk..

Jumlah Candi: {database.candi.candi_list.size}

Yah, Bandung Bondowoso memenangkan permainan!""")