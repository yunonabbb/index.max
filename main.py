array = []
for _ in range(5):
    num = int(input("Введите число: "))
    array.append(num)

length = int(input("Введите длину массива: "))
array = []
for _ in range(length):
    num = int(input("Введите число: "))
    array.append(num)

array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
sum_array = sum(array)
print("Сумма чисел в массиве:", sum_array)

array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
even_sum = sum([num for num in array if num % 2 == 0])
print("Сумма четных ячеек массива:", even_sum)

array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
even_values_sum = sum([num for num in array if num % 2 == 0])
print("Сумма четных значений:", even_values_sum)


array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
max_num = max(array)
min_num = min(array)
print("Максимальное число:", max_num)
print("Минимальное число:", min_num)



array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
max_num = max(array)
min_num = min(array)
index_max = array.index(max_num)
index_min = array.index(min_num)
if index_max < index_min:
    sum_between = sum(array[index_max+1:index_min])
else:
    sum_between = sum(array[index_min+1:index_max])
print("Сумма чисел между минимальным и максимальным значением:", sum_between)


array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)


array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
max_num = max(array)
min_num = min(array)
index_max = array.index(max_num)
index_min = array.index(min_num)
if index_max < index_min:
    sum_between = sum(array[index_max+1:index_min])
else:
    sum_between = sum(array[index_min+1:index_max])
print("Сумма ячеек между минимальным и максимальным значением:", sum_between)



array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
center = len(array) // 2
diff_sum = sum([abs(array[i] - array[center]) for i in range(center, len(array))])
diff_sum += sum([abs(array[i] - array[center]) for i in range(center)])
print("Сумма разниц от центра до конца и от начала до центра массива:", diff_sum)


array = []
for _ in range(10):
    value = bool(input("Введите логическое значение (True/False): "))
    array.append(value)
true_count = sum(array)
print("Количество правдивых значений:", true_count)


array = []
for _ in range(10):
    num = int(input("Введите число: "))
    array.append(num)
pair_count = sum([1 for i in range(len(array)-1) if array[i+1] - array[i] == 1])
print("Количество пар с шагом в 1:", pair_count)













