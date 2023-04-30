# Задача 3. Найдите все простые несократимые дроби,
# лежащие между 0 и 1, знаменатель которых не превышает 11.
def Prost(num1, num2):
    # преверяем не сократимая ли дробь
    nesokr = True
    for i in range(2, num1+1):
        if num1 % i == 0 and num2 % i == 0:
            return False
    return nesokr

print("Простые несократимые дроби между 0 и 1:")
for i in range(2,12):
    for j in range(1,i+1):
        if Prost(j, i):
            print(f"{j}/{i}, ", end = " ")