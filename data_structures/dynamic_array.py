class DynamicArray:
    def __init__(self, capacity=1):
        self.array = [None for i in range(capacity)]
        self.size = 0
        self.capacity = capacity

def append_array(dynamic_array, value):
    if dynamic_array.size < dynamic_array.capacity:
        dynamic_array.array[dynamic_array.size] = value
        dynamic_array.size += 1
    elif dynamic_array.size == dynamic_array.capacity:
        new_array = DynamicArray(dynamic_array.capacity * 2)
        for element in dynamic_array.array:
            new_array.array[new_array.size] = element
            new_array.size += 1
        new_array.array[new_array.size] = value
        new_array.size += 1
        
        dynamic_array.array = new_array.array
        dynamic_array.size = new_array.size
        dynamic_array.capacity = new_array.capacity    

def erase_array(dynamic_array, element, is_equal_func):
    i = 0
    while i < dynamic_array.size:
        if is_equal_func(dynamic_array.array[i], element):
            break
        i += 1
    if i == dynamic_array.size:
        return
    dynamic_array.array[i] = None
    for j in range(i, dynamic_array.size - 1):
        dynamic_array.array[j], dynamic_array.array[j+1] = dynamic_array.array[j+1], dynamic_array.array[j]
    dynamic_array.size -= 1

