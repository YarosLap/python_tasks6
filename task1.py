#     Задача 1. Дано натуральное число N. Найдите значение
#       выражения:
#       N + NN + NNN
#       N может быть любой длины.
def NumNum(num, count):
    numCount = ""
    for i in range(count):
        numCount += num 
    return numCount

number = input("Введите натуральное число  ")
print(f"{number} + {NumNum(number, 2)} + {NumNum(number, 3)} = {str( int(number) + int(NumNum(number,2)) + int(NumNum(number, 3) ) ) }")