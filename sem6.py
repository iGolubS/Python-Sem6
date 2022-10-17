# 1.Вводится список целых чисел в одну строчку через пробел. Необходимо оставить в нем только двузначные
# числа. Реализовать программу с использованием функции filter. Результат отобразить на экране в виде
# последовательности оставшихся чисел в одну строчку через пробел.

# arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
# print(list(filter(lambda e: 9< e < 100, arr)))



# def FilterDigits(inputList: list[int]) -> list[int]:
#     return list(filter(lambda x: 10<=int(x)<=99, inputList))
# arr = list(map(int, input("Введите последовательность чисел через пробел: ").split()))
# print(arr, FilterDigits(arr))





# 2. Дан список, вывести отдельно буквы и цифры.

# list1 = [1, 'e', 't', 's', 3, 5, 'f', 6, 'a', 9]
# nums = [i for i in list1 if type(i) == int]
# print(nums)
# letters = [i for i in list1 if type(i) != int]
# print(letters)





# 3. Преобразовать набора списков 
# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# в другой набор 
# ['user1', 4, 111]
# ['user2', 5, 222]
# ['user3', 9, 333]
# и потом вернуть в исходное состояние
# ['user1', 'user2', 'user3']
# [4, 5, 9]
# [111, 222, 333]

# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# data = list(zip(users, ids, salary))
# print(data)
# users1 = [i[0] for i in data]
# ids1 = [i[1] for i in data]
# salary1 = [i[2] for i in data]
# print(users1, ids1, salary1)



# users = ['user1','user2','user3','user4','user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111,222,333]
# a,b,c = map(list,zip(users, ids, salary))
# print(a,b,c, sep="\n")
# a,b,c= map(list,zip(a,b,c))
# print(a,b,c, sep="\n")