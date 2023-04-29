from algorithms.string_processing import split, strip
from data_structures.dynamic_array import DynamicArray, append_array, erase_array
from constants import MIN_PASSWORD_LENGTH, MAX_PASSWORD_LENGTH
import variables
import os

# Variabel global berfungsi sebagai database untuk mengload file csv, 
# melakukan perubahan (summonjin/hapusjin) jin, dan sumber ketika penyimpanan diakhir.
user_list = DynamicArray()

# Tipe bentukan untuk menyimpan informasi mengenai suatu user.
class User:
    def __init__(self, username='', password='', role=''):
        self.username = username
        self.password = password
        self.role = role

    def __repr__(self):
        return f"[{self.username} & {self.password} & {self.role}]"

def load():
    global user_list
    user_count = 0
    # Menghitung jumlah user.
    with open(os.path.join(variables.load_folder, "user.csv")) as file:
        file.readline()
        for line in file:
            user_count += 1
    # Setiap baris ditambah ke database user_list.
    with open(os.path.join(variables.load_folder, "user.csv")) as file:
        file.readline()
        for i in range(user_count):
            username, password, role = split(strip(file.readline()), ';')
            append_array(user_list, User(username, password, role))

# Melakukan penyimpanan.
def save(location):
    with open(os.path.join(location, "user.csv"), 'w') as file:
        file.write("username;password;role\n")
        for i in range(user_list.size):
            file.write(f"{user_list.array[i].username};{user_list.array[i].password};{user_list.array[i].role}\n")

# Mengecek apakah 2 variabel bertipe User memiliki username yang sama.
def user_equality_by_username(user1, user2):
    return user1.username == user2.username

# Mengecek apakah 2 variabel bertipe User memiliki role yang sama.
def user_equality_by_role(user1, user2):
    return user1.role == user2.role

# Menambahkan user pada database variabel global user_list. 
def add_user(username, password, role):
    global user_list
    append_array(user_list, User(username, password, role))

# Menghapus user dengan username tertentu.
def erase_user(username):
    global user_list
    erase_array(user_list, User(username, None, None), user_equality_by_username)

# Mengecek apakah terdapat user dengan username yang bersangkutan.
def is_user_exist(username):
    for i in range(user_list.size):
        if user_list.array[i].username == username:
            return True, user_list.array[i]
    return False, User()

# Mengecek apakah username valid.
def is_username_valid(username):
    return strip(username) != ''

# Mengecek apakah password valid.
def is_password_valid(password):
    return MIN_PASSWORD_LENGTH <= len(password) <= MAX_PASSWORD_LENGTH

# Menghitung jumlah user yang memiliki kesamaan.
def user_count(equality_function, username=None, password=None, role=None):
    count = 0
    for i in range(user_list.size):
        if equality_function(User(username, password, role), user_list.array[i]):
            count += 1
    return count