try:
    n = int(input("Введіть довжину масиву (N): "))
    if n <= 0:
        print("Довжина масиву повинна бути додатним числом.")
    else:
        print(f"Введіть {n} елементів масиву через пробіл:")
        elements = list(map(float, input().split()))

        if len(elements) != n:
            print("Кількість введених елементів не відповідає вказаній довжині.")
        else:

            positive_elements = [el for el in elements if el > 0]

            if positive_elements:
                min_positive = min(positive_elements)
                print(f"Мінімальний додатний елемент: {min_positive}")
            else:
                print("У масиві немає додатних елементів.")
except ValueError:
    print("Помилка: введіть числові значення.")
