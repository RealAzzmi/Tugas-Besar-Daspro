# DynamicArray adalah implementasi dynamic array dari static array.

# Implementasi dari dynamic array cukup terkenal yaitu membuat static array dengan suatu kapasitas tertentu
# sehingga ketika penambahan elemen memenuhi static array, kapasitas bertambah dan dibuat static array baru
# dan diisi static array baru dengan data lama dari static array sebelumnya. 

class DynamicArray:
    def __init__(self, capacity=1):
        # static array dengan kapasitas tertentu.
        self.array = [None for i in range(capacity)]
        # Jumlah elemen yang berada pada static array.
        self.size = 0
        # Kapasitas static array.
        self.capacity = capacity

# Menambah elemen pada dynamic array.
def append_array(dynamic_array, value):
    # Mengecek apakah memungkinkan menambahkan suatu elemen yang baru.
    if dynamic_array.size < dynamic_array.capacity:
        # Jika iya, diindex static array untuk menyimpan elemen barunya.
        dynamic_array.array[dynamic_array.size] = value
        dynamic_array.size += 1
    elif dynamic_array.size == dynamic_array.capacity:
        # Jika sudah memenuhi kapasitas, kapasitas harus diperbesar. Dalam kasus ini, kapasitas
        # diperbesar dua kali.

        # Dibuat DynamicArray baru dengan kapasitas dua kali sebelumnya,
        new_array = DynamicArray(dynamic_array.capacity * 2)
        # Diisi elemen lama.
        for element in dynamic_array.array:
            new_array.array[new_array.size] = element
            new_array.size += 1
        # Ditambah elemen baru.
        new_array.array[new_array.size] = value
        new_array.size += 1
        # Diupdate parameter dynamic array sehingga tidak diperlukan mengreturn dynamic array.
        dynamic_array.array = new_array.array
        dynamic_array.size = new_array.size
        dynamic_array.capacity = new_array.capacity    

# Menghapus 1 elemen pada dynamic array.
def erase_array(dynamic_array, element, is_equal_func):
    # Looping hingga ketemu indeks i yang sama dengan elemen yang dicari.
    i = 0
    while i < dynamic_array.size:
        if is_equal_func(dynamic_array.array[i], element):
            break
        i += 1
    # Ketika i == dynamic_array.size, elemen tidak ditemukan karena i menunjuk "one-past-the-end".
    if i == dynamic_array.size:
        return
    # Dihapus elemen tersebut.
    dynamic_array.array[i] = None
    # Dilakukan swap sehingga None tersebut, berada pada ujung akhir array dan bukan pada tengah array.
    for j in range(i, dynamic_array.size - 1):
        dynamic_array.array[j], dynamic_array.array[j+1] = dynamic_array.array[j+1], dynamic_array.array[j]
    dynamic_array.size -= 1
