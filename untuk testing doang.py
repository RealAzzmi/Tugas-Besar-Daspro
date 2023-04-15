# class DynamicArray:
#     def __init__(self, capacity=1):
#         self.array = [None for i in range(capacity)]
#         self.size = 0
#         self.capacity = capacity

# def append_array(dynamic_array, value):
#     if dynamic_array.size < dynamic_array.capacity:
#         dynamic_array.array[dynamic_array.size] = value
#         dynamic_array.size += 1
#     elif dynamic_array.size == dynamic_array.capacity:
#         new_array = DynamicArray(dynamic_array.capacity * 2)
#         for element in dynamic_array.array:
#             new_array.array[new_array.size] = element
#             new_array.size += 1
#         new_array.array[new_array.size] = value
#         new_array.size += 1
        
#         dynamic_array.array = new_array.array
#         dynamic_array.size = new_array.size
#         dynamic_array.capacity = new_array.capacity

# def extend_array(dynamic_array, new_array):
#     for element in new_array:
#         append_array(dynamic_array, element)
    
# # def erase_array(dynamic_array, element):
# #     for i in range(dynamic_array.size):
# #         if dynamic_array.array[i] == element:
# #             break
# #     dynamic_array.array[i] = None
# #     for j in range(i, dynamic_array.size - 1):
# #         dynamic_array.array[j], dynamic_array.array[j+1] = dynamic_array.array[j+1], dynamic_array.array[j]

# def print_array(arr):
#     print(f"The size is {arr.size}: ", end='')
#     for i in arr.array:
#         print(i, end=' ')
#     print()
 
# da = DynamicArray()

# x = 1
# t = 2 if x != 1 else 10
# print(t)




    
