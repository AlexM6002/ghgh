# Лабораторная работа № 1
# Задание 1

'''a = int(input("Введите число: "))
for i in range(1, a+1):
    print(i)'''

# Задание 2

'''a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a>=b:
    print("Большее число: {a}")
else:
    print(f"Большее число: {b}")'''






# Лабораторная работа № 2
# Задание 1

def greet(name):
    print(f"Hello, {name}")

#greet(input("Введите имя: "))

def square(number):
    return number**2

#a = square(int(input("Введите число: ")))
#print(a)

def max_of_two(x, y):
    if x>=y:
        return x
    return y

#a = max_of_two(int(input("1 число: ")), int(input("2 число: ")))
#print(a)

# Задание 2

def describe_person(name, age = 30):
    print(f"Имя: {name}")
    print(f"Возраст: {age}")

#describe_person('Alex', 25)


# Задание 3

def prime(number):
    return number>1 and all(number%i != 0 for i in range(2, int(number**0.5)+1))

print(prime(15))






























    





























       






































    
