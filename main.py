import commands
import database.user, database.bahan_bangunan, database.candi
from algorithms.string_processing import strip


def main():
    # Load ini menerima lokasi folder tempat penyimpanan file csv dan mengecek apakah folder eksis.
    commands.load()

    # Masing-masing file csv diload.
    database.user.load()
    database.bahan_bangunan.load()
    database.candi.load()

    # Loop ini menerima command dan akan berhenti ketika fungsi yang dijalankan di commands.run(command)
    # memanggil sys.exit().
    while True:
        command = input(">>> ")
        command = strip(command)
        commands.run(command)

if __name__ == "__main__":
    main()